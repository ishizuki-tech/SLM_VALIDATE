# Prompt Log (Grouped Flow)

`all.prompts.jsonl` を解析し、p1→p2→p3 を1セットにまとめています。


---

## 1. Item `line1`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** A maize variety that matures in 90 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: A maize variety that matures in 90 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Lacks context – doesn’t specify the region or climate suitability. Could be more informative."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: A maize variety that matures in 90 days
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Lacks context – doesn’t specify the region or climate suitability. Could be more informative."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks context – no region or climate details. Needs to be more specific about the trait being considered as 'early maturing'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: A maize variety that matures in 90 days
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – no region or climate details. Needs to be more specific about the trait being considered as 'early maturing'."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "High",
  "usability": "Medium",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 75
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"Medium",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":75
}
```

</details>

---

## 2. Item `line10`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** The variety that allows me sell green maize after 3 months of planting  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: The variety that allows me sell green maize after 3 months of planting
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for ‘early maturing’ – only mentions green maize, no details about growth stage or yield expectations."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: The variety that allows me sell green maize after 3 months of planting
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for ‘early maturing’ – only mentions green maize, no details about growth stage or yield expectations."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for ‘early maturing’ – only mentions green maize, no details about growth stage or yield expectations."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: The variety that allows me sell green maize after 3 months of planting
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for ‘early maturing’ – only mentions green maize, no details about growth stage or yield expectations."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":30
}
```

</details>

---

## 3. Item `line11`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Variety that matures quickly enough to allow me to sell green maize early in the season  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that matures quickly enough to allow me to sell green maize early in the season
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Lacks specific criteria for ‘early’ and ‘quickly’ – needs quantification of maturity time.”}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that matures quickly enough to allow me to sell green maize early in the season
Analysis: {}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Mentions 'green maize' which might be a later stage. No details about the timeframe for 'early' maturity."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that matures quickly enough to allow me to sell green maize early in the season
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 30,
  "specificity": 20,
  "usability": 40,
  "clarity": 30,
  "completeness": 20,
  "relevance": 40,
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 30,
  "specificity": 20,
  "usability": 40,
  "clarity": 30,
  "completeness": 20,
  "relevance": 40,
  "overall_score": 63
}
```

</details>

---

## 4. Item `line12`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Anything below 100 days I would say is early maturing  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Anything below 100 days I would say is early maturing
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn't define what constitutes a 'short' timeframe."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Anything below 100 days I would say is early maturing
Analysis: {"specificity": "High", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn't define what constitutes a 'short' timeframe."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks definition of 'early maturing'. Doesn't specify timeframe criteria."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Anything below 100 days I would say is early maturing
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks definition of 'early maturing'. Doesn't specify timeframe criteria."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "High",
  "relevance": "High",
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"High",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 5. Item `line13`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Early means I can harvest my maize in 3 months about 90 to 95 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Early means I can harvest my maize in 3 months about 90 to 95 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific variety name or region, no data on yield or resistance."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Early means I can harvest my maize in 3 months about 90 to 95 days
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific variety name or region, no data on yield or resistance."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific variety name or region, no data on yield or resistance."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Early means I can harvest my maize in 3 months about 90 to 95 days
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific variety name or region, no data on yield or resistance."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Medium",
  "usability": "High",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 68
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Medium",
  "usability":"High",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":68
}
```

</details>

---

