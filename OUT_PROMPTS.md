# Prompt Log (Grouped Flow)

`all.prompts.jsonl` を解析し、p1→p2→p3 を1セットにまとめています。


---

## 1. Item `q001`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** I planted more seeds this year  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- Inspect canopy-specific Answer.
- specificity, detail, usability → one allowed label each. Focus on details about leaf coverage and growth stage.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I planted more seeds this year
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Lack of detail about expected growth - no specific timeframe or growth stage information."}
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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I planted more seeds this year
Analysis: {"specificity": "Low", "detail": "Medium", "usability": "Low", "weaknesses": "Lack of detail about expected growth - no specific timeframe or growth stage information."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses":"Missing expected growth stage and timeframe. No data on expected yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I planted more seeds this year
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Missing expected growth stage and timeframe. No data on expected yield."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "High", "overall_score": 35}
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
  "overall_score":47
}
```

</details>

---

## 2. Item `q002`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Better than last year.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- Inspect canopy-specific Answer.
- specificity, detail, usability → one allowed label each. Focus on details about leaf coverage and growth stage.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Better than last year.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"Low","weaknesses":"Lack of detail about growth stage and expected yield makes this weak."}
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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Better than last year.
Analysis: {"specificity": "Medium", "detail": "Medium", "usability": "Low", "weaknesses": "Lack of detail about growth stage and expected yield makes this weak."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"High","relevance":"High","weaknesses":"Missing quantitative data and context about 'healthy plants'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Better than last year.
Analysis: {"completeness": "Low", "clarity": "High", "relevance": "High", "weaknesses": "Missing quantitative data and context about 'healthy plants'."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "Low", "clarity": "High", "completeness": "Low", "relevance": "High", "overall_score": 40}
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
  "overall_score":57
}
```

</details>

---

## 3. Item `q003`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Only a few gaps here and there.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- Inspect canopy-specific Answer.
- specificity, detail, usability → one allowed label each. Focus on details about leaf coverage and growth stage.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Only a few gaps here and there.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Lack of detail about growth stage and expected yield makes this weak."}
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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Only a few gaps here and there.
Analysis: {"specificity": "Low", "detail": "Medium", "usability": "Low", "weaknesses": "Lack of detail about growth stage and expected yield makes this weak."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific yield expectations and growth stage details."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Only a few gaps here and there.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific yield expectations and growth stage details."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 4. Item `q004`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** The stand is adequate  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- Inspect canopy-specific Answer.
- specificity, detail, usability → one allowed label each. Focus on details about leaf coverage and growth stage.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: The stand is adequate
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"Low","weaknesses":"Lack of detail about growth stage and expected yield. Needs more specific data points."}
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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: The stand is adequate
Analysis: {"specificity": "Medium", "detail": "Medium", "usability": "Low", "weaknesses": "Lack of detail about growth stage and expected yield. Needs more specific data points."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Missing expected yield and growth stage details. Needs quantification."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: The stand is adequate
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Missing expected yield and growth stage details. Needs quantification."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
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
  "overall_score":43
}
```

</details>

---

## 5. Item `q005`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Almost all.  


<details>
<summary>Show this set</summary>


### Stage `p1` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (4 total): specificity, detail, usability, weaknesses.
Rules:
- Inspect canopy-specific Answer.
- specificity, detail, usability → one allowed label each. Focus on details about leaf coverage and growth stage.
- weaknesses → short free-text string (≤ 140 chars).
- Never output an empty string or placeholder for weaknesses.

Example:
{"specificity":"Low","detail":"Medium","usability":"Low","weaknesses":"Too vague and lacks numeric values."}

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Almost all.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Medium","usability":"High","weaknesses":"Lack of detail about growth stage and expected yield makes this vague."}
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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Almost all.
Analysis: {"specificity": "High", "detail": "Medium", "usability": "High", "weaknesses": "Lack of detail about growth stage and expected yield makes this vague."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific yield expectation and growth phase details."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Almost all.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific yield expectation and growth phase details."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Medium", "usability": "High", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 68}
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
  "overall_score":70
}
```

</details>

---

## 6. Item `q006`

**Question:** By six weeks after planting, how much of the ground should be covered by the crop’s leaves?  
**Answer:** Enough to shade most weeds.  


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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: Enough to shade most weeds.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific detail about leaf coverage and doesn’t quantify the amount."}
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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: Enough to shade most weeds.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific detail about leaf coverage and doesn’t quantify the amount."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Low","weaknesses":"Lacks specific detail about leaf coverage and doesn’t quantify the amount."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: Enough to shade most weeds.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Low", "weaknesses": "Lacks specific detail about leaf coverage and doesn’t quantify the amount."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 7. Item `q007`

