# Day 08 — Strings and Encoding: Exercises

## Learning objectives

After completing these exercises you will be able to:
1. Create, index, slice, and inspect strings using built-in methods (concepts 1–9).
2. Transform, split, join, replace, and format strings for data processing (concepts 10–16).
3. Analyse character frequency, encode/decode text, normalize Unicode, and build industrial text utilities (concepts 17–25).

## Skills assessed

| Skill ID | Skill | Exercise | Proficiency target |
|----------|-------|----------|-------------------|
| PY-02 | String operations & formatting | ex01, ex02, ex03 | proficient |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | developing |
| PY-06 | Data structures (list, dict, set, tuple) | ex02, ex03 | developing |

## Concept coverage map

| Checklist # | Concept | Covered in |
|-------------|---------|------------|
| 1 | String creation | ex01 — `create_greeting` |
| 2 | Raw strings | ex01 — `raw_path_parts` |
| 3 | Indexing / negative | ex01 — `first_last` |
| 4 | Slicing | ex01 — `slice_extract` |
| 5 | Immutability | ex01 — `safe_replace_char` |
| 6 | `len()` | ex01 — `first_last` |
| 7 | Case methods | ex02 — `normalize_compare` |
| 8 | Search methods | ex02 — `find_all_positions` |
| 9 | Boolean checks | ex01 — `classify_token` |
| 10 | Strip | ex02 — `clean_fields` |
| 11 | Split / join | ex02 — `clean_fields` |
| 12 | Replace | ex02 — `censor_word` |
| 13 | f-strings advanced | ex02 — `format_invoice_line` |
| 14 | Legacy formatting | ex02 — `format_invoice_line` |
| 15 | Concatenation / repetition | ex01 — `create_greeting` |
| 16 | `in` substring check | ex02 — `censor_word` |
| 17 | Character frequency | ex03 — `char_frequency` |
| 18 | `bytes` vs `str` | ex03 — `safe_decode` |
| 19 | `bytearray` | ex03 — `mask_bytes` |
| 20 | Unicode normalization | ex03 — `normalize_and_compare` |
| 21 | Regex preview | ex03 — `extract_emails` |
| 22 | Multi-line / textwrap | ex02 — `build_template` |
| 23 | `translate()` / `maketrans()` | ex03 — `strip_punctuation` |
| 24 | Anti-pattern: str + bytes | ex03 — `safe_decode` |
| 25 | Industrial: slugify, sanitizer | ex03 — `slugify` |

---

## ex01_basic.py — String Foundations (Checklist items #1–#6, #9, #15)

**Must-pass behaviors:**
- Create strings with different quote styles including raw strings.
- Index, slice, and measure strings correctly (including negatives).
- Handle immutability by returning new strings instead of mutating.
- Classify tokens using boolean string methods.

**Stretch behaviors:**
- Handle empty-string and single-character edge cases without crashing.

### Functions to implement:
1. `create_greeting(name, times)` — Build a greeting using concatenation and repetition.
2. `first_last(s)` — Return a tuple of (first_char, last_char, length).
3. `slice_extract(s, start, stop)` — Return the substring `s[start:stop]` with validation.
4. `safe_replace_char(s, index, new_char)` — Return a new string with one character replaced (immutability-safe).
5. `raw_path_parts(raw_path)` — Given a raw Windows path string, split on `\\` and return the parts list.
6. `classify_token(token)` — Return `"digit"`, `"alpha"`, `"alnum"`, or `"other"` using boolean check methods.

---

## ex02_intermediate.py — Transform and Format (Checklist items #7–#8, #10–#14, #16, #22)

**Must-pass behaviors:**
- Normalize case for comparison using `casefold()`.
- Find all positions of a substring in a string.
- Strip, split, and join CSV-like fields cleanly.
- Censor a target word using `in` and `replace`.
- Format data using both f-strings and `.format()`.

**Stretch behaviors:**
- Build a multi-line template using `textwrap.dedent`.

