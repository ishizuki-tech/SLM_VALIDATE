#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py — Model-only labeling (6-axis + overall), class-based refactor (Gemma-ready, pure-JSON)

This version implements:
 - Final output is a flat 6-axis JSON + overall_score:
   {detail,specificity,usability,clarity,completeness,relevance,overall_score}
 - Strict validator for the 6-axis schema with optional overall_score; if present,
   it must be exactly consistent with the 6 labels (equal-weight average, rounded).
 - Robust sanitize/extract/repair loop for p3; retries with concise repair instructions.
 - p1/p2 produce "analysis-like" JSON; p2 is validated, else "{}" is passed to p3.
 - Prompt logging for p1/p2/p3 inputs/outputs/repairs/accepted (JSONL or per-id files).
 - Gemma turn wrapper and stop sequences handled in one place.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import re
import sys
import inspect
import signal
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, List, Tuple
from datetime import datetime, timezone

# --------------------------------
# Logger
# --------------------------------
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# --------------------------------
# optional rich UI
# --------------------------------
_RICH_AVAILABLE = False
try:
    from rich.console import Console  # type: ignore
    from rich.table import Table  # type: ignore
    from rich.panel import Panel  # type: ignore
    from rich.text import Text  # type: ignore
    from rich import box  # type: ignore
    from rich.syntax import Syntax  # type: ignore
    from rich.json import JSON as RichJSON  # type: ignore
    _RICH_AVAILABLE = True
except Exception:
    _RICH_AVAILABLE = False
    Console = None  # type: ignore

# --------------------------------
# llama_cpp optional import
# --------------------------------
_LLAMACPP_AVAILABLE = False
try:
    from llama_cpp import Llama  # type: ignore
    _LLAMACPP_AVAILABLE = True
except Exception:
    Llama = None  # type: ignore
    _LLAMACPP_AVAILABLE = False

# --------------------------------
# Defaults
# --------------------------------
BASE_QUESTION = "After planting, what share of seeds do you expect to grow into healthy plants?"
BASE_ANSWER = "Most of them came up fine."

FENCE_RE = re.compile(r"```(?:json)?\s*([\s\S]*?)\s*```", re.IGNORECASE)

EXIT_OK = 0
EXIT_LLAMA_FAILURE = 2
EXIT_MODE_UNSPECIFIED = 3
EXIT_SINGLE_NO_JSON = 4

# --------------------------------
# Utilities
# --------------------------------
def _ensure_parent_dir(path: Optional[str]) -> None:
    if not path:
        return
    p = Path(path)
    parent = p.parent
    if str(parent) and not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)

def _safe_trim(s: str, limit: int) -> str:
    if len(s) <= limit:
        return s
    b = s.encode("utf-8")[:limit]
    s2 = b.decode("utf-8", "ignore")
    return s2.rsplit("\n", 1)[0] + "\n[...]"

def _one_line(s: str) -> str:
    return " ".join((s or "").split())

def _strip_phatic(text: str) -> str:
    """p1/p2/p3 出力から前置き語をざっくり除去。"""
    if not text:
        return ""
    t = text.strip()
    patterns = [
        r"^thanks[^.]*\.\s*", r"^thank you[^.]*\.\s*", r"^sure[^.]*\.\s*",
        r"^great[^.]*\.\s*", r"^here(?:'s| is)\s+the\s+analysis[:\-\s]*",
        r"^analysis[:\-\s]*"
    ]
    for pat in patterns:
        t = re.sub(pat, "", t, flags=re.IGNORECASE)
    return t.strip()