**Question:** By six weeks after planting, how much of the ground should be covered by the crop’s leaves?  
**Answer:** I like it looking ‘closed’ by then.  


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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: I like it looking ‘closed’ by then.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative measurement and assumes a specific outcome. “Closed” is subjective.”}
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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: I like it looking ‘closed’ by then.
Analysis: {}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Missing specific yield target, lacks context about ‘closed’ meaning, no measurement or calculation."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: I like it looking ‘closed’ by then.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Missing specific yield target, lacks context about ‘closed’ meaning, no measurement or calculation."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 8. Item `q008`

**Question:** By six weeks after planting, how much of the ground should be covered by the crop’s leaves?  
**Answer:** Shouldn’t see much bare soil.  


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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: Shouldn’t see much bare soil.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative measurement and assumes a consistent coverage."}
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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: Shouldn’t see much bare soil.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative measurement and assumes a consistent coverage."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses": "Lacks quantitative measurement and assumes a consistent coverage."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: Shouldn’t see much bare soil.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Lacks quantitative measurement and assumes a consistent coverage."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Medium", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "High", "overall_score": 35}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":50
}
```

</details>

---

## 9. Item `q009`

**Question:** By six weeks after planting, how much of the ground should be covered by the crop’s leaves?  
**Answer:** About three-quarters.  


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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: About three-quarters.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Medium","weaknesses":"Lacks context – no specific crop type or planting timeframe. Doesn’t specify ‘about three-quarters’ – needs quantification."}
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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: About three-quarters.
Analysis: {"specificity": "Medium", "detail": "Low", "usability": "Medium", "weaknesses": "Lacks context – no specific crop type or planting timeframe. Doesn’t specify ‘about three-quarters’ – needs quantification."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific details about the crop and timeframe. Needs quantification of 'about three-quarters'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: About three-quarters.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific details about the crop and timeframe. Needs quantification of 'about three-quarters'."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Medium", "usability": "High", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 63}
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
  "overall_score":70
}
```

</details>

---

## 10. Item `q010`

**Question:** By six weeks after planting, how much of the ground should be covered by the crop’s leaves?  
**Answer:** More than half.  


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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: More than half.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific crop type or planting method. Doesn’t specify ‘more than half’ – needs quantification."}
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

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: More than half.
Analysis: {"specificity": "Medium", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no specific crop type or planting method. Doesn’t specify ‘more than half’ – needs quantification."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks context and specific measurement."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By six weeks after planting, how much of the ground should be covered by the crop’s leaves?
Answer: More than half.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context and specific measurement."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Medium", "usability": "High", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 63}
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
  "overall_score":70
}
```

</details>

---

## 11. Item `q011`

**Question:** How high do you like the ears to be from the ground for easy picking?  
**Answer:** Not too low.  


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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Not too low.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify ‘easy picking’ – only a general preference.”}
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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Not too low.
Analysis: {}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Missing context – ‘easy picking’ is undefined. No specific height range provided. No reasoning or evidence."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Not too low.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Missing context – ‘easy picking’ is undefined. No specific height range provided. No reasoning or evidence."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Medium", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Low",
  "overall_score":43
}
```

</details>

---

## 12. Item `q012`

**Question:** How high do you like the ears to be from the ground for easy picking?  
**Answer:** Comfortable to reach.  


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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Comfortable to reach.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"High","weaknesses":"Lacks context – no specific height range. Could be improved with a range or example."}
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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Comfortable to reach.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "High", "weaknesses": "Lacks context – no specific height range. Could be improved with a range or example."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks context – no specific height range. Needs to be quantified."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Comfortable to reach.
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – no specific height range. Needs to be quantified."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"High","specificity":"Medium","usability":"High","clarity":"Medium","completeness":"Medium","relevance":"High","overall_score":92}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"Medium",
  "usability":"High",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":70
}
```

</details>

---

## 13. Item `q013`

**Question:** How high do you like the ears to be from the ground for easy picking?  
**Answer:** Around waist to chest high.  


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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Around waist to chest high.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Medium","weaknesses":"Lacks context – doesn’t specify ‘easy picking’ – assumes a specific height range.”}
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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Around waist to chest high.
Analysis: {}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific height range, no context about 'easy picking'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Around waist to chest high.
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific height range, no context about 'easy picking'."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Medium","specificity":"Low","usability":"High","clarity":"High","completeness":"Medium","relevance":"High","overall_score":76}
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
  "overall_score":67
}
```

