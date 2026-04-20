# Day 05 Exercises — Tuples & NamedTuple

## Learning objectives
- Use tuples as immutable sequences for grouping and returning multiple values.
- Apply sequence operations (indexing, slicing, unpacking) to tuples.
- Use NamedTuple for structured, self-documenting records.
- Practice type hints and API clarity with tuple-based data.

## Skills assessed
| Skill ID | Skill | Exercise mapping |
|----------|-------|------------------|
| PY-03 | Input validation & error handling | ex01, ex02, ex03 |
| PY-06 | Data structures (tuple, NamedTuple) | ex01, ex02, ex03 |
| PY-16 | Type hints & API clarity | ex01, ex02, ex03 |

## Exercise specs

### ex01_basic.py — Tuple Basics
Must-pass:
- Implement `first_and_last(nums: tuple[int, ...]) -> tuple[int, int]`.
- Return a tuple with the first and last elements of `nums`.
- Raise `ValueError` if `nums` is empty.

Stretch:
- Support any sequence type (list, tuple) as input.

Failure modes:
- Do not mutate the input.
- Do not print instead of returning.

**Example:**
```python
first_and_last((10, 20, 30, 40))  # (10, 40)
```

---

### ex02_intermediate.py — Tuple Unpacking & Multiple Returns
Must-pass:
- Implement `min_and_max(nums: tuple[int, ...]) -> tuple[int, int]`.
- Return a tuple `(min, max)` from `nums`.
- Demonstrate tuple unpacking in your test/asserts.
- Raise `ValueError` if `nums` is empty.

Stretch:
- Accept any sequence type (list, tuple) as input.

Failure modes:
- Do not mutate the input.
- Do not print instead of returning.

**Example:**
```python
lo, hi = min_and_max((5, 2, 9, 1))
# lo == 1, hi == 9
```

---

### ex03_advanced.py — NamedTuple for Records
Must-pass:
- Define a NamedTuple `Book` with fields `title: str` and `pages: int`.
- Implement `shortest_book(books: tuple[Book, ...]) -> Book`.
- Return the book with the fewest pages.
- Raise `ValueError` if `books` is empty.

Stretch:
- Support any sequence of Book (list, tuple).
- Return all books tied for fewest pages.

Failure modes:
- Do not mutate the input.
- Do not print instead of returning.

**Example:**
```python
from typing import NamedTuple
class Book(NamedTuple):
    title: str
    pages: int
books = (
    Book("Python 101", 250),
    Book("Deep Dive", 180),
    Book("Quick Start", 200),
)
result = shortest_book(books)
# result.title == "Deep Dive"
```

---

## Scoring (per file, 0-100)
| Criterion | Points |
|-----------|--------|
| All must-pass behaviors implemented | 40 |
| Stretch behaviors (partial credit ok) | 15 |
| Inline asserts + AI-verified coverage | 25 |
| Style — types, ruff, docstrings | 20 |
| **Total** | **100** |

---

**Instructions:**
- Write your solutions in the corresponding ex01_basic.py, ex02_intermediate.py, and ex03_advanced.py files.
- Use tuple and NamedTuple features as described.
- Test your code with the provided examples.
