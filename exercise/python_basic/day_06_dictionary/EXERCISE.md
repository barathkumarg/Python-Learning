# Day 06 Exercises — Dictionaries

## Learning objectives

- Create, read, update, and delete dictionary entries using built-in methods.
- Use `get()`, `setdefault()`, and dict comprehensions to write safe, concise code.
- Merge dictionaries with `|`, `update()`, and `**` unpacking without mutating originals.
- Traverse nested dicts safely and build industrial patterns like inverted indexes and config merges.

---

## Exercise specs

### ex01_basic.py — Word frequency counter

**Must pass:**
- Implement `word_frequency(text: str) -> dict[str, int]`.
- Split on whitespace, count case-insensitively (lowercase all words).
- Raise `TypeError` if `text` is not a string.
- Return a dict mapping each word to its count.

**Stretch:**
- Implement `top_n_words(freq: dict[str, int], n: int = 3) -> list[tuple[str, int]]`.
- Return the `n` most frequent words as `(word, count)` tuples sorted by count descending, then alphabetically.

**Failure modes:**
- Must NOT mutate any input.
- Must NOT use `Counter` (practice manual counting with `get()`).

**Example:**
- Input: `"the cat sat on the mat the cat"` → Output: `{"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}`

---

### ex02_intermediate.py — Config merger

**Must pass:**
- Implement `merge_configs(defaults: dict[str, object], overrides: dict[str, object]) -> dict[str, object]`.
- Return a new dict where `overrides` values take precedence.
- The original `defaults` and `overrides` must NOT be mutated.
- Raise `TypeError` if either argument is not a `dict`.

**Stretch:**
- Implement `deep_merge(base: dict, patch: dict) -> dict`.
- Recursively merge nested dicts; non-dict values in `patch` replace `base` values.

**Failure modes:**
- Must NOT mutate input dicts.
- Must NOT lose keys that exist only in `defaults`.

**Example:**
- Input: `{"color": "green", "width": 80}`, `{"color": "red", "height": 24}` → Output: `{"color": "red", "width": 80, "height": 24}`

---

### ex03_advanced.py — Inverted index builder

**Must pass:**
- Implement `build_inverted_index(documents: dict[str, str]) -> dict[str, list[str]]`.
- Map each lowercased word to a sorted list of doc IDs that contain it.
- Each doc ID appears at most once per word.
- Raise `TypeError` if `documents` is not a `dict`.

**Stretch:**
- Implement `search_index(index: dict[str, list[str]], *terms: str) -> list[str]`.
- Return sorted doc IDs that contain **all** given terms (AND search).
- Raise `ValueError` if no terms are provided.

**Failure modes:**
- Must NOT mutate the input documents dict.
- Must NOT include duplicate doc IDs for the same word.

**Example:**
- Input: `{"d1": "the cat sat", "d2": "the dog sat"}` → `index["the"]` == `["d1", "d2"]`

---

## Skills assessed

| Skill ID | Skill | Exercise |
|----------|-------|----------|
| PY-03 | Input validation & error handling | ex01, ex02, ex03 |
| PY-06 | Data structures (dict) | ex01, ex02, ex03 |
| PY-02 | String operations & formatting | ex01, ex03 |
| PY-09 | Comprehensions & generators | ex02, ex03 |

---

## Scoring (per file, 0–100)

| Criterion | Points |
|-----------|--------|
| All **must-pass** behaviors implemented | 40 |
| **Stretch** behaviors (partial credit ok) | 15 |
| **Inline asserts + AI-verified** behavior coverage | 25 |
| **Style** — types, ruff-clean, docstrings | 20 |
| **Total** | **100** |

---

## Suggested practice