</details>

---

## 14. Item `q014`

**Question:** How high do you like the ears to be from the ground for easy picking?  
**Answer:** About a meter.  


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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: About a meter.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Medium","weaknesses":"Lacks context – doesn’t specify ‘easy picking’ – assumes a standard height."}
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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: About a meter.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Medium", "weaknesses": "Lacks context – doesn’t specify ‘easy picking’ – assumes a standard height."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks context – doesn’t specify ‘easy picking’ – assumes a standard height."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How high do you like the ears to be from the ground for easy picking?
Answer: About a meter.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – doesn’t specify ‘easy picking’ – assumes a standard height."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "High", "clarity": "Medium", "completeness": "Medium", "relevance": "High", "overall_score": 63}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"High",
  "clarity":"Medium",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 15. Item `q015`

**Question:** How high do you like the ears to be from the ground for easy picking?  
**Answer:** Mid-plant.  


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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Mid-plant.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Medium","weaknesses":"Lacks context – doesn’t specify ‘easy picking’ – only a general height range."}
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

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Mid-plant.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Medium", "weaknesses": "Lacks context – doesn’t specify ‘easy picking’ – only a general height range."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific criteria for ‘easy picking’ – only a general height range. Needs to define what ‘easy picking’ means."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How high do you like the ears to be from the ground for easy picking?
Answer: Mid-plant.
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific criteria for ‘easy picking’ – only a general height range. Needs to define what ‘easy picking’ means."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Medium","specificity":"Low","usability":"Low","clarity":"Medium","completeness":"Low","relevance":"Medium","overall_score":36}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"Medium",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":50
}
```

</details>

---

## 16. Item `q016`

**Question:** What is the most pest or disease damage you will accept before you stop using a maize variety?  
**Answer:** If worms get out of hand, I switch.  


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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: If worms get out of hand, I switch.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific details about the pests/diseases, no quantification of damage."}
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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: If worms get out of hand, I switch.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific details about the pests/diseases, no quantification of damage."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks specific details about pests/diseases, no quantification of damage."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: If worms get out of hand, I switch.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific details about pests/diseases, no quantification of damage."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
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
  "overall_score":43
}
```

</details>

---

## 17. Item `q017`

**Question:** What is the most pest or disease damage you will accept before you stop using a maize variety?  
**Answer:** When leaves look too spotted.  


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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: When leaves look too spotted.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific details about the damage, no range provided. Could be more precise."}
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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: When leaves look too spotted.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific details about the damage, no range provided. Could be more precise."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Low","weaknesses":"Lacks specific details about the damage, no range provided. Could be more precise."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: When leaves look too spotted.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Low", "weaknesses": "Lacks specific details about the damage, no range provided. Could be more precise."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Low","overall_score":28}
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
  "overall_score":40
}
```

</details>

---

## 18. Item `q018`

**Question:** What is the most pest or disease damage you will accept before you stop using a maize variety?  
**Answer:** If many cobs rot, I’m done.  


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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: If many cobs rot, I’m done.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific details about the damage, no indication of severity or timeframe.","topic":"Very Low"}
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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: If many cobs rot, I’m done.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific details about the damage, no indication of severity or timeframe.", "topic": "Very Low"}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses": "Lacks specific details about the damage, no indication of severity or timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: If many cobs rot, I’m done.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific details about the damage, no indication of severity or timeframe."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":28}
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
  "overall_score":43
}
```

</details>

---

## 19. Item `q019`

**Question:** What is the most pest or disease damage you will accept before you stop using a maize variety?  
**Answer:** Around one in ten plants.  


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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: Around one in ten plants.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify the type of damage or the timeframe. Doesn’t provide any data or quantification."}
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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: Around one in ten plants.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify the type of damage or the timeframe. Doesn’t provide any data or quantification."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Missing specific damage type and timeframe. Lacks context for 'most pest/disease damage'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: Around one in ten plants.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Missing specific damage type and timeframe. Lacks context for 'most pest/disease damage'."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":32}
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
  "overall_score":43
}
```

</details>

---

## 20. Item `q020`

**Question:** What is the most pest or disease damage you will accept before you stop using a maize variety?  
**Answer:** Not much.  


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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: Not much.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific details about the damage, no quantifiable limits provided."}
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

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: Not much.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific details about the damage, no quantifiable limits provided."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific details about the damage, no quantifiable limits provided."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most pest or disease damage you will accept before you stop using a maize variety?
Answer: Not much.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific details about the damage, no quantifiable limits provided."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 21. Item `q021`

**Question:** If there’s a two- or three-week dry spell, what harvest would you still be happy with?  
**Answer:** As long as I can cover costs.  


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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: As long as I can cover costs.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific details about the dry spell's severity or impact. Doesn’t consider potential mitigation strategies."}
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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: As long as I can cover costs.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific details about the dry spell's severity or impact. Doesn’t consider potential mitigation strategies."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "No specific details about the dry spell, making it difficult to assess the situation."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: As long as I can cover costs.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "No specific details about the dry spell, making it difficult to assess the situation."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Low","overall_score":27}
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
  "overall_score":40
}
```

