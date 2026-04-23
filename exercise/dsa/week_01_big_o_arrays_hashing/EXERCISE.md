# Week 01 Exercises — Big-O, Arrays, Hashing Basics

## Learning objectives

- Choose between array-scan and hash-based approaches with explicit complexity tradeoffs.
- Implement stable dictionary/set patterns for lookup, counting, and grouping.
- Write clear function signatures that return data structures suitable for tests.

## Exercise specs

Implementation note:
- Include expected output examples in docstrings and near `__main__` asserts.
- Keep solutions deterministic where output ordering matters.

### ex01_basic.py — Contains duplicate

**Must pass:**
- Implement `contains_duplicate(nums: list[int]) -> bool`.
- Return `True` when any element repeats, else `False`.
- Target complexity: O(n) time using a set.

**Stretch:**
- Short-circuit immediately when a duplicate is found.

**Failure modes:**
- O(n^2) nested-loop solution for the main path.
- Printing instead of returning.

**Traversal snapshot (graphical):**
```text
nums = [1, 2, 3, 1]
seen={}
1 -> add
2 -> add
3 -> add
1 -> hit duplicate -> True
```

### ex02_intermediate.py — Two-sum indices

**Must pass:**
- Implement `two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None`.
- Return a valid index pair `(i, j)` with `i < j` where `nums[i] + nums[j] == target`.
- Return `None` when no pair exists.
- Target complexity: O(n) average time with a hash map.

**Stretch:**
- Keep first valid pair discovered in left-to-right scan.

**Failure modes:**
- Returning values instead of indices.
- Reusing the same element twice.

**Traversal snapshot (graphical):**
```text
nums=[2,7,11,15], target=9
map={}
i=0, val=2, need=7 -> store {2:0}
i=1, val=7, need=2 -> hit -> (0,1)
```

### ex03_advanced.py — Group anagrams (deterministic)

**Must pass:**
- Implement `group_anagrams(words: list[str]) -> list[list[str]]`.
- Group words that are anagrams.
- Return deterministic output: sort each group alphabetically, then sort groups by `(len(group), group[0])`.
- Target complexity: O(n * m) where `m` is average word length.

**Stretch:**
- Use a fixed-size frequency signature instead of sorted-string key.

**Failure modes:**
- Non-deterministic output order causing flaky assertions.
- Mutating input list.

**Traversal snapshot (graphical):**
```text
eat -> signature S1 -> group[S1]=[eat]
tea -> signature S1 -> group[S1]=[eat,tea]
tan -> signature S2 -> group[S2]=[tan]
...
sort each group, then sort outer list
```

## Skills assessed

| Skill ID | Skill | Exercise |
|----------|-------|----------|
| DSA-01 | Big-O reasoning and tradeoffs | ex01, ex02, ex03 |
| DSA-02 | Arrays and hash lookup patterns | ex01, ex02 |
| DSA-03 | Grouping and frequency-based keys | ex03 |
| PY-16 | Type hints and API clarity | ex01, ex02, ex03 |

## Scoring (per file, 0-100)

| Criterion | Points |
|-----------|--------|
| Must-pass behaviors | 40 |
| Stretch quality | 15 |
| Inline assert coverage | 25 |
| Style (types, docstrings, clarity) | 20 |
| Total | 100 |

Pass target: >= 75 per file.

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

## Self-check

```bash
python3 exercise/dsa/week_01_big_o_arrays_hashing/ex01_basic.py
python3 exercise/dsa/week_01_big_o_arrays_hashing/ex02_intermediate.py
python3 exercise/dsa/week_01_big_o_arrays_hashing/ex03_advanced.py
```

## Suggested practice

