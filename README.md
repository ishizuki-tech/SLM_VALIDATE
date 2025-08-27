# Six-Axis QA Labeler (Gemma/llama.cpp) — Strict JSON + Markdown Renderer

Evaluate short Q\&A answers on **six qualitative axes** and produce strict, machine-readable JSONL. Then render a compact **README.md** from those results. Designed to run **fully locally** with `llama.cpp` models (e.g., Gemma GGUF), enforce a **strict final schema**, and keep outputs auditable via structured prompt logs.

---

## What it does

* **Model-only evaluator** (`main.py`)

  * 3-stage prompt chain (p1 → p2 → p3) labels:

    * `detail`, `specificity`, `usability`, `clarity`, `completeness`, `relevance`
  * Produces a **final canonical JSON** per item, including a **required** integer `overall_score`.
  * Robust JSON sanitation/extraction (no prose, no fences) + strict validation.
  * Optional Rich TUI output and detailed prompt I/O logging.

* **README renderer** (`jsonl_to_readme.py`)

  * Reads evaluator JSONL and builds a clean **Markdown table**.
  * **Does not compute** `overall_score`. It assumes every record already includes it (else the row is skipped in the strict build).
  * Emits a “Common Meta” section when all rows share identical `meta`.

---

## Final JSON schema (strict)

Each evaluated item must end with this flat object:

```json
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "High",
  "clarity": "Medium",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 77
}
```

**Allowed labels (case-sensitive):** `Very High`, `High`, `Medium`, `Low`, `Very Low`
**`overall_score`:** required; integer in **\[0, 100]**.

> In the evaluator (`main.py`), `overall_score` is intended as the **equal-weight average** of the six labels mapped to points (`Very High=95`, `High=80`, `Medium=60`, `Low=40`, `Very Low=20`), rounded to an int and clamped to `[0,100]`.
> The renderer **never computes** or adjusts it; it only displays what’s in the JSONL.

---

## Repository layout

* `main.py` — model-only evaluator (3-stage prompts, strict final JSON, prompt logging).
* `jsonl_to_readme.py` — converts JSONL results into `README.md`.
* `prompts.jsonl` (optional) — per-question prompt overrides for p1/p2/p3.

---

## Installation

**Requirements**

* Python 3.9+ (3.10/3.11 recommended)
* `llama-cpp-python` (local inference)
* Optional: `rich` for better terminal UI

```bash
pip install --upgrade llama-cpp-python rich
```

> You’ll need a local `.gguf` model compatible with `llama.cpp`.

---

## Using the evaluator (`main.py`)

### Single item (quick run)

```bash
python main.py \
  --model ./models/your-model.gguf \
  --try-defaults \
  --question "After planting, what share of seeds do you expect to grow into healthy plants?" \
  --answer   "Most of them came up fine."
```

### Batch mode (JSONL input → JSONL/CSV output)

```bash
python main.py \
  --model ./models/your-model.gguf \
  --input-jsonl data/qas.jsonl \
  --output-jsonl results.jsonl \
  --out-csv results.csv \
  --prompts-jsonl logs/prompts.jsonl \
  --prompts-dir logs/per_item \
  --batch-continue-on-error
```

**Input JSONL (one object per line):**

```json
{"id":"q001","question":"...","answer":"..."}
```

**Output JSONL (from evaluator):**

```json
{
  "id":"q001",
  "question":"...",
  "answer":"...",
  "canonical":{
    "detail":"Medium","specificity":"Low","usability":"Low",
    "clarity":"High","completeness":"Medium","relevance":"High",
    "overall_score":60
  },
  "meta":{
    "model_path":"./models/your-model.gguf",
    "n_ctx":1024,
    "n_threads":4,
    "n_gpu_layers":null,
    "fallback_policy":"retry-only",
    "final_retries":3,
    "top_k":null,
    "top_p":null
  }
}
```

---

## Rendering a README (`jsonl_to_readme.py`)

This tool **does not compute** `overall_score`. Every record should already include a **valid integer** `overall_score` in `[0,100]`. Invalid rows are skipped.

```bash
python jsonl_to_readme.py results.jsonl --out README.md \
  --title "QA Evaluation Results (Labels + Overall; No Computation)"
```

Generated README includes:

