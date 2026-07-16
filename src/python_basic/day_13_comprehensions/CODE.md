# Day 13 — Comprehensions

> **TL;DR:** Comprehensions are Python's declarative way to build a new
> collection from an iterable in a single expression. They beat `for`+`append`
> on readability and runtime, come in list / dict / set / generator flavours,
> and chain naturally with `if` filters, conditional expressions, and the
> walrus operator. `code.py` shows production-style projection, indexing,
> and lazy-pipeline patterns built entirely from comprehensions and
> generator expressions.

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|--------------|----------------|----------------|---------------|
| 1 | List comprehension | `[x*x for x in nums]` | Build a list from any iterable in one expression | Fewer lines, faster than manual `for`+`append` | ETL transforms, column derivations | `square_all` |
| 2 | With `if` filter | `[x for x in nums if x > 0]` | Keep only items matching a predicate | One-pass select + transform | Cleaning datasets | `keep_positive` |
| 3 | With `if/else` | `[x if x>=0 else -x for x in xs]` | Map with branching per element | Encodes per-item logic inline | Per-row classification | `clamp_signs` |
| 4 | Nested comprehension | `[c for row in m for c in row]` | Iterate over a nested iterable in source order | Flatten matrices, unnest 1-level data | Log/event flattening | `flatten_matrix` |
| 5 | Dict comprehension | `{k: f(v) for k, v in d.items()}` | Build a new dict in one expression | Re-key/re-value without loops | Config rewriting | `rekey_dict` |
| 6 | Dict with filter | `{k: v for k, v in d.items() if v}` | Project + filter dict items together | Strip empty/None values cleanly | API response shaping | `drop_falsy_values` |
| 7 | Set comprehension | `{w.lower() for w in words}` | Deduplicate + transform in one shot | O(1) lookup downstream | Distinct-id extraction | `unique_lowercased` |
| 8 | Generator expression | `(x*x for x in nums)` | Lazy iterator — no list materialised | Constant memory on huge streams | Log processing | `lazy_squares` |
| 9 | Generator in calls | `sum(x*x for x in nums)` | Drop parens when only argument to a func | Cleanest aggregation form | Pipelines with `sum/any/all/min/max` | `sum_of_squares` |
| 10 | Memory: list vs gen | `getsizeof([...])` vs `getsizeof((...))` | Demonstrates the memory delta | Avoid OOM on million-row inputs | Big-data scripts | `compare_memory` |
| 11 | `yield` preview | `def gen(): yield x` | Define generator functions explicitly | Reusable lazy producers with state | Custom iterators | `countdown` |
| 12 | `next()` on generator | `next(it)` | Manually pull the next value | Step through, peek, or batch | Streaming protocols | `peek_first` |
| 13 | `StopIteration` | Raised when iterator exhausts | Signal end-of-stream | Drives `for` loop termination | Custom iterators | `peek_first` |
| 14 | Scoping (Py3) | Loop var does not leak | Comprehension creates its own scope | No accidental name clashes | Cleaner refactors | `show_scoping` |
| 15 | Walrus `:=` | `[y for x in xs if (y := f(x)) > 0]` | Bind once, filter+use | Avoids calling `f(x)` twice | Costly predicates | `filter_with_walrus` |
| 16 | Readability limits | Max ~2 nesting levels | Beyond that → refactor to a function | Comprehensions read top-down; deep nesting reads sideways | Code review rule | `flatten_matrix` (clear), anti-pattern snippet |
| 17 | Performance | Comprehensions > `for`+`append` | C-level loop vs Python-level attribute lookups | Hot paths get 30–50% faster | Inner loops | `benchmark_comprehension_vs_loop` |
| 18 | `itertools` connection | `chain`, `islice`, `groupby` | Graduate when comprehensions stop fitting | Multi-source / windowed / grouped iteration | Stream ops | `take_first_n` |
| 19 | Anti-pattern: over-nested | 3+ `for` clauses | Hard to read, hides bugs | Refactor to a helper function | Code review block | anti-pattern snippet |
| 20 | Industrial: filtered projection | Select+rename rows | One-pass column subset | API serialisation, masking | DB row → DTO | `project_users` |
| 21 | Industrial: index structure | `{u["id"]: u for u in users}` | Build O(1) lookup from a list | Avoid repeated O(n) scans | Join-by-id pipelines | `index_by` |

## Snippets

### 1. List comprehension — basics (#1)

The canonical form: `[expression for item in iterable]`.

