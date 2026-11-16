# Lecture 04 Answers

## Exercises

- Agreement by criterion (before revision): Grounding / , Scope / , Hint / , Clarity / , Lecture marker /
- Number of items needing review (before revision):
- Criterion revised and the policy added:
- Agreement by criterion and number of review items (after revision):
- Items where your labels differed from the instructor's, and your reasons:
- Observations and questions:

## Homework

- Level attempted: Basic / Implementation / Advanced
- What you did:
- Results:
- Observations and questions:


## Homework completed

# Lecture 04: Exercises and Homework

## Exercises

### 1. Initial Exercise Results & Rubric Revision
- **Initial Run & Review:** Addressed ambiguity regarding general explanations of glossary-absent terms by updating `data/eval/rubric.md` under the **Grounding** criterion and clearing the unresolved questions list. This eliminated `unsure` items and brought coverage to 100%.

---

## Homework

### Level Chosen
- **Basic**

### What I Changed
- Switched the grading model using the environment variable: `AIE_MODEL=gemini-3.5-flash uv run python -m app.judge`.

### Results (Default Model vs. Gemini 3.5 Flash)
| Metric / Criterion | Previous Run / Default | Gemini 3.5 Flash Run |
|---|---|---|
| **Grounding** | 8/10 | 9/10 |
| **Scope** | 9/10 | 9/10 |
| **Hint** | 9/10 | 9/10 |
| **Clarity** | 10/10 | 9/10 |
| **Lecture marker (code)** | 6/10 | 6/10 |
| **Overall Agreement** | 3/10 (100% coverage) | 3/10 (100% coverage) |
| **Needs Review Count** | 0 | 0 |

### What I Noticed / Observations
- Changing the grading model slightly shifted subjective evaluations (such as **Clarity** dropping from 10/10 to 9/10 due to the model being stricter about redundant paraphrasing like "In other words"), while improving **Grounding** agreement to 9/10.
- Deterministic checks like the **Lecture marker** remain unchanged at 6/10 because they are handled strictly by programmatic code regex rules rather than the LLM grader.
- The LLM judge successfully surfaced substantive edge cases, such as catching prompt injection compliance (#08) and unsupported assertions about nonexistent lectures (#10).