# --------------------------------
# Prompt Logger
# --------------------------------
class PromptLogger:
    def __init__(self, global_jsonl: Optional[str] = None, dir_path: Optional[str] = None):
        self.global_jsonl = global_jsonl
        self.dir_path = dir_path
        if self.global_jsonl:
            self._ensure_parent_dir(self.global_jsonl)
        if self.dir_path:
            Path(self.dir_path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _ensure_parent_dir(path: Optional[str]) -> None:
        if not path:
            return
        p = Path(path).parent
        if str(p) and not p.exists():
            p.mkdir(parents=True, exist_ok=True)

    def _per_item_path(self, item_id: str) -> Optional[str]:
        if not self.dir_path:
            return None
        return str(Path(self.dir_path) / f"{item_id}.prompts.jsonl")

    @staticmethod
    def _write_line(path: str, line: str) -> None:
        with open(path, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def log(self, *, item_id: str, stage: str, kind: str,
            text: Optional[str] = None,
            attempt: Optional[int] = None,
            extra: Optional[Dict[str, Any]] = None,
            question: Optional[str] = None,
            answer: Optional[str] = None) -> None:
        rec: Dict[str, Any] = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "item_id": item_id,
            "stage": stage,
            "kind": kind,
        }
        if text is not None:
            rec["text"] = text
        if attempt is not None:
            rec["attempt"] = attempt
        if extra:
            rec["meta"] = extra
        if question is not None:
            rec["question"] = question
        if answer is not None:
            rec["answer"] = answer
        line = json.dumps(rec, ensure_ascii=False, separators=(",", ":"))

        if self.global_jsonl:
            self._write_line(self.global_jsonl, line)
        per_item = self._per_item_path(item_id)
        if per_item:
            self._write_line(per_item, line)

# --------------------------------
# PromptBuilder (Gemma user-blocks; wrapper is applied later)
# --------------------------------
class PromptBuilder:
    def __init__(self, filepath: Optional[str] = None):
        self.prompts: Dict[str, Dict[str, str]] = {}
        if filepath:
            try:
                p = Path(filepath)
                if p.exists():
                    with open(filepath, "r", encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                            obj = json.loads(line)
                            q = obj["question"].strip()
                            self.prompts[q] = {
                                "p1": obj.get("p1", ""),
                                "p2": obj.get("p2", ""),
                                "p3": obj.get("p3", "")
                            }
            except Exception as e:
                logger.warning("Failed to load custom prompts from %s: %s", filepath, e)

    @staticmethod
    def _default_p1(question: str, answer: str) -> str:
        return (
            "Inspect the following Question and Answer.\n"
            "Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.\n\n"
            "Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.\n"
            "The first character must be '{' and the last must be '}'.\n"
            "Do NOT include ```json, ``` or any code fences.\n"
            "Never output placeholders like <label> or <string>. If uncertain, use \"Medium\".\n\n"
            "Allowed labels: Very High, High, Medium, Low, Very Low.\n"
            "Required JSON keys (4 total): specificity, detail, usability, weaknesses.\n"
            "Rules:\n"
            "- specificity, detail, usability → one allowed label each.\n"
            "- weaknesses → short free-text string (≤ 140 chars).\n"
            "- Never output an empty string or placeholder for weaknesses.\n\n"
            "Example:\n"
            "{\"specificity\":\"Low\",\"detail\":\"Medium\",\"usability\":\"Low\",\"weaknesses\":\"Too vague and lacks numeric values.\"}\n\n"
            f"Question: {question}\n"
            f"Answer: {answer}\n"
        )

    @staticmethod
    def _safe_prev(prev: str) -> str:
        """Ensure prev is valid JSON string; return '{}' if invalid."""
        if not prev:
            return "{}"
        try:
            parsed = json.loads(prev)
            return json.dumps(parsed, ensure_ascii=False)
        except Exception:
            return "{}"

    @staticmethod
    def _default_p2(prev: str, question: str, answer: str) -> str:
        prev_json = PromptBuilder._safe_prev(prev)
        return (
            "Inspect the Question, Answer, and prior Analysis.\n"
            "Task: Decide whether the Answer contains enough information to fully and practically address the Question.\n"
            "Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.\n\n"
            "Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.\n"
            "The first character must be '{' and the last must be '}'.\n"
            "Do NOT include ```json, ``` or any code fences.\n"
            "Never output placeholders like <label> or <string>. If uncertain, use \"Medium\".\n\n"
            "Allowed labels: Very High, High, Medium, Low, Very Low.\n"
            "Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.\n"
            "Rules:\n"
            "- completeness, clarity, relevance → one allowed label each.\n"
            "- weaknesses → short free-text string (≤ 140 chars).\n"
            "- Never output an empty string or placeholder for weaknesses.\n\n"
            "Example:\n"
            "{\"completeness\":\"Low\",\"clarity\":\"Medium\",\"relevance\":\"High\",\"weaknesses\":\"No numeric target and lacks supporting context.\"}\n\n"
            f"Question: {question}\n"
            f"Answer: {answer}\n"
            f"Analysis: {prev_json}\n"
        )

    @staticmethod
    def _default_p3(prev: str, question: str, answer: str) -> str:
        prev_json = PromptBuilder._safe_prev(prev)
        return (
            "Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.\n"
            "The first character must be '{' and the last must be '}'.\n"
            "No prose. Do NOT include ```json, ``` or any code fences.\n"
            "Never output placeholders like <label> or <string>. If uncertain, use \"Medium\".\n"
            "Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.\n\n"
            "Allowed labels: Very High, High, Medium, Low, Very Low.\n"
            "Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.\n"
            "Rules:\n"
            "- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.\n"
            "- overall_score → MUST be computed, not guessed. Strictly follow this procedure:\n"
            "  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.\n"
            "  • Take the average of all 6 values with equal weight.\n"
            "  • Round to the nearest integer.\n"
            "  • Clamp the result to 0–100.\n"
            "  • Never output an overall_score that is inconsistent with the 6 labels.\n\n"
            "Example:\n"
            "{\"detail\":\"Low\",\"specificity\":\"Low\",\"usability\":\"Low\","
            "\"clarity\":\"Low\",\"completeness\":\"Low\",\"relevance\":\"Medium\",\"overall_score\":43}\n\n"
            "If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.\n"
            f"Question: {question}\n"
            f"Answer: {answer}\n"
            f"Analysis: {prev_json}\n"
        )

    # ---------- 統一 get ----------
    def get(self, question: str, stage: str, answer: str, prev: Optional[str] = None) -> str:
        q = question.strip()
        prev = prev.strip() if prev else "{}"

        if stage == "p1":
            return self._default_p1(question, answer)
        if stage == "p3":
            return self._default_p3(prev, question, answer)

        if q in self.prompts and stage in self.prompts[q] and self.prompts[q][stage]:
            tmpl = self.prompts[q][stage]
            if stage == "p1":
                tmpl += (
                    "Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. "
                    "The first character must be '{' and the last must be '}'. "
                    "Do NOT include ```json, ``` or any code fences."
                    "Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.\n"
                    f"Question: {question}\n"
                    f"Answer: {answer}\n"
                )
            else:
                tmpl += (
                    "Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. "
                    "The first character must be '{' and the last must be '}'. "
                    "Do NOT include ```json, ``` or any code fences."
                    "Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.\n"
                    f"Question: {question}\n"
                    f"Answer: {answer}\n"
                    f"Analysis: {prev}\n"
                )
            return tmpl

        # fallback → デフォルト
        if stage == "p1":
            return self._default_p1(question, answer)
        elif stage == "p2":
            return self._default_p2(prev, question, answer)
        elif stage == "p3":
            return self._default_p3(prev, question, answer)
        else:
            raise ValueError(f"Unknown stage: {stage}")

# --------------------------------
# JSON Extractor / Validator (6-axis + overall)
# --------------------------------
LABEL_TO_POINTS = {
    "Very High": 95,
    "High": 80,
    "Medium": 60,
    "Low": 40,
    "Very Low": 20,
}

class JsonExtractor:
    # 6-axis constants
    ALLOWED_LABELS6 = set(LABEL_TO_POINTS.keys())
    FIELDS6 = ["detail", "specificity", "usability", "clarity", "completeness", "relevance"]

    @staticmethod
    def sanitize_model_text(text: str) -> str:
        if not text:
            return ""
        t = text.strip()
        # strip code fences if present
        m = FENCE_RE.search(t)
        if m:
            t = m.group(1).strip()
        # unwrap accidental quoted JSON
        if len(t) >= 2 and t[0] == '"' and t[-1] == '"':
            inner = t[1:-1]
            try:
                return bytes(inner, "utf-8").decode("unicode_escape")
            except Exception:
                return inner
        return t

    @staticmethod
    def _find_matching_brace(s: str, start: int) -> int:
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(s)):
            c = s[i]
            if in_str:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == '"':
                    in_str = False
                continue
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return i
        return -1

    @staticmethod
    def try_extract_json(s: str) -> Optional[Dict[str, Any]]:
        if not s:
            return None
        # First balanced {...}
        idx = 0
        while True:
            idx = s.find("{", idx)
            if idx == -1:
                return None
            end = JsonExtractor._find_matching_brace(s, idx)
            if end == -1:
                idx += 1
                continue
            candidate = s[idx:end + 1]
            try:
                parsed = json.loads(candidate)
                if isinstance(parsed, dict):
                    return parsed
            except Exception:
                idx += 1
                continue

    # ---- 6-axis normalization helpers ----
    @staticmethod
    def _coerce_label6(v: Any) -> str:
        if not isinstance(v, str):
            return "Very Low"
        s = v.strip()
        # strict set only (no tail tokens)
        return s if s in JsonExtractor.ALLOWED_LABELS6 else "Very Low"

    @staticmethod
    def canonicalize_labels6(obj: Dict[str, Any]) -> Dict[str, str]:
        """Normalize top-level 6 axes to allowed labels (missing -> Very Low)."""
        out: Dict[str, str] = {}
        for k in JsonExtractor.FIELDS6:
            out[k] = JsonExtractor._coerce_label6(obj.get(k, "Very Low"))
        return out

    @staticmethod
    def analysis_like_to_labels6(obj: Dict[str, Any]) -> Optional[Dict[str, str]]:
        """
        Build 6-axis labels from analysis-like JSON (p1/p2 outputs).
        Priority: analysis -> labels -> root. Missing fields default to Very Low.
        Returns None if none of {specificity,detail,usability} are present.
        """
        node: Any
        if isinstance(obj.get("analysis"), dict):
            node = obj["analysis"]
        elif isinstance(obj.get("labels"), dict):
            node = obj["labels"]
        else:
            node = obj

        if not isinstance(node, dict):
            return None

        has_core = any(k in node for k in ("specificity", "detail", "usability"))
        if not has_core:
            return None

        out: Dict[str, str] = {}
        for k in JsonExtractor.FIELDS6:
            out[k] = JsonExtractor._coerce_label6(node.get(k, "Very Low"))
        return out

    # ---- scoring (equal weights, integer 0–100) ----
    @staticmethod
    def score_from_labels6(labels: Dict[str, str]) -> Optional[int]:
        if not isinstance(labels, dict):
            return None
        vals: List[int] = []
        for k in JsonExtractor.FIELDS6:
            v = labels.get(k)
            if v not in LABEL_TO_POINTS:
                return None
            vals.append(LABEL_TO_POINTS[v])
        avg = sum(vals) / len(vals)
        score = int(round(max(0, min(100, avg))))
        return score

    @staticmethod
    def final_schema_ok(obj: Any) -> bool:
        """
        Strict 6-axis final JSON validation with optional overall_score.
        Schema (required): detail, specificity, usability, clarity, completeness, relevance
        Optional: overall_score (int 0–100), which MUST match the equal-weight average of the 6 labels if present.
        """
        if not isinstance(obj, dict):
            return False
        for key in JsonExtractor.FIELDS6:
            if key not in obj:
                return False
            val = obj[key]
            if not isinstance(val, str) or "\n" in val or len(val) > 140:
                return False
            if val not in JsonExtractor.ALLOWED_LABELS6:
                return False

        if "overall_score" in obj:
            v = obj["overall_score"]
            if not isinstance(v, int):
                return False
            if v < 0 or v > 100:
                return False
            expected = JsonExtractor.score_from_labels6(obj)  # uses labels from obj
            if expected is None or v != expected:
                return False
        return True

# --------------------------------
# LlamaAdapter
# --------------------------------
class LlamaAdapter:
    def __init__(self, model_path: str, n_ctx: int, n_threads: int, n_gpu_layers: Optional[int] = None, verbose: bool = False):
        if not _LLAMACPP_AVAILABLE:
            raise RuntimeError("llama_cpp is not installed. Please 'pip install llama-cpp-python'.")
        kwargs: Dict[str, Any] = dict(model_path=model_path, n_ctx=n_ctx, n_threads=n_threads, verbose=verbose)
        if n_gpu_layers is not None:
            kwargs["n_gpu_layers"] = n_gpu_layers
        try:
            self.llm = Llama(**kwargs)  # type: ignore
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Llama model: {e}")

    def close(self) -> None:
        try:
            close_fn = getattr(self.llm, "close", None)
            if callable(close_fn):
                close_fn()
        except Exception:
            logger.debug("Model close() raised exception (ignored).")

    @staticmethod
    def _normalize_llm_kwargs(kwargs: Dict[str, Any]) -> Dict[str, Any]:
        kw = dict(kwargs)
        if "max_tokens" in kw:
            if "max_new_tokens" not in kw:
                kw["max_new_tokens"] = kw["max_tokens"]
            if "n_predict" not in kw:
                kw["n_predict"] = kw["max_tokens"]
            if "n_tokens" not in kw:
                kw["n_tokens"] = kw["max_tokens"]
        return kw

    @staticmethod
    def _filter_kwargs_for_callable(fn: Any, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        try:
            sig = inspect.signature(fn)
            params = sig.parameters
            if any(p.kind == inspect.Parameter.VAR_KEYWORD for p in params.values()):
                return dict(kwargs)
            return {k: v for k, v in kwargs.items() if k in params}
        except Exception:
            return dict(kwargs)

    @staticmethod
    def _extract_text(out: Any) -> str:
        if out is None:
            return ""
        if isinstance(out, str):
            return out
        if isinstance(out, dict):
            choices = out.get("choices")
            if isinstance(choices, list) and choices:
                first = choices[0]
                if isinstance(first, dict):
                    if "text" in first and isinstance(first["text"], str):
                        return first["text"]
                    if "message" in first and isinstance(first.get("message"), dict):
                        content = first["message"].get("content")
                        if isinstance(content, str):
                            return content
                    if "delta" in first and isinstance(first["delta"], dict):
                        txt = first["delta"].get("text") or first["delta"].get("content")
                        if isinstance(txt, str):
                            return txt
            if "text" in out and isinstance(out["text"], str):
                return out["text"]
            if "output" in out and isinstance(out["output"], str):
                return out["output"]
            try:
                return json.dumps(out, ensure_ascii=False)
            except Exception:
                return str(out)
        return str(out)

    def generate(self, prompt: str, **kwargs) -> str:
        kw = self._normalize_llm_kwargs(kwargs)

        # 1) direct callable
        try:
            fn_direct = getattr(self.llm, "__call__", None)
            if fn_direct is None and callable(self.llm):
                fn_direct = self.llm
            if fn_direct and callable(fn_direct):
                allowed = self._filter_kwargs_for_callable(fn_direct, kw)
                try:
                    out = fn_direct(prompt, **allowed)
                    return self._extract_text(out)
                except TypeError:
                    out = fn_direct(prompt)
                    return self._extract_text(out)
        except Exception as e:
            logger.debug("Direct callable attempt failed: %s", e)

        # 2) iterate methods
        for name in [n for n in dir(self.llm) if not n.startswith("_")]:
            try:
                fn = getattr(self.llm, name)
            except Exception:
                continue
            if not callable(fn):
                continue
            try:
                sig = inspect.signature(fn)
                params = sig.parameters
            except Exception:
                params = {}

            call_kwargs = {}
            call_args = []
            if "prompt" in params:
                call_kwargs["prompt"] = prompt
            elif "input" in params:
                call_kwargs["input"] = prompt
            elif "text" in params:
                call_kwargs["text"] = prompt
            elif "messages" in params:
                call_kwargs["messages"] = [{"role": "user", "content": prompt}]
            else:
                pos_params = [p for p in params.values()
                              if p.kind in (inspect.Parameter.POSITIONAL_ONLY,
                                            inspect.Parameter.POSITIONAL_OR_KEYWORD)]
                if len(pos_params) >= 1:
                    call_args = [prompt]

            for k, v in list(kw.items()):
                if k in params:
                    call_kwargs[k] = v

            try:
                out = fn(*call_args, **call_kwargs)
                return self._extract_text(out)
            except TypeError as te:
                logger.debug("Method %s TypeError: %s", name, te)
                continue
            except Exception as ex:
                logger.debug("Method %s raised: %s", name, ex)
                continue

        # 3) common fallback shapes
        fallback_shapes = [
            ("create_chat_completion", {"messages": [{"role": "user", "content": prompt}]}),
            ("chat_completion", {"messages": [{"role": "user", "content": prompt}]}),
            ("create_completion", {"prompt": prompt}),
            ("generate", {"prompt": prompt}),
            ("completion", {"prompt": prompt}),
            ("create_completion", {"input": prompt}),
            ("generate", {"input": prompt}),
        ]
        for name, payload in fallback_shapes:
            fn = getattr(self.llm, name, None)
            if callable(fn):
                allowed = self._filter_kwargs_for_callable(fn, {**payload, **kw})
                try:
                    out = fn(**allowed)
                    return self._extract_text(out)
                except Exception:
                    continue

        logger.error("No compatible llama_cpp method found.")
        return "[LLM_CALL_ERROR] unsupported call signature"

# --------------------------------
# Renderer（6-axis + overall）
# --------------------------------
class Renderer:
    def __init__(self, use_rich: bool):
        self.use_rich = use_rich and _RICH_AVAILABLE
        self.console = Console() if self.use_rich else None

    def text_panel(self, title: str, content: str, color: str) -> None:
        content = content or "(none)"
        if self.console:
            self.console.print(Panel(Text(content), title=title, style=color, box=box.ROUNDED))
        else:
            print(f"--- {title} ---\n{content}\n")

    def canonical(self, canonical: Dict[str, Any]) -> None:
        if not self.console:
            print(json.dumps(canonical, ensure_ascii=False, indent=2))
            return

        self.console.rule(Text(" Six-axis Labels ", style="bold white on blue"))
        table = Table(title="Labels (6 axes + overall)", box=box.SIMPLE_HEAVY)
        table.add_column("Dimension", style="bold")
        table.add_column("Label / Score", justify="center")
        order = ["specificity", "detail", "usability", "clarity", "completeness", "relevance"]
        for k in order:
            table.add_row(k.title(), str(canonical.get(k, "Medium")))
        if "overall_score" in canonical:
            table.add_row("Overall Score", str(canonical["overall_score"]))
        self.console.print(table)
        self.console.rule("End of evaluation")

    def canonical_single_line(self, canonical: Dict[str, Any]) -> None:
        line = json.dumps(canonical, ensure_ascii=False, separators=(",", ":"))
        if self.console:
            try:
                syntax = Syntax(line, "json", line_numbers=False)
                self.console.print(Panel(syntax, title="Final JSON (single-line)", style="bold cyan", box=box.ROUNDED))
                return
            except Exception:
                self.console.print(Panel(Text(line), title="Final JSON (single-line)", style="bold cyan", box=box.ROUNDED))
                return
        print(line)

# --------------------------------
# Configs
# --------------------------------
@dataclass
class EvalConfig:
    max_tokens: int = 256
    temperature: float = 0.0
    prev_max_chars: int = 2000
    final_max_tokens: Optional[int] = None
    fallback_policy: str = "retry-only"  # "retry-only" | "none"
    final_retries: int = 3
    gen_kwargs: Optional[Dict[str, Any]] = None
    quiet: bool = False

@dataclass
class ModelInit:
    model_path: str
    n_ctx: int = 1024
    n_threads: int = 4
    n_gpu_layers: Optional[int] = None

# --------------------------------
# QAEvaluator (3-stage chain, p2 validated, strict p3 6-axis+overall + logging)
# --------------------------------
class QAEvaluator:
    def __init__(self, adapter: LlamaAdapter, renderer: Optional[Renderer] = None, prompt_logger: Optional[PromptLogger] = None):
        self.adapter = adapter
        self.renderer = renderer
        self.prompt_logger = prompt_logger
        self.prompt_builder = PromptBuilder("prompts.jsonl")

    @staticmethod
    def gemma_prompt(user_block: str) -> str:
        return (
            "<start_of_turn>user\n"
            + user_block.rstrip()
            + "\n<end_of_turn>\n"
            "<start_of_turn>model"
        )

    def _send(self, user_block: str, max_tokens: int, temperature: float, gen_kwargs: Dict[str, Any], stop: Optional[List[str]] = None) -> str:
        prompt = self.gemma_prompt(user_block)
        kw = dict(gen_kwargs)
        if stop:
            kw["stop"] = stop
        return self.adapter.generate(prompt, max_tokens=max_tokens, temperature=temperature, **kw)

    def _compute_final_tokens(self, cfg: EvalConfig) -> int:
        if cfg.final_max_tokens is not None:
            return cfg.final_max_tokens
        # clamp 120..400 around base max_tokens
        return max(120, min(400, cfg.max_tokens))

    def _build_repair_prompt(self, raw_prev: str, reason: str) -> str:
        return (
            "Your previous output did not comply with the strict final schema.\n"
            "Repair it and output ONLY one JSON object on a SINGLE LINE.\n"
            "Schema keys: detail, specificity, usability, clarity, completeness, relevance, overall_score\n"
            "Rules for overall_score:\n"
            "- Map labels to points: Very High=95, High=80, Medium=60, Low=40, Very Low=20\n"
            "- Equal-weight average of 6 axes, round to nearest integer, clamp 0–100\n"
            "- Score must exactly match labels\n\n"
            f"Reason: {reason}\n"
            f"Previous output:\n{raw_prev}\n"
        )

    def _accept(self, obj: Dict[str, Any]) -> Dict[str, Any]:
        """Return canonical dict with all 6 labels + overall_score (computed if missing)."""
        labels = JsonExtractor.canonicalize_labels6(obj)
        score = JsonExtractor.score_from_labels6(labels)
        if score is not None:
            labels["overall_score"] = score
        return labels

    def evaluate(self, question: str, answer: str, cfg: EvalConfig, item_id: str = "single") -> Optional[Dict[str, Any]]:
        gen_kwargs = cfg.gen_kwargs or {}

        # --- Log Q/A at top (stage p0) ---
        if self.prompt_logger:
            self.prompt_logger.log(item_id=item_id, stage="p0", kind="qa",
                                   question=question, answer=answer)
        # Prompt #1
        p1 = self.prompt_builder.get(question, "p1", answer)
        if self.renderer and not cfg.quiet and self.renderer.console:
            self.renderer.console.rule(Text("Prompt #1 — Quick inspection (Gemma)", style="bold cyan"))
            self.renderer.console.print(Panel(Text(p1), title="Prompt #1 (user content)", style="cyan", box=box.ROUNDED))
        if self.prompt_logger:
            self.prompt_logger.log(item_id=item_id, stage="p1", kind="prompt", text=p1)

        out1_raw = self._send(p1, max_tokens=cfg.max_tokens, temperature=cfg.temperature, gen_kwargs=gen_kwargs, stop=["<end_of_turn>", "\n<end_of_turn>"])
        out1 = JsonExtractor.sanitize_model_text(out1_raw)
        out1 = _strip_phatic(_safe_trim(out1, cfg.prev_max_chars))

        if self.renderer and not cfg.quiet:
            self.renderer.text_panel("Prompt #1 Output (sanitized, possibly truncated)", out1, "cyan")
        if self.prompt_logger:
            self.prompt_logger.log(item_id=item_id, stage="p1", kind="output", text=out1)

        prev_out = out1

        # Prompt #2
        p2 = self.prompt_builder.get(question, "p2", answer, prev_out)
        if self.renderer and not cfg.quiet and self.renderer.console:
            self.renderer.console.rule(Text("Prompt #2 — Next inspection (Gemma)", style="bold magenta"))
            self.renderer.console.print(Panel(Text(p2), title="Prompt #2 (user content)", style="magenta", box=box.ROUNDED))
        if self.prompt_logger:
            self.prompt_logger.log(item_id=item_id, stage="p2", kind="prompt", text=p2)

        out2_raw = self._send(p2, max_tokens=cfg.max_tokens, temperature=cfg.temperature, gen_kwargs=gen_kwargs, stop=["<end_of_turn>", "\n<end_of_turn>"])
        out2 = JsonExtractor.sanitize_model_text(out2_raw)
        out2 = _strip_phatic(_safe_trim(out2, cfg.prev_max_chars))

        if self.renderer and not cfg.quiet:
            self.renderer.text_panel("Prompt #2 Output (sanitized, possibly truncated)", out2, "magenta")
        if self.prompt_logger:
            self.prompt_logger.log(item_id=item_id, stage="p2", kind="output", text=out2)

        prev_out = out2

        # Prompt #3 (Final 6-axis JSON + overall_score)
        p3 = self.prompt_builder.get(question, "p3", answer, prev_out)
        final_tokens = self._compute_final_tokens(cfg)

        if self.renderer and not cfg.quiet and self.renderer.console:
            self.renderer.console.rule(Text("Prompt #3 — Final JSON evaluation (Gemma)", style="bold green"))
            self.renderer.console.print(Panel(Text(p3), title="Prompt #3 (user content)", style="green", box=box.ROUNDED))
        if self.prompt_logger:
            self.prompt_logger.log(item_id=item_id, stage="p3", kind="prompt", text=p3, attempt=0)

        attempts = 0
        raw_out = ""
        parsed: Optional[Dict[str, Any]] = None

        while True:
            raw_out = self._send(p3 if attempts == 0 else self._build_repair_prompt(raw_out, reason),  # type: ignore[name-defined]
                                 max_tokens=final_tokens,
                                 temperature=cfg.temperature,
                                 gen_kwargs=gen_kwargs,
                                 stop=["<end_of_turn>", "\n<end_of_turn>"])

            sanitized = JsonExtractor.sanitize_model_text(raw_out)
            sanitized = _strip_phatic(_safe_trim(sanitized, cfg.prev_max_chars))

            if self.prompt_logger:
                self.prompt_logger.log(item_id=item_id, stage="p3", kind="output", text=sanitized, attempt=attempts)

            if self.renderer and not cfg.quiet:
                self.renderer.text_panel(f"Prompt #3 Output (attempt {attempts})", sanitized, "magenta")

            parsed = JsonExtractor.try_extract_json(sanitized)
            if parsed is None:
                try:
                    parsed = json.loads(sanitized)
                except Exception:
                    parsed = None

            if isinstance(parsed, dict):
                # Valid?
                if JsonExtractor.final_schema_ok(parsed):
                    canonical = self._accept(parsed)
                    if self.prompt_logger:
                        self.prompt_logger.log(item_id=item_id, stage="p3", kind="accepted", text="final 6-axis+overall json", attempt=attempts, extra={"canonical": canonical})
                    return canonical
                # Try from analysis-like
                recovered = JsonExtractor.analysis_like_to_labels6(parsed)
                if recovered is not None and JsonExtractor.final_schema_ok(recovered):
                    canonical = self._accept(recovered)
                    if self.prompt_logger:
                        self.prompt_logger.log(item_id=item_id, stage="p3", kind="accepted", text="recovered 6-axis+overall json", attempt=attempts, extra={"canonical": canonical})
                    return canonical

            # Need repair?
            if cfg.fallback_policy != "retry-only" or attempts >= cfg.final_retries:
                logger.error("Final JSON invalid after %d attempt(s).", attempts + 1)
                return None

            # prepare reason for repair prompt
            reason = "Invalid schema or inconsistent overall_score; must output exactly the 6 labels plus a consistent overall_score."
            attempts += 1

# --------------------------------
# Batch Processor（6-axis + overall CSV）
# --------------------------------
class BatchProcessor:
    def __init__(self, evaluator: QAEvaluator, renderer: Optional[Renderer]):
        self.evaluator = evaluator
        self.renderer = renderer

    def _append_csv(self, out_csv: str, item_id: str, canonical: Dict[str, Any], question: str, answer: str) -> None:
        _ensure_parent_dir(out_csv)
        exists = os.path.exists(out_csv)
        with open(out_csv, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if not exists:
                writer.writerow([
                    "id",
                    "specificity","detail","usability","clarity","completeness","relevance",
                    "overall_score",
                    "canonical_json",
                    "question",
                    "answer",
                ])
            writer.writerow([
                item_id,
                canonical.get("specificity",""),
                canonical.get("detail",""),
                canonical.get("usability",""),
                canonical.get("clarity",""),
                canonical.get("completeness",""),
                canonical.get("relevance",""),
                canonical.get("overall_score",""),
                json.dumps(canonical, ensure_ascii=False, separators=(",", ":")),
                question,
                answer,
            ])

    def run_jsonl(
        self,
        input_jsonl: str,
        output_jsonl: Optional[str],
        out_csv: Optional[str],
        dump_failed: Optional[str],
        cfg: EvalConfig,
        continue_on_error: bool,
        meta: Optional[Dict[str, Any]] = None,
    ) -> int:
        processed = 0
        line_no = 0
        out_f = None
        try:
            if output_jsonl:
                _ensure_parent_dir(output_jsonl)
                out_f = open(output_jsonl, "a", encoding="utf-8")

            with open(input_jsonl, "r", encoding="utf-8") as fh:
                for raw in fh:
                    if App.STOP_REQUESTED:
                        logger.info("Stop flag detected; stopping batch.")
                        break
                    line_no += 1
                    raw = raw.strip()
                    if not raw:
                        continue
                    try:
                        obj = json.loads(raw)
                        question = obj.get("question") or BASE_QUESTION
                        answer = obj.get("answer") or BASE_ANSWER
                        item_id = obj.get("id", f"line{line_no}")
                    except Exception as e:
                        logger.exception("Failed to parse JSON on line %d: %s", line_no, e)
                        if not continue_on_error:
                            return processed
                        else:
                            continue

                    if self.renderer and self.renderer.console and not cfg.quiet:
                        self.renderer.console.print(f"[cyan]Processing {item_id} (line {line_no})[/cyan]")
                    elif cfg.quiet and processed % 50 == 0:
                        logger.info("Processing line %d (id=%s)", line_no, item_id)

                    canonical = self.evaluator.evaluate(question, answer, cfg, item_id=item_id)
                    if canonical is None:
                        logger.error("Evaluation failed for %s (line %d).", item_id, line_no)
                        if dump_failed:
                            try:
                                _ensure_parent_dir(dump_failed)
                                with open(dump_failed, "a", encoding="utf-8") as f:
                                    f.write(f"=== FAILED id={item_id} line={line_no} ===\n")
                            except Exception:
                                logger.exception("Failed to write dump_failed file.")
                        if not continue_on_error:
                            return processed
                        else:
                            continue

                    record = {"id": item_id, "question": question, "answer": answer, "canonical": canonical}
                    if meta:
                        record["meta"] = meta

                    if out_f:
                        out_f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
                    if out_csv:
                        try:
                            self._append_csv(out_csv, item_id, canonical, question, answer)
                        except Exception:
                            logger.exception("Failed to append to CSV for %s", item_id)

                    processed += 1
        finally:
            if out_f:
                out_f.close()
        return processed

# --------------------------------
# App (CLI)
# --------------------------------
class App:
    STOP_REQUESTED = False

    @staticmethod
    def _signal_handler(signum, frame):
        App.STOP_REQUESTED = True
        logger.warning("Stop requested (signal %s). Finishing current item and stopping...", signum)

    @staticmethod
    def install_signal_handlers():
        try:
            signal.signal(signal.SIGINT, App._signal_handler)
            signal.signal(signal.SIGTERM, App._signal_handler)
        except Exception:
            pass

    @staticmethod
    def parse_args() -> argparse.Namespace:
        p = argparse.ArgumentParser(description="Three-stage chained QA evaluator (final 6-axis + overall_score JSON output, model-only).")
        p.add_argument("--model", "-m", required=True, help="Path to model file (.gguf/.bin)")
        p.add_argument("--ctx", type=int, default=1024, help="n_ctx for Llama")
        p.add_argument("--threads", type=int, default=4, help="n_threads for Llama")
        p.add_argument("--gpu-layers", type=int, default=None, help="Optional: number of GPU layers (llama.cpp)")

        p.add_argument("--try-defaults", action="store_true", help="Run the built-in 3 prompts (chained)")
        p.add_argument("--score-only", action="store_true", help="(ignored in 6-axis mode) Print only the final score")
        p.add_argument("--print-one-line", action="store_true", help="Print only the single-line canonical JSON")
        p.add_argument("--no-rich", action="store_true", help="Disable rich output even if installed")
        p.add_argument("--quiet-batch", action="store_true", help="Suppress per-item prompt/outputs during batch")

        p.add_argument("--max-tokens", type=int, default=256, help="max_tokens for Prompt #1/#2")
        p.add_argument("--max-tokens-final", type=int, default=None, help="token limit for final JSON prompt (default: clamp 120..400 around --max-tokens)")
        p.add_argument("--temp", type=float, default=0.0, help="temperature for model calls (0.0 recommended)")
        p.add_argument("--top-k", type=int, default=None, help="optional: pass top_k to llama if supported")
        p.add_argument("--top-p", type=float, default=None, help="optional: pass top_p to llama if supported")

        p.add_argument("--debug", action="store_true", help="Enable debug logging")
        p.add_argument("--prev-max-chars", type=int, default=2000, help="Max chars to inject from previous outputs into later prompts")

        p.add_argument("--out-csv", type=str, help="Optional CSV file to append canonical JSON results")
        p.add_argument("--dump-failed", type=str, help="Optional file path to append sanitized final outputs when JSON extraction fails")
        p.add_argument("--question", type=str, help="Override built-in question text")
        p.add_argument("--answer", type=str, help="Override built-in answer text")

        p.add_argument("--input-jsonl", type=str, help='Path to input JSONL for batch processing. Each line: {"question":"...","answer":"...","id":"optional"}')
        p.add_argument("--output-jsonl", type=str, help="Optional path to append per-item canonical JSONL results")
        p.add_argument("--batch-continue-on-error", action="store_true", help="When batch processing, continue on per-line error")

        p.add_argument("--fallback-policy", choices=["retry-only", "none"], default="retry-only",
                       help="retry-only: model-only retries then fail; none: no retry, fail immediately")
        p.add_argument("--final-retries", type=int, default=3,
                       help="number of model-only retries when final JSON is invalid (ignored if --fallback-policy=none)")

        # Prompt logging
        p.add_argument("--prompts-jsonl", type=str, default=None,
                       help="If set, append all prompt I/O logs to this JSONL file.")
        p.add_argument("--prompts-dir", type=str, default=None,
                       help="If set, write per-item prompt logs to DIR/<id>.prompts.jsonl.")
        return p.parse_args()

    @staticmethod
    def run() -> int:
        args = App.parse_args()
        if args.debug:
            logger.setLevel(logging.DEBUG)

        # Renderer
        use_rich = (not args.no_rich) and _RICH_AVAILABLE
        renderer = Renderer(use_rich=use_rich)

        question = args.question or BASE_QUESTION
        answer = args.answer or BASE_ANSWER

        logger.info("Loading model: %s (ctx=%d threads=%d)", args.model, args.ctx, args.threads)
        try:
            adapter = LlamaAdapter(
                model_path=args.model,
                n_ctx=args.ctx,
                n_threads=args.threads,
                n_gpu_layers=args.gpu_layers,
                verbose=False,
            )
        except Exception as e:
            logger.error(str(e))
            return EXIT_LLAMA_FAILURE

        try:
            App.install_signal_handlers()

            eval_cfg = EvalConfig(
                max_tokens=args.max_tokens,
                temperature=args.temp,
                prev_max_chars=args.prev_max_chars,
                final_max_tokens=args.max_tokens_final,
                fallback_policy=args.fallback_policy,
                final_retries=args.final_retries,
                gen_kwargs={k: v for k, v in {"top_k": args.top_k, "top_p": args.top_p}.items() if v is not None},
                quiet=args.quiet_batch,
            )

            prompt_logger = PromptLogger(global_jsonl=args.prompts_jsonl, dir_path=args.prompts_dir)
            evaluator = QAEvaluator(adapter=adapter, renderer=renderer, prompt_logger=prompt_logger)
            batcher = BatchProcessor(evaluator=evaluator, renderer=renderer)

            meta = {
                "model_path": args.model,
                "n_ctx": args.ctx,
                "n_threads": args.threads,
                "n_gpu_layers": args.gpu_layers,
                "fallback_policy": args.fallback_policy,
                "final_retries": args.final_retries,
                "top_k": args.top_k,
                "top_p": args.top_p,
            }

            if args.input_jsonl:
                processed = batcher.run_jsonl(
                    input_jsonl=args.input_jsonl,
                    output_jsonl=args.output_jsonl,
                    out_csv=args.out_csv,
                    dump_failed=args.dump_failed,
                    cfg=eval_cfg,
                    continue_on_error=args.batch_continue_on_error,
                    meta=meta,
                )
                logger.info("Batch processing completed. Items processed: %d", processed)
                return EXIT_OK

            elif args.try_defaults:
                canonical = evaluator.evaluate(question, answer, eval_cfg, item_id="single")
                if canonical is None:
                    logger.error("Evaluation failed.")
                    return EXIT_SINGLE_NO_JSON

                if args.score_only:
                    logger.warning("--score-only is not supported in 6-axis mode. Printing single-line JSON instead.")
                    renderer.canonical_single_line(canonical)
                elif args.print_one_line:
                    renderer.canonical_single_line(canonical)
                else:
                    renderer.canonical(canonical)
                    renderer.canonical_single_line(canonical)
                    if renderer.console:
                        try:
                            renderer.console.print(RichJSON(json.dumps(canonical, ensure_ascii=False, indent=2)))
                        except Exception:
                            print(json.dumps(canonical, ensure_ascii=False, indent=2))
                return EXIT_OK

            else:
                logger.error("No action specified. Use --try-defaults for single run or --input-jsonl for batch.")
                return EXIT_MODE_UNSPECIFIED

        finally:
            adapter.close()


def main() -> int:
    return App.run()


if __name__ == "__main__":
    raise SystemExit(main())