```python
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)
```

Expected output:
```text
[1, 4, 9, 16, 25]
```

> 💡 Read it as "for every `n` in `nums`, evaluate `n * n` and collect."

### 2. Filter with `if`, branch with `if/else` (#2, #3)

`if` after the loop = filter; `if/else` before the loop = conditional expression.

```python
nums = [-3, -1, 0, 2, 5]
positives = [n for n in nums if n > 0]            # filter
abs_nums = [n if n >= 0 else -n for n in nums]    # branch
print(positives, abs_nums)
```

Expected output:
```text
[2, 5] [3, 1, 0, 2, 5]
```

> 💡 Position matters: filter `if` goes at the **end**, branching `if/else`
> goes at the **front** of the expression.

### 3. Nested comprehensions — flatten in source order (#4)

The leftmost loop is the outer one, exactly like nested `for`.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [cell for row in matrix for cell in row]
print(flat)
```

Expected output:
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> 💡 Two `for` clauses are fine; three or more — extract to a function.

### 4. Dict and set comprehensions (#5, #6, #7)

Same syntax, different brackets.

```python
prices = {"apple": 1.2, "bread": 0.0, "milk": 2.5}
discounted = {item: p * 0.9 for item, p in prices.items() if p > 0}
unique_chars = {c.lower() for c in "Hello"}
print(discounted)
print(sorted(unique_chars))
```

Expected output:
```text
{'apple': 1.08, 'milk': 2.25}
['e', 'h', 'l', 'o']
```

> 💡 Set comprehensions deduplicate for free — no explicit `set(...)` wrapper needed.

### 5. Generator expressions — lazy pipelines (#8, #9, #10)

Parentheses build a generator; pass straight into an aggregator and you can
even drop the parens.

```python
import sys

nums = range(10_000)
list_size = sys.getsizeof([n * n for n in nums])
gen_size = sys.getsizeof((n * n for n in nums))
total = sum(n * n for n in nums)   # no outer parens needed
print(list_size > gen_size, total)
```

Expected output:
```text
True 333283335000
```

> 💡 A generator is a *recipe*; the list is the *baked cake*. Use the recipe
> when you only need each value once.

### 6. `yield`, `next()`, and `StopIteration` (#11, #12, #13)

A generator function with `yield` is the explicit cousin of a genexp.

```python
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1

g = countdown(3)
print(next(g), next(g), next(g))
try:
    next(g)
except StopIteration:
    print("done")
```

Expected output:
```text
3 2 1
done
```

> 💡 `for` loops swallow `StopIteration` for you — only catch it when stepping manually.

### 7. Comprehension scoping (Py3) (#14)

The loop variable lives only inside the comprehension.

```python
x = "outer"
squares = [x * x for x in range(3)]
print(x)        # still "outer" — not leaked
print(squares)
```

Expected output:
```text
outer
[0, 1, 4]
```

> 💡 In Python 2 the loop name leaked; Python 3 fixed this — write safely without worrying.

### 8. Walrus operator `:=` in comprehensions (#15)

**In simple terms:** the walrus operator `:=` lets you **assign a value to a
variable *and* use that same value in the same expression**, all in one go.
Think of it as "calculate once, name it, then reuse the name right here."

- Normal `=` is a *statement* — it stands alone on its own line.
- Walrus `:=` is an *expression* — it returns the value it just assigned, so
  you can drop it inside an `if`, a `while`, or a comprehension.

Read `(y := expensive(x))` as: *"compute `expensive(x)`, store it in `y`,
and hand that value back to the surrounding expression."*

Bind a costly result once and reuse it in both filter and output.

```python
def expensive(x: int) -> int:
    return x * x - 1

results = [y for x in range(5) if (y := expensive(x)) > 0]
print(results)
```

Expected output:
```text
[3, 8, 15]
```

> 💡 Without walrus you'd call `expensive(x)` twice — once in the `if`, once
> in the projection. With walrus, you call it once, name the result `y`,
> and reuse `y` in both the filter and the output.

**Tiny mental model — outside a comprehension:**

```python
# ❌ Without walrus — repeats the work or needs an extra line
line = input()
while line != "quit":
    print(line)
    line = input()

# ✅ With walrus — read once, test once, use once
while (line := input()) != "quit":
    print(line)
