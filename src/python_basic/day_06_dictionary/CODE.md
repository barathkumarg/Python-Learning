# Day 06 — Dictionaries: CODE.md

## Overview
Dictionaries are Python’s built-in mapping type, allowing you to associate keys with values. They are mutable, unordered (as of Python 3.6+ insertion-ordered), and support fast lookups, insertions, and deletions.

---

## Key Concepts

| Concept                | Example/Notes                                  |
|------------------------|------------------------------------------------|
| Dictionary creation    | `d = {"a": 1, "b": 2}`                        |
| Access by key          | `d["a"]`                                       |
| Insert/update          | `d["c"] = 3`                                   |
| Delete by key          | `del d["b"]`                                   |
| Membership test        | `'a' in d`                                      |
| Iteration              | `for k, v in d.items()`                         |
| Default values         | `d.get("x", 0)`                                |
| Dict comprehensions    | `{k: v*v for k, v in d.items()}`                |

---

## Examples

### 1. Creating and Accessing Dictionaries
```python
d = {"name": "Alice", "age": 30}
print(d["name"])
# Output: Alice
```

### 2. Adding, Updating, and Deleting
```python
d = {"a": 1}
d["b"] = 2
print(d)  # {'a': 1, 'b': 2}
d["a"] = 10
print(d)  # {'a': 10, 'b': 2}
del d["b"]
print(d)  # {'a': 10}
```

### 3. Membership and Safe Access
```python
d = {"x": 42}
print("x" in d)         # True
print(d.get("y", 0))   # 0
```

### 4. Iterating and Comprehensions
```python
d = {"a": 2, "b": 3}
for k, v in d.items():
    print(k, v)
# Output:
# a 2
# b 3
squares = {k: v*v for k, v in d.items()}
print(squares)  # {'a': 4, 'b': 9}
```

---

## Pitfalls
- Keys must be hashable (immutable types like str, int, tuple).
- Accessing a missing key with `d[key]` raises KeyError; use `get()` for safe access.
- Dictionaries do not allow duplicate keys; later assignments overwrite earlier ones.

---

## Further Reading
- [Python Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Real Python — Dictionaries 101](https://realpython.com/python-dicts/)
