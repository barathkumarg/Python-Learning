# Day 06 — Dictionaries: Exercises

Welcome to Day 06! Practice using Python dictionaries for mapping, safe access, mutation, and comprehensions.

---

## ex01_basic.py — Dictionary Lookup & Safe Access
Implement `safe_lookup(d: dict, key, default=None)` that returns the value for `key` if present, else `default`.

**Example:**
```python
safe_lookup({"a": 1}, "a")  # 1
safe_lookup({"a": 1}, "b", 0)  # 0
```

---

## ex02_intermediate.py — Add, Update, and Delete
Implement `add_or_update(d: dict, key, value)` to add or update a key-value pair, and `delete_key(d: dict, key)` to remove a key if present.

**Example:**
```python
d = {"x": 1}
add_or_update(d, "y", 2)
# d == {"x": 1, "y": 2}
delete_key(d, "x")
# d == {"y": 2}
```

---

## ex03_advanced.py — Dictionary Comprehensions
Implement `square_values(d: dict[str, int]) -> dict[str, int]` that returns a new dictionary with all values squared.

**Example:**
```python
square_values({"a": 2, "b": 3})  # {"a": 4, "b": 9}
```

---

**Instructions:**
- Write your solutions in the corresponding ex01_basic.py, ex02_intermediate.py, and ex03_advanced.py files.
- Use dictionary features as described.
- Test your code with the provided examples.
