# Day 06 — Dictionaries

> **TL;DR:** Dictionaries map unique, hashable keys to arbitrary values with O(1) average lookup. Day 06 covers creation, CRUD operations, views, comprehensions, merging, nesting, and common industrial patterns like config merge and inverted indexes.

## Concepts

| # | Concept | What it does | `code.py` ref |
|---|---------|-------------|---------------|
| 1 | Literal creation `{"k": v}` | Creates a dict with curly-brace syntax | `build_word_count` |
| 2 | `dict()` constructor | Builds dicts from kwargs, zip, or iterables | snippet |
| 3 | `dict.fromkeys()` | Creates a dict with default values for all keys | snippet |
| 4 | Access `[]` / KeyError | Direct key lookup; raises if missing | `safe_nested_get` |
| 5 | `get()` with default | Returns a fallback instead of raising | `build_word_count` |
| 6 | `setdefault()` | Gets existing or inserts default; great for grouping | `build_inverted_index` |
| 7 | Insert / update `[]` | Assigns a value to a new or existing key | `merge_configs` |
| 8 | `update()` / `\|=` | Merges another mapping into the dict in-place | `merge_configs` |
| 9 | Merge `\|` | Creates a new dict from two dicts (3.9+) | `merge_configs` |
| 10 | `del` | Removes a key-value pair by key | snippet |
| 11 | `pop()` / `popitem()` | Removes and returns value by key / last pair | snippet |
| 12 | `clear()` | Removes all items from a dict | snippet |
| 13 | `.keys()` / `.values()` / `.items()` | Returns live view objects for iteration | `build_word_count` |
| 14 | Dict comprehension | `{k: f(v) for k, v in items}` | `build_inverted_index` |
| 15 | `in` membership | O(1) average key lookup | `merge_configs` |
| 16 | Nested dict access | `d["a"]["b"]`, chained `.get()` | `safe_nested_get` |
| 17 | `copy()` vs `deepcopy` | Shallow copy shares nested objects | snippet |
| 18 | Dict unpacking `**` | `{**d1, **d2}` merges into new dict | `merge_configs` |
| 19 | Insertion-order guarantee | Python 3.7+ preserves insertion order | snippet |
| 20 | Hashability rules | Keys must be immutable (str, int, tuple) | snippet |
| 21 | `KeyError` handling | `try/except KeyError` vs `get()` | snippet (anti-pattern) |
| 22 | `defaultdict` preview | Auto-creates missing keys with a factory | snippet |
| 23 | Anti-pattern: bare `[]` access | Use `get()` or `in` check to avoid crashes | snippet (anti-pattern) |
| 24 | Industrial: config merge, inverted index | `setdefault` / `\|` patterns for real tasks | `merge_configs`, `build_inverted_index` |

## Snippets

**Literal creation** — curly braces are the most common way to create a dict.
```python
config = {"host": "localhost", "port": 8080, "debug": True}
print(config["host"])
```
Expected output:
```text
localhost
```
> Keys and values are separated by `:` inside `{}`.

**`dict()` constructor** — build from keyword arguments or `zip()`.
```python
from_kwargs = dict(host="localhost", port=8080)
keys = ["a", "b", "c"]
values = [1, 2, 3]
from_zip = dict(zip(keys, values))
print(from_kwargs)
print(from_zip)
```
Expected output:
```text
{'host': 'localhost', 'port': 8080}
{'a': 1, 'b': 2, 'c': 3}
```
> `dict(zip(k, v))` is handy when keys and values live in separate lists.

**`dict.fromkeys()`** — initialize many keys to the same default.
```python
statuses = dict.fromkeys(["pending", "active", "closed"], 0)
print(statuses)
```
Expected output:
```text
{'pending': 0, 'active': 0, 'closed': 0}
```
> Useful for counters or flag initialization.

