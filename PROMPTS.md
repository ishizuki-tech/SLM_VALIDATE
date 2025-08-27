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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I planted more seeds this year
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data; no specific percentage expected."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I planted more seeds this year
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data; no specific percentage expected."}
```

### Stage `p2` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data; no specific percentage expected."}
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
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data; no specific percentage expected."}
```

### Stage `p3` — 💡 Output
```text
“Medium”
```

### Stage `p3` — 💡 Output
```text
“60"""
```

### Stage `p3` — 💡 Output
```text
{
  "detail": "The response provides a basic explanation of the topic.",
  "specificity": "Lacks specific examples or details.",
  "usability": "Easy to understand but could be more engaging.",
  "clarity": "The explanation is somewhat unclear and could be more precise.",
  "completeness": "Doesn't cover all aspects of the topic.",
  "relevance": "Relevant to the topic but could be more focused."
}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Very Low",
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

## 2. Item `q002`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Better than last year.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Better than last year.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no data on planting conditions or expected outcome. Doesn’t specify ‘healthy’ plants."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Better than last year.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no data on planting conditions or expected outcome. Doesn’t specify ‘healthy’ plants."}
```

### Stage `p2` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context"}
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
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context"}
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

## 3. Item `q003`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Only a few gaps here and there.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Only a few gaps here and there.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no range provided for expected growth, needs specific metric (e.g., percentage)."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Only a few gaps here and there.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no range provided for expected growth, needs specific metric (e.g., percentage)."}
```

### Stage `p2` — 💡 Output
```text
{"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no range provided for expected growth, needs specific metric (e.g., percentage)."}
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
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data, no range provided for expected growth, needs specific metric (e.g., percentage)."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 28}
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

## 4. Item `q004`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** The stand is adequate  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: The stand is adequate
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and context. Doesn’t specify ‘healthy’ or ‘adequate’ in relation to the plant’s species or conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: The stand is adequate
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and context. Doesn’t specify ‘healthy’ or ‘adequate’ in relation to the plant’s species or conditions."}
```

### Stage `p2` — 💡 Output
```text
{
  "specificity": "Low",
  "detail": "Low",
  "usability": "Low",
  "weaknesses": "Lacks quantitative data and context. Doesn’t specify ‘healthy’ or ‘adequate’ in relation to the plant’s species or conditions."
}
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
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and context. Doesn’t specify ‘healthy’ or ‘adequate’ in relation to the plant’s species or conditions."}
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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Almost all.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data (percentage) and assumes a consistent outcome. Doesn’t specify the conditions for ‘almost all’."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Almost all.
Analysis: {"specificity":"Medium","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data (percentage) and assumes a consistent outcome. Doesn’t specify the conditions for ‘almost all’."}
```

### Stage `p2` — 💡 Output
```text
{"specificity":"Medium","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data (percentage) and assumes a consistent outcome."}
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
Analysis: {"specificity": "Medium", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data (percentage) and assumes a consistent outcome."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Medium", "usability": "Low", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 76}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 6. Item `q006`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Good stand in the upper half of the field.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Good stand in the upper half of the field.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn't specify 'healthy' plants.","topic":"Unclear goal."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Good stand in the upper half of the field.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn't specify 'healthy' plants.","topic":"Unclear goal."}
```

### Stage `p2` — 💡 Output
```text
{
  "specificity": "Low",
  "detail": "Low",
  "usability": "Low",
  "weaknesses": "Lacks quantitative data and doesn't specify 'healthy' plants.",
  "topic": "Unclear goal"
}
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
Answer: Good stand in the upper half of the field.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and doesn't specify 'healthy' plants.", "topic": "Unclear goal"}
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

