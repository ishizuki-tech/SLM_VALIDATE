#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jsonl_to_readme.py

Reads evaluation results in JSONL format and generates README.md.

Behavior (strict):
- Expects each JSONL line to be a dict with:
    {
      "id": "...",
      "question": "...",
      "answer": "...",
      "canonical": {
        "detail": "...",
        "specificity": "...",
        "usability": "...",
        "clarity": "...",
        "completeness": "...",
        "relevance": "...",
        "overall_score": 77   # REQUIRED; int in [0, 100]
      },
      "meta": { ... }         # OPTIONAL; shown if common across all records
    }
- This script NEVER computes overall_score. It only displays it.
- If overall_score is missing, non-integer, or out of range, the record is skipped with a warning.
- The "Overall" column is always rendered (since overall_score is mandatory by schema).
"""

from __future__ import annotations
import argparse
import json
import sys
from typing import Any, Dict, List, Optional, Iterable
from dataclasses import dataclass

# ---------- Data model ----------

@dataclass
class Canonical:
    """
    Six required labels plus a REQUIRED overall_score.
    Note: Label value normalization/validation is not enforced here; strings are printed as-is.
    """
    detail: str
    specificity: str
    usability: str
    clarity: str
    completeness: str
    relevance: str
    overall_score: int  # REQUIRED; must be an int in [0, 100]

@dataclass
class Record:
    """
    One input row from the JSONL source.
    """
    id: str
    question: str
    answer: str
    canonical: Canonical
    meta: Dict[str, Any]

# ---------- Utilities ----------

def _md_escape(text: str) -> str:
    """
    Minimal escaping for Markdown table cells.
    Only escapes pipe '|' to avoid column splits.
    If your content contains frequent newlines/backticks/HTML, consider extending:
      - replace '\n' with '<br>'
      - escape '`', '<', '>'
    """
    return (text or "").replace("|", "\\|")

def _read_jsonl(fp) -> Iterable[Dict[str, Any]]:
    """
    Stream-parse a JSONL file-like object.
    Skips blank lines, yields only dicts, warns on parse errors.
    """
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

def _parse_record(obj: Dict[str, Any], line_no: int) -> Optional[Record]:
    """
    Convert a raw dict into a Record.
    Strictly requires canonical.overall_score as int in [0, 100];
    otherwise logs a warning and returns None to skip the row.
    """
    rid = str(obj.get("id") or "")
    if not rid:
        print(f"[WARN] Missing 'id' at line {line_no}; skipping.", file=sys.stderr)
        return None

    q = str(obj.get("question") or "")
    a = str(obj.get("answer") or "")

    can = obj.get("canonical")
    if not isinstance(can, dict):
        print(f"[WARN] Missing or invalid 'canonical' for id={rid} (line {line_no}); skipping.", file=sys.stderr)
        return None

    ov = can.get("overall_score", None)
    if not isinstance(ov, int):
        print(f"[WARN] overall_score must be an int for id={rid} (line {line_no}); skipping.", file=sys.stderr)
        return None
    if ov < 0 or ov > 100:
        print(f"[WARN] overall_score out of range [0,100] for id={rid} (line {line_no}); skipping.", file=sys.stderr)
        return None

    cobj = Canonical(
        detail=can.get("detail", ""),
        specificity=can.get("specificity", ""),
        usability=can.get("usability", ""),
        clarity=can.get("clarity", ""),
        completeness=can.get("completeness", ""),
        relevance=can.get("relevance", ""),
        overall_score=ov,
    )

    meta = obj.get("meta") or {}
    return Record(id=rid, question=q, answer=a, canonical=cobj, meta=meta)

# ---------- Markdown rendering ----------

def render_markdown(records: List[Record], title: str) -> str:
    """
    Build README markdown.
    Always renders the 'Overall' column because overall_score is mandatory by schema.
    Prints a 'Common Meta' block only if all meta dicts are identical.
    """
    n = len(records)

    lines: List[str] = []
    lines.append(f"# {title}\n")
    lines.append(f"Items: **{n}**\n")
    lines.append("---\n")

    # Common Meta section: only if meta is identical across all records.
    lines.append("## Common Meta")
    if records and all(r.meta == records[0].meta for r in records):
        meta = records[0].meta
        for k, v in meta.items():
            lines.append(f"- **{_md_escape(str(k))}**: `{_md_escape(str(v))}`")
    else:
        lines.append("- (meta varies by record)")
    lines.append("\n---\n")

    # Table header (always includes Overall)
    lines.append("## Results\n")
    lines.append("| ID | Question | Answer | Specificity | Detail | Usability | Clarity | Completeness | Relevance | Overall |")
    lines.append("|---|---|---|---|---|---|---|---|---|---:|")

    # Rows
    for r in records:
        can = r.canonical
        lines.append(
            f"| **{_md_escape(r.id)}** | "
            f"{_md_escape(r.question)} | "
            f"{_md_escape(r.answer)} | "
            f"{can.specificity or '—'} | "
            f"{can.detail or '—'} | "
            f"{can.usability or '—'} | "
            f"{can.clarity or '—'} | "
            f"{can.completeness or '—'} | "
            f"{can.relevance or '—'} | "
            f"{can.overall_score} |"
        )

    # Reminder: we do not compute or adjust overall_score; it is taken as-is from input.
    lines.append("\n> **Note**: `overall_score` is required and shown as provided by input; the script does not compute or modify it.\n")

    return "\n".join(lines)

# ---------- Main ----------

def main() -> int:
    """
    CLI entry point.
    - Positional 'input' can be a file path or '-' to read from STDIN.
    - Writes a Markdown file with a strict 'Overall' column.
    """
    ap = argparse.ArgumentParser(description="Render strict 6-axis labels + required overall_score from JSONL into README.md (no computation).")
    ap.add_argument("input", help="Path to JSONL file or '-' for STDIN")
    ap.add_argument("--out", default="README.md", help="Output Markdown path (default: README.md)")
    ap.add_argument("--title", default="QA Evaluation Results (Labels + Overall; No Computation)",
                    help="Title for the README (default provided)")
    args = ap.parse_args()

    # Ingest JSONL
    if args.input == "-":
        objs = list(_read_jsonl(sys.stdin))
    else:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                objs = list(_read_jsonl(f))
        except FileNotFoundError:
            print(f"[ERROR] file not found: {args.input}", file=sys.stderr)
            return 1

    # Parse into Records (strict overall_score)
    records: List[Record] = []
    for idx, o in enumerate(objs, start=1):
        r = _parse_record(o, line_no=idx)
        if r:
            records.append(r)

    if not records:
        print("[ERROR] no valid records (all skipped or file empty).", file=sys.stderr)
        return 2

    # Render and write
    md = render_markdown(records, args.title)
    try:
        with open(args.out, "w", encoding="utf-8") as fw:
            fw.write(md)
    except Exception as e:
        print(f"[ERROR] failed to write output: {e}", file=sys.stderr)
        return 3

    print(f"[OK] wrote {args.out} ({len(records)} items)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
