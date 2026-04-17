# Day 04 - Lists and Sorting
> **TL;DR:** Lists are ordered, mutable sequences. The practical flow is: read by index, cut with slices, mutate safely, use list methods intentionally, and then sort with key functions, stable tie-breakers, and top-k selection patterns.
## Concepts
| Concept | What it does | Why it matters | `code.py` ref |
|---------|--------------|----------------|---------------|
| Indexing | Reads one element by position (`items[i]`) | Fast random access (`O(1)`) for targeted updates | `bump_score` |
| Slicing | Copies a range (`items[start:stop]`) | Builds filtered views without mutating source data | `slice_page` |
| Mutation | Replaces values in place | Useful for updates, but requires bounds and value validation | `bump_score` |
| List methods | `append`, `extend`, `remove`, `pop`, `copy` | Makes intent explicit and avoids manual index juggling | `validate_scores` |
| Sorting keys | `sorted(..., key=...)` customizes order | Lets us encode business rules (score desc, name asc) | `sort_leaderboard` |
| Stable sort | Equal keys keep original order | Enables multi-pass tie-breaking without custom comparator code | `sort_leaderboard` |
| Top-k pattern | Sort then slice first `k` elements | Common leaderboard and report requirement | `top_k_players` |
## Snippets
**Indexing** - grab specific elements quickly, but guard boundaries.
```python
players = ["Maya", "Arun", "Lina"]
first = players[0]
last = players[-1]
```
Expected output:
```text
first -> Maya
last -> Lina
```

**Slicing** - produce a view subset without touching the original list.
```python
scores = [91, 88, 77, 95, 84]
recent_three = scores[-3:]
middle_window = scores[1:4]
```
Expected output:
```text
recent_three -> [77, 95, 84]
middle_window -> [88, 77, 95]
```

**Mutation** - replace one item in place after validation.
```python
scores = [91, 88, 77]
player_index = 1
scores[player_index] = 90
```
Expected output:
```text
scores -> [91, 90, 77]
```

**List methods** - append new data and remove old data with clear intent.
```python
events = ["signup", "purchase"]
events.append("refund")
events.remove("signup")
```
Expected output:
```text
events -> ['purchase', 'refund']
```

**Sorting with key functions** - encode domain ordering directly.
```python
players = [("Maya", 88), ("arun", 91), ("lina", 91)]
ordered = sorted(players, key=lambda row: (-row[1], row[0].lower()))
```
Expected output:
```text
ordered -> [('arun', 91), ('lina', 91), ('Maya', 88)]
```

**Stable sort for tie-breakers** - multi-pass sorting stays predictable.
```python
rows = [("Maya", 91, 4), ("Arun", 91, 2), ("Lina", 88, 1)]
by_name = sorted(rows, key=lambda row: row[0].lower())
by_penalty = sorted(by_name, key=lambda row: row[2])
final = sorted(by_penalty, key=lambda row: row[1], reverse=True)
```
Expected output:
```text
final -> [('Arun', 91, 2), ('Maya', 91, 4), ('Lina', 88, 1)]
```

**Top-k pattern** - sort once, then slice what the caller asked for.
```python
rows = [("Maya", 88), ("Arun", 91), ("Lina", 95), ("Ira", 86)]
top_2 = sorted(rows, key=lambda row: row[1], reverse=True)[:2]
```
Expected output:
```text
top_2 -> [('Lina', 95), ('Arun', 91)]
```

**Anti-pattern -> corrected pattern** - avoid accidental in-place mutation.
```python
scores = [88, 91, 77]
bad = scores
bad.sort(reverse=True)  # mutates both references

safe = sorted(scores, reverse=True)  # returns a new list
```
Expected output:
```text
scores after bad.sort -> [91, 88, 77]
safe -> [91, 88, 77]
```

## Pitfalls
- Using `.sort()` when callers expect the original list to remain unchanged.
- Sorting without a tie-breaker key and getting unstable-looking leaderboard output.
- Mutating list positions without checking index bounds first.
- Using repeated `max()` calls for top-k and accidentally introducing `O(k*n)` work.

## Why this design

The reference implementation mirrors the source progression: list access first, then shape control (slices and mutation), then list methods, and finally sorting strategies used in real leaderboard workflows. The examples stay small but carry production habits: typed APIs, explicit validation, and predictable ordering.

## Further reading

- [Real Python - Python Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Python docs - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python docs - `sorted()` built-in](https://docs.python.org/3/library/functions.html#sorted)
