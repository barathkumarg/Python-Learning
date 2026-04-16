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
