# Day 07 — Sets and frozenset: Exercises

## Learning objectives

After completing these exercises you will be able to:
1. Create sets from literals, constructors, and iterables, and apply basic mutation methods (add, remove, discard, update).
2. Use set algebra (union, intersection, difference, symmetric difference) and containment checks (subset, superset, disjoint) to solve real problems.
3. Build set comprehensions, use `frozenset` as dict keys, enforce hashability rules, and implement industrial patterns (dedup, allowlist, RBAC).

## Skills assessed

| Skill ID | Skill | Exercise | Proficiency target |
|----------|-------|----------|-------------------|
| PY-06 | Data structures (set, frozenset) | ex01, ex02, ex03 | proficient |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | developing |
| PY-09 | Comprehensions & generators | ex02, ex03 | developing |
| PY-02 | String operations & formatting | ex03 | developing |

## Concept coverage map

| Checklist # | Concept | Covered in |
|-------------|---------|------------|
| 1 | Literal creation | ex01 — `create_set_from_values` |
| 2 | `set()` constructor | ex01 — `unique_from_list` |
| 3 | `add()` | ex01 — `build_seen_tracker` |
| 4 | `remove()` vs `discard()` | ex01 — `safe_remove` |
| 5 | `pop()` / `clear()` | ex01 — `drain_set` |
| 6 | `update()` / `\|=` | ex02 — `merge_tag_sets` |
| 7 | Union `\|` | ex02 — `combine_teams` |
| 8 | Intersection `&` | ex02 — `find_common_members` |
| 9 | Difference `-` | ex02 — `find_exclusive` |
| 10 | Symmetric difference `^` | ex02 — `find_all_differences` |
| 11 | Subset `<=` / superset `>=` | ex02 — `check_containment` |
| 12 | `isdisjoint()` | ex02 — `check_containment` |
| 13 | `in` membership | ex01 — `build_seen_tracker` |
| 14 | Iteration | ex01 — `drain_set` |
| 15 | Set comprehension | ex03 — `normalize_tags` |
| 16 | `frozenset` | ex03 — `group_by_letter_set` |
| 17 | `frozenset` as dict key | ex03 — `group_by_letter_set` |
| 18 | Hashability requirement | ex03 — `make_hashable` |
| 19 | Built-in aggregation | ex01 — `set_stats` |
| 20 | Anti-pattern: unhashable in set | ex03 — `make_hashable` |
| 21 | Industrial: dedupe, allowlist | ex03 — `dedupe_preserve_order` |
| 22 | Industrial: permission comparison | ex03 — `permission_report` |

---

## ex01_basic.py — Creation, Mutation, and Basics (Checklist #1–#5, #13–#14, #19)

**Must-pass behaviors:**
- `create_set_from_values` returns a set from variable positional args.
- `unique_from_list` deduplicates a list into a sorted list using `set()`.
- `build_seen_tracker` tracks which elements have been seen, returns duplicates.
- `safe_remove` removes an element using `discard`; raises `KeyError` when `strict=True` and element is missing.
- `drain_set` pops all elements from a copy, returns them as a sorted list.
- `set_stats` returns count, min, max, sum for a numeric set.

**Stretch behaviors:**
- `set_stats` raises `ValueError` on empty set.
- `safe_remove` supports both strict and lenient modes.

### Functions to implement:
1. `create_set_from_values(*values: object) -> set[object]` — build a set from positional args
2. `unique_from_list(items: list[object]) -> list[object]` — deduplicate and return sorted unique values
3. `build_seen_tracker(items: list[int]) -> set[int]` — return the set of duplicate values
4. `safe_remove(s: set[object], elem: object, *, strict: bool = False) -> set[object]` — remove element with optional strictness
5. `drain_set(s: set[int]) -> list[int]` — pop all elements from a copy, return sorted
6. `set_stats(s: set[int | float]) -> dict[str, int | float]` — return count/min/max/sum

---

## ex02_intermediate.py — Set Algebra and Containment (Checklist #6–#12)

**Must-pass behaviors:**
- `combine_teams` returns the union of two sets (all members).
- `find_common_members` returns the intersection (shared members).
- `find_exclusive` returns elements in the first set but not the second.
- `find_all_differences` returns the symmetric difference.
- `check_containment` returns a dict with `is_subset`, `is_superset`, `is_disjoint` booleans.
- `merge_tag_sets` merges multiple tag sets into one using `update`.

**Stretch behaviors:**
- `merge_tag_sets` accepts an arbitrary number of sets via `*args`.

### Functions to implement:
1. `combine_teams(team_a: set[str], team_b: set[str]) -> set[str]` — union
2. `find_common_members(group_a: set[str], group_b: set[str]) -> set[str]` — intersection
3. `find_exclusive(primary: set[str], secondary: set[str]) -> set[str]` — difference
4. `find_all_differences(set_a: set[str], set_b: set[str]) -> set[str]` — symmetric difference
5. `check_containment(subset_candidate: set[str], superset_candidate: set[str]) -> dict[str, bool]` — subset/superset/disjoint
6. `merge_tag_sets(*tag_sets: set[str]) -> set[str]` — merge N sets via update

---

## ex03_advanced.py — Comprehensions, frozenset, and Industrial Patterns (Checklist #15–#22)