</details>

---

## 22. Item `q022`

**Question:** If there’s a two- or three-week dry spell, what harvest would you still be happy with?  
**Answer:** Better than my local seed in a dry year.  


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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Better than my local seed in a dry year.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context and doesn’t specify the harvest type. Doesn’t address the ‘happy’ aspect."}
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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Better than my local seed in a dry year.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context and doesn’t specify the harvest type. Doesn’t address the ‘happy’ aspect."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Lacks context and doesn’t specify the harvest type. Doesn’t address the ‘happy’ aspect."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Better than my local seed in a dry year.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks context and doesn’t specify the harvest type. Doesn’t address the ‘happy’ aspect."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Low","overall_score":28}
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
  "overall_score":40
}
```

</details>

---

## 23. Item `q023`

**Question:** If there’s a two- or three-week dry spell, what harvest would you still be happy with?  
**Answer:** Enough to keep seed next season.  


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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Enough to keep seed next season.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific details about the dry spell's severity or impact. Doesn’t consider potential mitigation strategies."}
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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Enough to keep seed next season.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific details about the dry spell's severity or impact. Doesn’t consider potential mitigation strategies."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"High","weaknesses":"Missing context about the dry spell's duration and impact. No consideration of potential harvest yield reduction."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Enough to keep seed next season.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "High", "weaknesses": "Missing context about the dry spell's duration and impact. No consideration of potential harvest yield reduction."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "High", "overall_score": 35}
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
  "overall_score":47
}
```

</details>

---

## 24. Item `q024`

**Question:** If there’s a two- or three-week dry spell, what harvest would you still be happy with?  
**Answer:** About ten bags.  


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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: About ten bags.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific crop or region. Doesn’t consider potential impacts beyond bags."}
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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: About ten bags.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no specific crop or region. Doesn’t consider potential impacts beyond bags."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks context and doesn't address potential impacts beyond bags."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: About ten bags.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks context and doesn't address potential impacts beyond bags."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 36}
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
  "relevance":"Medium",
  "overall_score":47
}
```

</details>

---

## 25. Item `q025`

**Question:** If there’s a two- or three-week dry spell, what harvest would you still be happy with?  
**Answer:** Two tonnes.  


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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Two tonnes.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Doesn't specify the type of crop or yield, lacks context."}
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

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Two tonnes.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Doesn't specify the type of crop or yield, lacks context."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Missing crop type and yield target. Needs more detail."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: If there’s a two- or three-week dry spell, what harvest would you still be happy with?
Answer: Two tonnes.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Missing crop type and yield target. Needs more detail."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Medium", "usability": "High", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 68}
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
  "overall_score":70
}
```

</details>

---

## 26. Item `q026`

**Question:** In a bad year, what is the smallest harvest you would accept and still plant this maize again?  
**Answer:** If it beats what my neighbors get.  


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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If it beats what my neighbors get.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific timeframe or yield target, doesn’t address risk mitigation."}
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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If it beats what my neighbors get.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no specific timeframe or yield target, doesn’t address risk mitigation."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Missing quantitative target, lacks context about 'bad year', no risk assessment."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If it beats what my neighbors get.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Missing quantitative target, lacks context about 'bad year', no risk assessment."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Low","overall_score":28}
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
  "overall_score":40
}
```

</details>

---

## 27. Item `q027`

**Question:** In a bad year, what is the smallest harvest you would accept and still plant this maize again?  
**Answer:** If I still have grain to sell.  


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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If I still have grain to sell.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, doesn’t consider weather conditions, and doesn’t specify a minimum harvest amount."}
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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If I still have grain to sell.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, doesn’t consider weather conditions, and doesn’t specify a minimum harvest amount."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Missing specific harvest target, no consideration for weather, and lacks quantitative data."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If I still have grain to sell.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Missing specific harvest target, no consideration for weather, and lacks quantitative data."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "relevance":"Low",
  "overall_score":43
}
```