## 6. Item `line14`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Some maize varieties can be harvested, in 75 days, that is early  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Some maize varieties can be harvested, in 75 days, that is early
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early' – only a timeframe, no definition of maturity level. Needs more context about what constitutes 'early' in maize."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Some maize varieties can be harvested, in 75 days, that is early
Analysis: {"specificity": "Medium", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early' – only a timeframe, no definition of maturity level. Needs more context about what constitutes 'early' in maize."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"Medium","relevance":"High","weaknesses":"Lacks definition of 'early' – timeframe is vague. Needs more context about maize maturity levels."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Some maize varieties can be harvested, in 75 days, that is early
Analysis: {"completeness": "High", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks definition of 'early' – timeframe is vague. Needs more context about maize maturity levels."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "High",
  "relevance": "High",
  "overall_score": 68
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"High",
  "relevance":"High",
  "overall_score":68
}
```

</details>

---

## 7. Item `line15`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** For me if I harvest in exaclty 3 months, that is an early maturing variety  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: For me if I harvest in exaclty 3 months, that is an early maturing variety
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early' – only harvest time. No mention of yield or resistance traits."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: For me if I harvest in exaclty 3 months, that is an early maturing variety
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early' – only harvest time. No mention of yield or resistance traits."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for 'early' – only harvest time. No mention of yield or resistance traits."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: For me if I harvest in exaclty 3 months, that is an early maturing variety
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early' – only harvest time. No mention of yield or resistance traits."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Low",
  "usability": "High",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"High",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 8. Item `line16`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Variety that matures faster than traditional/ local variety  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that matures faster than traditional/ local variety
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks definition of ‘early maturing’ and doesn’t specify criteria for comparison."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that matures faster than traditional/ local variety
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks definition of ‘early maturing’ and doesn’t specify criteria for comparison."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks definition of ‘early maturing’ and doesn’t specify criteria for comparison."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that matures faster than traditional/ local variety
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks definition of ‘early maturing’ and doesn’t specify criteria for comparison."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 9. Item `line17`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** A variety that i can plant in short rains  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that i can plant in short rains
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for ‘early maturing’ – no criteria for duration or yield.  Doesn’t define ‘short rains’ – needs context for region.”}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that i can plant in short rains
Analysis: {}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn't define 'short rains' – needs context. Missing details about expected yield or growth stage."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that i can plant in short rains
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn't define 'short rains' – needs context. Missing details about expected yield or growth stage."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 25
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":25
}
```

</details>

---

## 10. Item `line18`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** The type my neighbour planted last season  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: The type my neighbour planted last season
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific characteristics, no data provided about the variety's maturity."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: The type my neighbour planted last season
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific characteristics, no data provided about the variety's maturity."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific characteristics and maturity assessment criteria."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: The type my neighbour planted last season
Analysis: {"completeness": "Medium", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific characteristics and maturity assessment criteria."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 11. Item `line19`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** A variety that i can plant twice with an year  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that i can plant twice with an year
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics.  Doesn't specify the region or climate suitability."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that i can plant twice with an year
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics.  Doesn't specify the region or climate suitability."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics.  Doesn't specify the region or climate suitability."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that i can plant twice with an year
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics.  Doesn't specify the region or climate suitability."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Very Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Very Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":20
}
```

</details>

---

## 12. Item `line2`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Variety that i can harvest before short rains end in my area  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that i can harvest before short rains end in my area
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for ‘early maturing’ – no timeframe or indicators of maturity stage.  Doesn’t define the region or climate conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that i can harvest before short rains end in my area
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for ‘early maturing’ – no timeframe or indicators of maturity stage.  Doesn’t define the region or climate conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for ‘early maturing’ – no timeframe or indicators of maturity stage. Doesn’t define the region or climate conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that i can harvest before short rains end in my area
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for ‘early maturing’ – no timeframe or indicators of maturity stage. Doesn’t define the region or climate conditions."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":20
}
```

</details>

---

## 13. Item `line20`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** It matures early even if the rains are short  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: It matures early even if the rains are short
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early' and ‘maize’ – vague.”}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: It matures early even if the rains are short
Analysis: {}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn't define what constitutes 'early' or 'maturity'. No context or examples provided."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: It matures early even if the rains are short
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn't define what constitutes 'early' or 'maturity'. No context or examples provided."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 14. Item `line21`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Katumani is early maturing  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Katumani is early maturing
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Lacks specific characteristics like yield, resistance, or maturity date. Doesn't provide context about the variety's strengths or weaknesses."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Katumani is early maturing
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Lacks specific characteristics like yield, resistance, or maturity date. Doesn't provide context about the variety's strengths or weaknesses."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific details about the maize variety, such as yield, resistance, or maturity date. Doesn't offer any comparative analysis."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Katumani is early maturing
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific details about the maize variety, such as yield, resistance, or maturity date. Doesn't offer any comparative analysis."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 15. Item `line22`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** I planted it last year and harvested in August, that was early  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: I planted it last year and harvested in August, that was early
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: I planted it last year and harvested in August, that was early
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: I planted it last year and harvested in August, that was early
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":30
}
```

</details>

---

## 16. Item `line23`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** The one I can eat green maize after two months  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: The one I can eat green maize after two months
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for ‘early maturing’ and doesn’t define any growth stage or yield expectations."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: The one I can eat green maize after two months
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for ‘early maturing’ and doesn’t define any growth stage or yield expectations."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for ‘early maturing’ and doesn’t define any growth stage or yield expectations."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: The one I can eat green maize after two months
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for ‘early maturing’ and doesn’t define any growth stage or yield expectations."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Very Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Very Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 17. Item `line24`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** A variety that takes 4 months to produce flowers  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that takes 4 months to produce flowers
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"Low","weaknesses":"Lacks context – doesn’t specify the region or climate suitability. Doesn’t mention any specific traits like yield or resistance."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that takes 4 months to produce flowers
Analysis: {"specificity": "High", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify the region or climate suitability. Doesn’t mention any specific traits like yield or resistance."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn’t define ‘maize’ or ‘variety’ in context."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that takes 4 months to produce flowers
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn’t define ‘maize’ or ‘variety’ in context."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 18. Item `line25`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** A variety that after planting, takes 4 months to grow enough to be harvested  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that after planting, takes 4 months to grow enough to be harvested
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing' – only a timeframe, not characteristics like yield or resistance."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that after planting, takes 4 months to grow enough to be harvested
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing' – only a timeframe, not characteristics like yield or resistance."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing' – only a timeframe, not characteristics like yield or resistance."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that after planting, takes 4 months to grow enough to be harvested
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing' – only a timeframe, not characteristics like yield or resistance."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "High",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"High",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 19. Item `line26`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** A variety that 3 to 4 months before it's ready to be eaten  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that 3 to 4 months before it's ready to be eaten
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn't define '3 to 4 months'."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that 3 to 4 months before it's ready to be eaten
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn't define '3 to 4 months'."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn't define '3 to 4 months'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: A variety that 3 to 4 months before it's ready to be eaten
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn't define '3 to 4 months'."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "High",
  "usability": "Low",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"High",
  "usability":"Low",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 20. Item `line27`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** This season i planted Sungura which matures very fast, about 75 to 85 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: This season i planted Sungura which matures very fast, about 75 to 85 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"Medium","weaknesses":"Lacks specific characteristics like resistance to pests or diseases, and doesn’t mention any unique traits that differentiate it from other maize varieties."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: This season i planted Sungura which matures very fast, about 75 to 85 days
Analysis: {"specificity": "High", "detail": "Medium", "usability": "Medium", "weaknesses": "Lacks specific characteristics like resistance to pests or diseases, and doesn’t mention any unique traits that differentiate it from other maize varieties."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing' and doesn't provide details about the variety's traits."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: This season i planted Sungura which matures very fast, about 75 to 85 days
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing' and doesn't provide details about the variety's traits."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "High",
  "relevance": "High",
  "overall_score": 68
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"High",
  "relevance":"High",
  "overall_score":68
}
```

</details>

---

## 21. Item `line28`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Very Low",
  "clarity": "Very Low",
  "completeness": "Very Low",
  "relevance": "Very Low",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Very Low",
  "clarity":"Very Low",
  "completeness":"Very Low",
  "relevance":"Very Low",
  "overall_score":20
}
```

</details>

---

## 22. Item `line29`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. No details about growth characteristics or yield potential are provided."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Very Low",
  "clarity": "Very Low",
  "completeness": "Very Low",
  "relevance": "Very Low",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Very Low",
  "clarity":"Very Low",
  "completeness":"Very Low",
  "relevance":"Very Low",
  "overall_score":20
}
```

</details>

---

## 23. Item `line3`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** One that allows me to plant another crop in the same season  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: One that allows me to plant another crop in the same season
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics. Focuses on a single crop, not the maize itself."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: One that allows me to plant another crop in the same season
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics. Focuses on a single crop, not the maize itself."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics. Focuses on a single crop, not the maize itself."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: One that allows me to plant another crop in the same season
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing' and doesn't define any growth characteristics. Focuses on a single crop, not the maize itself."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":20
}
```

</details>

---

## 24. Item `line30`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It takes 90 days from planting to harvesting  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes 90 days from planting to harvesting
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Could be more precise – specify the stage of maturity (e.g., grain fill, maturity stage) and provide a range if possible."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes 90 days from planting to harvesting
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Could be more precise – specify the stage of maturity (e.g., grain fill, maturity stage) and provide a range if possible."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Could be more specific about the stage of maturity."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It takes 90 days from planting to harvesting
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Could be more specific about the stage of maturity."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 90,
  "specificity": 90,
  "usability": 60,
  "clarity": 70,
  "completeness": 70,
  "relevance": 90,
  "overall_score": 77
}
```

### Stage `p3` — 💡 Output
```text
“Very High”
```

</details>

---

