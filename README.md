# QA Evaluation Results (Model-Only, Pure-JSON)

This README summarizes the **final canonical JSON** produced by a 3-stage evaluator in an easy-to-read format.  
Items: **10** / Average final score: **70.9 / 100**

---

## Common Meta
- **model_path**: `gemma-3-1b-it-q4_k_m.gguf`
- **n_ctx**: `1024`
- **n_threads**: `4`
- **n_gpu_layers**: `—`
- **fallback_policy**: `retry-only`
- **final_retries**: `3`
- **top_k**: `—`
- **top_p**: `—`

---

## How to read the scores (summary)
- Labels: **Very High / High / Medium / Low / Very Low**  
- Unit mapping (0..1): VH=0.95, H=0.80, M=0.60, L=0.40, VL=0.20  
- Weights: **specificity 0.35 / detail 0.40 / usability 0.25**  
- `weighted_base_0_100 = 100 × (0.35×S + 0.40×D + 0.25×U)` (1 decimal place)  
- `penalty = min(3 × number_of_weaknesses, 15)`  
- `final_score_0_100 = round(clamp(weighted_base_0_100 − penalty, 0..100))`

---

## Results

| ID | Question | Answer | Labels (S / D / U) | weighted_base | penalty | final |
|---|---|---|---|---:|---:|---:|
| **q001** | After planting, what share of seeds do you expect to grow into healthy plants? | Most of them came up fine. | **High / Low / High** | **64.0** | **0** | **64** |
| **q002** | After planting, what share of seeds do you expect to grow into healthy plants? | Better than last year. | **Medium / Medium / Medium** | **60.0** | **0** | **60** |
| **q003** | After planting, what share of seeds do you expect to grow into healthy plants? | Only a few gaps here and there. | **Medium / Medium / Medium** | **60.0** | **0** | **60** |
| **q004** | After planting, what share of seeds do you expect to grow into healthy plants? | About 80%. | **Medium / Medium / Medium** | **60.0** | **0** | **60** |
| **q005** | After planting, what share of seeds do you expect to grow into healthy plants? | Almost all. | **Very High / High / Very High** | **89.0** | **0** | **89** |
| **q006** | After planting, what share of seeds do you expect to grow into healthy plants? | Good stand in the upper half of the field. | **Medium / Medium / Medium** | **60.0** | **0** | **60** |
| **q007** | After planting, what share of seeds do you expect to grow into healthy plants? | At least 85% of seeds should be healthy by day 14 after planting. | **Medium / Medium / Medium** | **60.0** | **0** | **60** |
| **q008** | After planting, what share of seeds do you expect to grow into healthy plants? | 90% survival by two weeks, counted against my target spacing. | **High / High / Very High** | **83.8** | **0** | **84** |
| **q009** | After planting, what share of seeds do you expect to grow into healthy plants? | Not less than 45,000 plants/ha by 14 days. | **Very High / Medium / High** | **77.2** | **0** | **77** |
| **q010** | After planting, what share of seeds do you expect to grow into healthy plants? | I bought certified seed this time. | **Very High / Very High / Very High** | **95.0** | **0** | **95** |

> **Note**: S=Specificity, D=Detail, U=Usability

---

## Notes
- Values are copied directly from the already **canonicalized final JSON**; no recalculation is performed here.
- `penalty` typically reflects deductions based on the number of listed weaknesses (max 15). If no weaknesses array is present in p2, many implementations treat it as 0.
- When meta is identical across runs, you can use this table to monitor drift in answer quality.
