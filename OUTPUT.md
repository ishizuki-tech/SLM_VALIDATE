# QA Evaluation Results (Model-Only).

This README summarizes the **final canonical JSON** produced by a 3-stage evaluator in an easy-to-read format.  
Items: **30** / Average final score: **— / 100**

---

## Common Meta
- **model_path**: `./models/gemma-3-1b-it-q4_k_m.gguf`
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
| **q001** | After planting, what share of seeds do you expect to grow into healthy plants? | I expect about 70% to germinate and roughly 60% to reach healthy seedling stage. | **? / ? / ?** | **—** | **—** | **—** |
| **q002** | How many weeks until seedlings are ready to transplant? | Typically 3 to 4 weeks, depending on temperature and watering. | **? / ? / ?** | **—** | **—** | **—** |
| **q003** | Did you use treated seed or untreated seed? | We used treated seed coated with fungicide. | **? / ? / ?** | **—** | **—** | **—** |
| **q004** | What is your expected survival rate under drought conditions? | Under severe drought I would estimate 30-40% survival; with occasional rains maybe 60%. | **? / ? / ?** | **—** | **—** | **—** |
| **q005** | Describe any problems observed after emergence. | Some damping-off in low patches and several seedlings were damaged by birds on the first night. | **? / ? / ?** | **—** | **—** | **—** |
| **q006** | What fertilizer regimen did you use? | We applied NPK (10-20-10) at planting and side-dressed with urea (46%) three weeks later. | **? / ? / ?** | **—** | **—** | **—** |
| **q007** | How uniform was germination across the field? | Germination was fairly uniform, about ±5% variation across plots. | **? / ? / ?** | **—** | **—** | **—** |
| **q008** | Did you perform any pest control measures? | Yes — one foliar spray for aphids at 2 weeks and manual removal of caterpillars. | **? / ? / ?** | **—** | **—** | **—** |
| **q009** | How deep were the seeds planted? | Planted at approximately 2.5 cm depth in well-prepared seedbeds. | **? / ? / ?** | **—** | **—** | **—** |
| **q010** | Anything else to note about planting conditions? | Soil was loamy with good drainage; night temps were around 15–18°C during emergence. | **? / ? / ?** | **—** | **—** | **—** |
| **q011** | How many weeks until seedlings are ready to transplant? | Typically 3 to 4 weeks, depending on temperature and watering. | **? / ? / ?** | **—** | **—** | **—** |
| **q012** | Describe any problems observed after emergence. | Some damping-off in low patches and several seedlings were damaged by birds on the first night. | **? / ? / ?** | **—** | **—** | **—** |
| **q013** | What is your expected survival rate under drought conditions? | Under severe drought I would estimate 30-40% survival; with occasional rains maybe 60%. | **? / ? / ?** | **—** | **—** | **—** |
| **q014** | How many weeks until seedlings are ready to transplant? | About 3 weeks under ideal greenhouse conditions. | **? / ? / ?** | **—** | **—** | **—** |
| **q015** | How deep were the seeds planted? | Planted at approximately 2.5 cm depth in well-prepared seedbeds. | **? / ? / ?** | **—** | **—** | **—** |
| **q016** | Anything else to note about planting conditions? | We planted after light rains; soil moisture was optimal for germination. | **? / ? / ?** | **—** | **—** | **—** |
| **q017** | After planting, what share of seeds do you expect to grow into healthy plants? | I expect about 70% to germinate and roughly 60% to reach healthy seedling stage. | **? / ? / ?** | **—** | **—** | **—** |
| **q018** | How many weeks until seedlings are ready to transplant? | Typically 3 to 4 weeks, depending on temperature and watering. | **? / ? / ?** | **—** | **—** | **—** |
| **q019** | What is your expected survival rate under drought conditions? | Hard to be exact, but roughly 35-55% depending on severity. | **? / ? / ?** | **—** | **—** | **—** |
| **q020** | Anything else to note about planting conditions? | Soil was loamy with good drainage; night temps were around 15–18°C during emergence. | **? / ? / ?** | **—** | **—** | **—** |
| **q021** | How deep were the seeds planted? | Planted at approximately 2.5 cm depth in well-prepared seedbeds. | **? / ? / ?** | **—** | **—** | **—** |
| **q022** | How deep were the seeds planted? | About 1 to 3 cm depending on seed size; average ~2 cm. | **? / ? / ?** | **—** | **—** | **—** |
| **q023** | What is your expected survival rate under drought conditions? | If drought persists, survival could be as low as 25%; with light rains around 50%. | **? / ? / ?** | **—** | **—** | **—** |
| **q024** | Anything else to note about planting conditions? | We planted after light rains; soil moisture was optimal for germination. | **? / ? / ?** | **—** | **—** | **—** |
| **q025** | After planting, what share of seeds do you expect to grow into healthy plants? | I expect about 70% to germinate and roughly 60% to reach healthy seedling stage. | **? / ? / ?** | **—** | **—** | **—** |
| **q026** | How uniform was germination across the field? | There were some low spots with poorer germination, overall ~10% variability. | **? / ? / ?** | **—** | **—** | **—** |
| **q027** | Describe any problems observed after emergence. | Some damping-off in low patches and several seedlings were damaged by birds on the first night. | **? / ? / ?** | **—** | **—** | **—** |
| **q028** | What is your expected survival rate under drought conditions? | If drought persists, survival could be as low as 25%; with light rains around 50%. | **? / ? / ?** | **—** | **—** | **—** |
| **q029** | How many weeks until seedlings are ready to transplant? | Typically 3 to 4 weeks, depending on temperature and watering. | **? / ? / ?** | **—** | **—** | **—** |
| **q030** | How uniform was germination across the field? | Germination was fairly uniform, about ±5% variation across plots. | **? / ? / ?** | **—** | **—** | **—** |

> **Note**: S=Specificity, D=Detail, U=Usability

---

## Notes
- Values are copied directly from the already **canonicalized final JSON**; no recalculation is performed here.
- `penalty` typically reflects deductions based on the number of listed weaknesses (max 15). If no weaknesses array is present in p2, many implementations treat it as 0.
- When meta is identical across runs, you can use this table to monitor drift in answer quality.