## 25. Item `line31`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It takes around 3 to 4 months depending on the rains  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 3 to 4 months depending on the rains
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Medium","weaknesses":"Could be more precise about the rainfall duration."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 3 to 4 months depending on the rains
Analysis: {"specificity": "Medium", "detail": "Low", "usability": "Medium", "weaknesses": "Could be more precise about the rainfall duration."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Could be more specific about the rainfall duration."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 3 to 4 months depending on the rains
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Could be more specific about the rainfall duration."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 78
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":78
}
```

</details>

---

## 26. Item `line32`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It doesn’t take too long, maybe a few months  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It doesn’t take too long, maybe a few months
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and doesn’t specify the duration."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It doesn’t take too long, maybe a few months
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and doesn’t specify the duration."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific timeframe and doesn’t specify the duration."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It doesn’t take too long, maybe a few months
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific timeframe and doesn’t specify the duration."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 27. Item `line33`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** I’m not sure, I just harvest when it’s ready  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: I’m not sure, I just harvest when it’s ready
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe, no data provided."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: I’m not sure, I just harvest when it’s ready
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe, no data provided."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific timeframe and data."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: I’m not sure, I just harvest when it’s ready
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific timeframe and data."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 25
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":25
}
```

</details>

---

## 28. Item `line34`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** it takes too long, sometimes more than half of the year  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: it takes too long, sometimes more than half of the year
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe, doesn’t specify the duration, and doesn’t provide a range."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: it takes too long, sometimes more than half of the year
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe, doesn’t specify the duration, and doesn’t provide a range."}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Low","relevance":"Medium","weaknesses":"Lacks specific timeframe, doesn’t provide a range, and doesn’t specify the duration."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: it takes too long, sometimes more than half of the year
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "The answer provides a vague estimate of the maturity time, indicating a lack of specific data.",
  "specificity": "Very Low",
  "usability": "Very Low",
  "clarity": "Very Low",
  "completeness": "Very Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "The answer provides a vague estimate of the maturity time, indicating a lack of specific data.",
  "specificity": "Very Low",
  "usability": "Very Low",
  "clarity": "Very Low",
  "completeness": "Very Low",
  "relevance": "High",
  "overall_score": 20
}
```

</details>

---

## 29. Item `line35`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** If i plant in March, i harvest in August  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: If i plant in March, i harvest in August
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no yield data or specific conditions. Doesn’t specify the maize variety or region."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: If i plant in March, i harvest in August
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no yield data or specific conditions. Doesn’t specify the maize variety or region."}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks context – no yield data or specific conditions. Doesn’t specify the maize variety or region."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: If i plant in March, i harvest in August
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 7,
  "specificity": 7,
  "usability": 6,
  "clarity": 7,
  "completeness": 6,
  "relevance": 7,
  "overall_score": 73
}
```

### Stage `p3` — 💡 Output
```text
“Very High”
```

</details>

---

## 30. Item `line36`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** If i plant in March, i harvest in August  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: If i plant in March, i harvest in August
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no yield data or specific conditions. Doesn’t specify the maize variety or region."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: If i plant in March, i harvest in August
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no yield data or specific conditions. Doesn’t specify the maize variety or region."}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks context – no yield data or specific conditions. Doesn’t specify the maize variety or region."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: If i plant in March, i harvest in August
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 7,
  "specificity": 7,
  "usability": 6,
  "clarity": 7,
  "completeness": 6,
  "relevance": 7,
  "overall_score": 73
}
```

### Stage `p3` — 💡 Output
```text
“Very High”
```

</details>

---

## 31. Item `line37`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It takes a long time  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes a long time
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe, no context about the maize variety or growing conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes a long time
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe, no context about the maize variety or growing conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific timeframe and context."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It takes a long time
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific timeframe and context."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Low",
  "overall_score": 25
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Low",
  "overall_score":25
}
```

</details>

---

## 32. Item `line38`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It doesn’t take too long  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It doesn’t take too long
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no yield data or timeframe."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It doesn’t take too long
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no yield data or timeframe."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Lacks context and timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It doesn’t take too long
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks context and timeframe."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Low",
  "overall_score": 25
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Low",
  "overall_score":25
}
```

</details>

---

## 33. Item `line39`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It usually matures in 90 to 120 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It usually matures in 90 to 120 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Could be more precise with yield data."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It usually matures in 90 to 120 days
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Could be more precise with yield data."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Could be more precise with yield data."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It usually matures in 90 to 120 days
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Could be more precise with yield data."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 90,
  "specificity": 90,
  "usability": 70,
  "clarity": 70,
  "completeness": 70,
  "relevance": 70,
  "overall_score": 75
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 90,
  "specificity": 90,
  "usability": 70,
  "clarity": 70,
  "completeness": 70,
  "relevance": 70,
  "overall_score": 75
}
```

</details>

---

## 34. Item `line4`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Variety that i can harvest before pest destroy it  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that i can harvest before pest destroy it
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing' and doesn't define any measurable characteristics.","topic":"Very Low"}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that i can harvest before pest destroy it
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing' and doesn't define any measurable characteristics.", "topic": "Very Low"}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses": "Lacks specific criteria for 'early maturing' and doesn't define any measurable characteristics."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Variety that i can harvest before pest destroy it
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing' and doesn't define any measurable characteristics."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 35. Item `line40`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It usualy takes 3 months but sometimes longer when rains delay  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It usualy takes 3 months but sometimes longer when rains delay
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and doesn't specify conditions for delay."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It usualy takes 3 months but sometimes longer when rains delay
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and doesn't specify conditions for delay."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific timeframe and doesn't specify conditions for delay."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It usualy takes 3 months but sometimes longer when rains delay
Analysis: {"completeness": "Medium", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific timeframe and doesn't specify conditions for delay."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 70,
  "specificity": 60,
  "usability": 60,
  "clarity": 60,
  "completeness": 70,
  "relevance": 60,
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output
```text
“Excellent!”
```

</details>

---

## 36. Item `line41`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It’s not too early and not too late  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It’s not too early and not too late
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe, no context about growth stage."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It’s not too early and not too late
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe, no context about growth stage."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific timeframe and context about maize maturity."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It’s not too early and not too late
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific timeframe and context about maize maturity."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 37. Item `line42`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** Sometimes it matures faster other times it delays depending on the weather  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: Sometimes it matures faster other times it delays depending on the weather
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and doesn’t specify weather conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: Sometimes it matures faster other times it delays depending on the weather
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and doesn’t specify weather conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific timeframe and doesn’t specify weather conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: Sometimes it matures faster other times it delays depending on the weather
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific timeframe and doesn’t specify weather conditions."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 38. Item `line43`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** Around the time we start harvesting beans  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: Around the time we start harvesting beans
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify the maize variety or growing conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: Around the time we start harvesting beans
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify the maize variety or growing conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Lacks context and doesn't specify the maize variety or growing conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: Around the time we start harvesting beans
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks context and doesn't specify the maize variety or growing conditions."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Low",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Low",
  "overall_score":20
}
```

</details>

---

## 39. Item `line44`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** I grow Duma and I am able to harvest in 85 to 90 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: I grow Duma and I am able to harvest in 85 to 90 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Medium","weaknesses":"Lacks specific yield data and doesn’t specify the growing conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: I grow Duma and I am able to harvest in 85 to 90 days
Analysis: {"specificity": "Medium", "detail": "Low", "usability": "Medium", "weaknesses": "Lacks specific yield data and doesn’t specify the growing conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific yield data and doesn't specify growing conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: I grow Duma and I am able to harvest in 85 to 90 days
Analysis: {"completeness": "High", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific yield data and doesn't specify growing conditions."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 68
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":68
}
```