### Functions to implement:
1. `normalize_compare(a, b)` — Return `True` if two strings are equal under `casefold()`.
2. `find_all_positions(text, sub)` — Return a list of all start indices where `sub` appears.
3. `clean_fields(csv_line, sep)` — Split on `sep`, strip each field, drop empty fields, return list.
4. `censor_word(text, word)` — Replace every occurrence of `word` with `"***"` (case-insensitive).
5. `format_invoice_line(item, qty, price)` — Return `"item          x3   $  9.99"` using f-string alignment.
6. `build_template(name, items)` — Return a dedented multi-line receipt string.

---

## ex03_advanced.py — Encoding, Analysis, and Industrial Patterns (Checklist items #17–#25)

**Must-pass behaviors:**
- Count character frequency using `collections.Counter`.
- Encode and decode text safely across encoding boundaries.
- Normalize Unicode before comparison.
- Use `translate/maketrans` to strip punctuation.
- Build an industrial-quality slugify function.

**Stretch behaviors:**
- Extract email addresses using a basic regex pattern.
- Mutate bytes in-place with `bytearray`.

### Functions to implement:
1. `char_frequency(text)` — Return a dict of character → count (ignore spaces).
2. `safe_decode(data, encoding)` — Decode `bytes` to `str`, return `""` on failure instead of raising.
3. `mask_bytes(data, mask_byte)` — Use `bytearray` to XOR each byte with `mask_byte`, return new `bytes`.
4. `normalize_and_compare(a, b)` — NFC-normalize both strings, return whether they are equal.
5. `strip_punctuation(text)` — Remove all ASCII punctuation using `str.maketrans` + `translate`.
6. `extract_emails(text)` — Use `re.findall` to extract all email addresses from text.
7. `slugify(title, max_length)` — NFKD-normalize, ASCII-fold, lowercase, hyphenate, truncate.

---

## Failure modes to watch for
- Forgetting the trailing comma in single-element tuples returned by helper functions.
- Using `==` instead of `casefold()` for case-insensitive comparison.
- Mixing `str` and `bytes` — always decode/encode at boundaries.
- `.find()` returning `-1` and treating it as a valid index.
- `re.findall` returning an empty list instead of `None` — no need for None checks.
- `bytearray` XOR requires `int` operands — iterate over bytes.

## Scoring

| Criterion | Max | ex01 | ex02 | ex03 |
|-----------|-----|------|------|------|
| Must-pass behaviors | 40 | | | |
| Stretch behaviors | 15 | | | |
| Inline asserts + AI-verified | 25 | | | |
| Style (types, ruff, docstrings) | 20 | | | |
| **Total** | **100** | | | |

