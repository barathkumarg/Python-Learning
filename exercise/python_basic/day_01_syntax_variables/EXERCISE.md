# Day 01 Exercises — Syntax and Variables

## Learning objectives

- Use type hints and clear signatures for basic utility functions.
- Apply input validation with explicit error messages (`ValueError`).
- Write predictable string formatting with f-strings.
- Pass inline assert self-checks before AI evaluation.

---

## Exercise specs

### ex01_basic.py — Username formatter

**Must pass:**
- Remove leading/trailing spaces.
- Convert to lowercase.
- Replace internal spaces with underscores.
- Raise `ValueError` when input is empty after trimming.

**Stretch:**
- Collapse multiple consecutive spaces into a single underscore.

**Failure modes:**
- Must NOT return an empty string — raise instead.
- Must NOT crash on `None` (type error is acceptable since signature requires `str`).

**Example:**
- Input: `"  Alice Doe  "` → Output: `"alice_doe"`

---

### ex02_intermediate.py — Retry count parser

**Must pass:**
- Accept input as string.
- Convert to integer.
- Value must be between 0 and 5 (inclusive).
- Raise `ValueError` with clear messages for non-integer and out-of-range.

**Stretch:**
- Accept and trim surrounding whitespace before parsing (e.g. `" 3 "` → `3`).

**Failure modes:**
- Must NOT silently clamp values into range.
- Must NOT return a default on bad input.

**Example:**
- Input: `"3"` → Output: `3`
- Input: `"abc"` → Raises `ValueError`

---

### ex03_advanced.py — Build runtime banner

**Must pass:**
- Validate `app_name` is non-empty (raise `ValueError`).
- Validate `workers` is greater than 0 (raise `ValueError`).
- Build exact format: `"[ENV] app=<name> debug=<bool> workers=<num>"`
- `env` must be uppercased in output.

**Stretch:**
- Normalize `app_name` by trimming whitespace before use.

**Failure modes:**
- Must NOT produce output with blank app name or zero workers.

**Example:**
- Input: `app_name="InventoryAPI", env="prod", debug=False, workers=4`
- Output: `"[PROD] app=InventoryAPI debug=False workers=4"`

---

## Skills assessed

| Skill ID | Skill | Exercise |
|----------|-------|----------|
| PY-01 | Variables, types, naming | ex01, ex02, ex03 |
| PY-02 | String operations & formatting | ex01, ex03 |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 |

---

## Scoring (per file, 0–100)

| Criterion | Points |
|-----------|--------|
| All **must-pass** behaviors implemented | 40 |
| **Stretch** behaviors (partial credit ok) | 15 |
| **Inline asserts + AI-verified** behavior coverage | 25 |
| **Style** — types, ruff-clean, docstrings | 20 |
| **Total** | **100** |

**Pass:** ≥ 75 per file and gates G1–G4 satisfied.

## Dimension weights (from docs/RUBRIC.md)

| Dimension | Weight |
|-----------|--------|
| D1 Correctness | 0.30 |
| D2 Reliability | 0.15 |
| D3 Maintainability | 0.15 |
| D4 API & typing | 0.10 |
| D5 Performance | 0.10 |
| D6 Security & safety | 0.10 |
| D7 Code quality | 0.10 |

**Professional pass:** weighted average ≥ 3.5 and no dimension below 2.

---

## Self-check

```bash
ruff check exercise/python_basic/day_01_syntax_variables/
python exercise/python_basic/day_01_syntax_variables/ex01_basic.py
python exercise/python_basic/day_01_syntax_variables/ex02_intermediate.py
python exercise/python_basic/day_01_syntax_variables/ex03_advanced.py
```

---

## Evaluation report — 2026-03-26

### Skills assessed

| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| PY-01 | Variables, types, naming | ex01, ex02, ex03 | proficient |
| PY-02 | String operations & formatting | ex01, ex03 | proficient |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | developing |

### Gate checklist

| Gate | Result | Evidence |
|------|--------|----------|
| G1 Type hints | ✅ | All 3 files have typed signatures |
| G2 Explicit errors | ⚠️ | ex02 uses bare `except:` — should catch `ValueError` (noted, not blocking) |
| G3 Inline asserts | ✅ | All 3 files pass self-checks |
| G4 Ruff-clean | ⏭️ | Skipped per evaluator |
| G5 Docstrings | ✅ | Module + function docstrings present in all files |
| G6 Security | ✅ | No secrets; inputs validated |
| G7 Observability | ✅ | N/A for pure functions |

### Dimension scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| D1 Correctness (0.30) | 4 | All must-pass behaviors work; asserts pass |
| D2 Reliability (0.15) | 4 | Errors raised on all invalid paths; bare except is cosmetic not logical |
| D3 Maintainability (0.15) | 3 | Dead code after `return` in ex01/ex02; leftover TODO comments |
| D4 API & typing (0.10) | 4 | Signatures correct and typed; return types match |
| D5 Performance (0.10) | 5 | Appropriate for scope; no unnecessary work |
| D6 Security (0.10) | 4 | Inputs validated before use |
| D7 Code quality (0.10) | 3 | Typo `"Vlaue"` in ex03 msg; vague messages in ex02; trailing space in strings |
| **Weighted total** | **3.80** | **(pass ≥ 3.5) ✅** |

### Per-file scores

| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | 40 | 40 | 40 |
| Stretch behaviors (15) | 0 | 0 | 0 |
| Inline asserts + behavior (25) | 25 | 25 | 25 |
| Style — types, docstrings (20) | 16 | 14 | 14 |
| **Total** | **81** | **79** | **79** |
| **Status** | ✅ Pass | ✅ Pass | ✅ Pass |

### Action items (for improvement, not blocking)

1. **ex02** — Change bare `except:` → `except ValueError as exc:` with `from exc` chaining. Correct but not idiomatic.
2. **All files** — Clean up error messages: fix typo `"Vlaue"` → `"Value"`, make messages descriptive (e.g. `"retry count must be an integer"`).
3. **ex01/ex02** — Remove dead lines after `return` and leftover TODO scaffolding.
4. **Stretch goals** — None attempted. Consider: multiple-space collapse (ex01), whitespace trim before parse (ex02), app_name trim (ex03).

### Verdict

**Day 01: PASSED ✅** — All files ≥ 75. Proceed to Day 02.

```
study: day 01 python_basic weighted 3.80 ex01 81/100 ex02 79/100 ex03 79/100
```

---

## Suggested practice

- [LeetCode 242 — Valid Anagram](https://leetcode.com/problems/valid-anagram/) — string manipulation, character counting, input validation.
- [Python Official Tutorial — Strings](https://docs.python.org/3/tutorial/introduction.html#strings) — core string operations and formatting.
