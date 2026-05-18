# Day 12 — Built-ins in Pipelines

> **TL;DR:** Python's built-in functions (`enumerate`, `zip`, `sorted`, `map`,
> `filter`, `any`, `all`, `sum`, `min`/`max`, `iter`/`next`, …) are the bricks of
> readable data pipelines. Day 12 chains them into a **parse → map → filter →
> aggregate** flow, learns when a comprehension is clearer than `list(map(...))`,
> and uses introspection helpers (`isinstance`, `callable`, `hash`) to keep
> production pipelines safe.

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|--------------|----------------|----------------|---------------|
| 1 | `enumerate()` | `enumerate(xs, start=1)` | Yields `(index, value)` pairs | Avoid manual counters in loops | Numbered log/audit lines | `enumerate_rows` |
| 2 | `zip()` | `zip(keys, values)` | Pairs items from N iterables (stops at shortest) | Join parallel columns without index math | Combine CSV header + row | `zip_columns` |
| 3 | `zip()` strict | `zip(a, b, strict=True)` | Raises `ValueError` on length mismatch | Catch data bugs at the join point | ETL row/header validation | `zip_columns_strict` |
| 4 | `sorted()` | `sorted(xs, key=..., reverse=True)` | Returns a new sorted list | Stable, key-driven ordering | Leaderboards, ranking | `sort_records` |
| 5 | `reversed()` | `reversed(seq)` | Lazy reverse iterator | Walk a sequence backwards w/o copy | Replaying recent events first | `reverse_history` |
| 6 | `map()` | `map(func, xs)` | Lazy transform iterator | Compose transforms in pipelines | `parse → normalize` stage | `transform_prices` |
| 7 | `filter()` | `filter(pred, xs)` | Lazy selection iterator | Drop bad/irrelevant rows | Remove disabled users | `keep_active` |
| 8 | `any()` | `any(p(x) for x in xs)` | Short-circuits at first truthy | Cheap existence check | "any failed job?" | `has_failed_job` |
| 9 | `all()` | `all(p(x) for x in xs)` | Short-circuits at first falsy | Cheap invariant check | "every field valid?" | `all_fields_present` |
| 10 | `sum()` | `sum(xs, start=0)` | Aggregates numerics (or lists with `start=[]`) | Final aggregation step | Revenue totals | `total_revenue` |
| 11 | `min()` / `max()` | `max(xs, key=..., default=...)` | Picks extreme value safely | `default=` avoids empty-iterable errors | Top-spender, cheapest item | `top_spender` |
| 12 | `abs()` / `round()` / `divmod()` | `divmod(125, 60)` | Numeric helpers | Money rounding, time math | Currency, duration formatting | `format_duration`, `round_amount` |
| 13 | `len()` / `range()` | `range(0, n, step)` | Sizing & index sequences | Window iteration, batch sizing | Pagination, batching | `batched_indices` |
| 14 | `isinstance()` | `isinstance(x, (int, float))` | Runtime type guard | Validate inputs before pipeline runs | API payload validation | `coerce_amount` |
| 15 | `type()` / `id()` / `hash()` | `hash(("a", 1))` | Introspection & identity | Cache keys, dedupe, debugging | Memoization, dedupe by tuple | `dedupe_by_key` |
| 16 | `input()` / `print()` | `print(*xs, sep=" | ", end="\n")` | I/O with separators | Pretty CLI output | Report rendering | `print_report` |
| 17 | `iter()` / `next()` | `next(it, default)` | Manual iterator stepping | Peek the first match cheaply | Find-first in a stream | `first_match` |
| 18 | `callable()` | `callable(obj)` | Tests if an object is callable | Plugin / strategy registries | Validate registered hooks | `apply_if_callable` |
| 19 | `map+filter` vs comprehension | `[f(x) for x in xs if p(x)]` | Same intent, different style | Comprehensions usually clearer | Code-review readability rule | `comprehension_vs_map` |
| 20 | Chaining built-ins | `sum(map(f, filter(p, xs)))` | One-pass lazy pipeline | Composable, memory-friendly | Streaming aggregations | `pipeline_total` |
| 21 | Anti-pattern: `list(map(lambda…))` | `list(map(lambda x: x*2, xs))` | Verbose vs `[x*2 for x in xs]` | Hurts readability/perf | Code review reject | `anti_pattern_list_map` |
| 22 | Industrial: data pipeline | `parse → map → filter → aggregate` | Full ETL micro-pipeline | The everyday shape of analytics jobs | Daily revenue rollup | `daily_revenue_report` |