## 7. Item `q007`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** At least 85% of seeds should be healthy by day 14 after planting.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: At least 85% of seeds should be healthy by day 14 after planting.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Medium","detail":"Medium","usability":"High","weaknesses":"Lacks context – no specific conditions for ‘healthy’ plants. Doesn’t mention environmental factors.”}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: At least 85% of seeds should be healthy by day 14 after planting.
Analysis: {"specificity":"Medium","detail":"Medium","usability":"High","weaknesses":"Lacks context – no specific conditions for ‘healthy’ plants. Doesn’t mention environmental factors.”}
```

### Stage `p2` — 💡 Output
```text
: {
  "specificity": "Low",
  "detail": "High",
  "usability": "High",
  "weaknesses": "Lacks context and specific conditions for 'healthy' plants."
}
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
Answer: At least 85% of seeds should be healthy by day 14 after planting.
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{"detail":"High","specificity":"High","usability":"High","clarity":"High","completeness":"High","relevance":"High","overall_score":93}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"High",
  "specificity":"High",
  "usability":"High",
  "clarity":"High",
  "completeness":"High",
  "relevance":"High",
  "overall_score":80
}
```

</details>

---

## 8. Item `q008`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** 90% survival by two weeks, counted against my target spacing.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: 90% survival by two weeks, counted against my target spacing.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific criteria for ‘healthy’ plants, no context about the planting conditions."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: 90% survival by two weeks, counted against my target spacing.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data, no specific criteria for ‘healthy’ plants, no context about the planting conditions."}
```

### Stage `p2` — 💡 Output
```text
{
  "specificity": "Moderate",
  "detail": "Low",
  "usability": "Low",
  "weaknesses": "Lacks quantitative data and context"
}
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
Answer: 90% survival by two weeks, counted against my target spacing.
Analysis: {"specificity": "Moderate", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and context"}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Low", "usability": "Low", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 68}
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

## 9. Item `q009`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Not less than 45,000 plants/ha by 14 days.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Not less than 45,000 plants/ha by 14 days.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"High","detail":"Specific number and timeframe","usability":"Low","weaknesses":"Lacks context – no explanation of how the number was determined or why this timeframe is important."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Not less than 45,000 plants/ha by 14 days.
Analysis: {"specificity":"High","detail":"Specific number and timeframe","usability":"Low","weaknesses":"Lacks context – no explanation of how the number was determined or why this timeframe is important."}
```

### Stage `p2` — 💡 Output
```text
{
  "specificity": "High",
  "detail": "Specific number and timeframe",
  "usability": "Low",
  "weaknesses": "Lacks context – no explanation of how the number was determined or why this timeframe is important."
}
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
Answer: Not less than 45,000 plants/ha by 14 days.
Analysis: {"specificity": "High", "detail": "Specific number and timeframe", "usability": "Low", "weaknesses": "Lacks context – no explanation of how the number was determined or why this timeframe is important."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Specific number and timeframe", "specificity": "High", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "High", "overall_score": 36}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Very Low",
  "specificity":"High",
  "usability":"Low",
  "clarity":"Low",
  "completeness":"Low",
  "relevance":"High",
  "overall_score":50
}
```

</details>

---

## 10. Item `q010`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** I bought certified seed this time.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I bought certified seed this time.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no planting conditions or expected outcome. Doesn’t specify ‘healthy’ criteria."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I bought certified seed this time.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no planting conditions or expected outcome. Doesn’t specify ‘healthy’ criteria."}
```

### Stage `p2` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context - no planting conditions or expected outcome."}
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
Answer: I bought certified seed this time.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context - no planting conditions or expected outcome."}
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

## 11. Item `q011`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** We planted right after the first big rain.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: We planted right after the first big rain.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn’t specify the conditions (e.g., soil, sunlight) for healthy growth."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: We planted right after the first big rain.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data and doesn’t specify the conditions (e.g., soil, sunlight) for healthy growth."}
```

