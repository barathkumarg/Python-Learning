# CODE.md Template (Golden Reference)

Every `src/<track>/day_NN_topic/CODE.md` (or `src/dsa/week_WW_topic/CODE.md`) **must** follow this structure. Target: **80–120 lines** per day.

---

## Source-aligned teaching flow (required when a study source is named)

When `README.md` or `DAILY_STUDY_PLAN.md` points to a specific tutorial source, mirror that source's **learning progression** in your own words.

- Use the cited source as the teaching arc, not as copy-paste material.
- Paraphrase concepts and build fresh examples; do **not** copy proprietary text or long examples verbatim.
- Cover fundamentals before advanced production patterns. Do not jump straight to edge-case API design if the day is an introductory topic.
- Keep repo-specific production notes, but layer them **after** the learner has seen the base concept.

Recommended progression for Python basics:
- What the feature is and why it exists
- Small base example
- How it is called or used
- Return values / outputs
- Common optional features
- Pitfalls and readability guidance
- One small real-world example

Day 03+ output clarity rule:
- For each concept snippet: include short textual explanation, a compact code example, and expected output (or expected error).

Recommended progression for Day 03 Functions when following the Real Python source:
- Why functions help
- `def` and basic calls
- Parameters vs arguments
- Return values
- Default arguments
- `*args`
- `**kwargs`
- Unpacking with `*` / `**`
- Small, readable `lambda` use

---

## Professional training mode (required)

Treat CODE.md as a **code-first training handout**:

- Cover all core concepts for the day topic (from README + DAILY_STUDY_PLAN row), not just one slice.
- Keep prose tight: 1-2 lines per concept explanation, 1 line takeaway per snippet.
- Prefer examples over text: include enough snippets to show base case, edge case, and common pitfall.
- If a named source exists for the day, order snippets to match that source's progression before adding project-specific patterns.
- Snippet density target:
  - Python day: **6-9 snippets**
  - DSA week: **5-8 snippets** + required visual section
- Snippet quality target:
  - Small (3-10 lines), runnable-looking, typed where relevant
  - Include expected output text for each snippet (or expected exception behavior)
  - At least one anti-pattern -> corrected pattern snippet
  - At least one input-validation/error-path snippet
- Every concept in the table should map to either `code.py` reference code or an explicit snippet in CODE.md.

---

## DSA-specific must-haves

For `src/dsa/week_WW_*/CODE.md`, these are mandatory:

- Include a short **Big-O in practice** explanation. Week 01 must explicitly answer: what Big-O notation measures and why we use it before implementation.
- Use a concepts table that includes **Time / Space** complexity for every discussed operation/problem.
- For each DSA snippet, include explicit complexity notes (`Time: ...`, `Space: ...`) in either the snippet explanation or takeaway line.
- For each DSA snippet/example, include a **Traversal (graphical)** block right after expected output (ASCII step trace preferred; Mermaid optional).
- Add visuals that cover the main algorithm flow (use one or more diagrams so each core algorithm/topic in the week is represented).
- Cover every subtopic explicitly listed in that week's row in `DAILY_STUDY_PLAN.md` (including advanced tags such as Kadane, 3Sum dedupe, recursion processed/unprocessed state, interval patterns, string operations, substring/consecutive-string patterns, Rabin-Karp, KMP `k-map`, sorting algorithms, matrix traversal, and math basics).

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

For DSA weeks, use this concepts table variant:

| Concept | What it does | Why it matters | Time / Space | `code.py` ref |
|---------|--------------|----------------|--------------|---------------|
| `concept_1` | One-line explanation | One-line production relevance | `O(?) / O(?)` | function name |
| `concept_2` | … | … | … | … |

## Big-O in Practice *(required for DSA Week 01; recommended for all DSA weeks)*

- What Big-O measures (growth with input size, not wall-clock on one machine)
- Why we use it (choose scalable approach before coding)
- One concrete tradeoff example for this week's topic (e.g., nested loops vs hash lookup)

## Snippets

Pick key concepts from the table above. For each, show a **short** (3–10 line) code block + a 1-line explanation. Pull from `code.py` or write a minimal standalone example.
After each code block, include expected output in a plain-text block.

Python days: **6–9 snippets**.  
DSA weeks: **5–8 snippets** (plus visual section).

**`concept_name`** — one-line what + why.
```python
# minimal focused example (3–10 lines max)
```
Expected output:
```text
# concrete output line(s) for the snippet
```
> One-line takeaway or gotcha.
> DSA complexity note: `Time O(?)`, `Space O(?)`.
Traversal (graphical):
```text
# step-by-step state transition for this snippet
```

## Visual / Diagram *(required for DSA; optional for Python days)*

<!-- ASCII art, Mermaid diagram, or table showing the data structure / algorithm flow -->

For DSA, optional GIF support (when useful):
- You may embed one GIF to show dynamic behavior (pointer movement, window shift, traversal order).
- Still include ASCII or Mermaid fallback so the file remains readable in plain markdown viewers.
- Add a one-line caption: what to observe in the animation.
- Prefer repo-local assets when available (for example, `docs/assets/dsa_gifs/...`), otherwise use a stable source URL.

## Pitfalls

- Pitfall 1 — why it's dangerous and what to do instead.
- Pitfall 2 — …
- Pitfall 3 — …

## Why this design

[2–3 lines: why code.py uses this approach — testability, reuse, explicit errors, etc.]

## Further reading

- [Link 1](url) — one-line description
- [Link 2](url) — one-line description
- [Link 3](url) — one-line advanced/deeper reference
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
| Any dynamic pointer/traversal flow | Optional GIF (+ required fallback) | GIF for intuition, plus ASCII/Mermaid retained in file |

---

## Filled example — Day 01 (abridged)

Note: this sample is shortened for readability. Real day files must satisfy the snippet-density rules above.

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

## Snippets

**`strip()` + validation** — clean user input before any logic touches it.
```python
cleaned = user_name.strip()
if not cleaned:
    raise ValueError("user_name must not be empty")
```
> Always strip first, then validate. Skipping this lets `"   "` pass as valid.

**`int()` with safe conversion** — parse string input without crashing.
```python
try:
    count = int(raw_value)
except ValueError as exc:
    raise ValueError("must be an integer") from exc
```
> Chain with `from exc` so the original traceback isn't lost during debugging.

**`Final` constant** — mark values that should never be reassigned.
```python
from typing import Final
MAX_RETRY: Final[int] = 3
```
> `Final` is a hint, not enforced at runtime. `mypy` catches reassignment.

**f-string formatting** — embed variables directly, no concatenation.
```python
return f"app={APP_NAME} env={env} debug={debug}"
```
> Prefer f-strings over `.format()` or `%` — shorter, faster, and easier to read.

**Type hints** — document what goes in and what comes out.
```python
def parse_retry_count(raw_value: str) -> int:
```
> Types make function signatures self-documenting. Pair with `mypy` for static checking.

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