</details>

---

## 40. Item `line45`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** Even with little rain, the maize I grow is ready for harvest in less than 90 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: Even with little rain, the maize I grow is ready for harvest in less than 90 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"High","weaknesses":"Lacks specific details about the growing conditions (soil, climate) and potential challenges. Could be more precise with data points."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: Even with little rain, the maize I grow is ready for harvest in less than 90 days
Analysis: {"specificity": "Medium", "detail": "Medium", "usability": "High", "weaknesses": "Lacks specific details about the growing conditions (soil, climate) and potential challenges. Could be more precise with data points."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific details about growing conditions and potential challenges."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: Even with little rain, the maize I grow is ready for harvest in less than 90 days
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific details about growing conditions and potential challenges."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "High",
  "usability": "Medium",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 82
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"Medium",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":82
}
```

</details>

---

## 41. Item `line46`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It takes around 90 days, then I can harvest  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 90 days, then I can harvest
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific details about the growing conditions or variety. Doesn’t mention any potential challenges."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 90 days, then I can harvest
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific details about the growing conditions or variety. Doesn’t mention any potential challenges."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific details about the growing conditions or variety. Doesn’t mention any potential challenges."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 90 days, then I can harvest
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific details about the growing conditions or variety. Doesn’t mention any potential challenges."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 70,
  "specificity": 70,
  "usability": 60,
  "clarity": 70,
  "completeness": 60,
  "relevance": 70,
  "overall_score": 68
}
```

### Stage `p3` — 💡 Output
```text
“Very High”
```

</details>

---

## 42. Item `line47`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It matures in 3 months or less, around 85 to 90 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It matures in 3 months or less, around 85 to 90 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Could be more precise with yield data. Missing specific growth stage."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It matures in 3 months or less, around 85 to 90 days
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Could be more precise with yield data. Missing specific growth stage."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Could specify the maturity stage (e.g., early, mid, late) for better context."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It matures in 3 months or less, around 85 to 90 days
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Could specify the maturity stage (e.g., early, mid, late) for better context."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "High",
  "usability": "Medium",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 83
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"Medium",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":83
}
```

</details>

---

## 43. Item `line48`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** If the rains are good, it takes 90 days, but if the rains are not that food it will mature faster, in 80 days  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: If the rains are good, it takes 90 days, but if the rains are not that food it will mature faster, in 80 days
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"Low","weaknesses":"Lacks specific details about the conditions (rain) and offers a general estimate. Could be more precise with timeframe details."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: If the rains are good, it takes 90 days, but if the rains are not that food it will mature faster, in 80 days
Analysis: {"specificity": "Medium", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks specific details about the conditions (rain) and offers a general estimate. Could be more precise with timeframe details."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific timeframe details and doesn't specify conditions for faster maturation."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: If the rains are good, it takes 90 days, but if the rains are not that food it will mature faster, in 80 days
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific timeframe details and doesn't specify conditions for faster maturation."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 68
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":68
}
```

</details>

---

## 44. Item `line49`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** This one I grew this season, matured very fast, than what I grew in the previous seasons  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: This one I grew this season, matured very fast, than what I grew in the previous seasons
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific data points, imprecise, and doesn’t provide context about the maize variety or growing conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: This one I grew this season, matured very fast, than what I grew in the previous seasons
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific data points, imprecise, and doesn’t provide context about the maize variety or growing conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Medium","weaknesses":"Lacks specific data points, imprecise, and doesn’t provide context about the maize variety or growing conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: This one I grew this season, matured very fast, than what I grew in the previous seasons
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Medium", "weaknesses": "Lacks specific data points, imprecise, and doesn’t provide context about the maize variety or growing conditions."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":35
}
```

</details>

---

## 45. Item `line5`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Any variety that matures within 3 months  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Any variety that matures within 3 months
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn’t define ‘3 months’ as a benchmark."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Any variety that matures within 3 months
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn’t define ‘3 months’ as a benchmark."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Doesn't define ‘3 months’ as a benchmark."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Any variety that matures within 3 months
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. Doesn't define ‘3 months’ as a benchmark."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 46. Item `line50`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** Two and a half months then we can eat green maize  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: Two and a half months then we can eat green maize
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific yield data, no measurement of maturity, only a vague timeframe."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: Two and a half months then we can eat green maize
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific yield data, no measurement of maturity, only a vague timeframe."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses":"Lacks specific yield data, no measurement of maturity, only a vague timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: Two and a half months then we can eat green maize
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks specific yield data, no measurement of maturity, only a vague timeframe."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 47. Item `line51`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It’s usually ready before Christmas  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It’s usually ready before Christmas
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no yield data or timeframe."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It’s usually ready before Christmas
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no yield data or timeframe."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks context – no yield data or timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It’s usually ready before Christmas
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks context – no yield data or timeframe."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 48. Item `line52`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** We harvest In August if planted in April  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: We harvest In August if planted in April
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no yield data or specific conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: We harvest In August if planted in April
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no yield data or specific conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks context – no yield data."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: We harvest In August if planted in April
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – no yield data."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Medium",
  "usability": "Low",
  "clarity": "High",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"High",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 49. Item `line53`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It’s ready before the short rains end  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It’s ready before the short rains end
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no yield data or timeframe."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It’s ready before the short rains end
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no yield data or timeframe."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific yield data and timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It’s ready before the short rains end
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific yield data and timeframe."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "High",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"High",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 50. Item `line54`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It depends, sometimes 3 months, sometimes 4 if rains are bad  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It depends, sometimes 3 months, sometimes 4 if rains are bad
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and doesn’t specify conditions for maturity."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It depends, sometimes 3 months, sometimes 4 if rains are bad
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and doesn’t specify conditions for maturity."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Medium","weaknesses":"Lacks specific timeframe and doesn’t specify conditions for maturity."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It depends, sometimes 3 months, sometimes 4 if rains are bad
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Medium", "weaknesses": "Lacks specific timeframe and doesn’t specify conditions for maturity."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 3,
  "specificity": 2,
  "usability": 1,
  "clarity": 1,
  "completeness": 1,
  "relevance": 1,
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output
```text
“High”
```

</details>

---

## 51. Item `line55`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** It takes around 6 months  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 6 months
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Could be more precise – specify the growth stage (e.g., from planting to harvest)."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 6 months
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Could be more precise – specify the growth stage (e.g., from planting to harvest)."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Could be more precise regarding the timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: It takes around 6 months
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Could be more precise regarding the timeframe."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "High",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 82
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"High",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":82
}
```