**Must-pass behaviors:**
- `normalize_tags` uses a set comprehension to lowercase and strip tags.
- `make_hashable` converts a list to a tuple so it can be added to a set; raises `TypeError` if input is not a list.
- `group_by_letter_set` groups words by their `frozenset` of characters (like anagram grouping by letter set).
- `dedupe_preserve_order` deduplicates a list while preserving first-occurrence order.
- `permission_report` compares required vs granted permissions, returning missing, extra, and authorized status.

**Stretch behaviors:**
- `permission_report` includes `shared` and `all_perms` keys.
- `group_by_letter_set` sorts each group alphabetically and sorts the outer list.

### Functions to implement:
1. `normalize_tags(tags: list[str]) -> set[str]` — set comprehension with lower+strip
2. `make_hashable(items: list[object]) -> tuple[object, ...]` — convert list to hashable tuple
3. `group_by_letter_set(words: list[str]) -> list[list[str]]` — group by frozenset of chars
4. `dedupe_preserve_order(items: list[str]) -> list[str]` — seen-set dedup pattern
5. `permission_report(required: set[str], granted: set[str]) -> dict[str, object]` — RBAC comparison

---

## Failure modes to watch for
- Using `{}` to create an empty set (creates a dict).
- Using `remove()` when `discard()` is intended — causes unexpected `KeyError`.
- Forgetting that sets are unordered — sort before comparing with expected lists.
- Putting unhashable objects (lists, dicts) into sets.
- Mutating input sets instead of working on copies.

## Scoring

| Criterion | Max | ex01 | ex02 | ex03 |
|-----------|-----|------|------|------|
| Must-pass behaviors | 40 | | | |
| Stretch behaviors | 15 | | | |
| Inline asserts + AI-verified | 25 | | | |
| Style (types, ruff, docstrings) | 20 | | | |
| **Total** | **100** | | | |

## Suggested practice
- [Real Python — Sets in Python](https://realpython.com/python-sets/) — comprehensive set tutorial
- [Python docs — set types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) — official API

## Self-check commands
```bash
ruff check exercise/python_basic/day_07_sets/
python exercise/python_basic/day_07_sets/ex01_basic.py
python exercise/python_basic/day_07_sets/ex02_intermediate.py
python exercise/python_basic/day_07_sets/ex03_advanced.py
```

---

## Evaluation report — 2026-04-23

### Gate checklist

| Gate | Result | Evidence |
|------|--------|----------|
| G1 — Type hints | ✅ PASS | All 17 functions have full typed signatures (params + return) |
| G2 — Explicit errors | ✅ PASS | All functions validate inputs with `isinstance` and raise `TypeError`/`ValueError`/`KeyError` with descriptive messages |
| G3 — Inline asserts | ✅ PASS | All 3 files have `__main__` assert blocks covering normal, edge, and error cases (3–5 asserts per function) |
| G4 — Ruff clean | ✅ PASS | `ruff check` → "All checks passed!" |
| G5 — Docstrings | ✅ PASS | Google-style docstrings with Args/Returns/Raises/Examples on all functions |
| G6 — Security | ✅ PASS | No secrets, inputs validated, no mutation of originals |
| G7 — Observability | ✅ PASS | Clean output, no debug prints |
| G8 — Concept completeness | N/A | Applies to generated artifacts, not student solutions |

### Dimension scores

| Dimension | Score (1–5) | Notes |
|-----------|-------------|-------|
| D1 Correctness | 5 | All asserts pass, all edge cases handled, correct operators used throughout |
| D2 Reliability | 5 | Every function validates inputs; `safe_remove` strict/lenient modes work correctly; no mutation of originals |
| D3 Maintainability | 5 | Clean naming, small focused functions, no dead code, no debug prints |
| D4 API & typing | 5 | Full type hints, proper use of `set[str]`, `set[int | float]`, keyword-only `strict` |
| D5 Performance | 5 | Correct use of set operations (O(1) membership, O(n) algebra); `dedupe_preserve_order` uses seen-set |
| D6 Security | 5 | All inputs validated before use, copies made to prevent mutation |
| D7 Code quality | 4 | Ruff clean, consistent style; minor: leftover TODO comments in ex01 and commented-out code at top of `create_set_from_values` |
| **Weighted total** | **4.90** | 5×0.30 + 5×0.15 + 5×0.15 + 5×0.10 + 5×0.10 + 5×0.10 + 4×0.10 = 4.90 |

### Per-file scores

| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | 40 | 40 | 40 |
| Stretch behaviors (15) | 15 | 15 | 15 |
| Inline asserts + AI-verified (25) | 24 | 25 | 25 |
| Style (types, ruff, docstrings) (20) | 17 | 20 | 20 |
| **Total** | **96** | **100** | **100** |

### Skills assessed

| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| PY-06 | Data structures (set, frozenset) | ex01, ex02, ex03 | strong |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | proficient |
| PY-09 | Comprehensions & generators | ex02, ex03 | proficient |
| PY-02 | String operations & formatting | ex03 | proficient |

### Action items

1. **Remove leftover commented-out code** in [ex01_basic.py](ex01_basic.py#L34-L37) — the old `create_set_from_values` attempt is still there as dead comments.
2. **Minor typo in error message** at [ex01_basic.py](ex01_basic.py#L97) — `"No a list"` should be `"Not a list"`.
3. No functional issues — all solutions are clean and correct.

### Verdict

**🌟 STRONG PASS** — all files ≥ 90, weighted avg 4.90 ≥ 4.5.

Commit message: `study: day 07 python_basic weighted 4.9 ex01 96/100 ex02 100/100 ex03 100/100`
