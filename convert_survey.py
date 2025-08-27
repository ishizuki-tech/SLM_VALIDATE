#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert survey TSV into JSONL.
- 列名の末尾スペースやノーブレークスペース(NBSP)を自動除去
- 各行を {"id","category","question","answer","completeness","followup"} に変換
"""

import csv
import json
import sys

def normalize_fieldnames(fieldnames):
    """列名を正規化（strip + NBSP削除）"""
    if not fieldnames:
        return []
    return [fn.replace("\u00a0", " ").strip() if fn else "" for fn in fieldnames]

def convert_csv_to_jsonl(input_file: str, output_file: str) -> None:
    with open(input_file, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")

        # 列名を正規化して上書き
        reader.fieldnames = normalize_fieldnames(reader.fieldnames)

        with open(output_file, "w", encoding="utf-8") as out:
            for i, row in enumerate(reader, start=1):
                # 各行のキーも正規化して安全にする
                cleaned_row = {k.replace("\u00a0", " ").strip(): (v or "").strip()
                               for k, v in row.items()}

                obj = {
                    "id": f"q{i:03d}",
                    "category": cleaned_row.get("Category", ""),
                    "question": cleaned_row.get("Survey Question", ""),
                    "answer": cleaned_row.get("Provided Answer", ""),
                    "completeness": cleaned_row.get("Completeness Theme", ""),
                    "followup": cleaned_row.get("Follow-up Question", "")
                }
                out.write(json.dumps(obj, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_survey.py input.tsv output.jsonl")
        sys.exit(1)

    convert_csv_to_jsonl(sys.argv[1], sys.argv[2])