</details>

---

## 52. Item `line56`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** About a month after I harvest beans  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: About a month after I harvest beans
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no yield data, no specific variety, no growing conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: About a month after I harvest beans
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no yield data, no specific variety, no growing conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific yield data and context about the maize variety."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: About a month after I harvest beans
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific yield data and context about the maize variety."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Medium",
  "usability": "High",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Medium",
  "usability":"High",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 53. Item `line57`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe, no data provided, vague and imprecise."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe, no data provided, vague and imprecise."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific timeframe and data."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific timeframe and data."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Low",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Low",
  "overall_score":20
}
```

</details>

---

## 54. Item `line58`

**Question:** How long does the maize you currently grow take to mature?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How long does the maize you currently grow take to mature?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe, no data provided, vague and imprecise."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How long does the maize you currently grow take to mature?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe, no data provided, vague and imprecise."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific timeframe and data."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How long does the maize you currently grow take to mature?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific timeframe and data."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Low",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Low",
  "overall_score":20
}
```

</details>

---

## 55. Item `line59`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I would accept loosing 10% of my yield to harvest earlier  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would accept loosing 10% of my yield to harvest earlier
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Low","weaknesses":"Losing 10% is a significant percentage, lacks context about the yield, and doesn't specify the type of yield."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would accept loosing 10% of my yield to harvest earlier
Analysis: {"specificity": "Medium", "detail": "Low", "usability": "Low", "weaknesses": "Losing 10% is a significant percentage, lacks context about the yield, and doesn't specify the type of yield."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Loses a substantial portion of yield, lacks context about the yield type."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I would accept loosing 10% of my yield to harvest earlier
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Loses a substantial portion of yield, lacks context about the yield type."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "High",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 56. Item `line6`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** One that I can harvest before the rains stop  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: One that I can harvest before the rains stop
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing' – only a general timeframe. Doesn’t define any measurable characteristics like yield or resistance."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: One that I can harvest before the rains stop
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing' – only a general timeframe. Doesn’t define any measurable characteristics like yield or resistance."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing' – only a general timeframe. Doesn't define any measurable characteristics like yield or resistance."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: One that I can harvest before the rains stop
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing' – only a general timeframe. Doesn't define any measurable characteristics like yield or resistance."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 57. Item `line60`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I wouldn't give up any yield, I would rather harvest late  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I wouldn't give up any yield, I would rather harvest late
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantification and doesn’t explain the reasoning behind the decision.","topic":"Harvesting timing","context":"Not specified"}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I wouldn't give up any yield, I would rather harvest late
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantification and doesn’t explain the reasoning behind the decision.", "topic": "Harvesting timing", "context": "Not specified"}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"High","relevance":"High","weaknesses":"Lacks quantification and doesn’t explain the reasoning behind the decision.","topic": "Harvesting timing", "context": "Not specified"}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I wouldn't give up any yield, I would rather harvest late
Analysis: {"completeness": "Low", "clarity": "High", "relevance": "High", "weaknesses": "Lacks quantification and doesn’t explain the reasoning behind the decision.", "topic": "Harvesting timing", "context": "Not specified"}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 58. Item `line61`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Loosing 1 to 2 bags is okay for more so long i escape the dry spell  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Loosing 1 to 2 bags is okay for more so long i escape the dry spell
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, imprecise language, and doesn’t specify the ‘earlier’ timeframe."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Loosing 1 to 2 bags is okay for more so long i escape the dry spell
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, imprecise language, and doesn’t specify the ‘earlier’ timeframe."}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Lacks quantitative data, imprecise language, and doesn’t specify the ‘earlier’ timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Loosing 1 to 2 bags is okay for more so long i escape the dry spell
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 2,
  "specificity": 1,
  "usability": 1,
  "clarity": 1,
  "completeness": 1,
  "relevance": 1,
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output
```text
“High”
```

</details>

---

## 59. Item `line62`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I would only give up a little of my harvest  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would only give up a little of my harvest
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no quantity provided.  Doesn't address the trade-off."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would only give up a little of my harvest
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no quantity provided.  Doesn't address the trade-off."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks context – no quantity provided.  Doesn't address the trade-off."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I would only give up a little of my harvest
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks context – no quantity provided.  Doesn't address the trade-off."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 1,
  "specificity": 1,
  "usability": 1,
  "clarity": 1,
  "completeness": 1,
  "relevance": 1,
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output
```text
জাহि
```

</details>

---

## 60. Item `line63`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I could give up about one bag per acre  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I could give up about one bag per acre
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Doesn't specify the amount, only a single bag per acre. Could be more precise."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I could give up about one bag per acre
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Doesn't specify the amount, only a single bag per acre. Could be more precise."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks context – what is the yield being compared to? No mention of the timeframe or conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I could give up about one bag per acre
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – what is the yield being compared to? No mention of the timeframe or conditions."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 70,
  "specificity": 70,
  "usability": 60,
  "clarity": 70,
  "completeness": 60,
  "relevance": 70,
  "overall_score": 65
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 70,
  "specificity": 70,
  "usability": 60,
  "clarity": 70,
  "completeness": 60,
  "relevance": 70,
  "overall_score": 70
}
```

</details>

---

## 61. Item `line64`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I could give a few bags per acre  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I could give a few bags per acre
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no unit or timeframe. Doesn’t specify the value of the yield."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I could give a few bags per acre
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no unit or timeframe. Doesn’t specify the value of the yield."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks context and doesn’t quantify the yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I could give a few bags per acre
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks context and doesn’t quantify the yield."}
```

### Stage `p3` — 💡 Output
```text
{25, 30, 60, 40, 20, 20}
```

### Stage `p3` — 💡 Output
```text
please provide the input text for me to evaluate?
```

</details>

---

