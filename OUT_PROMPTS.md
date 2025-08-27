# Prompt Log (Grouped Flow)

`all.prompts.jsonl` を解析し、p1→p2→p3 を1セットにまとめています。


---

## 1. Item `line1`

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

## 2. Item `line2`

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

## 3. Item `line3`

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

## 4. Item `line4`

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

## 5. Item `line5`

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