## Snippets

### 1. `enumerate()` + `zip()` — index and parallel iteration

Use `enumerate` instead of `for i in range(len(xs))`; use `zip` instead of index math across two lists.

```python
names = ["Ada", "Linus", "Grace"]
scores = [91, 88, 95]
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} -> {score}")
```

Expected output:
```text
1. Ada -> 91
2. Linus -> 88
3. Grace -> 95
```

> 💡 `start=1` makes numbered reports read like a human list, not an array index.

### 2. `zip(..., strict=True)` — fail fast on mismatched columns

When two iterables *must* line up (CSV header + row), `strict=True` turns a silent bug into a loud `ValueError`.

```python
header = ["id", "name", "email"]
row = ["7", "Ada"]            # missing email
list(zip(header, row, strict=True))
```

Expected output:
```text
ValueError: zip() argument 2 is shorter than argument 1
```

> 💡 Always use `strict=True` in ETL code — silent truncation corrupts downstream tables.

### 3. `sorted()` with `key=` and `reverse=` — stable, key-driven ordering

`sorted` is **stable** (equal keys keep original order) and accepts any callable as a key.

```python
records = [{"name": "Ada", "amt": 30}, {"name": "Grace", "amt": 50}, {"name": "Linus", "amt": 30}]
ranked = sorted(records, key=lambda r: (-r["amt"], r["name"]))
print([r["name"] for r in ranked])
```

Expected output:
```text
['Grace', 'Ada', 'Linus']
```

> 💡 The `(-amt, name)` key is the classic "sort by amount desc, then name asc" trick.

### 4. `map()` + `filter()` — lazy transforms and selections

`map` and `filter` return *iterators*, not lists — nothing runs until you consume them.

```python
nums = [1, 2, 3, 4, 5]
doubled_evens = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums))
print(type(doubled_evens).__name__, "->", list(doubled_evens))
```

Expected output:
```text
map -> [4, 8]
```

> 💡 Materialize with `list(...)` only at the boundary; keep the middle of the pipeline lazy.

### 5. `any()` / `all()` — short-circuit boolean aggregations

Both stop at the first decisive value, so they are cheap even on huge iterables.

```python
jobs = [{"id": 1, "status": "ok"}, {"id": 2, "status": "failed"}, {"id": 3, "status": "ok"}]
print(any(j["status"] == "failed" for j in jobs))
print(all(j["status"] == "ok" for j in jobs))
```

Expected output:
```text
True
False
```

> 💡 Prefer `any(... for ...)` over building a temporary list — it short-circuits.

### 6. `sum()`, `min()`, `max()` — safe aggregations with `default=`

`min`/`max` raise `ValueError` on empty iterables unless you pass `default=`.

```python
amounts = [12.5, 30.0, 7.25]
print(sum(amounts))
print(max(amounts, default=0.0))
print(max([], default=0.0))     # safe on empty input
```

Expected output:
```text
49.75
30.0
0.0
```

> 💡 Always pass `default=` in pipelines — production data is sometimes empty.

### 7. Numeric helpers — `abs()`, `round()`, `divmod()`

`divmod(a, b)` returns `(a // b, a % b)` in one call — useful for time and money math.

```python
seconds = 3725
hours, rest = divmod(seconds, 3600)
minutes, secs = divmod(rest, 60)
print(f"{hours:02d}:{minutes:02d}:{secs:02d}")
print(abs(-3.7), round(3.14159, 2))
```

Expected output:
```text
01:02:05
3.7 3.14
```

