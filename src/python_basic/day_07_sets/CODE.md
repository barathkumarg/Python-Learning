# Day 07 — Sets and frozenset

> **TL;DR:** Sets provide O(1) average membership testing, automatic deduplication,
> and powerful set-algebra operations (union, intersection, difference). `frozenset`
> adds immutability so sets can be used as dict keys or nested inside other sets.
> `code.py` demonstrates creation, mutation, set math, frozenset usage, and two
> industrial patterns: log deduplication and RBAC permission comparison.

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|-------------|----------------|---------------|---------------|
| 1 | Literal creation | `{1, 2, 3}`, empty: `set()` | Creates a mutable set from literals | Foundation of all set work; `{}` creates a dict, not a set | Config allow-lists | `demo_creation` |
| 2 | `set()` constructor | `set(iterable)` | Builds a set from any iterable, deduping automatically | Convert lists/strings to unique elements | Log line deduplication | `demo_creation` |
| 3 | `add()` | `s.add(elem)` | Inserts one element; no-op if already present | O(1) insertion | Tracking seen items | `demo_mutation` |
| 4 | `remove()` vs `discard()` | `remove` raises `KeyError`, `discard` is silent | Delete by value with or without error on miss | Choose based on whether absence is a bug | Cache eviction | `demo_mutation` |
| 5 | `pop()` / `clear()` | `s.pop()`, `s.clear()` | Remove arbitrary element / empty the set | `pop` useful for drain loops; `clear` resets state | Queue-drain patterns | `demo_mutation` |
| 6 | `update()` / `\|=` | `s.update(other)` | Add all elements from another iterable in-place | Bulk insertion, merging tag sets | Merging feature flags | `demo_mutation` |
| 7 | Union `\|` | `s1 \| s2` | Returns new set with all elements from both | Combine without mutating originals | Merging role permissions | `compare_permissions` |
| 8 | Intersection `&` | `s1 & s2` | Returns new set with common elements | Find overlap between groups | Shared access audit | `compare_permissions` |
| 9 | Difference `-` | `s1 - s2` | Elements in first but not second | Identify what's missing or extra | Permission gap analysis | `compare_permissions` |
| 10 | Symmetric difference `^` | `s1 ^ s2` | Elements in either but not both | Find all differences between groups | Config drift detection | `compare_permissions` |
| 11 | Subset `<=` / superset `>=` | `s1.issubset(s2)` | Test containment relationships | Validate required permissions | RBAC checks | `compare_permissions` |
| 12 | `isdisjoint()` | `s1.isdisjoint(s2)` | True if no common elements | Quick conflict check | Exclusive lock groups | `compare_permissions` |
| 13 | `in` membership | `elem in s` | O(1) average membership test | Fastest way to check presence | Allow/deny-list filtering | `dedupe_logs` |
| 14 | Iteration | `for x in s:` | Loop over elements (unordered) | Process every unique element | Batch operations | `demo_iteration` |
| 15 | Set comprehension | `{expr for x in iterable}` | Build set with transform + optional filter | Concise creation with dedup | Extract unique tags | `demo_comprehension` |
| 16 | `frozenset` | `frozenset(iterable)` | Immutable set — cannot add/remove after creation | Hashable, safe for concurrent reads | Immutable config sets | `demo_frozenset` |
| 17 | `frozenset` as dict key | `{frozenset({1,2}): "val"}` | Use frozen set as dict key | Group data by unordered key | Anagram/combination grouping | `demo_frozenset` |
| 18 | Hashability requirement | No lists/dicts in sets | Only hashable objects allowed | Prevents subtle runtime errors | Validate before insertion | `demo_frozenset` |
| 19 | Built-in aggregation | `len()`, `min()`, `max()`, `sum()` | Standard aggregates work on sets | Quick stats on unique values | Unique-value analytics | `demo_aggregation` |
| 20 | Anti-pattern: unhashable in set | `{[1,2]}` → `TypeError` | Lists are mutable → not hashable | Common beginner trap; convert to tuple first | — | snippet 8 |
| 21 | Industrial: dedupe, allowlist | `set()` for O(1) checks | Seen-tracker pattern for deduplication | O(n) total vs O(n²) with list `in` | Log/event dedup pipelines | `dedupe_logs` |
| 22 | Industrial: permission comparison | Intersection/difference for RBAC | Compare granted vs required permissions | Core RBAC building block | API authorization middleware | `compare_permissions` |