</details>

---

## 28. Item `q028`

**Question:** In a bad year, what is the smallest harvest you would accept and still plant this maize again?  
**Answer:** If I don’t need a food loan.  


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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If I don’t need a food loan.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific context about the bad year, no quantitative target, no consideration for yield reduction."}
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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If I don’t need a food loan.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific context about the bad year, no quantitative target, no consideration for yield reduction."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Missing specific context, no quantifiable target, lacks reasoning, no constraints."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: If I don’t need a food loan.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Missing specific context, no quantifiable target, lacks reasoning, no constraints."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "relevance":"Low",
  "overall_score":43
}
```

</details>

---

## 29. Item `q029`

**Question:** In a bad year, what is the smallest harvest you would accept and still plant this maize again?  
**Answer:** About six bags.  


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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: About six bags.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no explanation of ‘bad year’ or maize yield. Doesn’t consider potential risks or mitigation strategies."}
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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: About six bags.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no explanation of ‘bad year’ or maize yield. Doesn’t consider potential risks or mitigation strategies."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks context and doesn't address the core question of acceptable yield."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: About six bags.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks context and doesn't address the core question of acceptable yield."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "High", "overall_score": 35}
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
  "overall_score":50
}
```

</details>

---

## 30. Item `q030`

**Question:** In a bad year, what is the smallest harvest you would accept and still plant this maize again?  
**Answer:** One and a half tonnes.  


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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: One and a half tonnes.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"High","weaknesses":"Doesn't consider weather variability or risk mitigation. Could be a broad estimate."}
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

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: One and a half tonnes.
Analysis: {"specificity": "Medium", "detail": "Medium", "usability": "High", "weaknesses": "Doesn't consider weather variability or risk mitigation. Could be a broad estimate."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Doesn't address risk management or weather sensitivity."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: In a bad year, what is the smallest harvest you would accept and still plant this maize again?
Answer: One and a half tonnes.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Doesn't address risk management or weather sensitivity."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "1.5", "specificity": "Harvest", "usability": "Planting", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 38}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Very Low",
  "specificity":"Very Low",
  "usability":"Very Low",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":47
}
```

</details>

---

## 31. Item `q031`

**Question:** What is the most fallen or leaning plants you can accept at harvest?  
**Answer:** I don’t like much falling.  


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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: I don’t like much falling.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific examples or plant types, no detail about the ‘falling’ aspect."}
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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: I don’t like much falling.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific examples or plant types, no detail about the ‘falling’ aspect."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Missing specific plants, no details about ‘falling’."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: I don’t like much falling.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Missing specific plants, no details about ‘falling’."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 32. Item `q032`

**Question:** What is the most fallen or leaning plants you can accept at harvest?  
**Answer:** If it slows picking, it’s too much.  


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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: If it slows picking, it’s too much.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific examples of plants, no detail about the ‘most’ fallen, only a general statement."}
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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: If it slows picking, it’s too much.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific examples of plants, no detail about the ‘most’ fallen, only a general statement."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Medium","weaknesses":"Lacks specific examples, no detail about the ‘most’ fallen, only a general statement."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: If it slows picking, it’s too much.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Medium", "weaknesses": "Lacks specific examples, no detail about the ‘most’ fallen, only a general statement."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
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
  "overall_score":43
}
```

</details>

---

## 33. Item `q033`

**Question:** What is the most fallen or leaning plants you can accept at harvest?  
**Answer:** Just a few bent stalks is okay.  


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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: Just a few bent stalks is okay.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific plant type, no details about bending or leaning, no harvest timeframe."}
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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: Just a few bent stalks is okay.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific plant type, no details about bending or leaning, no harvest timeframe."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific plant type and doesn't address the question of 'most fallen or leaning'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: Just a few bent stalks is okay.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific plant type and doesn't address the question of 'most fallen or leaning'."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 34. Item `q034`

