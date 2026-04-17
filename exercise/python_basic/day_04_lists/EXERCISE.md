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