> 💡 `round()` uses banker's rounding — use `decimal.Decimal` for money totals.

### 8. `iter()` / `next()` — peek the first match without scanning

`next(iter, default)` is the idiomatic "find-first" in a stream.

```python
users = [{"id": 1, "role": "guest"}, {"id": 2, "role": "admin"}, {"id": 3, "role": "guest"}]
first_admin = next((u for u in users if u["role"] == "admin"), None)
print(first_admin)
```

Expected output:
```text
{'id': 2, 'role': 'admin'}
```

> 💡 Pass a `default` to `next` — otherwise you get `StopIteration` on no match.

### 9. Chained pipeline — `parse → map → filter → sum`

This is the day's headline pattern: each stage does one job and stays lazy.

```python
rows = ["12.50", "bad", "30.0", "7.25", ""]            # ① source

total = sum(                                            # ④ reduce  (eager driver)
    map(float,                                          # ③ transform (lazy)
        filter(lambda s: s.replace(".", "", 1).isdigit(),  # ② validate (lazy)
               rows)                                    # ↑ feeds from source
    )
)
print(total)
```

Expected output:
```text
49.75
```

#### Conveyor-belt model

Each function is a station; items flow left → right and only valid ones reach the end:

```text
rows ──▶ filter(is_numeric) ──▶ map(float) ──▶ sum
"12.50" ─────▶ keep ─────────▶ 12.50 ─────────┐
"bad"   ─────▶ drop                            │
"30.0"  ─────▶ keep ─────────▶ 30.0  ──────────┤── 49.75
"7.25"  ─────▶ keep ─────────▶ 7.25  ──────────┘
""      ─────▶ drop
```

Nothing is materialised between stages — `filter` and `map` return **lazy iterators**, so `sum` pulls one value at a time. Memory stays O(1) regardless of input size.

#### Stage ① — source `rows`

A mixed-quality list (CSV column, log field, form input). Some valid numbers, some garbage, one empty string. The pipeline's job is to be robust against this.

#### Stage ② — `filter(predicate, rows)`: keep only numeric-looking strings

```python
filter(lambda s: s.replace(".", "", 1).isdigit(), rows)
```

`filter(pred, iterable)` yields each `s` where `pred(s)` is truthy. The predicate `s.replace(".", "", 1).isdigit()` is a compact check for "non-negative decimal":

| Input `s` | `s.replace(".", "", 1)` | `.isdigit()` | Kept? |
|-----------|------------------------|--------------|-------|
| `"12.50"` | `"1250"` | `True` | ✅ |
| `"bad"`   | `"bad"`  | `False` | ❌ |
| `"30.0"`  | `"300"`  | `True` | ✅ |
| `"7.25"`  | `"725"`  | `True` | ✅ |
| `""`      | `""`     | `False` (empty fails `isdigit`) | ❌ |

The `1` in `replace(".", "", 1)` strips **at most one** dot, so `"1.2.3"` correctly fails. `filter(...)` itself returns an iterator — no predicate runs yet.

> ⚠️ This predicate rejects negatives (`"-3.14"`), scientific notation (`"1e3"`), and whitespace. For production, prefer a `try/except float(s)` helper.

#### Stage ③ — `map(float, …)`: parse survivors to numbers

```python
map(float, <filter iterator>)
```

`map(fn, iterable)` yields `fn(item)` per upstream value. `float` is passed **by reference** (not called), so `map` invokes it per element. Still lazy — `map(...)` returns a `map` object.

> 💡 Order matters: `filter` runs **before** `map` so `float("bad")` never executes. Swapping the stages would raise `ValueError`.

#### Stage ④ — `sum(…)`: the eager driver

`sum` is the first consumer that actually pulls values. Trace of execution:

```text
sum needs next ──▶ map needs next ──▶ filter needs next ──▶ rows yields "12.50"
                                                          ──▶ predicate True
                                  ──▶ float("12.50") = 12.50
              ──▶ accumulator = 0 + 12.50 = 12.50

sum needs next ──▶ map needs next ──▶ filter needs next ──▶ "bad"  → drop
                                                          ──▶ "30.0" → keep
                                  ──▶ float("30.0") = 30.0
              ──▶ accumulator = 12.50 + 30.0 = 42.50

... continues until rows is exhausted.
Final: 12.50 + 30.0 + 7.25 = 49.75
```

`sum` keeps a single running accumulator (init `0`). Memory cost: one float — the input list could be 5 million rows and the footprint would not change.

#### Equivalent generator-expression form

```python
total = sum(
    float(s)
    for s in rows
    if s.replace(".", "", 1).isdigit()
)
```

Same laziness, same result, reads top-to-bottom (source → filter → transform). Pick by team preference.

#### Why the pipeline beats the imperative loop

```python
# Imperative equivalent — works, but 3 concerns interleaved
total = 0.0
for s in rows:
    if s.replace(".", "", 1).isdigit():   # filter
        n = float(s)                       # map
        total += n                         # sum
```

The pipeline version makes every stage **independently replaceable**: swap `float` → `int`, swap the predicate, swap `sum` → `max` — without touching the others.

> 💡 Comprehensions can express the same idea more readably — see the anti-pattern below.

## Anti-patterns

### Anti-pattern: `list(map(lambda …))` instead of a comprehension
```python
# ❌ Bad — verbose, harder to read, no real perf win
doubled = list(map(lambda x: x * 2, [1, 2, 3]))

# ✅ Corrected — comprehension is the Pythonic default
doubled = [x * 2 for x in [1, 2, 3]]
```
> Reach for `map`/`filter` only when you already have a *named* function to pass; otherwise comprehensions are clearer and equally fast.

### Anti-pattern: silent `zip()` truncation on mismatched columns
```python
# ❌ Bad — silently drops the missing email and corrupts downstream rows
record = dict(zip(["id", "name", "email"], ["7", "Ada"]))

# ✅ Corrected — fail fast in ETL code
record = dict(zip(["id", "name", "email"], ["7", "Ada"], strict=True))
```
> In production, the silent version turns into a 3 a.m. data-quality incident.

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| Lazy chain | `sum(map(parse, filter(valid, lines)))` | Streaming files / large inputs — keep memory flat |
| `key=` for domain sort | `sorted(orders, key=lambda o: (-o.amount, o.id))` | Leaderboards / multi-field ranking |
| `default=` on `max`/`min` | `max(prices, default=0.0)` | Any aggregation that can see empty input |
| Comprehension over `list(map(lambda))` | `[x.upper() for x in names]` | Default style — only switch when reusing a named function |

## Pitfalls

- `map`/`filter` return **iterators** — printing them shows `<map object …>` and consuming twice yields nothing the second time.
- `sorted(..., key=str.lower)` is fine for strings, but mixing types (`int` and `str`) raises `TypeError` in Python 3.
- `min([])` / `max([])` raise `ValueError` unless you pass `default=`.
- `hash()` works only on **hashable** types (no `list`/`dict`/`set`); use `tuple(sorted(d.items()))` for dict keys.
- `round(0.5)` returns `0`, not `1`, because of banker's rounding — use `decimal` for currency.

## Why this design

`code.py` keeps each built-in in its own small typed function so the file reads as a *catalogue* of pipeline stages, then assembles them into `daily_revenue_report` to show the full **parse → map → filter → aggregate** flow. Every public function validates its inputs with explicit `ValueError` messages and uses lazy iterators internally to mirror what production ETL code looks like.

## Further reading

- [Python Built-in Functions](https://docs.python.org/3/library/functions.html) — authoritative reference for every function used today
- [Real Python — `map`, `filter`, `reduce`](https://realpython.com/python-map-filter-reduce/) — when each is the right tool
- [PEP 618 — `zip(strict=True)`](https://peps.python.org/pep-0618/) — rationale for strict zipping
- [Python HOWTO — Functional Programming](https://docs.python.org/3/howto/functional.html) — composing iterators in pipelines