**Question:** What is the most fallen or leaning plants you can accept at harvest?  
**Answer:** About five percent.  


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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: About five percent.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific plant type, no detail about the fall or leaning, no context about harvest."}
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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: About five percent.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific plant type, no detail about the fall or leaning, no context about harvest."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses": "Lacks specific plant type and doesn't address the question of 'most fallen or leaning'."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: About five percent.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific plant type and doesn't address the question of 'most fallen or leaning'."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Medium", "completeness": "Low", "relevance": "High", "overall_score": 35}
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
  "overall_score":50
}
```

</details>

---

## 35. Item `q035`

**Question:** What is the most fallen or leaning plants you can accept at harvest?  
**Answer:** Very little.  


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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: Very little.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific examples or categories. Doesn’t define ‘fallen’ or ‘leaning’ in terms of plant type or condition."}
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

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: Very little.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific examples or categories. Doesn’t define ‘fallen’ or ‘leaning’ in terms of plant type or condition."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "No specific plant types or conditions are mentioned. Lacks detail about how to determine ‘fallen’ or ‘leaning’."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: What is the most fallen or leaning plants you can accept at harvest?
Answer: Very little.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "No specific plant types or conditions are mentioned. Lacks detail about how to determine ‘fallen’ or ‘leaning’."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 36. Item `q036`

**Question:** How many days after planting should the maize start to flower for your needs?  
**Answer:** Not too late for the rains.  


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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Not too late for the rains.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and doesn't consider weather conditions."}
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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Not too late for the rains.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and doesn't consider weather conditions."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Low","weaknesses":"Lacks specific timeframe and doesn't consider weather conditions."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many days after planting should the maize start to flower for your needs?
Answer: Not too late for the rains.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Low", "weaknesses": "Lacks specific timeframe and doesn't consider weather conditions."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Medium", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"Medium",
  "overall_score":47
}
```

</details>

---

## 37. Item `q037`

**Question:** How many days after planting should the maize start to flower for your needs?  
**Answer:** Soon after the first topdressing.  


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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Soon after the first topdressing.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and assumes a standard planting duration. Doesn’t specify the ideal timing for optimal flower development."}
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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Soon after the first topdressing.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and assumes a standard planting duration. Doesn’t specify the ideal timing for optimal flower development."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific timeframe and assumes a standard planting duration. Doesn't specify the ideal timing for optimal flower development."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many days after planting should the maize start to flower for your needs?
Answer: Soon after the first topdressing.
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific timeframe and assumes a standard planting duration. Doesn't specify the ideal timing for optimal flower development."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
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
  "overall_score":43
}
```

</details>

---

## 38. Item `q038`

**Question:** How many days after planting should the maize start to flower for your needs?  
**Answer:** Earlier than my old one.  


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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Earlier than my old one.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and context. Doesn't specify the ‘needs’ for the answer."}
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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Earlier than my old one.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and context. Doesn't specify the ‘needs’ for the answer."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks specific timeframe and context. Doesn't specify the ‘needs’ for the answer."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many days after planting should the maize start to flower for your needs?
Answer: Earlier than my old one.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks specific timeframe and context. Doesn't specify the ‘needs’ for the answer."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 39. Item `q039`

**Question:** How many days after planting should the maize start to flower for your needs?  
**Answer:** About two months.  


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

Question: How many days after planting should the maize start to flower for your needs?
Answer: About two months.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks specific timeframe and doesn't specify the ‘needs’ – needs to consider crop type and region."}
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

Question: How many days after planting should the maize start to flower for your needs?
Answer: About two months.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks specific timeframe and doesn't specify the ‘needs’ – needs to consider crop type and region."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses":"Lacks specific timeframe and doesn’t consider crop type/region."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many days after planting should the maize start to flower for your needs?
Answer: About two months.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific timeframe and doesn’t consider crop type/region."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "Low", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 63}
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
  "overall_score":60
}
```

</details>

---

## 40. Item `q040`

**Question:** How many days after planting should the maize start to flower for your needs?  
**Answer:** Sixties.  


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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Sixties.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific planting timeframe. Doesn’t specify the goal of the flowering."}
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

Question: How many days after planting should the maize start to flower for your needs?
Answer: Sixties.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no specific planting timeframe. Doesn’t specify the goal of the flowering."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses": "Lacks specific timeframe and context. Doesn't address the goal of flowering."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many days after planting should the maize start to flower for your needs?
Answer: Sixties.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks specific timeframe and context. Doesn't address the goal of flowering."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
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
  "overall_score":43
}
```

</details>

---

## 41. Item `q041`

**Question:** By when should the maize be ready to harvest for your conditions?  
**Answer:** Before the heavy short-rains storms.  


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

Question: By when should the maize be ready to harvest for your conditions?
Answer: Before the heavy short-rains storms.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no conditions, timeframe, or specific weather."}
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

Question: By when should the maize be ready to harvest for your conditions?
Answer: Before the heavy short-rains storms.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no conditions, timeframe, or specific weather."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses": "Lacks context – no conditions, timeframe, or specific weather."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By when should the maize be ready to harvest for your conditions?
Answer: Before the heavy short-rains storms.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks context – no conditions, timeframe, or specific weather."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":35}
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
  "overall_score":43
}
```

