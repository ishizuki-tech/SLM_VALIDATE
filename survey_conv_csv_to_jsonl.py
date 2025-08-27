#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
convert_early_maturity_csv_to_jsonl.py

Convert a CSV like below into JSONL:
Header (example):
  Category,Survey Question,Aspired answer,Provided Answer,Provided Answer,Follow-up Question

- The CSV has two "Provided Answer" columns:
  * The FIRST  "Provided Answer" = the respondent's answer (string)
  * The SECOND "Provided Answer" = status/completeness label (e.g., "Complete", "incomplete")
- "Follow-up Question" may be blank if status is complete.

Output JSONL schema per row:
{
  "category":           str,
  "question":           str,
  "aspired_answer":     str,
  "provided_answer":    str,
  "status":             str,            # e.g., "Complete", "incomplete", "Simple but incomplete"
  "followup_question":  str or null
}

Usage:
  python convert_early_maturity_csv_to_jsonl.py -i input.csv -o output.jsonl
  # or pipe:
  cat input.csv | python convert_early_maturity_csv_to_jsonl.py > output.jsonl

Notes:
- Robust to BOM (UTF-8-SIG) and non-breaking spaces in headers.
- Ignores case, spaces, hyphens when matching header names.
- If a field is missing in a row, it becomes "" (or null for followup_question).
"""

from __future__ import annotations
import sys, csv, json, argparse, re
from typing import List, Dict, Optional, Tuple, Any, Iterable

NBSP = "\u00A0"

def normalize_header(s: str) -> str:
    """Normalize header: lower, strip, collapse spaces, remove hyphens/underscores, replace NBSP."""
    if s is None:
        return ""
    t = s.replace(NBSP, " ").strip().lower()
    t = re.sub(r"[\s\-_]+", " ", t)  # collapse to single space
    t = t.replace("-", " ")          # just in case
    t = re.sub(r"\s+", " ", t)
    return t

def canonical_key(s: str) -> str:
    """Map normalized header to a canonical key used internally."""
    t = normalize_header(s)
    # unify variants
    if t in {"category"}:
        return "category"
    if t in {"survey question", "question"}:
        return "question"
    if t in {"aspired answer", "aspired", "target answer", "gold answer"}:
        return "aspired_answer"
    if t in {"follow up question", "follow-up question", "followup question"}:
        return "followup_question"
    if t in {"provided answer", "answer"}:
        return "provided_answer"  # note: we will resolve duplicates by index/position
    return t  # fallback (still normalized)

def resolve_header_indices(headers: List[str]) -> Dict[str, Any]:
    """
    Figure out which columns correspond to which fields.
    Special-case duplicate 'provided answer': first = provided_answer, second = status.
    Returns a dict with indices for keys: category, question, aspired_answer, provided_answer, status, followup_question.
    """
    norm = [canonical_key(h) for h in headers]
    idx = {
        "category": None,
        "question": None,
        "aspired_answer": None,
        "provided_answer": None,
        "status": None,
        "followup_question": None,
    }

    # Basic singles
    def find_first(name: str) -> Optional[int]:
        try:
            return norm.index(name)
        except ValueError:
            return None

    idx["category"] = find_first("category")
    idx["question"] = find_first("question")
    idx["aspired_answer"] = find_first("aspired_answer")
    idx["followup_question"] = find_first("followup_question")

    # Handle the duplicate Provided Answer columns by position
    provided_positions = [i for i, n in enumerate(norm) if n == "provided_answer"]
    if len(provided_positions) >= 1:
        idx["provided_answer"] = provided_positions[0]
    if len(provided_positions) >= 2:
        # treat the second provided answer column as the status/completeness label
        idx["status"] = provided_positions[1]

    return idx

def safe_get(row: List[str], i: Optional[int]) -> str:
    if i is None:
        return ""
    if i < 0 or i >= len(row):
        return ""
    return (row[i] or "").strip()

def row_to_record(row: List[str], idx: Dict[str, Optional[int]]) -> Dict[str, Any]:
    category = safe_get(row, idx.get("category"))
    question = safe_get(row, idx.get("question"))
    aspired = safe_get(row, idx.get("aspired_answer"))
    provided = safe_get(row, idx.get("provided_answer"))
    status = safe_get(row, idx.get("status"))
    followup = safe_get(row, idx.get("followup_question"))
    if followup == "":
        followup_val: Optional[str] = None
    else:
        followup_val = followup

    return {
        "category": category,
        "question": question,
        "aspired_answer": aspired,
        "answer": provided,
        "completeness": status,
        "followup": followup_val,
    }

def convert_csv_to_jsonl(in_stream, out_stream) -> None:
    # Detect BOM by using utf-8-sig at the file-opening layer; if we're given an already-open
    # text stream, we just read via csv.reader. Here, we assume caller passed text mode.
    reader = csv.reader(in_stream)
    # Read header
    try:
        headers = next(reader)
    except StopIteration:
        return

    # Normalize NBSPs in header cells
    headers = [h.replace(NBSP, " ") if isinstance(h, str) else h for h in headers]
    idx = resolve_header_indices(headers)

    # Warn to stderr if key columns look missing
    required = ["category", "question", "aspired_answer", "provided_answer"]
    missing = [k for k in required if idx.get(k) is None]
    if missing:
        sys.stderr.write(f"[WARN] Missing columns inferred for: {', '.join(missing)}. Rows will use empty strings.\n")

    for row in reader:
        # Skip completely empty rows
        if not any(cell.strip() for cell in row if isinstance(cell, str)):
            continue
        rec = row_to_record(row, idx)
        out_stream.write(json.dumps(rec, ensure_ascii=False) + "\n")

def main():
    ap = argparse.ArgumentParser(description="Convert Early Maturity CSV → JSONL")
    ap.add_argument("-i", "--input", help="Input CSV file (default: stdin)")
    ap.add_argument("-o", "--output", help="Output JSONL file (default: stdout)")
    args = ap.parse_args()

    # Open input
    if args.input:
        in_f = open(args.input, "r", encoding="utf-8-sig", newline="")
        close_in = True
    else:
        in_f = sys.stdin
        close_in = False

    # Open output
    if args.output:
        out_f = open(args.output, "w", encoding="utf-8", newline="")
        close_out = True
    else:
        out_f = sys.stdout
        close_out = False

    try:
        convert_csv_to_jsonl(in_f, out_f)
    finally:
        if close_in:
            in_f.close()
        if close_out:
            out_f.close()

if __name__ == "__main__":
    main()