- [Real Python — Dictionaries in Python](https://realpython.com/python-dicts/)
- [Python docs — dict](https://docs.python.org/3/library/stdtypes.html#dict)

---

## Evaluation report — 2026-04-23

### Gate checklist

| Gate | Result | Evidence |
|------|--------|----------|
| G1 — Type hints | ⚠️ PARTIAL | All function signatures are typed, but `frequency: dict[str:int]` in ex01 L43 uses `:` instead of `,` in the generic — this is a slice, not a type hint |
| G2 — Explicit errors | ❌ FAIL | `merge_configs` uses `and` instead of `or` — only raises when **both** are non-dict. `word_frequency` never raises `TypeError` at all (checks falsy, not type). `build_inverted_index` ✓ |
| G3 — Inline asserts | ✅ PASS | All 3 files have `__main__` assert blocks covering normal + edge cases |
| G4 — Ruff clean | ✅ PASS | `ruff check` → "All checks passed!" |
| G5 — Docstrings | ✅ PASS | Google-style docstrings on all public functions |
| G6 — Security | ✅ PASS | No secrets, inputs validated (with caveats noted in G2) |
| G7 — Observability | ⚠️ PARTIAL | Debug `print()` statements left in every function — should be removed for production style |
| G8 — Concept completeness | N/A | G8 applies to generated artifacts (CODE.md/code.py), not student solutions |

### Dimension scores

| Dimension | Score (1–5) | Notes |
|-----------|-------------|-------|
| D1 Correctness | 4 | All asserts pass; but `word_frequency` doesn't lowercase, `merge_configs` TypeError is broken |
| D2 Reliability | 3 | `word_frequency` silently returns `{}` for non-str input instead of raising `TypeError` |
| D3 Maintainability | 3 | Debug `print()` in every function; commented-out dead code in ex02 & ex03 |
| D4 API & typing | 3 | `dict[str:int]` is a syntax error in strict checking; signatures otherwise fine |
| D5 Performance | 4 | Correct data structures used; `set` intersection in `search_index` is good |
| D6 Security | 4 | No issues beyond missing input validation |
| D7 Code quality | 3 | Leftover `print()`, dead commented code, inconsistent spacing around `:` and `,` |
| **Weighted total** | **3.50** | 4×0.30 + 3×0.15 + 3×0.15 + 3×0.10 + 4×0.10 + 4×0.10 + 3×0.10 = 3.50 |

### Per-file scores

| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | 30 | 35 | 38 |
| Stretch behaviors (15) | 12 | 13 | 13 |
| Inline asserts + AI-verified (25) | 20 | 23 | 23 |
| Style (types, ruff, docstrings) (20) | 12 | 14 | 15 |
| **Total** | **74** | **85** | **89** |

### Skills assessed

| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | developing |
| PY-06 | Data structures (dict) | ex01, ex02, ex03 | proficient |
| PY-02 | String operations & formatting | ex01, ex03 | developing |
| PY-09 | Comprehensions & generators | ex02, ex03 | developing |

### Action items

1. **ex01 `word_frequency` — missing `TypeError` + no lowercasing** ([ex01_basic.py](ex01_basic.py#L42-L43)): The spec says "raise `TypeError` if text is not a string" and "lowercase all words". Currently `if not text` just returns `{}` for non-str, and words aren't lowercased. Fix:
   ```python
   if not isinstance(text, str):
       raise TypeError(f"expected str, got {type(text).__name__}")
   ```
   and use `text.lower().split()` or lowercase each word in the loop.

2. **ex02 `merge_configs` — `and` vs `or` in TypeError guard** ([ex02_intermediate.py](ex02_intermediate.py#L48)): `not isinstance(…) and not isinstance(…)` only triggers when **both** are non-dict. Should be `or`. Also uses `return TypeError(…)` instead of `raise TypeError(…)`.

3. **Remove debug `print()` statements and dead commented code** from all 3 files — these hurt readability and would fail a code-review gate in production.

### Rewritten snippet — worst issue (`word_frequency`)

```python
def word_frequency(text: str) -> dict[str, int]:
    if not isinstance(text, str):
        raise TypeError(f"expected str, got {type(text).__name__}")
    if not text.strip():
        return {}
    frequency: dict[str, int] = {}
    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
```

### Verdict

**REWORK** — ex01 scores 74 (below 75 threshold).

Key fixes needed: (1) add `TypeError` raise in `word_frequency`, (2) lowercase words, (3) fix `and` → `or` + `return` → `raise` in `merge_configs`, (4) remove debug prints.

Commit message (after fixes): `study: day 06 python_basic weighted 3.5 ex01 74/100 ex02 85/100 ex03 89/100`
