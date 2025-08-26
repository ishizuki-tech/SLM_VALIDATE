# QA Evaluation Results (Model-Only, Pure-JSON)

This README summarizes the **final canonical JSON** produced by a 3-stage evaluator in an easy-to-read format.  
Items: **150** / Average final score: **— / 100**

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
| **q001** | After planting, what share of seeds do you expect to grow into healthy plants? | Most of them came up fine. | **? / ? / ?** | **—** | **—** | **—** |
| **q002** | After planting, what share of seeds do you expect to grow into healthy plants? | Better than last year. | **? / ? / ?** | **—** | **—** | **—** |
| **q003** | After planting, what share of seeds do you expect to grow into healthy plants? | Only a few gaps here and there. | **? / ? / ?** | **—** | **—** | **—** |
| **q004** | After planting, what share of seeds do you expect to grow into healthy plants? | About 80%. | **? / ? / ?** | **—** | **—** | **—** |
| **q005** | After planting, what share of seeds do you expect to grow into healthy plants? | Almost all. | **? / ? / ?** | **—** | **—** | **—** |
| **q006** | After planting, what share of seeds do you expect to grow into healthy plants? | Good stand in the upper half of the field. | **? / ? / ?** | **—** | **—** | **—** |
| **q007** | After planting, what share of seeds do you expect to grow into healthy plants? | At least 85% of seeds should be healthy by day 14 after planting. | **? / ? / ?** | **—** | **—** | **—** |
| **q008** | After planting, what share of seeds do you expect to grow into healthy plants? | 90% survival by two weeks, counted against my target spacing. | **? / ? / ?** | **—** | **—** | **—** |
| **q009** | After planting, what share of seeds do you expect to grow into healthy plants? | Not less than 45,000 plants/ha by 14 days. | **? / ? / ?** | **—** | **—** | **—** |
| **q010** | After planting, what share of seeds do you expect to grow into healthy plants? | I bought certified seed this time. | **? / ? / ?** | **—** | **—** | **—** |
| **q011** | After planting, what share of seeds do you expect to grow into healthy plants? | We planted right after the first big rain. | **? / ? / ?** | **—** | **—** | **—** |
| **q012** | After planting, what share of seeds do you expect to grow into healthy plants? | I used a jab planter instead of a hoe. | **? / ? / ?** | **—** | **—** | **—** |
| **q013** | After planting, what share of seeds do you expect to grow into healthy plants? | Most of them. | **? / ? / ?** | **—** | **—** | **—** |
| **q014** | After planting, what share of seeds do you expect to grow into healthy plants? | Around eight out of ten. | **? / ? / ?** | **—** | **—** | **—** |
| **q015** | After planting, what share of seeds do you expect to grow into healthy plants? | A good stand overall. | **? / ? / ?** | **—** | **—** | **—** |
| **q016** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | Enough to shade most weeds. | **? / ? / ?** | **—** | **—** | **—** |
| **q017** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | I like it looking ‘closed’ by then. | **? / ? / ?** | **—** | **—** | **—** |
| **q018** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | Shouldn’t see much bare soil. | **? / ? / ?** | **—** | **—** | **—** |
| **q019** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | About three-quarters. | **? / ? / ?** | **—** | **—** | **—** |
| **q020** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | More than half. | **? / ? / ?** | **—** | **—** | **—** |
| **q021** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | Good cover in the center rows. | **? / ? / ?** | **—** | **—** | **—** |
| **q022** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | At least 70% ground cover at 6 weeks. | **? / ? / ?** | **—** | **—** | **—** |
| **q023** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | 75–80% canopy closure by week 6 at midday. | **? / ? / ?** | **—** | **—** | **—** |
| **q024** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | No less than 70% cover at six weeks after planting. | **? / ? / ?** | **—** | **—** | **—** |
| **q025** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | I weed twice before topdressing. | **? / ? / ?** | **—** | **—** | **—** |
| **q026** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | This field has fewer stones than the other one. | **? / ? / ?** | **—** | **—** | **—** |
| **q027** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | We added manure at planting. | **? / ? / ?** | **—** | **—** | **—** |
| **q028** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | About three quarters or so. | **? / ? / ?** | **—** | **—** | **—** |
| **q029** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | Enough that weeds don’t bother me much. | **? / ? / ?** | **—** | **—** | **—** |
| **q030** | By six weeks after planting, how much of the ground should be covered by the crop’s leaves? | Quite a lot by then. | **? / ? / ?** | **—** | **—** | **—** |
| **q031** | How high do you like the ears to be from the ground for easy picking? | Not too low. | **? / ? / ?** | **—** | **—** | **—** |
| **q032** | How high do you like the ears to be from the ground for easy picking? | Comfortable to reach. | **? / ? / ?** | **—** | **—** | **—** |
| **q033** | How high do you like the ears to be from the ground for easy picking? | Around waist to chest high. | **? / ? / ?** | **—** | **—** | **—** |
| **q034** | How high do you like the ears to be from the ground for easy picking? | About a meter. | **? / ? / ?** | **—** | **—** | **—** |
| **q035** | How high do you like the ears to be from the ground for easy picking? | Mid-plant. | **? / ? / ?** | **—** | **—** | **—** |
| **q036** | How high do you like the ears to be from the ground for easy picking? | Higher than my old variety. | **? / ? / ?** | **—** | **—** | **—** |
| **q037** | How high do you like the ears to be from the ground for easy picking? | 90–110 cm ear height from the ground. | **? / ? / ?** | **—** | **—** | **—** |
| **q038** | How high do you like the ears to be from the ground for easy picking? | Target ~1.0 m ear placement. | **? / ? / ?** | **—** | **—** | **—** |
| **q039** | How high do you like the ears to be from the ground for easy picking? | Between 0.9 and 1.1 m so we can pick easily. | **? / ? / ?** | **—** | **—** | **—** |
| **q040** | How high do you like the ears to be from the ground for easy picking? | The plants look taller than last year. | **? / ? / ?** | **—** | **—** | **—** |
| **q041** | How high do you like the ears to be from the ground for easy picking? | We harvest with family on weekends. | **? / ? / ?** | **—** | **—** | **—** |
| **q042** | How high do you like the ears to be from the ground for easy picking? | I prefer varieties with big cobs. | **? / ? / ?** | **—** | **—** | **—** |
| **q043** | How high do you like the ears to be from the ground for easy picking? | Around waist height. | **? / ? / ?** | **—** | **—** | **—** |
| **q044** | How high do you like the ears to be from the ground for easy picking? | Not too low, not too high. | **? / ? / ?** | **—** | **—** | **—** |
| **q045** | How high do you like the ears to be from the ground for easy picking? | Comfortable to reach. | **? / ? / ?** | **—** | **—** | **—** |
| **q046** | What is the most pest or disease damage you will accept before you stop using a maize variety? | If worms get out of hand, I switch. | **? / ? / ?** | **—** | **—** | **—** |
| **q047** | What is the most pest or disease damage you will accept before you stop using a maize variety? | When leaves look too spotted. | **? / ? / ?** | **—** | **—** | **—** |
| **q048** | What is the most pest or disease damage you will accept before you stop using a maize variety? | If many cobs rot, I’m done. | **? / ? / ?** | **—** | **—** | **—** |
| **q049** | What is the most pest or disease damage you will accept before you stop using a maize variety? | Around one in ten plants. | **? / ? / ?** | **—** | **—** | **—** |
| **q050** | What is the most pest or disease damage you will accept before you stop using a maize variety? | Not much. | **? / ? / ?** | **—** | **—** | **—** |
| **q051** | What is the most pest or disease damage you will accept before you stop using a maize variety? | Only light attacks. | **? / ? / ?** | **—** | **—** | **—** |
| **q052** | What is the most pest or disease damage you will accept before you stop using a maize variety? | No more than 10% of plants with moderate or worse damage at peak. | **? / ? / ?** | **—** | **—** | **—** |
| **q053** | What is the most pest or disease damage you will accept before you stop using a maize variety? | Reject if >15% of plants show moderate foliar disease by tasseling. | **? / ? / ?** | **—** | **—** | **—** |
| **q054** | What is the most pest or disease damage you will accept before you stop using a maize variety? | Stop using it if >10% ears have rot at harvest. | **? / ? / ?** | **—** | **—** | **—** |
| **q055** | What is the most pest or disease damage you will accept before you stop using a maize variety? | I sprayed once with a pyrethroid. | **? / ? / ?** | **—** | **—** | **—** |
| **q056** | What is the most pest or disease damage you will accept before you stop using a maize variety? | Our neighbor’s field had worse worms. | **? / ? / ?** | **—** | **—** | **—** |
| **q057** | What is the most pest or disease damage you will accept before you stop using a maize variety? | The agro-dealer said this seed resists disease. | **? / ? / ?** | **—** | **—** | **—** |
| **q058** | What is the most pest or disease damage you will accept before you stop using a maize variety? | Only a small amount. | **? / ? / ?** | **—** | **—** | **—** |
| **q059** | What is the most pest or disease damage you will accept before you stop using a maize variety? | If it’s more than I’m used to. | **? / ? / ?** | **—** | **—** | **—** |
| **q060** | What is the most pest or disease damage you will accept before you stop using a maize variety? | When it starts to show too much. | **? / ? / ?** | **—** | **—** | **—** |
| **q061** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | As long as I can cover costs. | **? / ? / ?** | **—** | **—** | **—** |
| **q062** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Better than my local seed in a dry year. | **? / ? / ?** | **—** | **—** | **—** |
| **q063** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Enough to keep seed next season. | **? / ? / ?** | **—** | **—** | **—** |
| **q064** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | About ten bags. | **? / ? / ?** | **—** | **—** | **—** |
| **q065** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Two tonnes. | **? / ? / ?** | **—** | **—** | **—** |
| **q066** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Close to my normal harvest. | **? / ? / ?** | **—** | **—** | **—** |
| **q067** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | At least 10 bags/acre (≈2.2 t/ha) even with a 2‑week dry spell. | **? / ? / ?** | **—** | **—** | **—** |
| **q068** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | No less than 2.5 t/ha after a 2–3 week mid-season dry spell. | **? / ? / ?** | **—** | **—** | **—** |
| **q069** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Keep if I get ≥9 bags/acre (≈2.0 t/ha) despite a 3‑week dry spell. | **? / ? / ?** | **—** | **—** | **—** |
| **q070** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | We mulched this season. | **? / ? / ?** | **—** | **—** | **—** |
| **q071** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | The borehole is far from this plot. | **? / ? / ?** | **—** | **—** | **—** |
| **q072** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | I planted a week earlier than usual. | **? / ? / ?** | **—** | **—** | **—** |
| **q073** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Close to my normal. | **? / ? / ?** | **—** | **—** | **—** |
| **q074** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Enough to make it worthwhile. | **? / ? / ?** | **—** | **—** | **—** |
| **q075** | If there’s a two- or three-week dry spell, what harvest would you still be happy with? | Something decent for a dry year. | **? / ? / ?** | **—** | **—** | **—** |
| **q076** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | If it beats what my neighbors get. | **? / ? / ?** | **—** | **—** | **—** |
| **q077** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | If I still have grain to sell. | **? / ? / ?** | **—** | **—** | **—** |
| **q078** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | If I don’t need a food loan. | **? / ? / ?** | **—** | **—** | **—** |
| **q079** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | About six bags. | **? / ? / ?** | **—** | **—** | **—** |
| **q080** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | One and a half tonnes. | **? / ? / ?** | **—** | **—** | **—** |
| **q081** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | Half my good-year harvest. | **? / ? / ?** | **—** | **—** | **—** |
| **q082** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | ≥6 bags/acre (≈1.3 t/ha) in a bad year. | **? / ? / ?** | **—** | **—** | **—** |
| **q083** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | At least 60% of my good-year yield; my good year is 12 bags/acre, so ≥7 bags/acre. | **? / ? / ?** | **—** | **—** | **—** |
| **q084** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | Minimum 1.8 t/ha in a poor season or I switch varieties. | **? / ? / ?** | **—** | **—** | **—** |
| **q085** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | We usually sell to the same trader. | **? / ? / ?** | **—** | **—** | **—** |
| **q086** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | Storage space is limited at home. | **? / ? / ?** | **—** | **—** | **—** |
| **q087** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | I prefer white grain for the market. | **? / ? / ?** | **—** | **—** | **—** |
| **q088** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | About half of a good year. | **? / ? / ?** | **—** | **—** | **—** |
| **q089** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | What I can live with. | **? / ? / ?** | **—** | **—** | **—** |
| **q090** | In a bad year, what is the smallest harvest you would accept and still plant this maize again? | The minimum to cover costs. | **? / ? / ?** | **—** | **—** | **—** |
| **q091** | What is the most fallen or leaning plants you can accept at harvest? | I don’t like much falling. | **? / ? / ?** | **—** | **—** | **—** |
| **q092** | What is the most fallen or leaning plants you can accept at harvest? | If it slows picking, it’s too much. | **? / ? / ?** | **—** | **—** | **—** |
| **q093** | What is the most fallen or leaning plants you can accept at harvest? | Just a few bent stalks is okay. | **? / ? / ?** | **—** | **—** | **—** |
| **q094** | What is the most fallen or leaning plants you can accept at harvest? | About five percent. | **? / ? / ?** | **—** | **—** | **—** |
| **q095** | What is the most fallen or leaning plants you can accept at harvest? | Very little. | **? / ? / ?** | **—** | **—** | **—** |
| **q096** | What is the most fallen or leaning plants you can accept at harvest? | One or two per row. | **? / ? / ?** | **—** | **—** | **—** |
| **q097** | What is the most fallen or leaning plants you can accept at harvest? | ≤5% total lodging (stalk + root) at harvest. | **? / ? / ?** | **—** | **—** | **—** |
| **q098** | What is the most fallen or leaning plants you can accept at harvest? | No more than 3% broken stalks and 2% root-lodged. | **? / ? / ?** | **—** | **—** | **—** |
| **q099** | What is the most fallen or leaning plants you can accept at harvest? | Accept ≤5% leaning or fallen plants when we pick. | **? / ? / ?** | **—** | **—** | **—** |
| **q100** | What is the most fallen or leaning plants you can accept at harvest? | We stake beans but not maize. | **? / ? / ?** | **—** | **—** | **—** |
| **q101** | What is the most fallen or leaning plants you can accept at harvest? | The wind was strong this July. | **? / ? / ?** | **—** | **—** | **—** |
| **q102** | What is the most fallen or leaning plants you can accept at harvest? | Cattle sometimes pass along the edge. | **? / ? / ?** | **—** | **—** | **—** |
| **q103** | What is the most fallen or leaning plants you can accept at harvest? | Just a few. | **? / ? / ?** | **—** | **—** | **—** |
| **q104** | What is the most fallen or leaning plants you can accept at harvest? | Very little, ideally. | **? / ? / ?** | **—** | **—** | **—** |
| **q105** | What is the most fallen or leaning plants you can accept at harvest? | Only what doesn’t slow us down. | **? / ? / ?** | **—** | **—** | **—** |
| **q106** | How many days after planting should the maize start to flower for your needs? | Not too late for the rains. | **? / ? / ?** | **—** | **—** | **—** |
| **q107** | How many days after planting should the maize start to flower for your needs? | Soon after the first topdressing. | **? / ? / ?** | **—** | **—** | **—** |
| **q108** | How many days after planting should the maize start to flower for your needs? | Earlier than my old one. | **? / ? / ?** | **—** | **—** | **—** |
| **q109** | How many days after planting should the maize start to flower for your needs? | About two months. | **? / ? / ?** | **—** | **—** | **—** |
| **q110** | How many days after planting should the maize start to flower for your needs? | Sixties. | **? / ? / ?** | **—** | **—** | **—** |
| **q111** | How many days after planting should the maize start to flower for your needs? | Before the long dry spell. | **? / ? / ?** | **—** | **—** | **—** |
| **q112** | How many days after planting should the maize start to flower for your needs? | Start silking at ~60–65 days after planting. | **? / ? / ?** | **—** | **—** | **—** |
| **q113** | How many days after planting should the maize start to flower for your needs? | Flower by day 62 so it matches our rains. | **? / ? / ?** | **—** | **—** | **—** |
| **q114** | How many days after planting should the maize start to flower for your needs? | Target silks by 60–64 days. | **? / ? / ?** | **—** | **—** | **—** |
| **q115** | How many days after planting should the maize start to flower for your needs? | I topdress around a month after planting. | **? / ? / ?** | **—** | **—** | **—** |
| **q116** | How many days after planting should the maize start to flower for your needs? | The long rains came late this year. | **? / ? / ?** | **—** | **—** | **—** |
| **q117** | How many days after planting should the maize start to flower for your needs? | My old variety was medium-maturing. | **? / ? / ?** | **—** | **—** | **—** |
| **q118** | How many days after planting should the maize start to flower for your needs? | Roughly two months. | **? / ? / ?** | **—** | **—** | **—** |
| **q119** | How many days after planting should the maize start to flower for your needs? | Soon after the first topdressing. | **? / ? / ?** | **—** | **—** | **—** |
| **q120** | How many days after planting should the maize start to flower for your needs? | Before the heavy dry spell. | **? / ? / ?** | **—** | **—** | **—** |
| **q121** | By when should the maize be ready to harvest for your conditions? | Before the heavy short-rains storms. | **? / ? / ?** | **—** | **—** | **—** |
| **q122** | By when should the maize be ready to harvest for your conditions? | In time for school fees. | **? / ? / ?** | **—** | **—** | **—** |
| **q123** | By when should the maize be ready to harvest for your conditions? | Before storage pests get bad. | **? / ? / ?** | **—** | **—** | **—** |
| **q124** | By when should the maize be ready to harvest for your conditions? | Around four months. | **? / ? / ?** | **—** | **—** | **—** |
| **q125** | By when should the maize be ready to harvest for your conditions? | By August. | **? / ? / ?** | **—** | **—** | **—** |
| **q126** | By when should the maize be ready to harvest for your conditions? | Early, not late. | **? / ? / ?** | **—** | **—** | **—** |
| **q127** | By when should the maize be ready to harvest for your conditions? | Harvest by 120–130 days after planting. | **? / ? / ?** | **—** | **—** | **—** |
| **q128** | By when should the maize be ready to harvest for your conditions? | Ready by late August for long-rains planting in April. | **? / ? / ?** | **—** | **—** | **—** |
| **q129** | By when should the maize be ready to harvest for your conditions? | Dry enough to shell by ~125 days under normal weather. | **? / ? / ?** | **—** | **—** | **—** |
| **q130** | By when should the maize be ready to harvest for your conditions? | We have a small crib for drying. | **? / ? / ?** | **—** | **—** | **—** |
| **q131** | By when should the maize be ready to harvest for your conditions? | School fees are due in September. | **? / ? / ?** | **—** | **—** | **—** |
| **q132** | By when should the maize be ready to harvest for your conditions? | The road to the market is rough. | **? / ? / ?** | **—** | **—** | **—** |
| **q133** | By when should the maize be ready to harvest for your conditions? | Around four months. | **? / ? / ?** | **—** | **—** | **—** |
| **q134** | By when should the maize be ready to harvest for your conditions? | Before the short rains get strong. | **? / ? / ?** | **—** | **—** | **—** |
| **q135** | By when should the maize be ready to harvest for your conditions? | By the time schools reopen. | **? / ? / ?** | **—** | **—** | **—** |
| **q136** | How many ears per plant do you prefer? | A good cob on each plant. | **? / ? / ?** | **—** | **—** | **—** |
| **q137** | How many ears per plant do you prefer? | More cobs are fine if they fill. | **? / ? / ?** | **—** | **—** | **—** |
| **q138** | How many ears per plant do you prefer? | Not too many small cobs. | **? / ? / ?** | **—** | **—** | **—** |
| **q139** | How many ears per plant do you prefer? | One. | **? / ? / ?** | **—** | **—** | **—** |
| **q140** | How many ears per plant do you prefer? | One, sometimes two. | **? / ? / ?** | **—** | **—** | **—** |
| **q141** | How many ears per plant do you prefer? | Big ears. | **? / ? / ?** | **—** | **—** | **—** |
| **q142** | How many ears per plant do you prefer? | One ear per plant, well-filled. | **? / ? / ?** | **—** | **—** | **—** |
| **q143** | How many ears per plant do you prefer? | Prefer 1; 2 is fine only if both are full size. | **? / ? / ?** | **—** | **—** | **—** |
| **q144** | How many ears per plant do you prefer? | 1 ear/plant consistently, rather than two small ones. | **? / ? / ?** | **—** | **—** | **—** |
| **q145** | How many ears per plant do you prefer? | We shell by hand. | **? / ? / ?** | **—** | **—** | **—** |
| **q146** | How many ears per plant do you prefer? | Buyers here pay more for clean grain. | **? / ? / ?** | **—** | **—** | **—** |
| **q147** | How many ears per plant do you prefer? | I like deep yellow kernels for feed. | **? / ? / ?** | **—** | **—** | **—** |
| **q148** | How many ears per plant do you prefer? | Usually one. | **? / ? / ?** | **—** | **—** | **—** |
| **q149** | How many ears per plant do you prefer? | One, maybe two if they fill. | **? / ? / ?** | **—** | **—** | **—** |
| **q150** | How many ears per plant do you prefer? | One good cob per plant. | **? / ? / ?** | **—** | **—** | **—** |

> **Note**: S=Specificity, D=Detail, U=Usability

---

## Notes
- Values are copied directly from the already **canonicalized final JSON**; no recalculation is performed here.
- `penalty` typically reflects deductions based on the number of listed weaknesses (max 15). If no weaknesses array is present in p2, many implementations treat it as 0.
- When meta is identical across runs, you can use this table to monitor drift in answer quality.
