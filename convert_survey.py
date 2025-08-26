#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert survey TSV (Category, Survey Question, Provided Answer)
into JSON Lines format like:

{"id": "q001", "question": "...", "answer": "..."}

Usage:
  python convert_survey.py input.tsv output.jsonl
"""

import csv
import json
import sys

def convert_csv_to_jsonl(input_file: str, output_file: str) -> None:
    with open(input_file, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = list(reader)

    with open(output_file, "w", encoding="utf-8") as out:
        for i, row in enumerate(rows, start=1):
            obj = {
                "id": f"q{i:03d}",
                "question": row["Survey Question"].strip(),
                "answer": row["Provided Answer"].strip()
            }
            out.write(json.dumps(obj, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_survey.py input.tsv output.jsonl")
        sys.exit(1)

    convert_csv_to_jsonl(sys.argv[1], sys.argv[2])