</details>

---

## 42. Item `q042`

**Question:** By when should the maize be ready to harvest for your conditions?  
**Answer:** In time for school fees.  


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

Question: By when should the maize be ready to harvest for your conditions?
Answer: In time for school fees.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific conditions or timeframe. Doesn’t address weather, soil, or crop health."}
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

Question: By when should the maize be ready to harvest for your conditions?
Answer: In time for school fees.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no specific conditions or timeframe. Doesn’t address weather, soil, or crop health."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses": "Lacks context and specific timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By when should the maize be ready to harvest for your conditions?
Answer: In time for school fees.
Analysis: {"completeness": "Low", "clarity": "Low", "relevance": "Low", "weaknesses": "Lacks context and specific timeframe."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Low", "overall_score": 35}
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
  "overall_score":40
}
```

</details>

---

## 43. Item `q043`

**Question:** By when should the maize be ready to harvest for your conditions?  
**Answer:** Before storage pests get bad.  


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

Question: By when should the maize be ready to harvest for your conditions?
Answer: Before storage pests get bad.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – what conditions? No timeframe is provided."}
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

Question: By when should the maize be ready to harvest for your conditions?
Answer: Before storage pests get bad.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – what conditions? No timeframe is provided."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses": "Lacks specific timeframe and conditions. Needs more detail."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By when should the maize be ready to harvest for your conditions?
Answer: Before storage pests get bad.
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific timeframe and conditions. Needs more detail."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
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
  "overall_score":43
}
```

</details>

---

## 44. Item `q044`

**Question:** By when should the maize be ready to harvest for your conditions?  
**Answer:** Around four months.  


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

Question: By when should the maize be ready to harvest for your conditions?
Answer: Around four months.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Low","usability":"Medium","weaknesses":"Lacks context – what conditions? No specific timeframe beyond ‘around four months’."}
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

Question: By when should the maize be ready to harvest for your conditions?
Answer: Around four months.
Analysis: {"specificity": "High", "detail": "Low", "usability": "Medium", "weaknesses": "Lacks context – what conditions? No specific timeframe beyond ‘around four months’."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses": "Lacks context – conditions. No specific timeframe."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By when should the maize be ready to harvest for your conditions?
Answer: Around four months.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – conditions. No specific timeframe."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Medium","specificity":"Low","usability":"Low","clarity":"High","completeness":"High","relevance":"High","overall_score":47}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"High",
  "completeness":"High",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 45. Item `q045`

**Question:** By when should the maize be ready to harvest for your conditions?  
**Answer:** By August.  


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

Question: By when should the maize be ready to harvest for your conditions?
Answer: By August.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Low","usability":"Low","weaknesses":"Lacks context – what conditions? No date range specified."}
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

