# Day 04 Exercises - Lists and Sorting

## Learning objectives

- Read and slice list data without mutating the original sequence unless required.
- Apply safe in-place style updates with index and value validation.
- Build deterministic leaderboard sorting with explicit tie-breakers.
- Use sort-plus-slice top-k patterns for concise result extraction.

## Skills assessed

| Skill ID | Skill | Exercise mapping |
|----------|-------|------------------|
| PY-03 | Input validation & error handling | ex01, ex02, ex03 |
| PY-05 | Functions, args, kwargs, lambda | ex02, ex03 |
| PY-06 | Data structures (list, dict, set, tuple) | ex01, ex02, ex03 |
| PY-16 | Type hints & API clarity | ex01, ex02, ex03 |

## Exercise specs

### ex01_basic.py - Slice a result window

Must-pass:
- Implement `slice_result_window(items: list[str], *, start: int, size: int) -> list[str]`.
- Validate `start >= 0` and `size >= 1`.
- Return a new list using slicing semantics.
- Raise `ValueError` with the invalid value when constraints fail.

Stretch:
- Return an empty list cleanly when `start` is beyond the end of `items`.

Failure modes:
- Do not mutate `items`.
- Do not silently clamp invalid inputs.

### ex02_intermediate.py - Leaderboard sort with tie-breakers

Must-pass:
- Implement `sort_leaderboard(entries: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]`.
- Tuple format is `(name, score, penalty_minutes)`.
- Sort by score descending, then penalty ascending, then name (case-insensitive) ascending.
- Validate non-empty names, score in `0..100`, and non-negative penalty.

Stretch:
- Use stable multi-pass sorting to make tie-breakers explicit and readable.

Failure modes:
- Do not mutate the incoming list.
- Do not skip validation for malformed entries.

### ex03_advanced.py - Filtered top-k leaderboard view

Must-pass:
- Implement `top_k_by_min_score(entries: list[tuple[str, int, int]], *, min_score: int, k: int) -> list[tuple[str, int, int]]`.
- Keep only entries with `score >= min_score`.
- Sort using the same ranking rules from ex02.
- Return at most top `k` entries.

Stretch:
- Make behavior explicit for `k` larger than available results (return all available rows).

Failure modes:
- Do not perform repeated `max()` scans for top-k.
- Do not accept `k < 1` or invalid `min_score` without raising `ValueError`.

## Scoring (per file, 0-100)

- Must-pass behaviors: 40
- Stretch behaviors: 15
- Asserts and AI-verified behavior: 25
- Style (types, ruff, docstrings): 20
- Total: 100

Pass rule: >= 75 per file, with gates G1-G7 satisfied.

## Suggested practice

- [Real Python - Python Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Python docs - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

## Evaluation report - 2026-04-19

### Gate checklist
| Gate | Result | Evidence |
|------|--------|----------|
| G1 | Pass | Public APIs are fully typed in ex01/ex02/ex03 signatures and returns. |
| G2 | Pass | Explicit `ValueError` checks with invalid values in all three exercises; no bare `except:`. |
| G3 | Pass | Inline `assert` self-checks present in each `__main__`, and behavior was executed and verified. |
| G4 | Pass | `ruff check exercise/python_basic/day_04_lists/` returned `All checks passed!`. |
| G5 | Pass | Public functions include structured Google-style docstrings (`Args`, `Returns`, `Raises`). |
| G6 | Pass | No secrets or unsafe operations; input validation enforces value constraints. |
| G7 | Pass | Error messages are descriptive and include offending values (for validated constraints). |

### Dimension scores
| Dimension | Score | Notes |
|-----------|-------|-------|
| D1 Correctness | 4.6 | Core behavior matches spec and edge cases pass; malformed-entry shape checks are implicit, not explicit. |
| D2 Reliability | 4.0 | Validations are strong for numeric/name constraints; tuple-shape/type checks can be made explicit. |
| D3 Maintainability | 4.2 | Readable structure and tie-breaker clarity; validation logic duplicated across ex02/ex03. |
| D4 API & typing | 4.0 | Good type hints/docstrings; tuple schema validation can align runtime behavior with type intent. |
| D5 Performance | 5.0 | Uses linear passes + stable sorting; avoids repeated top-k scans. |
| D6 Security | 4.5 | Safe local logic with constrained inputs and no sensitive handling risks. |
| D7 Code quality | 4.8 | Ruff-clean, consistent naming, clean control flow, descriptive messages. |
| **Weighted total** | **4.44 / 5.00** | Pass threshold met (>= 3.5, no dimension below 2). |

### Per-file scores
| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | 40 | 37 | 38 |
| Stretch behaviors (15) | 15 | 15 | 14 |
| Inline asserts + AI-verified behavior (25) | 23 | 22 | 22 |
| Style (types, ruff, docstrings) (20) | 20 | 19 | 19 |
| **Total** | **98** | **93** | **93** |

### Skills assessed
| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | Proficient |
| PY-05 | Functions, args, kwargs, lambda | ex02, ex03 | Proficient |
| PY-06 | Data structures (list, dict, set, tuple) | ex01, ex02, ex03 | Strong |
| PY-16 | Type hints & API clarity | ex01, ex02, ex03 | Proficient |

### Action items
1. Add explicit malformed-entry validation before tuple unpacking in ex02/ex03 for clearer runtime errors.
2. Expand asserts for boundary failures (`size=0`, `min_score=-1/101`) and for `k > available` explicit behavior.
3. Consider extracting shared entry-validation logic to reduce duplication between ex02 and ex03.

### Verdict
PASS - commit message: `study: day 04 python_basic weighted 4.4 ex01 98/100 ex02 93/100 ex03 93/100`