## Snippets

### 1. Creation — literal, constructor, empty set

Sets are created with braces or `set()`. Remember `{}` makes a dict, not a set.

```python
tags = {"python", "backend", "api"}
from_list = set([1, 2, 2, 3, 3, 3])
empty = set()                        # NOT {} — that's a dict

print(type(tags), tags)
print(from_list)
print(type(empty), len(empty))
```

Expected output:
```text
<class 'set'> {'python', 'backend', 'api'}
{1, 2, 3}
<class 'set'> 0
```

> 💡 `set()` deduplicates automatically — pass any iterable and duplicates vanish.

### 2. Mutation — add, remove, discard, update

Single-element and bulk mutation methods.

```python
s = {1, 2, 3}
s.add(4)                # {1, 2, 3, 4}
s.discard(99)           # no-op — silent
s.remove(2)             # removes 2; KeyError if missing
s.update([5, 6])        # bulk add
s |= {7}               # same as update with a set
print(sorted(s))
```

Expected output:
```text
[1, 3, 4, 5, 6, 7]
```

> 💡 Use `discard()` when absence is not a bug; use `remove()` when absence should crash loudly.

### 3. Set algebra — union, intersection, difference, symmetric difference

The four core set operations, each available as operator and method.

```python
devs = {"alice", "bob", "carol"}
ops  = {"bob", "carol", "dave"}

print("union:     ", devs | ops)
print("intersect: ", devs & ops)
print("dev-only:  ", devs - ops)
print("sym diff:  ", devs ^ ops)
```

Expected output:
```text
union:      {'alice', 'bob', 'carol', 'dave'}
intersect:  {'bob', 'carol'}
dev-only:   {'alice'}
sym diff:   {'alice', 'dave'}
```

> 💡 Operators return new sets; method forms (`.union()`, `.intersection()`) accept any iterable, not just sets.

### 4. Subset, superset, disjoint checks

Containment predicates for access-control logic.

```python
required = {"read", "write"}
granted  = {"read", "write", "admin"}
other    = {"execute"}

print(required <= granted)          # True — subset
print(granted >= required)          # True — superset
print(required.isdisjoint(other))   # True — no overlap
```

Expected output:
```text
True
True
True
```

> 💡 `<=` is the operator form of `.issubset()` — both are idiomatic.

### 5. Membership and iteration

O(1) `in` check and unordered iteration.

```python
allowed = {"png", "jpg", "webp"}
upload = "gif"

if upload not in allowed:
    print(f"Rejected: {upload}")

for ext in sorted(allowed):
    print(ext, end=" ")
print()
```

Expected output:
```text
Rejected: gif
jpg png webp
```

> 💡 Always `sorted()` when you need deterministic output — sets are inherently unordered.

### 6. Set comprehension

Build a set with a transform and optional filter.

```python
words = ["Hello", "hello", "WORLD", "world", "Python"]
unique_lower = {w.lower() for w in words}
print(sorted(unique_lower))
```

Expected output:
```text
['hello', 'python', 'world']
```

> 💡 Set comprehensions automatically deduplicate — great for normalization tasks.

### 7. frozenset — immutable sets and dict keys

`frozenset` is hashable, so it can serve as a dict key or nest inside other sets.

```python
pair_a = frozenset({"read", "write"})
pair_b = frozenset({"write", "read"})  # same contents

print(pair_a == pair_b)            # True
print(hash(pair_a) == hash(pair_b))  # True

combo_map = {pair_a: "standard"}
print(combo_map[pair_b])           # "standard" — same key
```