## Suggested practice
- [zhiwehu — Python programming exercises](https://github.com/zhiwehu/Python-programming-exercises) — string manipulation drills
- [Exercism — Python track](https://exercism.org/tracks/python) — mentored string exercises

## Self-check commands
```bash
ruff check exercise/python_basic/day_08_strings/
python exercise/python_basic/day_08_strings/ex01_basic.py
python exercise/python_basic/day_08_strings/ex02_intermediate.py
python exercise/python_basic/day_08_strings/ex03_advanced.py
```

---

## Evaluation report — 2026-04-28

### Gate checklist

| Gate | Result | Evidence |
|------|--------|----------|
| G1 | **PASS** | All public functions have typed signatures (params + return) across all 3 files |
| G2 | **FAIL** | No `ValueError` raised in any function despite docstrings requiring them (ex01: all 6, ex02: `normalize_compare`, `find_all_positions`, `clean_fields`, `build_template`; ex03: `char_frequency`, `mask_bytes`, `strip_punctuation`) |
| G3 | **PASS** | All 3 files have `assert` blocks in `__main__` and run green |
| G4 | **PASS** | `ruff check` — all checks passed |
| G5 | **PASS** | Google-style docstrings on all public functions |
| G6 | **PASS** | No secrets, inputs validated at boundary (partial — see G2) |
| G7 | **FAIL** | Debug `print()` statements left in production code: `find_all_positions`, `clean_fields`, `extract_emails` |
| G8 | **PASS** | All 25 checklist concepts mapped in Concept Coverage Map and exercised |

### Dimension scores

| Dimension | Score (1–5) | Notes |
|-----------|-------------|-------|
| D1 Correctness | 3 | `safe_replace_char` uses `.replace()` which replaces ALL occurrences of that char, not just at index — incorrect logic. `normalize_and_compare` only normalizes `b`, not `a`. `find_all_positions` uses `set` — loses ordering guarantee on older Pythons. |
| D2 Reliability | 2 | Zero `ValueError` guards despite every docstring specifying them. Empty-string inputs silently crash with `IndexError`. |
| D3 Maintainability | 3 | Clean naming and structure. Debug `print()` left in 3 functions hurts. `build_template` doesn't use `textwrap.dedent` as specified. |
| D4 API & typing | 4 | Signatures correct and consistent. `from __future__ import annotations` present. |
| D5 Performance | 4 | Reasonable structures. `find_all_positions` loops entire string range calling `.find()` each time — O(n²) instead of O(n·m). |
| D6 Security | 4 | No injection risks. Slugify validates empty. |
| D7 Code quality | 3 | Ruff-clean but debug prints, dead `...` statements before code, imports inside functions instead of top-level. |
| **Weighted total** | **3.05** | `0.30×3 + 0.15×2 + 0.15×3 + 0.10×4 + 0.10×4 + 0.10×4 + 0.10×3 = 3.05` |

### Per-file scores

| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | 30 | 35 | 35 |
| Stretch behaviors (15) | 5 | 12 | 12 |
| Inline asserts + AI-verified (25) | 20 | 22 | 23 |
| Style (types, ruff, docstrings) (20) | 18 | 15 | 14 |
| **Total** | **73** | **84** | **84** |

### Skills assessed

| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| PY-02 | String operations & formatting | ex01, ex02, ex03 | developing |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | learning |
| PY-06 | Data structures (list, dict, set, tuple) | ex02, ex03 | developing |

### Action items

1. **[Critical] Add input validation to all functions.** Every docstring promises `Raises: ValueError` but none actually raise. Example: [ex01_basic.py](exercise/python_basic/day_08_strings/ex01_basic.py#L63) `first_last("")` will `IndexError` instead of `ValueError`. Add guards like `if not s: raise ValueError("s must be non-empty")` to every function.

2. **[Critical] Fix `safe_replace_char` logic** at [ex01_basic.py](exercise/python_basic/day_08_strings/ex01_basic.py#L116): `s.replace(s[index], new_char)` replaces ALL occurrences of that character. Use slicing: `s[:idx] + new_char + s[idx+1:]` (normalize negative index first with `idx = index % len(s)`).

3. **[Important] Remove debug `print()` statements** from [ex02_intermediate.py](exercise/python_basic/day_08_strings/ex02_intermediate.py#L73) (`find_all_positions`), [line 91](exercise/python_basic/day_08_strings/ex02_intermediate.py#L91) (`clean_fields`), and [ex03_advanced.py](exercise/python_basic/day_08_strings/ex03_advanced.py#L175) (`extract_emails`).

### Rewritten snippet — `safe_replace_char` (worst issue)

```python
def safe_replace_char(s: str, index: int, new_char: str) -> str:
    if not s:
        raise ValueError("s must be non-empty")
    if len(new_char) != 1:
        raise ValueError(f"new_char must be length 1, got {len(new_char)}")
    if not (-len(s) <= index < len(s)):
        raise ValueError(f"index {index} out of range for string of length {len(s)}")
    idx = index % len(s)  # normalize negative index
    return s[:idx] + new_char + s[idx + 1:]
```

### Verdict

**REWORK** — ex01 scores 73/100 (below 75 threshold). Weighted total 3.05 (below 3.5). G2 fails across all files.

**Priority fixes:** (1) add `ValueError` guards to all functions, (2) fix `safe_replace_char` slicing logic, (3) remove debug prints.

Commit message after fix: `study: day 08 python_basic weighted [X.X] ex01 [YY]/100 ex02 [YY]/100 ex03 [YY]/100`