- [Two Sum (LeetCode)](https://leetcode.com/problems/two-sum/) — hash-map complement pattern.
- [Contains Duplicate (LeetCode)](https://leetcode.com/problems/contains-duplicate/) — set-based membership checks.
- [Group Anagrams (LeetCode)](https://leetcode.com/problems/group-anagrams/) — canonical grouping design.

---

## Evaluation report — 2026-04-23

### Gate checklist

| Gate | Result | Evidence |
|------|--------|----------|
| G1 — Type hints | ✅ PASS | All function signatures fully typed (params + return) |
| G2 — Explicit errors | ⚠️ PARTIAL | No input validation on any function (e.g. no `TypeError` if `nums` is not a list) — spec doesn't require it, but RUBRIC G2 expects descriptive error handling |
| G3 — Inline asserts | ⚠️ PARTIAL | Assert blocks present but minimal — only 2 asserts per file; no edge cases (empty list for ex01/ex02, single element, all duplicates, negative numbers) |
| G4 — Ruff clean | ✅ PASS | `ruff check` → "All checks passed!" |
| G5 — Docstrings | ⚠️ PARTIAL | Module-level docstrings good; function docstrings lack Args/Returns/Raises sections (only have summary + complexity note) |
| G6 — Security | ✅ PASS | No secrets, no injection vectors |
| G7 — Observability | ✅ PASS | Clean output, no debug prints |
| G8 — Concept completeness | N/A | Applies to generated artifacts, not student solutions |

### Dimension scores

| Dimension | Score (1–5) | Notes |
|-----------|-------------|-------|
| D1 Correctness | 5 | All solutions correct, optimal complexity, all asserts pass |
| D2 Reliability | 3 | No input validation; no handling for edge cases like non-list input |
| D3 Maintainability | 4 | Clean code, good naming; `anagram_signature` is well-extracted as a helper |
| D4 API & typing | 4 | Full type hints; return type on `two_sum_indices` uses modern `X | None` union — good |
| D5 Performance | 5 | All solutions hit target complexity: O(n) set, O(n) hash map, O(n·m) frequency sig |
| D6 Security | 4 | Safe defaults, no mutation of inputs |
| D7 Code quality | 3 | Docstrings incomplete (missing Args/Returns); TODO comments left in ex02/ex03; extra space before `:` in ex02 L33 `seek : dict` |
| **Weighted total** | **4.10** | 5×0.30 + 3×0.15 + 4×0.15 + 4×0.10 + 5×0.10 + 4×0.10 + 3×0.10 = 4.10 |

### Per-file scores

| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | 38 | 38 | 40 |
| Stretch behaviors (15) | 15 | 12 | 15 |
| Inline asserts + AI-verified (25) | 18 | 18 | 18 |
| Style (types, ruff, docstrings) (20) | 15 | 14 | 17 |
| **Total** | **86** | **82** | **90** |

### Skills assessed

| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| DSA-01 | Big-O reasoning and tradeoffs | ex01, ex02, ex03 | proficient |
| DSA-02 | Arrays and hash lookup patterns | ex01, ex02 | proficient |
| DSA-03 | Grouping and frequency-based keys | ex03 | strong |
| PY-16 | Type hints and API clarity | ex01, ex02, ex03 | developing |

### Action items

1. **Add edge-case asserts to all files**: empty list, single element, all-same values, negative numbers. Currently only 2 asserts per file — aim for 4–5 covering boundaries.
2. **Expand docstrings to full Google style** (Args/Returns/Raises) on all functions — currently only a summary line + complexity comment.
3. **Remove leftover TODO comments** in ex02 and ex03 — dead comments reduce readability.

### Rewritten snippet — weakest area (ex02 docstring + validation)

```python
def two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of two numbers that sum to target.

    Args:
        nums: List of integers to search.
        target: Target sum value.

    Returns:
        Tuple (i, j) with i < j where nums[i] + nums[j] == target,
        or None if no valid pair exists.

    Raises:
        TypeError: If nums is not a list.

    Examples:
        >>> two_sum_indices([2, 7, 11, 15], 9)
        (0, 1)
    """
    if not isinstance(nums, list):
        raise TypeError(f"expected list, got {type(nums).__name__}")
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None
```

### Verdict

**✅ PASS** — all files ≥ 75, weighted avg 4.10 ≥ 3.5.

Commit message: `study: week 01 dsa weighted 4.1 ex01 86/100 ex02 82/100 ex03 90/100`