## 62. Item `line65`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I would give up few sacks in order to harvest before drought  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would give up few sacks in order to harvest before drought
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantification, vague, doesn't specify the ‘few sacks’ amount."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would give up few sacks in order to harvest before drought
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantification, vague, doesn't specify the ‘few sacks’ amount."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Medium","weaknesses":"Lacks quantification, vague, doesn't specify the ‘few sacks’ amount."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I would give up few sacks in order to harvest before drought
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Medium", "weaknesses": "Lacks quantification, vague, doesn't specify the ‘few sacks’ amount."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 25
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":25
}
```

</details>

---

## 63. Item `line66`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I'm fine planting early maturity variety even if it gives 6bags less than late maturing variety  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I'm fine planting early maturity variety even if it gives 6bags less than late maturing variety
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify ‘earlier’ or ‘harvesting’ – only offers a comparison of yields."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I'm fine planting early maturity variety even if it gives 6bags less than late maturing variety
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify ‘earlier’ or ‘harvesting’ – only offers a comparison of yields."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks context and doesn’t address the core question of yield trade-off."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I'm fine planting early maturity variety even if it gives 6bags less than late maturing variety
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context and doesn’t address the core question of yield trade-off."}
```

### Stage `p3` — 💡 Output
```text
{35, 25, 60, 40, 30, 20}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Clear and concise explanation of the concept.",
  "specificity": "Provides specific examples to illustrate the concept.",
  "usability": "Easy to understand and follow.",
  "clarity": "Well-written and avoids jargon.",
  "completeness": "Covers all necessary aspects of the concept.",
  "relevance": "Directly applicable to the topic."
}
```

</details>

---

