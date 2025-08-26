#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jsonl_to_readme.py
------------------
`all.prompts.jsonl`（各行がJSON）のログをMarkdown形式のREADME.mdへ変換します。

仕様:
- item_id ごとにグルーピング（p1→p2→p3 を1セットとして折り畳み表示）
- kind="prompt" → Input、その他 → Output
- タイムスタンプ(tsキー/ISO8601/行頭のTimestampラベル)は削除
- p3 の Output が "final canonical json" または meta.canonical を含む場合は 🔥 ハイライト
- Question/Answer は **p0(kind=qa)** のみに存在する場合にタイトル下へ表示
"""

from __future__ import annotations
import json, re, sys
from pathlib import Path
from collections import defaultdict, OrderedDict
from typing import Dict, List, Any, Tuple, Optional

# ---- 正規表現: 時刻などを除去 ----
RE_TS_KEY = re.compile(r'"ts"\s*:\s*"[^"]*"\s*,?\s*')
RE_ISO_TIME = re.compile(r'\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})\b')
RE_LEADING_TIME_LABEL = re.compile(r'^\s*(Timestamp|Time|時刻)\s*:\s*.*$', re.IGNORECASE)

def sanitize_text(s: str) -> str:
    if not s: return ""
    out = RE_TS_KEY.sub("", s)
    out = RE_ISO_TIME.sub("", out)
    lines = out.splitlines()
    kept: List[str] = []
    for line in lines:
        if RE_LEADING_TIME_LABEL.match(line): continue
        if line.strip() in {",",";"}: continue
        kept.append(line)
    out = "\n".join(kept)
    out = re.sub(r'\n{3,}', '\n\n', out)
    return out.strip()

def natural_stage_key(stage: str) -> int:
    order = {"p1": 1, "p2": 2, "p3": 3}
    return order.get(str(stage).lower(), 99)

def try_extract_json(s: str) -> Optional[Dict[str, Any]]:
    if not s: return None
    start, end = s.find("{"), s.rfind("}")
    if start==-1 or end==-1 or end<=start: return None
    try: return json.loads(s[start:end+1])
    except: return None

def extract_canonical_json(meta: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not isinstance(meta, dict): return None
    for key in ("canonical","result","final","final_json"):
        if key in meta and isinstance(meta[key], dict):
            return meta[key]
    return None

def detect_final_canonical(stage:str, kind:str, text:str, meta:Optional[Dict[str,Any]]=None) -> Tuple[bool,Optional[Dict[str,Any]]]:
    if str(stage).lower()=="p3" and kind=="accepted":
        canonical = extract_canonical_json(meta)
        low = (text or "").lower()
        if "final canonical json" in low and canonical is not None: return True,canonical
        parsed = try_extract_json(text)
        if canonical is not None: return True,canonical
        if parsed is not None: return True,parsed
        if "final canonical json" in low: return True,None
    return False,None

def to_code_block(text:str, lang:str="text") -> str:
    return f"```{lang}\n{text}\n```"

def render_stage(stage:str, kind:str, text:str, meta:Optional[Dict[str,Any]]=None) -> str:
    role = "📝 Input" if kind=="prompt" else "💡 Output"
    title = f"### Stage `{stage}` — {role}\n"
    is_final, parsed = detect_final_canonical(stage,kind,text,meta)
    body: List[str] = []
    if is_final:
        title = f"### Stage `{stage}` — {role} 🔥 FINAL CANONICAL JSON\n\n"
        body.append("> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**\n")
        if parsed is not None:
            pretty = json.dumps(parsed,ensure_ascii=False,separators=(",",":"),indent=2)
            body.append(to_code_block(pretty,"json"))
            return title+"\n".join(body)+"\n"
    clean = sanitize_text(text or "")
    body.append(to_code_block(clean,"text"))
    return title+"\n".join(body)+"\n"

def main(infile:str,outfile:str)->None:
    src = Path(infile)
    lines = src.read_text(encoding="utf-8").splitlines()
    grouped: Dict[str,List[Dict[str,Any]]] = defaultdict(list)
    for line in lines:
        if not line.strip(): continue
        try: obj=json.loads(line)
        except: continue
        grouped[str(obj.get("item_id","")).strip() or "(no-id)"].append(obj)
    ordered=OrderedDict(sorted(grouped.items(), key=lambda kv: kv[0]))

    md: List[str] = ["# Prompt Log (Grouped Flow)\n",
                     "`all.prompts.jsonl` を解析し、p1→p2→p3 を1セットにまとめています。\n",
                     "\n---\n"]
    for idx,(item_id,entries) in enumerate(ordered.items(),1):
        md.append(f"## {idx}. Item `{item_id}`\n")

        # --- Q/A は p0(kind=qa) のみ ---
        p0 = next((e for e in entries if e.get("stage")=="p0" and e.get("kind")=="qa"),None)
        if p0:
            q_text,a_text=p0.get("question"),p0.get("answer")
            if q_text: md.append(f"**Question:** {sanitize_text(str(q_text))}  ")
            if a_text: md.append(f"**Answer:** {sanitize_text(str(a_text))}  ")
            md.append("\n")

        md.append("<details>\n<summary>Show this set</summary>\n\n")

        # qa（p0 kind=qa）は詳細出力には含めない
        non_qa_entries = [e for e in entries if not (e.get("stage")=="p0" and e.get("kind")=="qa")]

        # stage順, かつ kind=prompt(Input) を先
        entries_sorted = sorted(
            non_qa_entries,
            key=lambda e:(natural_stage_key(e.get("stage","")), 0 if e.get("kind")=="prompt" else 1)
        )

        for e in entries_sorted:
            stage=str(e.get("stage","")).lower() or "?"
            kind=str(e.get("kind","")).lower() or "?"
            text=e.get("text","") or e.get("content","") or ""
            md.append(render_stage(stage,kind,text,e.get("meta")))
            
        md.append("</details>\n\n---\n")

    Path(outfile).write_text("\n".join(md),encoding="utf-8")
    print(f"Wrote Markdown: {outfile}")

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: python jsonl_to_readme.py <in_jsonl> <out_md>")
        sys.exit(2)
    main(sys.argv[1],sys.argv[2])