Question: By when should the maize be ready to harvest for your conditions?
Answer: By August.
Analysis: {"specificity": "High", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – what conditions? No date range specified."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"High","clarity":"High","relevance":"High","weaknesses": "Lacks context – conditions are not specified."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: By when should the maize be ready to harvest for your conditions?
Answer: By August.
Analysis: {"completeness": "High", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context – conditions are not specified."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"High","completeness":"Medium","relevance":"High","overall_score":36}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Low",
  "specificity":"Low",
  "usability":"Low",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":57
}
```

</details>

---

## 46. Item `q046`

**Question:** How many ears per plant do you prefer?  
**Answer:** A good cob on each plant.  


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

Question: How many ears per plant do you prefer?
Answer: A good cob on each plant.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify ‘good’ or ‘a’ – doesn’t quantify preference."}
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

Question: How many ears per plant do you prefer?
Answer: A good cob on each plant.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify ‘good’ or ‘a’ – doesn’t quantify preference."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"High","weaknesses":"Lacks context – doesn’t specify ‘good’ or ‘a’ – doesn’t quantify preference."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many ears per plant do you prefer?
Answer: A good cob on each plant.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "High", "weaknesses": "Lacks context – doesn’t specify ‘good’ or ‘a’ – doesn’t quantify preference."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"High","overall_score":28}
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
  "overall_score":47
}
```

</details>

---

## 47. Item `q047`

**Question:** How many ears per plant do you prefer?  
**Answer:** More cobs are fine if they fill.  


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

Question: How many ears per plant do you prefer?
Answer: More cobs are fine if they fill.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify ‘preference’ or ‘cobs’ – feels like a response to a question rather than an answer."}
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

Question: How many ears per plant do you prefer?
Answer: More cobs are fine if they fill.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify ‘preference’ or ‘cobs’ – feels like a response to a question rather than an answer."}
```

### Stage `p2` — 💡 Output
```text
```json
{"completeness":"Low","clarity":"Low","relevance":"Low","weaknesses":"Lacks context, doesn’t answer the question, and is a response, not an answer."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many ears per plant do you prefer?
Answer: More cobs are fine if they fill.
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Low","overall_score":27}
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
  "overall_score":40
}
```

</details>

---

## 48. Item `q048`

**Question:** How many ears per plant do you prefer?  
**Answer:** Not too many small cobs.  


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

Question: How many ears per plant do you prefer?
Answer: Not too many small cobs.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify ‘preference’ or ‘plant’ – vague and doesn’t offer a range."}
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

Question: How many ears per plant do you prefer?
Answer: Not too many small cobs.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify ‘preference’ or ‘plant’ – vague and doesn’t offer a range."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"Medium","relevance":"Low","weaknesses":"Lacks context and doesn’t address the question of preference."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many ears per plant do you prefer?
Answer: Not too many small cobs.
Analysis: {"completeness": "Low", "clarity": "Medium", "relevance": "Low", "weaknesses": "Lacks context and doesn’t address the question of preference."}
```

### Stage `p3` — 💡 Output
```text
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Low","overall_score":28}
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
  "overall_score":40
}
```

</details>

---

## 49. Item `q049`

**Question:** How many ears per plant do you prefer?  
**Answer:** One.  


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

Question: How many ears per plant do you prefer?
Answer: One.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify preference type or range. Needs further elaboration."}
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

Question: How many ears per plant do you prefer?
Answer: One.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify preference type or range. Needs further elaboration."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Low","clarity":"High","relevance":"High","weaknesses":"Lacks context and specifies a preference, not a quantity."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many ears per plant do you prefer?
Answer: One.
Analysis: {"completeness": "Low", "clarity": "High", "relevance": "High", "weaknesses": "Lacks context and specifies a preference, not a quantity."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "High", "overall_score": 35}
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
  "overall_score":47
}
```

</details>

---

## 50. Item `q050`

**Question:** How many ears per plant do you prefer?  
**Answer:** One, sometimes two.  


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

Question: How many ears per plant do you prefer?
Answer: One, sometimes two.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – doesn’t specify preference for *how many* ears, only a general number. Needs more detail about the ‘sometimes’ and ‘sometimes’ aspects."}
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

Question: How many ears per plant do you prefer?
Answer: One, sometimes two.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – doesn’t specify preference for *how many* ears, only a general number. Needs more detail about the ‘sometimes’ and ‘sometimes’ aspects."}
```

### Stage `p2` — 💡 Output
```text
{"completeness":"Medium","clarity":"High","relevance":"High","weaknesses":"Lacks specific preference – only mentions ‘one’ and ‘sometimes’ which doesn’t address the question of ear count per plant."}
```

### Stage `p3` — 📝 Input
```text
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid.
The first character must be '{' and the last must be '}'.
No prose. Do NOT include ```json, ``` or any code fences.
Never output placeholders like <label> or <string>. If uncertain, use "Medium".
Task: Judge how well the Answer addresses the Question using the Question, Answer, and Analysis.

Allowed labels: Very High, High, Medium, Low, Very Low.
Required JSON keys (7 total): detail, specificity, usability, clarity, completeness, relevance, overall_score.
Rules:
- detail, specificity, usability, clarity, completeness, relevance → one allowed label each, chosen ONLY from the Allowed labels.
- overall_score → MUST be computed, not guessed. Strictly follow this procedure:
  • Convert each label to a number: Very High=95, High=80, Medium=60, Low=40, Very Low=20.
  • Take the average of all 6 values with equal weight.
  • Round to the nearest integer.
  • Clamp the result to 0–100.
  • Never output an overall_score that is inconsistent with the 6 labels.

Example:
{"detail":"Low","specificity":"Low","usability":"Low","clarity":"Low","completeness":"Low","relevance":"Medium","overall_score":43}

If conflicts exist between Analysis and the actual Q&A, prioritize the Q&A.

Question: How many ears per plant do you prefer?
Answer: One, sometimes two.
Analysis: {"completeness": "Medium", "clarity": "High", "relevance": "High", "weaknesses": "Lacks specific preference – only mentions ‘one’ and ‘sometimes’ which doesn’t address the question of ear count per plant."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 35}
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
  "overall_score":43
}
```

</details>

---
