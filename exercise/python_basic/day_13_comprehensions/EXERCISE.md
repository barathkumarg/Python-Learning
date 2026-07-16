# Day 13 — Comprehensions: Exercises

## Learning objectives

After completing these exercises you will be able to:
1. Write list, dict, and set comprehensions with filters, conditional expressions, and a single nesting level (checklist #1–#7).
2. Use generator expressions and generator functions (`yield`, `next`, `StopIteration`) to build lazy pipelines, and reason about list-vs-generator memory and scoping (checklist #8–#15).
3. Apply readability and performance limits, bridge to `itertools`, and ship industrial patterns — filtered projections and index dictionaries — while avoiding over-nested anti-patterns (checklist #16–#21).

## Skills assessed

| Skill ID | Skill | Exercise | Proficiency target |
|----------|-------|----------|--------------------|
| PY-15 | Comprehensions (list/dict/set) | ex01 | proficient |
| PY-09 | Comprehensions & generators | ex02 | proficient |
| PY-14 | Built-ins paired with comprehensions | ex02 | developing |
| PY-03 | Input validation with explicit errors | ex02, ex03 | proficient |
| PY-15 | Generator pipelines & itertools bridge | ex03 | developing |

## Concept coverage map

| Checklist # | Concept | Covered in |
|-------------|---------|------------|
| 1 | List comprehension | ex01 — `square_evens` |
| 2 | With `if` filter | ex01 — `square_evens` |
| 3 | With `if/else` | ex01 — `signs_to_words` |
| 4 | Nested comprehension | ex01 — `flatten_grid` |
| 5 | Dict comprehension | ex01 — `swap_keys_values` |
| 6 | Dict with filter | ex01 — `keep_truthy` |
| 7 | Set comprehension | ex01 — `unique_word_lengths` |
| 8 | Generator expression | ex02 — `lazy_doubles` |
| 9 | Generator in calls | ex02 — `total_lengths` |
| 10 | Memory: list vs generator | ex02 — `memory_delta` |
| 11 | `yield` preview | ex02 — `even_stream` |
| 12 | `next()` on generator | ex02 — `first_or_default` |
| 13 | `StopIteration` | ex02 — `first_or_default` |
| 14 | Comprehension scoping | ex02 — `no_leak` |
| 15 | Walrus `:=` | ex02 — `compact_squares` |
| 16 | Readability limits | ex03 — `refactor_nested` (docstring + body) |
| 17 | Performance | ex03 — `count_long_words` |
| 18 | `itertools` connection | ex03 — `first_n_squares` |
| 19 | Anti-pattern: over-nested | ex03 — `refactor_nested` |
| 20 | Industrial: filtered projection | ex03 — `select_active_users` |
| 21 | Industrial: index structures | ex03 — `index_orders_by_id` |

---

## ex01_basic.py — List / Dict / Set Comprehensions (Checklist items #1–#7)

**Must-pass behaviors:**
- `square_evens` uses a single list comprehension with an `if` filter.
- `signs_to_words` uses a list comprehension with `if/else` projection.
- `flatten_grid` flattens with a nested comprehension and rejects non-rectangular input.
- `swap_keys_values` uses a dict comprehension; raises on duplicate values.
- `keep_truthy` uses a dict comprehension with a trailing `if`.
- `unique_word_lengths` uses a set comprehension (no manual `set(...)` cast).

**Stretch behaviors:**
- `flatten_grid` works on any nested iterable, not only lists.
- `swap_keys_values` reports which value caused the duplicate.

### Functions to implement:
1. `square_evens(nums)` — list comprehension with `if n % 2 == 0`.
2. `signs_to_words(nums)` — list comprehension with `"+"`/`"0"`/`"-"` branching via `if/else`.
3. `flatten_grid(matrix)` — nested comprehension flattening 2-D input.
4. `swap_keys_values(d)` — dict comprehension swapping `k` and `v`.
5. `keep_truthy(d)` — dict comprehension filtering falsy values.
6. `unique_word_lengths(words)` — set comprehension of word lengths.

---

## ex02_intermediate.py — Generators, Scoping & Walrus (Checklist items #8–#15)

**Must-pass behaviors:**
- `lazy_doubles` returns a generator expression (not a list).
- `total_lengths` aggregates with `sum(... for ...)` (no outer parens).
- `memory_delta` returns `(list_bytes, gen_bytes)` and the list is bigger for non-zero `n`.
- `even_stream` is a `yield`-based generator function.
- `first_or_default` uses `next(...)` and handles `StopIteration` via a default.
- `no_leak` proves the comprehension loop variable does not escape into the caller's scope.
- `compact_squares` uses the walrus operator to compute each square only once.

**Stretch behaviors:**
- `even_stream` rejects negative limits with a descriptive `ValueError`.
- `compact_squares` is robust to non-numeric items via input validation.

### Functions to implement:
1. `lazy_doubles(nums)` — generator expression producing `2*n`.
2. `total_lengths(strings)` — `sum` over a bare generator expression.
3. `memory_delta(n)` — compare list vs generator byte size with `sys.getsizeof`.
4. `even_stream(limit)` — generator function yielding even numbers up to `limit`.
5. `first_or_default(it, default)` — call `next()`; catch `StopIteration`.
6. `no_leak()` — return `(outer_value, comprehension_result)` proving scoping.
7. `compact_squares(nums, threshold)` — walrus `:=` inside the comprehension.

---

## ex03_advanced.py — Industrial Pipelines & Anti-patterns (Checklist items #16–#21)

**Must-pass behaviors:**
- `refactor_nested` produces the same output as a 3-level `for` loop but keeps the comprehension to 2 levels by extracting a helper generator.
- `count_long_words` uses a generator expression inside `sum(...)` — must avoid materialising an intermediate list.
- `first_n_squares` uses `itertools.islice` to bridge a comprehension over an infinite generator.
- `select_active_users` returns a filtered projection (only `fields`, only active rows).
- `index_orders_by_id` builds an O(1) lookup dict keyed by `order_id`.

**Stretch behaviors:**
- `select_active_users` raises `ValueError` when `fields` is empty or contains unknown keys.
- `index_orders_by_id` raises `ValueError` on duplicate `order_id` values (instead of silently overwriting).

### Functions to implement:
1. `refactor_nested(workbook)` — helper-generator + 1-level comprehension replacing a 3-`for` nest.
2. `count_long_words(text, min_len)` — `sum(1 for w in text.split() if len(w) >= min_len)`.
3. `first_n_squares(n)` — `[x*x for x in islice(count(1), n)]`-style bridge.
4. `select_active_users(users, fields)` — filtered projection with field whitelist.
5. `index_orders_by_id(orders)` — dict comprehension keyed by `order_id`.

---

## Failure modes to watch for
- Calling `list()` on a generator twice and being surprised the second call is empty.
- Forgetting that comprehensions create their own scope — relying on the loop variable afterwards.
- Writing 3+ `for` clauses inside one comprehension and producing unreadable code.
- Using `[expr for x in xs if (y := f(x))]` without parentheses around the walrus.
- Materialising a generator just to pass it to `sum`/`any`/`all`/`max` — keep it lazy.
- Building an O(n²) `[x for x in big if x in other_big]` instead of converting `other_big` to a set first.

## Scoring

| Criterion | Max | ex01 | ex02 | ex03 |
|-----------|-----|------|------|------|
| Must-pass behaviors | 40 | | | |
| Stretch behaviors | 15 | | | |
| Inline asserts + AI-verified | 25 | | | |
| Style (types, ruff, docstrings) | 20 | | | |
| **Total** | **100** | | | |

## Suggested practice
- [Real Python — Comprehensions](https://realpython.com/list-comprehension-python/) — read each section and convert one of its examples into a generator expression.
- [Python docs — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) — official tutorial walk-through.

## Self-check commands
```bash
ruff check exercise/python_basic/day_13_comprehensions/
python exercise/python_basic/day_13_comprehensions/ex01_basic.py
python exercise/python_basic/day_13_comprehensions/ex02_intermediate.py
python exercise/python_basic/day_13_comprehensions/ex03_advanced.py
```
