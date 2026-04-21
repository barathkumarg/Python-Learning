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
