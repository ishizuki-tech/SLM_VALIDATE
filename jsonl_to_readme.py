#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jsonl_to_readme.py

Reads evaluation results in JSONL format (each line contains: id, question, answer, canonical, meta)
and generates a README.md (Markdown).

Usage:
  python jsonl_to_readme.py input.jsonl --out README.md --title "QA Evaluation Results (Model-Only, Pure-JSON)"

- Input: JSONL where each line is a JSON object, e.g.:
    {"id":"q001", "question":"...", "answer":"...", "canonical":{...}, "meta":{...}}
- Output: README.md (including a Markdown table)
"""

from __future__ import annotations
import argparse
import json
import math
import sys
from typing import Any, Dict, List, Optional, Tuple, Iterable
from dataclasses import dataclass

# ---------- Data model ----------
@dataclass
class Canonical:
    labels: Dict[str, Any]
    subscores_unit: Dict[str, Any]
    weighted_base_0_100: Optional[float]
    penalty: Optional[int]
    final_score_0_100: Optional[int]

@dataclass
class Record:
    id: str
    question: str
    answer: str
    canonical: Canonical
    meta: Dict[str, Any]

# ---------- Utilities ----------
def _md_escape(text: str) -> str:
    """Escape '|' for Markdown tables."""
    return (text or "").replace("|", "\\|")

def _try_float(x: Any) -> Optional[float]:
    try:
        if x is None:
            return None
        return float(x)
    except Exception:
        return None

def _try_int(x: Any) -> Optional[int]:
    try:
        if x is None:
            return None
        xf = float(x)
        if xf.is_integer():
            return int(xf)
        return int(round(xf))
    except Exception:
        return None

def _read_jsonl(fp) -> Iterable[Dict[str, Any]]:
    for line_no, line in enumerate(fp, 1):
        s = line.strip()
        if not s:
            continue
        try:
            obj = json.loads(s)
            if isinstance(obj, dict):
                yield obj
        except Exception as e:
            print(f"[WARN] JSON parse error at line {line_no}: {e}", file=sys.stderr)

def _parse_record(obj: Dict[str, Any]) -> Optional[Record]:
    rid = str(obj.get("id") or "")
    if not rid:
        return None
    q = str(obj.get("question") or "")
    a = str(obj.get("answer") or "")
    can = obj.get("canonical") or {}
    labels = can.get("labels") or {}
    subs = can.get("subscores_unit") or {}
    wb = _try_float(can.get("weighted_base_0_100"))
    pen = _try_int(can.get("penalty"))
    fin = _try_int(can.get("final_score_0_100"))
    meta = obj.get("meta") or {}
    return Record(
        id=rid,
        question=q,
        answer=a,
        canonical=Canonical(
            labels=labels,
            subscores_unit=subs,
            weighted_base_0_100=wb,
            penalty=pen,
            final_score_0_100=fin,
        ),
        meta=meta,
    )

def _meta_summary(records: List[Record]) -> Tuple[bool, Dict[str, Any], List[Tuple[str, Dict[str, Any]]]]:
    """Return whether all records share identical meta; if not, list meta per id."""
    if not records:
        return True, {}, []
    first = records[0].meta
    all_same = all(r.meta == first for r in records)
    if all_same:
        return True, first, []
    else:
        # If different, return (id, meta) pairs
        return False, {}, [(r.id, r.meta) for r in records]

def _avg_final(records: List[Record]) -> Optional[float]:
    vals = [r.canonical.final_score_0_100 for r in records if r.canonical.final_score_0_100 is not None]
    if not vals:
        return None
    return sum(vals) / len(vals)

def _labels_triplet(labels: Dict[str, Any]) -> str:
    s = labels.get("specificity", "")
    d = labels.get("detail", "")
    u = labels.get("usability", "")
    return f"{s or '?'} / {d or '?'} / {u or '?'}"

def _format_float1(x: Optional[float]) -> str:
    return f"{x:.1f}" if isinstance(x, float) and math.isfinite(x) else "—"

def _format_int(x: Optional[int]) -> str:
    return f"{x:d}" if isinstance(x, int) else "—"

# ---------- Markdown rendering ----------
def render_markdown(
    records: List[Record],
    title: str = "QA Evaluation Results (Model-Only, Pure-JSON)",
) -> str:
    n = len(records)
    avg = _avg_final(records)
    avg_str = f"{avg:.1f}" if avg is not None else "—"

    lines: List[str] = []
    lines.append(f"# {title}\n")
    lines.append("This README summarizes the **final canonical JSON** produced by a 3-stage evaluator in an easy-to-read format.  ")
    lines.append(f"Items: **{n}** / Average final score: **{avg_str} / 100**\n")
    lines.append("---\n")

    same, meta_common, meta_list = _meta_summary(records)
    lines.append("## Common Meta")
    if same:
        if meta_common:
            for k in ["model_path", "n_ctx", "n_threads", "n_gpu_layers", "fallback_policy", "final_retries", "top_k", "top_p"]:
                if k in meta_common:
                    v = meta_common.get(k)
                    v_str = "—" if v in (None, "", "null") else str(v)
                    lines.append(f"- **{k}**: `{v_str}`")
        else:
            lines.append("- (no meta information)")
    else:
        lines.append("- **Note**: `meta` differs across records; listing per id below.")
        lines.append("")
        lines.append("| id | meta |")
        lines.append("|---|---|")
        for rid, m in meta_list:
            m_compact = json.dumps(m, ensure_ascii=False, separators=(",", ":"))
            lines.append(f"| `{_md_escape(rid)}` | `{_md_escape(m_compact)}` |")
    lines.append("\n---\n")

    lines.append("## How to read the scores (summary)")
    lines.append("- Labels: **Very High / High / Medium / Low / Very Low**  ")
    lines.append("- Unit mapping (0..1): VH=0.95, H=0.80, M=0.60, L=0.40, VL=0.20  ")
    lines.append("- Weights: **specificity 0.35 / detail 0.40 / usability 0.25**  ")
    lines.append("- `weighted_base_0_100 = 100 × (0.35×S + 0.40×D + 0.25×U)` (1 decimal place)  ")
    lines.append("- `penalty = min(3 × number_of_weaknesses, 15)`  ")
    lines.append("- `final_score_0_100 = round(clamp(weighted_base_0_100 − penalty, 0..100))`\n")
    lines.append("---\n")

    lines.append("## Results\n")
    lines.append("| ID | Question | Answer | Labels (S / D / U) | weighted_base | penalty | final |")
    lines.append("|---|---|---|---|---:|---:|---:|")

    for r in records:
        labels_str = _labels_triplet(r.canonical.labels)
        wb = _format_float1(r.canonical.weighted_base_0_100)
        pen = _format_int(r.canonical.penalty)
        fin = _format_int(r.canonical.final_score_0_100)
        lines.append(
            f"| **{_md_escape(r.id)}** | {_md_escape(r.question)} | "
            f"{_md_escape(r.answer)} | **{_md_escape(labels_str)}** | "
            f"**{wb}** | **{pen}** | **{fin}** |"
        )

    lines.append("\n> **Note**: S=Specificity, D=Detail, U=Usability\n")
    lines.append("---\n")

    lines.append("## Notes")
    lines.append("- Values are copied directly from the already **canonicalized final JSON**; no recalculation is performed here.")
    lines.append("- `penalty` typically reflects deductions based on the number of listed weaknesses (max 15). If no weaknesses array is present in p2, many implementations treat it as 0.")
    lines.append("- When meta is identical across runs, you can use this table to monitor drift in answer quality.")
    lines.append("")
    return "\n".join(lines)

# ---------- Main ----------
def main() -> int:
    ap = argparse.ArgumentParser(description="JSONL → README.md converter")
    ap.add_argument("input", help="Input JSONL file path ('-' for stdin)")
    ap.add_argument("--out", default="README.md", help="Output Markdown file path (default: README.md)")
    ap.add_argument("--title", default="QA Evaluation Results (Model-Only, Pure-JSON)", help="Title of the README")
    args = ap.parse_args()

    # Read input
    if args.input == "-":
        src_iter = _read_jsonl(sys.stdin)
    else:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                objs = list(_read_jsonl(f))
        except FileNotFoundError:
            print(f"[ERROR] Input not found: {args.input}", file=sys.stderr)
            return 1
        src_iter = objs

    # Parse
    records: List[Record] = []
    for obj in src_iter:
        rec = _parse_record(obj)
        if rec:
            records.append(rec)

    if not records:
        print("[ERROR] No valid records found.", file=sys.stderr)
        return 2

    # Render Markdown
    md = render_markdown(records, title=args.title)

    # Write output
    with open(args.out, "w", encoding="utf-8") as fw:
        fw.write(md)

    print(f"[OK] Wrote {args.out} ({len(records)} items)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