### Stage `p2` — 💡 Output
```text
{
  "specificity": "Low",
  "detail": "Low",
  "usability": "Low",
  "weaknesses": "Lacks quantitative data and doesn't specify the conditions (e.g., soil, sunlight) for healthy growth."
}
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
Answer: We planted right after the first big rain.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks quantitative data and doesn't specify the conditions (e.g., soil, sunlight) for healthy growth."}
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

## 12. Item `q012`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** I used a jab planter instead of a hoe.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I used a jab planter instead of a hoe.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no data on planting conditions or expected outcome. Doesn’t specify the type of seeds or environment."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I used a jab planter instead of a hoe.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no data on planting conditions or expected outcome. Doesn’t specify the type of seeds or environment."}
```

### Stage `p2` — 💡 Output
```text
{
  "specificity": "Low",
  "detail": "Low",
  "usability": "Low",
  "weaknesses": "Lacks context – no data on planting conditions or expected outcome."
}
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
Answer: I used a jab planter instead of a hoe.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no data on planting conditions or expected outcome."}
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

## 13. Item `q013`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** Most of them.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Most of them.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific growth criteria. Doesn’t quantify ‘most’.”}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: Most of them.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific growth criteria. Doesn’t quantify ‘most’.”}
```

### Stage `p2` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks context – no specific growth criteria."}
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
Answer: Most of them.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Lacks context – no specific growth criteria."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Medium", "specificity": "Medium", "usability": "Low", "clarity": "High", "completeness": "Medium", "relevance": "High", "overall_score": 73}
```

### Stage `p3` — 💡 Output 🔥 FINAL CANONICAL JSON

> ⚠️ **Final Canonical JSON (最終スコア/確定結果)**

```json
{
  "detail":"Medium",
  "specificity":"Medium",
  "usability":"Low",
  "clarity":"High",
  "completeness":"Medium",
  "relevance":"High",
  "overall_score":63
}
```

</details>

---

## 14. Item `q014`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** I am satisfied with my crop this year.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I am satisfied with my crop this year.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Missing quantitative data – no specific percentage expected. Focuses on a general statement, not a measurable expectation."}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: I am satisfied with my crop this year.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Missing quantitative data – no specific percentage expected. Focuses on a general statement, not a measurable expectation."}
```

### Stage `p2` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Missing quantitative data - no specific percentage expected. Focuses on a general statement, not a measurable expectation."}
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
Answer: I am satisfied with my crop this year.
Analysis: {"specificity": "Low", "detail": "Low", "usability": "Low", "weaknesses": "Missing quantitative data - no specific percentage expected. Focuses on a general statement, not a measurable expectation."}
```

### Stage `p3` — 💡 Output
```text
{"detail": "Low", "specificity": "Low", "usability": "Low", "clarity": "Low", "completeness": "Low", "relevance": "Medium", "overall_score": 28}
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

## 15. Item `q015`

**Question:** After planting, what share of seeds do you expect to grow into healthy plants?  
**Answer:** A good stand overall.  


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

Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: A good stand overall.
```

### Stage `p1` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data – no percentage provided. Doesn’t specify ‘healthy’ – needs a metric or range.”}
```

### Stage `p2` — 📝 Input
```text
Inspect the Question, Answer, and prior Analysis. Decide whether the Answer contains enough information to fully and practically address the Question.
Output ONLY raw JSON on a SINGLE LINE. Any other text is invalid. The first character must be '{' and the last must be '}'. Do NOT include ```json, ``` or any code fences.Return EXACTLY ONE JSON object on a SINGLE LINE. No code fences. No prose.
Question: After planting, what share of seeds do you expect to grow into healthy plants?
Answer: A good stand overall.
Analysis: {"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data – no percentage provided. Doesn’t specify ‘healthy’ – needs a metric or range.”}
```

### Stage `p2` — 💡 Output
```text
{"specificity":"Low","detail":"Low","usability":"Low","weaknesses":"Lacks quantitative data – no percentage provided. Doesn’t specify ‘healthy’ – needs a metric or range.”}
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
Answer: A good stand overall.
Analysis: {}
```

### Stage `p3` — 💡 Output
```text
{"detail":"High","specificity":"Medium","usability":"High","clarity":"Medium","completeness":"Medium","relevance":"High","overall_score":78}
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
