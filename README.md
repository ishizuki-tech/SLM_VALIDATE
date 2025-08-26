# README — Six-Axis QA Labeling Tool (Gemma / llama.cpp)

This repository evaluates a Q\&A pair on **six axes** — `detail`, `specificity`, `usability`, `clarity`, `completeness`, `relevance` — and returns a **single-line flat JSON** with allowed labels only:

`Very High`, `High`, `Medium`, `Low`, `Very Low`.

Everything is **model-only** (no heuristics) with strict JSON validation and an automatic **repair + retry** loop for the final step.

---

## Features

* Final output: **one line of JSON** with the six fields above.
* Hard constraints: **no code fences**, no extra text; validator enforces labels.
* Robust p1 → p2 → p3 chain:

  * p1/p2 produce “analysis-like” JSON.
  * p3 emits the final six-axis labels.
* Logging for prompts & outputs (JSONL), per-item logs optional.
* Works with **llama-cpp-python** and **Gemma GGUF** models.

---

## Requirements

* Python **3.9+**
* A compatible **.gguf** model (e.g., `gemma-3-1b-it-q4_k_m.gguf`)
* Packages:

  * `llama-cpp-python`
  * `rich` (optional but recommended for nicer CLI output)

---

## Quick Setup (with venv)

### 1) Create & activate a virtual environment

**macOS / Linux (bash/zsh):**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 2) Install dependencies

If you have a `requirements.txt`, simply:

```bash
pip install -r requirements.txt
```

Or install explicitly:

```bash
pip install -U llama-cpp-python rich
```

### 3) Place your model

Download/copy your GGUF model (e.g., `gemma-3-1b-it-q4_k_m.gguf`) and note its full path.

---

## Usage

### Single run with built-in sample

```bash
python main.py \
  --model /path/to/gemma-3-1b-it-q4_k_m.gguf \
  --try-defaults
```

### Single run with your own Q\&A

```bash
python main.py \
  --model /path/to/gemma-3-1b-it-q4_k_m.gguf \
  --try-defaults \
  --question "After planting, what share of seeds do you expect to grow into healthy plants?" \
  --answer   "Most of them came up fine."
```

### Print **only** the final one-line JSON

```bash
python main.py \
  --model /path/to/gemma-3-1b-it-q4_k_m.gguf \
  --try-defaults \
  --print-one-line
```

> `--score-only` is ignored in six-axis mode.

---

## Batch Mode (JSONL)

Prepare an input JSONL file (`data/input.jsonl`) where each line contains:

```json
{"id":"ex1","question":"Q text here","answer":"A text here"}
{"id":"ex2","question":"...","answer":"..."}
```

Run:

```bash
python main.py \
  --model /path/to/gemma-3-1b-it-q4_k_m.gguf \
  --input-jsonl data/input.jsonl \
  --output-jsonl runs/out.jsonl \
  --out-csv runs/out.csv \
  --prompts-jsonl runs/prompts.jsonl \
  --prompts-dir runs/prompts_by_id \
  --quiet-batch
```

* `--output-jsonl`: appends `{id, question, answer, canonical}`.
* `--out-csv`: appends tabular results with the six labels as columns.
* `--prompts-jsonl` / `--prompts-dir`: full prompt I/O logs.

---

## Final Output Schema

The final object must contain exactly these six keys, each with one of the five allowed labels:

```json
{
  "detail": "Very High|High|Medium|Low|Very Low",
  "specificity": "Very High|High|Medium|Low|Very Low",
  "usability": "Very High|High|Medium|Low|Very Low",
  "clarity": "Very High|High|Medium|Low|Very Low",
  "completeness": "Very High|High|Medium|Low|Very Low",
  "relevance": "Very High|High|Medium|Low|Very Low"
}
```

The tool strictly validates this and will repair/retry if the model deviates.

---

## Notable CLI Options

* `--ctx` (default: 1024): context length
* `--threads` (default: 4): CPU threads
* `--gpu-layers`: number of layers to offload (if using GPU build)
* `--max-tokens`: max tokens for p1/p2
* `--max-tokens-final`: max tokens for p3 (default clamps to 120..400 around `--max-tokens`)
* `--temp` (default: 0.0): temperature
* `--top-k`, `--top-p`: sampling settings
* `--fallback-policy` (`retry-only` | `none`): final repair strategy
* `--final-retries` (default: 3): max p3 retries
* `--no-rich`: disable rich UI
* `--quiet-batch`: suppress per-item output during batch

---

## Troubleshooting

* **Model fails to load**
  Ensure your `llama-cpp-python` install matches your platform (CPU vs GPU builds), and that the model path is correct.

* **“unsupported call signature”**
  The adapter tries several llama-cpp call paths. If your environment exposes a different entrypoint, adjust `LlamaAdapter.generate()` accordingly.

* **Code fences or stray text in outputs**
  The sanitizer strips code fences; the validator enforces one-line JSON. If your model still struggles, lower temperature (`--temp 0.0`), and consider using grammar control (see below).

* **Forbidden labels like “Nearly Nothing”**
  The final validator rejects them and triggers a repair pass. To hard-prevent this, use a grammar constraint.

---

## (Optional) Stronger Constraining with Grammar

If you use llama.cpp’s grammar feature, you can restrict p3 to **exactly** the six keys and five labels. Example GBNF:

```bnf
root ::= "{" ws
  "\"detail\":" ws label "," ws
  "\"specificity\":" ws label "," ws
  "\"usability\":" ws label "," ws
  "\"clarity\":" ws label "," ws
  "\"completeness\":" ws label "," ws
  "\"relevance\":" ws label
  ws "}"

label ::= "\"" enum_label "\""
enum_label ::= "Very High" | "High" | "Medium" | "Low" | "Very Low"
ws ::= (" " | "\t")*
```

Pass it via your llama-cpp binding (e.g., `grammar=...`) for the p3 call to prevent invalid strings at generation time.

---

## Tips for Better Stability

* Keep `--temp 0.0` to reduce drift; try `0.1–0.2` if outputs are too “Medium”.
* Increase `--max-tokens-final` if p3 truncates.
* Provide concrete Q\&A for stronger signals: numbers, steps, conditions, definitions, constraints, examples.

---

## License

See `LICENSE` for this code. Model files and dependencies follow their own licenses.