* Title and item count
* “Common Meta” (only if all rows share the same `meta`)
* Results table: `Specificity | Detail | Usability | Clarity | Completeness | Relevance | Overall`

---

## GitHub Actions — CI/CD Examples

Below are two practical workflows. Copy them into `.github/workflows/`.

### 1) Render README on changes to `results.jsonl` (fast, no model)

Renders the Markdown table whenever `results.jsonl` changes and auto-commits `README.md`. This workflow **does not run the model**.

**Notes**

* Uses only `rich` and Python; no `llama-cpp-python` needed.
* Auto-commits via the built-in `GITHUB_TOKEN`.

---

### 2) Evaluate with the model, then render (manual, heavy)

Runs the evaluator (downloads a model), writes `results.jsonl`/`results.csv`, renders `OUTPUT.md`, and commits changes. Triggered manually to avoid heavy CI usage.

```yaml
# .github/workflows/slm-validate.yml
name: Evaluate and Render

on:
  workflow_dispatch:
    inputs:
      model_url:
        description: "Direct URL to GGUF model (authenticated if needed)"
        required: true
      input_jsonl_path:
        description: "Path to input Q/A JSONL in repo (e.g., data/qas.jsonl)"
        required: true
        default: "data/qas.jsonl"

jobs:
  eval:
    runs-on: ubuntu-latest
    timeout-minutes: 120
    steps:
      - name: Check out
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps (evaluator + renderer)
        run: |
          python -m pip install --upgrade pip
          pip install llama-cpp-python rich

      - name: Prepare model directory
        run: mkdir -p models

      - name: Download model
        env:
          MODEL_URL: ${{ inputs.model_url }}
        run: |
          curl -L --fail --retry 5 --retry-all-errors -o models/model.gguf "$MODEL_URL"
          ls -lh models

      - name: Run evaluator (JSONL + CSV)
        env:
          INPUT_JSONL: ${{ inputs.input_jsonl_path }}
        run: |
          python main.py \
            --model models/model.gguf \
            --input-jsonl "$INPUT_JSONL" \
            --output-jsonl results.jsonl \
            --out-csv results.csv \
            --prompts-dir logs/per_item \
            --prompts-jsonl logs/prompts.jsonl \
            --batch-continue-on-error

      - name: Render README
        run: |
          python jsonl_to_readme.py results.jsonl \
            --out OUTPUT.md \
            --title "QA Evaluation Results (Labels + Overall; No Computation)"

      - name: Upload artifacts (results & logs)
        uses: actions/upload-artifact@v4
        with:
          name: evaluation-artifacts
          path: |
            results.jsonl
            results.csv
            OUTPUT.md
            logs/**

      - name: Commit results if changed
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "feat(eval): update results.jsonl/OUTPUT.md"
          file_pattern: |
            results.jsonl
            results.csv
            OUTPUT.md
            logs/**
```

**Notes**

* **Model hosting:** provide a direct download URL via `workflow_dispatch` input, or store a URL in a repository secret and reference it (e.g., `secrets.MODEL_URL`). Large models should **not** live in the repo; prefer object storage or Releases.
* If your model requires extra system packages (e.g., BLAS/OpenMP), add an `apt-get` step accordingly.
* You can swap `curl` for authenticated downloads (AWS S3, GCS, Hugging Face, etc.).

---

## Tips & Gotchas

* Extremely long `question`/`answer` cells make Markdown wide; consider truncating upstream or teaching the renderer to replace `\n` with `<br>`.
* The renderer is strict about `overall_score`: it **does not compute** or fix it; invalid/missing scores are skipped (in the strict variant).
* For faster CI cycles, separate **render-only** workflow (cheap) from **inference** workflow (expensive & manual).
* Use `--fallback-policy retry-only` and `--final-retries` to let the evaluator self-repair invalid JSON from the model.

---

## Example table (snippet)

```
| ID   | Question ... | Answer ... | Specificity | Detail | Usability | Clarity | Completeness | Relevance | Overall |
|------|--------------|------------|-------------|--------|-----------|---------|--------------|-----------|--------:|
| q001 | ...          | ...        | Low         | Low    | Low       | Low     | Low          | Medium    |     43 |
```

> The `Overall` value is shown **as provided** by the evaluator output.

---

## License

Add your preferred license (e.g., MIT or Apache-2.0).