## 64. Item `line67`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** No yield loss, since i rely on the harvests form my household  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: No yield loss, since i rely on the harvests form my household
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no quantifiable value. Relies on a personal perspective."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: No yield loss, since i rely on the harvests form my household
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no quantifiable value. Relies on a personal perspective."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses":"Lacks context – no quantifiable value. Relies on a personal perspective."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: No yield loss, since i rely on the harvests form my household
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks context – no quantifiable value. Relies on a personal perspective."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 65. Item `line68`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I’m okay losing some yield if I can earn more by selling green maize ealier than my neighbours  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I’m okay losing some yield if I can earn more by selling green maize ealier than my neighbours
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Lacks quantitative data, vague, doesn’t specify the ‘earlier’ timeframe, no context about the ‘more’ earned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I’m okay losing some yield if I can earn more by selling green maize ealier than my neighbours
Analysis: {"specificity": "Low", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks quantitative data, vague, doesn’t specify the ‘earlier’ timeframe, no context about the ‘more’ earned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks quantitative data, vague, doesn’t specify the timeframe, doesn’t address the ‘earlier’ aspect."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I’m okay losing some yield if I can earn more by selling green maize ealier than my neighbours
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks quantitative data, vague, doesn’t specify the timeframe, doesn’t address the ‘earlier’ aspect."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 66. Item `line69`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I would rather loose a little than loose everything to drought  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would rather loose a little than loose everything to drought
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantification and doesn't explain the value lost."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I would rather loose a little than loose everything to drought
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantification and doesn't explain the value lost."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantification and doesn't explain the value lost."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I would rather loose a little than loose everything to drought
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantification and doesn't explain the value lost."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 67. Item `line7`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** Maize that matures quickly  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: Maize that matures quickly
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for ‘early maturing’ – no criteria for speed of maturation.  Doesn’t define ‘quickly’ – just states it’s fast."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: Maize that matures quickly
Analysis: {"specificity": "High", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for ‘early maturing’ – no criteria for speed of maturation.  Doesn’t define ‘quickly’ – just states it’s fast."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for ‘early maturing’ – no criteria for speed of maturation.  Doesn’t define ‘quickly’ – just states it’s fast."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: Maize that matures quickly
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for ‘early maturing’ – no criteria for speed of maturation.  Doesn’t define ‘quickly’ – just states it’s fast."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 68
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":68
}
```

</details>

---

## 68. Item `line70`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Even when the rain is not sufficient, the variety still performs well and gives me a harvest  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Even when the rain is not sufficient, the variety still performs well and gives me a harvest
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data; doesn't specify the yield amount or the impact of rain."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Even when the rain is not sufficient, the variety still performs well and gives me a harvest
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data; doesn't specify the yield amount or the impact of rain."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks quantitative data and context; doesn't address the core question of yield reduction."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Even when the rain is not sufficient, the variety still performs well and gives me a harvest
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks quantitative data and context; doesn't address the core question of yield reduction."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 69. Item `line71`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** This year the drought was really bad, I harvested much less than usual. I managed to harvest 12 bags from my 1 acre.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: This year the drought was really bad, I harvested much less than usual. I managed to harvest 12 bags from my 1 acre.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data (yield), doesn’t specify the ‘earlier’ timeframe, and doesn’t provide context about the drought’s severity."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: This year the drought was really bad, I harvested much less than usual. I managed to harvest 12 bags from my 1 acre.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data (yield), doesn’t specify the ‘earlier’ timeframe, and doesn’t provide context about the drought’s severity."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks quantitative yield data and doesn’t address the ‘earlier’ timeframe. The drought is mentioned but not quantified."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: This year the drought was really bad, I harvested much less than usual. I managed to harvest 12 bags from my 1 acre.
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks quantitative yield data and doesn’t address the ‘earlier’ timeframe. The drought is mentioned but not quantified."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "Low",
  "usability": "High",
  "clarity": "High",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"High",
  "clarity":"High",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 70. Item `line72`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Even if I lose some yield, that is okay, because last year, I barely got any harvest  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Even if I lose some yield, that is okay, because last year, I barely got any harvest
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantification, doesn't specify the ‘some’ yield, and doesn’t address the potential impact of the loss."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Even if I lose some yield, that is okay, because last year, I barely got any harvest
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantification, doesn't specify the ‘some’ yield, and doesn’t address the potential impact of the loss."}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks quantification, doesn’t specify the ‘some’ yield, and doesn’t address the potential impact of the loss."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Even if I lose some yield, that is okay, because last year, I barely got any harvest
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 2,
  "specificity": 1,
  "usability": 1,
  "clarity": 1,
  "completeness": 1,
  "relevance": 1,
  "overall_score": 40
}
```

### Stage `p3` — 💡 Output
```text
“High”
```

</details>

---

## 71. Item `line73`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I can lose 5 bags, more than that, will be too much  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I can lose 5 bags, more than that, will be too much
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Loses bags, lacks quantification, unclear impact."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I can lose 5 bags, more than that, will be too much
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Loses bags, lacks quantification, unclear impact."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"Low","relevance":"High","weaknesses":"Loses bags, lacks quantification, unclear impact."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I can lose 5 bags, more than that, will be too much
Analysis: {"completeness": "Medium", "clarity": "Low", "relevance": "High", "weaknesses": "Loses bags, lacks quantification, unclear impact."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 20,
  "specificity": 20,
  "usability": 10,
  "clarity": 30,
  "completeness": 10,
  "relevance": 10,
  "overall_score": 25
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 20,
  "specificity": 20,
  "usability": 10,
  "clarity": 30,
  "completeness": 10,
  "relevance": 10,
  "overall_score": 75
}
```

</details>

---

## 72. Item `line74`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** As long as i dont loss more that 10% of the harvest  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: As long as i dont loss more that 10% of the harvest
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Doesn't specify the yield loss threshold, lacks context."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: As long as i dont loss more that 10% of the harvest
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Doesn't specify the yield loss threshold, lacks context."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks a yield loss threshold, needs quantification."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: As long as i dont loss more that 10% of the harvest
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks a yield loss threshold, needs quantification."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 70,
  "specificity": 70,
  "usability": 60,
  "clarity": 70,
  "completeness": 60,
  "relevance": 70,
  "overall_score": 65
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 70,
  "specificity": 70,
  "usability": 60,
  "clarity": 70,
  "completeness": 60,
  "relevance": 70,
  "overall_score": 70
}
```

</details>

---

## 73. Item `line75`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Utmost Ksh 3000 worth of yield for each earlier cycle I supply the miller  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Utmost Ksh 3000 worth of yield for each earlier cycle I supply the miller
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Lacks context – no timeframe or specific yield. Numerical value is missing."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Utmost Ksh 3000 worth of yield for each earlier cycle I supply the miller
Analysis: {"specificity": "Low", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks context – no timeframe or specific yield. Numerical value is missing."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"High","relevance":"High","weaknesses":"Missing timeframe and specific yield. Numerical value absent."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Utmost Ksh 3000 worth of yield for each earlier cycle I supply the miller
Analysis: {"completeness": "Low", "clarity": "High", "relevance": "High", "weaknesses": "Missing timeframe and specific yield. Numerical value absent."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 30,
  "specificity": 3,
  "usability": 1,
  "clarity": 1,
  "completeness": 1,
  "relevance": 1,
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output
```text
“High”
```

</details>

---

## 74. Item `line76`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Utmost one 90kg bag per 1/4 of an acre  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Utmost one 90kg bag per 1/4 of an acre
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"Low","weaknesses":"Lacks context – no yield units. Could be more precise with acreage."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Utmost one 90kg bag per 1/4 of an acre
Analysis: {"specificity": "High", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks context – no yield units. Could be more precise with acreage."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks context – no yield units. Needs to be quantified."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Utmost one 90kg bag per 1/4 of an acre
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – no yield units. Needs to be quantified."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "High",
  "usability": "Medium",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 85
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"Medium",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":85
}
```

</details>

---

## 75. Item `line77`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** If I can eat in June, yield doesn’t matter much  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: If I can eat in June, yield doesn’t matter much
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no quantity or timeframe specified. “Doesn’t matter” is vague.”}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: If I can eat in June, yield doesn’t matter much
Analysis: {}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Lacks context about yield, doesn’t specify ‘earlier’ timeframe, and doesn’t quantify the ‘earlier’ aspect."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: If I can eat in June, yield doesn’t matter much
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 2,
  "specificity": 1,
  "usability": 1,
  "clarity": 1,
  "completeness": 1,
  "relevance": 1,
  "overall_score": 40
}
```

### Stage `p3` — 💡 Output
```text
“High”
```

</details>

---

## 76. Item `line78`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** The early ones don’t give as many bags, but I prefer them  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: The early ones don’t give as many bags, but I prefer them
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantification and doesn’t explain the trade-off."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: The early ones don’t give as many bags, but I prefer them
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantification and doesn’t explain the trade-off."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks quantification and doesn’t explain the trade-off."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: The early ones don’t give as many bags, but I prefer them
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks quantification and doesn’t explain the trade-off."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 30,
  "specificity": 30,
  "usability": 30,
  "clarity": 30,
  "completeness": 30,
  "relevance": 30,
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 30,
  "specificity": 30,
  "usability": 30,
  "clarity": 30,
  "completeness": 30,
  "relevance": 30,
  "overall_score": 30
}
```

</details>

---

## 77. Item `line79`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I can’t lose yield, food is not enough  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I can’t lose yield, food is not enough
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, doesn’t specify the impact of early harvesting."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I can’t lose yield, food is not enough
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, doesn’t specify the impact of early harvesting."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and doesn't explain the impact of early harvesting."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I can’t lose yield, food is not enough
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and doesn't explain the impact of early harvesting."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 78. Item `line8`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** The variety I can harvest before my neighbors  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: The variety I can harvest before my neighbors
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for 'early maturing'. Relies on neighbor observation, not defined characteristics."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: The variety I can harvest before my neighbors
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for 'early maturing'. Relies on neighbor observation, not defined characteristics."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses":"Lacks specific criteria for 'early maturing'. Relies on neighbor observation, not defined characteristics."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: The variety I can harvest before my neighbors
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks specific criteria for 'early maturing'. Relies on neighbor observation, not defined characteristics."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Very Low",
  "usability": "Very Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Very Low",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Very Low",
  "usability":"Very Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Very Low",
  "overall_score":20
}
```

</details>

---

## 79. Item `line80`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** I know early maize gives less, maybe two bags less per acre  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: I know early maize gives less, maybe two bags less per acre
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"Low","weaknesses":"Lacks quantification, doesn’t specify ‘earlier’ timeframe, could be improved with a range."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: I know early maize gives less, maybe two bags less per acre
Analysis: {"specificity": "Medium", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks quantification, doesn’t specify ‘earlier’ timeframe, could be improved with a range."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific yield figures, doesn't address the trade-off, and doesn't consider different yield levels."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: I know early maize gives less, maybe two bags less per acre
Analysis: {"completeness": "High", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific yield figures, doesn't address the trade-off, and doesn't consider different yield levels."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "Medium",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 63
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 80. Item `line81`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** It depends on the rains  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: It depends on the rains
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantification and doesn’t specify the type of yield."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: It depends on the rains
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantification and doesn’t specify the type of yield."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Lacks quantification and doesn't specify the type of yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: It depends on the rains
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks quantification and doesn't specify the type of yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":20
}
```

</details>

---

## 81. Item `line82`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 82. Item `line83`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 83. Item `line84`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 84. Item `line85`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 85. Item `line86`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 86. Item `line87`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 87. Item `line88`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 88. Item `line89`

**Question:** How much yield would you give up for harvesting earlier?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific yield mentioned."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield would you give up for harvesting earlier?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative data and context about yield."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 89. Item `line9`

**Question:** What would you consider to be an early maturing maize variety?  
**Answer:** The one that avoids the drought period  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: What would you consider to be an early maturing maize variety?
Answer: The one that avoids the drought period
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific criteria for ‘early maturing’ and doesn’t define any criteria for drought resistance."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: What would you consider to be an early maturing maize variety?
Answer: The one that avoids the drought period
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific criteria for ‘early maturing’ and doesn’t define any criteria for drought resistance."}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific criteria for ‘early maturing’ and doesn’t define any criteria for drought resistance."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: What would you consider to be an early maturing maize variety?
Answer: The one that avoids the drought period
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 30,
  "specificity": 20,
  "usability": 40,
  "clarity": 30,
  "completeness": 20,
  "relevance": 40,
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": 30,
  "specificity": 20,
  "usability": 40,
  "clarity": 30,
  "completeness": 20,
  "relevance": 40,
  "overall_score": 75
}
```

</details>

---

## 90. Item `line90`

**Question:** Have you noticed any yield difference depending on a variety's maturity period?  
**Answer:** Yes  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: Have you noticed any yield difference depending on a variety's maturity period?
Answer: Yes
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Lacks specific maturity periods, could be more precise. Might need further context to understand the question fully."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: Have you noticed any yield difference depending on a variety's maturity period?
Answer: Yes
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Lacks specific maturity periods, could be more precise. Might need further context to understand the question fully."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific maturity periods and doesn't explain the reasoning behind the yield difference."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: Have you noticed any yield difference depending on a variety's maturity period?
Answer: Yes
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific maturity periods and doesn't explain the reasoning behind the yield difference."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "High",
  "usability": "Medium",
  "clarity": "High",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 50
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"Medium",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":50
}
```

</details>

---

## 91. Item `line91`

**Question:** Have you noticed any yield difference depending on a variety's maturity period?  
**Answer:** No  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: Have you noticed any yield difference depending on a variety's maturity period?
Answer: No
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Missing context – no data provided about yield differences. Doesn’t specify maturity period or how it’s measured."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: Have you noticed any yield difference depending on a variety's maturity period?
Answer: No
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Missing context – no data provided about yield differences. Doesn’t specify maturity period or how it’s measured."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Missing data – yield differences are not addressed. No context about maturity period or measurement is provided."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: Have you noticed any yield difference depending on a variety's maturity period?
Answer: No
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Missing data – yield differences are not addressed. No context about maturity period or measurement is provided."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 20
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":20
}
```

</details>

---

## 92. Item `line92`

**Question:** How much yield do you lose when you plant an earlier maturing variety than normal?  
**Answer:** I harvest 3 bags less with Katumani compared to Duma 43  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: I harvest 3 bags less with Katumani compared to Duma 43
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"Low","weaknesses":"Lacks context – no yield comparison or explanation. Only states a difference, not the magnitude."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: I harvest 3 bags less with Katumani compared to Duma 43
Analysis: {"specificity": "Medium", "detail": "Medium", "usability": "Low", "weaknesses": "Lacks context – no yield comparison or explanation. Only states a difference, not the magnitude."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"High","relevance":"High","weaknesses":"Lacks context – no yield comparison or explanation. Only states a difference, not the magnitude."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: I harvest 3 bags less with Katumani compared to Duma 43
Analysis: {"completeness": "Low", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – no yield comparison or explanation. Only states a difference, not the magnitude."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "High",
  "specificity": "High",
  "usability": "Medium",
  "clarity": "Medium",
  "completeness": "Medium",
  "relevance": "High",
  "overall_score": 35
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"Medium",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":35
}
```

</details>

---

## 93. Item `line93`

**Question:** How much yield do you lose when you plant an earlier maturing variety than normal?  
**Answer:** The yield loss is significant  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: The yield loss is significant
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific variety or planting timing. Doesn’t quantify the loss."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: The yield loss is significant
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no specific variety or planting timing. Doesn’t quantify the loss."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses": "Lacks context and quantification. Doesn't specify the variety or timing."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: The yield loss is significant
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context and quantification. Doesn't specify the variety or timing."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Medium",
  "specificity": "High",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 45
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"High",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":45
}
```

</details>

---

## 94. Item `line94`

**Question:** How much yield do you lose when you plant an earlier maturing variety than normal?  
**Answer:** The yield loss is  not significant  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: The yield loss is  not significant
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: The yield loss is  not significant
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: The yield loss is  not significant
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "High",
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":30
}
```

</details>

---

## 95. Item `line95`

**Question:** How much yield do you lose when you plant an earlier maturing variety than normal?  
**Answer:** It  depends on the season  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: It  depends on the season
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn’t specify the impact on yield."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: It  depends on the season
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and doesn’t specify the impact on yield."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses":"Lacks specific yield figures and doesn’t consider factors like weather or soil conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: It  depends on the season
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks specific yield figures and doesn’t consider factors like weather or soil conditions."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Low",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 25
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":25
}
```

</details>

---

## 96. Item `line96`

**Question:** How much yield do you lose when you plant an earlier maturing variety than normal?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Low","weaknesses": "Lacks quantitative data and doesn't specify the type of yield loss."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Low", "weaknesses": "Lacks quantitative data and doesn't specify the type of yield loss."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":30
}
```

</details>

---

## 97. Item `line97`

**Question:** How much yield do you lose when you plant an earlier maturing variety than normal?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Low","weaknesses": "Lacks quantitative data and doesn't specify the type of yield loss."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Low", "weaknesses": "Lacks quantitative data and doesn't specify the type of yield loss."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":30
}
```

</details>

---

## 98. Item `line98`

**Question:** How much yield do you lose when you plant an earlier maturing variety than normal?  
**Answer:** Most of them came up fine.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Inspect the following Question and Answer.
Task: Provide a short evaluation of the Answer, focusing only on specificity, detail, and usability, plus main weaknesses.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- specificity, detail, usability → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis.
Task: Decide whether the Answer contains enough information to fully and practically address the Question.
Assess based on: coverage of all asked parts, concrete specifics (numbers, names, steps, conditions), reasoning/evidence, stated assumptions, constraints/edge cases, and actionability.

Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): completeness, clarity, relevance, weaknesses.
Rules:
- completeness, clarity, relevance → one allowed label each.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"No numeric target and lacks supporting context."}

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and doesn’t specify the type of yield loss."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Low","weaknesses": "Lacks quantitative data and doesn't specify the type of yield loss."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Very Low".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.

Rules:

- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
  Allowed labels: Very High, High, Medium, Low, Very Low.

- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
    Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
    Take the average of all 6 values with equal weight.
    Round to the nearest integer.
    Clamp the result to 0–100.
    Never output an overall_score that is inconsistent with the 6 labels.

Question: How much yield do you lose when you plant an earlier maturing variety than normal?
Answer: Most of them came up fine.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Low", "weaknesses": "Lacks quantitative data and doesn't specify the type of yield loss."}
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "Low",
  "specificity": "Low",
  "usability": "Low",
  "clarity": "Medium",
  "completeness": "Low",
  "relevance": "Medium",
  "overall_score": 30
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":30
}
```

</details>

---
