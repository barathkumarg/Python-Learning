# CODE.md Template (Golden Reference)

Every `src/<track>/day_NN_topic/CODE.md` (or `src/dsa/week_WW_topic/CODE.md`) **must** follow this structure. Target: **≤80 lines** per day.

---

## Template

```markdown
# Day [NN] — [Topic]

> **TL;DR:** [2–3 sentence summary: what this topic is, why it matters in production, what code.py demonstrates.]

## Concepts

| Concept | What it does | Why it matters | `code.py` ref |
|---------|-------------|----------------|---------------|
| `concept_1` | One-line explanation | One-line production relevance | `line NN` or function name |
| `concept_2` | … | … | … |

## Visual / Diagram *(required for DSA; optional for Python days)*

<!-- ASCII art, Mermaid diagram, or table showing the data structure / algorithm flow -->

## Pitfalls

- Pitfall 1 — why it's dangerous and what to do instead.
- Pitfall 2 — …
- Pitfall 3 — …

## Why this design

[2–3 lines: why code.py uses this approach — testability, reuse, explicit errors, etc.]

## Further reading

- [Link 1](url) — one-line description
- [Link 2](url) — one-line description
```

---

## DSA diagram style guide

Use the right visual for each DSA topic so the concept is graspable at a glance:

| DSA Topic | Recommended Visual | Example |
|-----------|--------------------|---------|
| Arrays / Hashing | Index-pointer ASCII with `^` markers | `[3, 7, 1, 9]`  `L→        ←R` |
| Two Pointers | Left/right arrow markers on array | `[1, 2, 3, 4, 5]`  `^L      ^R` |
| Sliding Window | Bracketed window on array | `[1, [3, 2, 1], 4, 5]  window=3` |
| Stack | Vertical push/pop ASCII | `| 3 | ← top`  `| 1 |`  `+---+` |
| Linked List | Node-arrow ASCII | `[1] → [2] → [3] → None` |
| Trees / BST | Mermaid `graph TD` or indented ASCII | `graph TD; A-->B; A-->C;` |
| Graphs (BFS/DFS) | Mermaid `graph LR` with visit order annotations | numbered visit order on edges |
| Heap | Array + tree dual view | array indices mapped to tree levels |
| DP (1D) | Single-row table with fill direction arrow | `dp: [0, 1, 1, 2, 3, →]` |
| DP (2D) | Grid table with fill direction arrows | `↓→` corner-to-corner grid |
| Trie | Indented prefix tree ASCII | `root → t → r → i → e` |
| Union-Find | Parent-pointer forest ASCII | `{1←2, 1←3, 4←5}` |
| Binary Search | Midpoint narrowing on sorted array | `[lo ... mid ... hi]` per iteration |
| Backtracking | Decision tree (Mermaid or ASCII) | branch + prune markers |
| Greedy / Intervals | Timeline ASCII with interval bars | `|---| |--|  |-----|` |

---

## Filled example — Day 01

```markdown
# Day 01 — Syntax, Types & Variables

> **TL;DR:** Variables, type hints, f-strings, and input validation are where production reliability starts. `code.py` shows small typed utility functions that validate inputs and return predictable outputs — the same style used in APIs, CLIs, and data pipelines.

## Concepts

| Concept | What it does | Why it matters | `code.py` ref |
|---------|-------------|----------------|---------------|
| `strip()` | Removes leading/trailing whitespace from strings | Prevents blank-input bugs in user-facing flows | `build_welcome_message` |
| `ValueError` | Exception for values that exist but violate rules | Explicit errors > silent fallbacks; easier debugging | all validation functions |
| `int()` | Converts a value to integer | Parsing CLI/env input safely | `parse_retry_count` |
| `round()` | Rounds float to N decimal places | Clean currency/metric output | `calculate_invoice_total` |
| `Final` | Typing hint marking a constant | Signals "don't reassign" to readers and static tools | module-level constants |
| f-string | Inline variable interpolation in strings | Readable log/output formatting without concatenation | all functions |
| Type hints | Annotate parameter and return types | Self-documenting signatures; enables mypy checks | all function signatures |

## Pitfalls

- Mixing string and number operations without conversion — causes `TypeError` at runtime.
- Using unclear names (`x`, `temp`) in business logic — kills code review speed.
- Catching all exceptions silently (`except: pass`) — hides bugs.
- Printing instead of returning from reusable functions — untestable code.

## Why this design

Pure functions with explicit return values and typed signatures. Easy to test, reuse across API handlers, CLI tools, and pipelines. Validation raises immediately rather than returning sentinel values.

## Further reading

- [Python Type Hints Cheat Sheet (mypy)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) — quick reference for annotations
- [PEP 498 — f-strings](https://peps.python.org/pep-0498/) — the spec behind formatted string literals
```