Expected output:
```text
True
True
standard
```

> 💡 Use `frozenset` when you need a set as a dict key or when you want to guarantee no mutation.

### 8. Anti-pattern: unhashable in set

```python
# ❌ Bad — list is not hashable
try:
    bad = {[1, 2, 3]}
except TypeError as exc:
    print(f"Error: {exc}")

# ✅ Corrected — convert to tuple first
good = {(1, 2, 3)}
print(good)
```

Expected output:
```text
Error: unhashable type: 'list'
{(1, 2, 3)}
```

> Why it's wrong: lists are mutable → not hashable → cannot be set members. Convert to tuples or frozensets.

### 9. Built-in aggregation on sets

`len`, `min`, `max`, `sum` work directly on sets.

```python
scores = {88, 92, 75, 100, 88}   # 88 deduped → {75, 88, 92, 100}
print(f"count={len(scores)}, min={min(scores)}, max={max(scores)}, sum={sum(scores)}")
```

Expected output:
```text
count=4, min=75, max=100, sum=355
```

> 💡 Aggregation on sets gives you unique-value statistics automatically.

## Anti-patterns

### Anti-pattern: using list for membership checks

```python
# ❌ Bad — O(n) per check → O(n²) total
denylist = ["spam", "phish", "malware"]
for msg in messages:
    if msg in denylist:  # linear scan every time
        block(msg)

# ✅ Corrected — O(1) per check → O(n) total
denylist = {"spam", "phish", "malware"}
for msg in messages:
    if msg in denylist:  # hash lookup
        block(msg)
```

> In production, deny/allow lists can have thousands of entries. Using a `set` drops
> membership checks from O(n) to O(1), making the overall loop O(n) instead of O(n²).

### Anti-pattern: mutating a set during iteration

```python
# ❌ Bad — RuntimeError: Set changed size during iteration
s = {1, 2, 3, 4, 5}
for x in s:
    if x % 2 == 0:
        s.remove(x)

# ✅ Corrected — iterate over a copy or build new set
s = {1, 2, 3, 4, 5}
s -= {x for x in s if x % 2 == 0}
print(s)  # {1, 3, 5}
```

> Modifying a set while iterating raises `RuntimeError`. Build a new set with a
> comprehension, or iterate over a snapshot (`set(s)` or `list(s)`).

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| Seen-tracker dedup | `seen = set(); if x not in seen: seen.add(x)` | Stream deduplication, log pipelines |
| Allow/deny-list filter | `if ext in allowed_extensions:` | Upload validation, firewall rules |
| RBAC permission diff | `missing = required - granted` | Authorization middleware |
| Tag/label normalization | `{t.lower().strip() for t in tags}` | Search indexing, ML feature prep |

## Pitfalls

- **`{}` is a dict, not a set** — use `set()` for empty sets.
- **Iteration order is not guaranteed** — don't depend on insertion order (unlike `dict` in 3.7+).
- **Unhashable elements** — only immutable (hashable) objects can be set members; convert lists to tuples first.
- **`pop()` is arbitrary** — do not assume which element will be removed.
- **`remove()` raises `KeyError`** — use `discard()` when absence is acceptable, or guard with `in`.

## Why this design

`code.py` groups functions into creation/mutation demos, a set comprehension builder,
a `frozenset` demo, and two industrial patterns (log dedup and RBAC permission comparison).
Every function validates inputs, uses type hints, and includes inline asserts so the
file is both a reference and a self-test.

## Further reading

- [Real Python — Sets in Python](https://realpython.com/python-sets/) — comprehensive tutorial covering set algebra, frozenset, and practical patterns
- [Python docs — set types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) — official API reference
- [Python docs — frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset) — immutable set reference
- [Real Python — Hashable](https://realpython.com/python-hash-table/) — deep dive on hashability and hash tables
