# QA Evaluation Results (Model-Only, Pure-JSON)

Items: **15**

---

## Common Meta
- **model_path**: `./models/gemma-3-1b-it-q4_k_m.gguf`
- **n_ctx**: `1024`
- **n_threads**: `4`
- **n_gpu_layers**: `None`
- **fallback_policy**: `retry-only`
- **final_retries**: `3`
- **top_k**: `None`
- **top_p**: `None`

---

## Results

| ID | Question | Answer | Specificity | Detail | Usability | Clarity | Completeness | Relevance | Overall |
|---|---|---|---|---|---|---|---|---|---:|
| **q001** | After planting, what share of seeds do you expect to grow into healthy plants? | I planted more seeds this year | Low | Low | Low | Low | Low | Medium | 43 |
| **q002** | After planting, what share of seeds do you expect to grow into healthy plants? | Better than last year. | Low | Low | Low | Low | Low | Medium | 43 |
| **q003** | After planting, what share of seeds do you expect to grow into healthy plants? | Only a few gaps here and there. | Low | Low | Low | Low | Low | Low | 40 |
| **q004** | After planting, what share of seeds do you expect to grow into healthy plants? | The stand is adequate | Low | Low | Low | Low | Low | Medium | 43 |
| **q005** | After planting, what share of seeds do you expect to grow into healthy plants? | Almost all. | Medium | High | Low | High | Medium | High | 67 |
| **q006** | After planting, what share of seeds do you expect to grow into healthy plants? | Good stand in the upper half of the field. | Low | Low | Low | Low | Low | Medium | 43 |
| **q007** | After planting, what share of seeds do you expect to grow into healthy plants? | At least 85% of seeds should be healthy by day 14 after planting. | High | Medium | High | High | High | High | 77 |
| **q008** | After planting, what share of seeds do you expect to grow into healthy plants? | 90% survival by two weeks, counted against my target spacing. | Very Low | High | Low | Medium | High | High | 60 |
| **q009** | After planting, what share of seeds do you expect to grow into healthy plants? | Not less than 45,000 plants/ha by 14 days. | High | Very Low | Low | Low | Low | High | 50 |
| **q010** | After planting, what share of seeds do you expect to grow into healthy plants? | I bought certified seed this time. | Low | Low | Low | Low | Low | Medium | 43 |
| **q011** | After planting, what share of seeds do you expect to grow into healthy plants? | We planted right after the first big rain. | Low | Low | Low | Low | Low | Medium | 43 |
| **q012** | After planting, what share of seeds do you expect to grow into healthy plants? | I used a jab planter instead of a hoe. | Low | Low | Low | Low | Low | Medium | 43 |
| **q013** | After planting, what share of seeds do you expect to grow into healthy plants? | Most of them. | Very Low | High | Low | High | Medium | High | 60 |
| **q014** | After planting, what share of seeds do you expect to grow into healthy plants? | I am satisfied with my crop this year. | Low | Low | Low | Low | Low | Medium | 43 |
| **q015** | After planting, what share of seeds do you expect to grow into healthy plants? | A good stand overall. | Medium | High | High | Medium | Medium | High | 70 |

> **Note**: `overall_score` is required and shown as provided by input; the script does not compute or modify it.