**`get()` with default and `setdefault()`** — safe access and group-building.
```python
d = {"apple": 3}
print(d.get("banana", 0))

groups: dict[str, list[str]] = {}
groups.setdefault("fruit", []).append("apple")
groups.setdefault("fruit", []).append("banana")
print(groups)
```
Expected output:
```text
0
{'fruit': ['apple', 'banana']}
```
> `setdefault` avoids an `if key not in d` check before appending.

**Merge `|` and `update()`** — combine two dicts (right side wins on collisions).
```python
defaults = {"color": "green", "width": 80}
overrides = {"color": "red", "height": 24}

merged = defaults | overrides          # new dict (3.9+)
print(merged)

defaults.update(overrides)             # in-place
print(defaults)
```
Expected output:
```text
{'color': 'red', 'width': 80, 'height': 24}
{'color': 'red', 'width': 80, 'height': 24}
```
> Use `|` when you want a new dict; use `update()` or `|=` for in-place mutation.

**`del`, `pop()`, `popitem()`, `clear()`** — removal operations.
```python
d = {"a": 1, "b": 2, "c": 3}
del d["a"]
val = d.pop("b", -1)
last = d.popitem()
print(val, last, d)
d.clear()
print(d)
```
Expected output:
```text
2 ('c', 3) {}
{}
```
> `pop()` returns the removed value; `popitem()` returns the last (key, value) pair.

**Dict comprehension** — transform or filter in one expression.
```python
prices = {"apple": 1.20, "banana": 0.50, "cherry": 2.80}
expensive = {k: v for k, v in prices.items() if v > 1.0}
print(expensive)
```
Expected output:
```text
{'apple': 1.2, 'cherry': 2.8}
```
> Comprehensions are concise and faster than manual loop + append.

**`copy()` vs `deepcopy`** — shallow copies share nested objects.
```python
from copy import deepcopy

original = {"tags": ["python", "dict"]}
shallow = original.copy()
deep = deepcopy(original)

shallow["tags"].append("shallow")
print(original["tags"])   # mutated!
print(deep["tags"])       # safe
```
Expected output:
```text
['python', 'dict', 'shallow']
['python', 'dict']
```
> Use `deepcopy` when nested mutables must stay independent.

**Anti-pattern → corrected: bare `[]` access** — crashes on missing keys.
```python
# BAD: d["missing_key"]  → KeyError

# GOOD: use get() or check membership
d = {"host": "localhost"}
port = d.get("port", 3000)         # safe fallback
if "port" in d:                     # explicit check
    print(d["port"])
print(port)
```
Expected output:
```text
3000
```
> Prefer `get()` for simple defaults; use `try/except KeyError` when the missing case needs special handling.

## Pitfalls

- Using `[]` access without checking if the key exists — prefer `get()` or `in`.
- Mutating a dict while iterating over it — build a new dict or iterate over a snapshot (`list(d.items())`).
- Using mutable objects (lists, dicts) as keys — only hashable (immutable) objects are allowed.
- Assuming `dict.fromkeys(keys, [])` gives independent lists — all values share the same list object.
- Forgetting that `copy()` is shallow — nested mutables are still shared.

## Why this design

The reference code mirrors the Real Python source progression: creation → access → CRUD → views → comprehensions → operators → iteration → advanced classes. Functions cover realistic tasks — word counting, config merging, inverted indexes, and safe nested access — so the patterns transfer directly to production code.

## Further reading

- [Real Python — Dictionaries in Python](https://realpython.com/python-dicts/) — primary reference for creation, methods, operators, and iteration
- [Python docs — dict](https://docs.python.org/3/library/stdtypes.html#dict) — official API reference for all dict methods
- [Python docs — collections](https://docs.python.org/3/library/collections.html) — `defaultdict`, `Counter`, `OrderedDict`
- [Real Python — Dictionary Comprehensions](https://realpython.com/python-dictionary-comprehension/) — deep dive on dict comprehension patterns