```

> 💡 Rule of thumb: reach for `:=` only when the *same value* is needed in
> both a **test** and a **use**. Otherwise, a plain `=` on its own line is
> clearer.

### 9. Performance: comprehension vs `for`+`append` (#17)

Comprehensions run the loop in C; the appended version pays Python attribute
lookup on every iteration.

```python
import timeit

setup = "nums = list(range(10_000))"
t_loop = timeit.timeit(
    "out=[]\nfor n in nums: out.append(n*n)", setup=setup, number=500
)
t_comp = timeit.timeit("[n*n for n in nums]", setup=setup, number=500)
print(f"loop={t_loop:.3f}s  comp={t_comp:.3f}s  speedup={t_loop / t_comp:.2f}x")
```

Expected output (numbers vary):
```text
loop=0.420s  comp=0.260s  speedup=1.62x
```

> 💡 The win shrinks for trivial bodies but is real on tight inner loops.

### 10. Industrial — projection + index (#20, #21)

Two patterns you will write every week in real code.

```python
users = [
    {"id": 1, "name": "Ada", "active": True},
    {"id": 2, "name": "Linus", "active": False},
    {"id": 3, "name": "Grace", "active": True},
]
active_names = [{"id": u["id"], "name": u["name"]} for u in users if u["active"]]
by_id = {u["id"]: u for u in users}
print(active_names)
print(by_id[3]["name"])
```

Expected output:
```text
[{'id': 1, 'name': 'Ada'}, {'id': 3, 'name': 'Grace'}]
Grace
```

> 💡 The dict comprehension turns an O(n) `next(u for u in users if u["id"]==k)` scan into an O(1) lookup.

## Anti-patterns

### Anti-pattern: over-nested comprehension (#19)

```python
# ❌ Bad — three for-clauses + conditional, unreadable
result = [
    cell.upper()
    for sheet in workbook
    for row in sheet
    for cell in row
    if isinstance(cell, str) and cell.strip()
]

# ✅ Corrected — extract a helper, keep ≤ 2 levels per comprehension
def iter_string_cells(workbook):
    for sheet in workbook:
        for row in sheet:
            for cell in row:
                if isinstance(cell, str) and cell.strip():
                    yield cell

result = [cell.upper() for cell in iter_string_cells(workbook)]
```
> Over-nested comprehensions hide branching and break code-review diffs. The
> generator helper documents the *what* and keeps the comprehension focused
> on the *transform*.

### Anti-pattern: `list(map(lambda ...))` instead of a comprehension (#21 docs)

```python
# ❌ Bad — verbose, slower in CPython, and the lambda obscures the body
upper_names = list(map(lambda n: n.upper(), names))

# ✅ Corrected — comprehension reads top-down and runs in C
upper_names = [n.upper() for n in names]
```
> Reserve `map`/`filter` for when you already have a named function — never
> wrap a lambda just to feed `map`.

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| Filtered projection | `[{"id": u["id"], "name": u["name"]} for u in users if u["active"]]` | Building API/DTO payloads |
| Index by key | `{u["id"]: u for u in users}` | Replacing repeated O(n) lookups |
| Inverted index | `{w: [i for i, t in enumerate(docs) if w in t] for w in vocab}` | Search prototypes |
| Lazy stream | `(parse(line) for line in open(path))` | Large-file or socket processing |

## Pitfalls

- **Mutating during iteration** — never modify the source list inside a comprehension; build a new one.
- **Exhausted generators** — a genexp can only be iterated once; assign to a variable if you need to peek then sum.
- **`list(gen())` defeats laziness** — only materialise when you truly need random access.
- **Walrus precedence surprises** — wrap `:=` expressions in parentheses inside `if` clauses.
- **Hidden N² cost** — `[x for x in big_list if x in other_big_list]` is O(n·m); convert `other_big_list` to a `set` first.

## Why this design

`code.py` keeps every comprehension under two nesting levels and prefers
generator expressions for any pipeline that flows straight into an aggregator
(`sum`, `any`, `max`). Industrial patterns (`project_users`, `index_by`) take
typed inputs and return plain Python collections so callers can compose them
into larger ETL flows.

## Further reading

- [Real Python — Comprehensions](https://realpython.com/list-comprehension-python/) — primary source
- [Python docs — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) — official reference
- [PEP 202 — List Comprehensions](https://peps.python.org/pep-0202/) — design rationale
- [PEP 274 — Dict Comprehensions](https://peps.python.org/pep-0274/) — dict syntax origins
- [PEP 572 — Assignment Expressions](https://peps.python.org/pep-0572/) — walrus operator
