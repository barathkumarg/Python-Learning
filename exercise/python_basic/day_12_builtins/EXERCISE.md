# Day 12 — Built-ins in Pipelines: Exercises

## Learning objectives

After completing these exercises you will be able to:
1. Use `enumerate`, `zip` (incl. `strict=True`), `sorted`, and `reversed` to iterate and order data without manual index math (checklist #1–#5).
2. Compose `map`, `filter`, `any`, `all`, `sum`, `min`/`max`, and numeric helpers into lazy pipelines that aggregate correctly on empty input (checklist #6–#13).
3. Apply introspection helpers (`isinstance`, `type`, `id`, `hash`, `callable`), use `iter`/`next` for find-first, and choose between comprehensions and `map`/`filter` deliberately — culminating in a full `parse → map → filter → aggregate` revenue pipeline (checklist #14–#22).

## Skills assessed

| Skill ID | Skill | Exercise | Proficiency target |
|----------|-------|----------|--------------------|
| PY-04 | Iteration & sequencing | ex01 | proficient |
| PY-06 | Functional built-ins (`map`/`filter`/`any`/`all`) | ex02 | proficient |
| PY-08 | Input validation with explicit errors | ex02, ex03 | proficient |
| PY-09 | Introspection & hashing | ex03 | developing |
| PY-12 | End-to-end data pipelines | ex03 | proficient |

## Concept coverage map

| Checklist # | Concept | Covered in |
|-------------|---------|------------|
| 1 | `enumerate()` | ex01 — `number_lines` |
| 2 | `zip()` | ex01 — `pair_columns` |
| 3 | `zip(strict=True)` | ex01 — `pair_columns_strict` |
| 4 | `sorted()` w/ `key=`, `reverse=` | ex01 — `rank_scores` |
| 5 | `reversed()` | ex01 — `recent_first` |
| 6 | `map()` | ex02 — `apply_discount` |
| 7 | `filter()` | ex02 — `drop_disabled` |
| 8 | `any()` | ex02 — `any_overdue` |
| 9 | `all()` | ex02 — `all_paid` |
| 10 | `sum()` | ex02 — `safe_total` |
| 11 | `min()` / `max()` w/ `default=` | ex02 — `cheapest_item` |
| 12 | `abs()` / `round()` / `divmod()` | ex02 — `format_hms` |
| 13 | `len()` / `range()` | ex02 — `paginate` |
| 14 | `isinstance()` | ex03 — `coerce_int` |
| 15 | `type()` / `id()` / `hash()` | ex03 — `dedupe_records` |
| 16 | `print(sep=, end=)` | ex03 — `render_csv_line` |
| 17 | `iter()` / `next()` | ex03 — `find_first_admin` |
| 18 | `callable()` | ex03 — `safe_apply` |
| 19 | comprehension vs `map`/`filter` | ex03 — `to_uppercase_names` |
| 20 | Chaining built-ins | ex03 — `pipeline_sum_positive` |
| 21 | Anti-pattern `list(map(lambda))` | ex03 — `to_uppercase_names` (docstring) |
| 22 | Industrial pipeline | ex03 — `daily_sales_report` |

---

## ex01_basic.py — Iteration & Ordering (Checklist items #1–#5)

**Must-pass behaviors:**
- `number_lines` uses `enumerate` with configurable `start`.
- `pair_columns` joins header/row with `zip` (silent truncation accepted).
- `pair_columns_strict` raises `ValueError` on length mismatch.
- `rank_scores` sorts descending by score, then ascending by name (tie-break).
- `recent_first` returns a reversed copy without mutating the input.

**Stretch behaviors:**
- `rank_scores` accepts a custom `key_field` parameter.
- `recent_first` works on any iterable (not just `list`).

### Functions to implement:
1. `number_lines(lines, start=1)` — return `[f"{i}. {line}", ...]` using `enumerate`.
2. `pair_columns(header, row)` — return a dict using plain `zip`.
3. `pair_columns_strict(header, row)` — return a dict using `zip(strict=True)`.
4. `rank_scores(records)` — sort by `(-score, name)` and return new list.
5. `recent_first(events)` — return a list of events newest-first using `reversed`.

---

## ex02_intermediate.py — Map / Filter / Aggregate (Checklist items #6–#13)

**Must-pass behaviors:**
- `apply_discount` returns an iterator (not a list) and validates `rate ∈ [0, 1]`.
- `drop_disabled` filters out users whose `enabled` is falsy.
- `any_overdue` short-circuits on the first overdue invoice.
- `all_paid` returns `True` for an empty list (vacuous truth).
- `safe_total` returns `0.0` on empty input (uses `sum(..., start=0.0)`).
- `cheapest_item` returns `default` on empty input (uses `min(..., default=...)`).
- `format_hms` uses `divmod` and rejects negative seconds.
- `paginate` uses `range` + `len` to yield `(start, end)` slice indices.

**Stretch behaviors:**
- `apply_discount` works on a generator input without consuming twice.
- `paginate` raises `ValueError` for `size <= 0`.

### Functions to implement:
1. `apply_discount(prices, rate)` — `map`-based lazy price reduction.
2. `drop_disabled(users)` — `filter`-based active-only selector.
3. `any_overdue(invoices)` — `any()` short-circuit predicate.
4. `all_paid(invoices)` — `all()` invariant check.
5. `safe_total(amounts)` — `sum` with `start=0.0`.
6. `cheapest_item(items, default=None)` — `min` with `default=`.
7. `format_hms(seconds)` — `divmod` formatter `"HH:MM:SS"`.
8. `paginate(total, size)` — `range`+`len` slice index pairs.

---

## ex03_advanced.py — Introspection, Chaining & Industrial Pipeline (Checklist items #14–#22)

**Must-pass behaviors:**
- `coerce_int` accepts `int` and numeric `str`, rejects `bool` and non-numeric strings.
- `dedupe_records` preserves first occurrence and uses `hash` (set of seen keys).
- `render_csv_line` uses `print(sep=, end=)` and returns the printed string.
- `find_first_admin` uses `next(iter(...), default)` — no full scan if a match is found early.
- `safe_apply` only invokes `func` when `callable(func)` is True.
- `to_uppercase_names` uses a comprehension (the anti-pattern `list(map(lambda ...))` is documented in the docstring as what NOT to write).
- `pipeline_sum_positive` chains `filter → map → sum` lazily.
- `daily_sales_report` runs the full `parse → map → filter → aggregate` flow and returns `{total, count, top, ranked}`.

**Stretch behaviors:**
- `daily_sales_report` accepts a custom `min_amount` and rejects negative values.
- `dedupe_records` raises `ValueError` when the chosen key is unhashable.

### Functions to implement:
1. `coerce_int(value)` — `isinstance` validation + coercion.
2. `dedupe_records(records, key_field)` — `hash`-based dedupe preserving order.
3. `render_csv_line(fields, sep=",")` — `print(sep=, end=)` row renderer.
4. `find_first_admin(users)` — `iter`/`next` find-first.
5. `safe_apply(func, value)` — `callable()`-guarded application.
6. `to_uppercase_names(names)` — comprehension form (NOT `list(map(lambda ...))`).
7. `pipeline_sum_positive(rows)` — chained `filter → map → sum`.
8. `daily_sales_report(rows, min_amount=0.0)` — full industrial pipeline.

---

## Failure modes to watch for
- Calling `list()` twice on the same `map`/`filter` iterator and being surprised the second call is empty.
- Forgetting `default=` on `max`/`min` and crashing on empty input.
- Using `zip` without `strict=True` in ETL code and silently truncating rows.
- Treating `bool` as a numeric in `coerce_int` (it's a subclass of `int`).
- Using `list(map(lambda x: ..., xs))` where a comprehension would be clearer.
- Forgetting that `all([])` is `True` and `any([])` is `False`.

## Scoring

| Criterion | Max | ex01 | ex02 | ex03 |
|-----------|-----|------|------|------|
| Must-pass behaviors | 40 | | | |
| Stretch behaviors | 15 | | | |
| Inline asserts + AI-verified | 25 | | | |
| Style (types, ruff, docstrings) | 20 | | | |
| **Total** | **100** | | | |

## Suggested practice
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html) — read each entry used today and skim its examples.
- [Real Python — `map`, `filter`, `reduce`](https://realpython.com/python-map-filter-reduce/) — practice converting `list(map(...))` calls into comprehensions.

## Self-check commands
```bash
ruff check exercise/python_basic/day_12_builtins/
python exercise/python_basic/day_12_builtins/ex01_basic.py
python exercise/python_basic/day_12_builtins/ex02_intermediate.py
python exercise/python_basic/day_12_builtins/ex03_advanced.py
```
