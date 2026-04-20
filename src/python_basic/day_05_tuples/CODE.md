# Day 05 — Tuples, Sequences, and NamedTuple


## TL;DR

Tuples are immutable, ordered collections and are a type of sequence in Python. They support all standard sequence operations (indexing, slicing, iteration, length, membership tests, etc.). Tuples are used for grouping related data, returning multiple values from functions, and as lightweight records. `NamedTuple` extends tuples with named fields for better readability, type safety, and self-documenting code.

---

## Concepts Table

| Concept                | Example/Notes                                  |
|------------------------|------------------------------------------------|
| Tuple creation         | `t = (1, 2, 3)`                                |
| Immutability           | Cannot change elements after creation           |
| Packing/Unpacking      | `a, b = (1, 2)`                                |
| Multiple returns       | `def f(): return 1, 2`                         |
| NamedTuple             | `from typing import NamedTuple`                |
| DTO-style records      | Use NamedTuple for structured, typed records    |
| Sequence operations    | `t[0]`, `t[1:3]`, `len(t)`, `for x in t`       |

---

## Key Snippets


### 1. Creating and Accessing Tuples as Sequences
```python
t = (1, 2, 3, 4)
print(t[0])      # Indexing
print(t[1:3])   # Slicing
print(len(t))   # Length
for x in t:
    print(x)    # Iteration
# Expected output:
# 1
# (2, 3)
# 4
# 1\n2\n3\n4
```
### 1b. Sequence Operations Supported by Tuples
```python
nums = (10, 20, 30, 40)
print(30 in nums)      # Membership test
print(nums.count(20))  # Count occurrences
print(nums.index(40))  # Find index
# Expected output:
# True
# 1
# 3
```

### 2. Tuple Immutability
```python
t = (1, 2, 3)
try:
    t[0] = 10
except TypeError as e:
    print(e)
# Expected output:
# 'tuple' object does not support item assignment
```

### 3. Packing and Unpacking
```python
a, b, c = (1, 2, 3)
print(a, b, c)
# Expected output:
# 1 2 3
```

### 4. Multiple Return Values
```python
def min_max(nums):
    return min(nums), max(nums)
lo, hi = min_max([2, 8, 5])
print(lo, hi)
# Expected output:
# 2 8
```


### 5. Using NamedTuple for Records (and Sequence Behavior)
```python
from typing import NamedTuple
class Point(NamedTuple):
    x: int
    y: int
p = Point(3, 4)
print(p.x, p.y)      # Named access
print(p[0], p[1])    # Sequence access
print(len(p))        # Sequence length
for value in p:
    print(value)     # Iteration
# Expected output:
# 3 4
# 3 4
# 2
# 3\n4
```

#### Why NamedTuple?
- NamedTuple provides both tuple (sequence) behavior and named fields.
- Improves code clarity, type checking, and IDE support.
- Fields are immutable, just like regular tuples.

### 6. Anti-pattern: Using Tuple for Unclear Data
```python
def get_user():
    return ("alice", 30)
user = get_user()
# What is user[0]? What is user[1]?
```
#### Corrected: Use NamedTuple for Clarity
```python
from typing import NamedTuple
class User(NamedTuple):
    name: str
    age: int
def get_user() -> User:
    return User("alice", 30)
user = get_user()
print(user.name, user.age)
# Expected output:
# alice 30 
```

---


## Pitfalls
- Tuples are immutable, but can contain mutable objects (e.g., lists inside tuples).
- Overusing plain tuples can reduce code clarity—prefer NamedTuple for structured data.
- Remember: Tuples and NamedTuples are both sequences, but NamedTuple adds field names and type hints.

---


## Why This Design?
- Tuples are lightweight, fast, and support all sequence operations.
- NamedTuple improves readability, type safety, and supports both sequence and attribute access.
- Multiple return values make APIs more ergonomic.

---


## Further Reading
- [Real Python — Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Python Docs — Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Docs — typing.NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)
