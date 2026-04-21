# Prompt Templates — Copy-Paste Playbook

> **Required files:** `.agent.md` (generation rules) · `docs/RUBRIC.md` (scoring & evaluation).
> **Look up first:** `study_plan/<track>.md` → day/week, slug, subtopics, **A-Z Concept Checklist**, primary source URL.

---

## Generate a Python day

```
@.agent.md @docs/RUBRIC.md @study_plan/<track>.md @docs/SOURCE_REGISTRY.md

Generate Day [NN] — [topic] (<track>, day_XX_<slug>).
Primary source: [URL from study_plan/<track>.md].

CRITICAL — A-Z Coverage:
1. Look up the A-Z Concept Checklist for this day in study_plan/<track>.md.
2. Every checklist concept MUST appear in the CODE.md Concepts table AND at least
   one of: snippet, code.py function, or exercise stub.
3. Open each Source Section link from the checklist before writing that concept's content.

Follow the CODE.md Structure Template, code.py Structure Template,
and Exercise Structure Template from this file.
Create 5 files per .agent.md §3.
Pass gates G1–G8. End with file list + self-check commands.
```

---

## Generate a DSA week

```
@.agent.md @docs/RUBRIC.md @study_plan/<track>.md @docs/SOURCE_REGISTRY.md

Generate DSA Week [WW] — [topic] (dsa, week_WW_<slug>).
Primary source: [URL]. LeetCode: [URLs from SOURCE_REGISTRY.md].

CRITICAL — A-Z Coverage:
1. Look up the A-Z Concept Checklist for this week in study_plan/<track>.md.
2. Every checklist concept MUST appear in the CODE.md Concepts table AND at least
   one of: visual/diagram, code.py function, or exercise stub.
3. Open each Source Section link from the checklist before writing that concept's content.

Follow the CODE.md Structure Template (DSA variant), code.py Structure Template,
and Exercise Structure Template from this file.
Create 5 files per .agent.md §3 + §4 (DSA extras).
Include Visual/Diagram section, traversal blocks, Big-O section.
Pass gates G1–G8. End with file list + self-check commands.
```

---

## Generate only CODE (study first)

```
@.agent.md @study_plan/<track>.md @docs/SOURCE_REGISTRY.md

Generate ONLY src/<track>/day_XX_<slug>/CODE.md + code.py.
Day [NN] — [topic]. Primary source: [URL].

CRITICAL: Cover ALL items from the A-Z Concept Checklist for this day.
Follow the CODE.md Structure Template and code.py Structure Template.
Mirror source order. Do NOT create exercise files.
```

---

## Generate only exercises

```
@.agent.md @docs/RUBRIC.md @study_plan/<track>.md @docs/SOURCE_REGISTRY.md

Generate ONLY exercise/<track>/day_XX_<slug>/ (EXERCISE.md + ex01–ex03).
Day [NN] — [topic]. Do NOT create CODE.md or code.py.

CRITICAL: Cover ALL items from the A-Z Concept Checklist for this day.
Follow the Exercise Structure Template. Map exercises to checklist concept ranges.
```

---

## Evaluate your solution

```
@.agent.md @docs/RUBRIC.md

Grade Day [NN] at exercise/<track>/day_XX_<slug>/.
Follow docs/RUBRIC.md §4 evaluation protocol exactly.
Include G8 (concept completeness) in the gate table.
```

---

## Batch generation

```
@.agent.md @docs/RUBRIC.md @study_plan/<track>.md @docs/SOURCE_REGISTRY.md

Generate these days as a batch (5 files each, per .agent.md §3):
- Day [NN] — [topic] (<track>, day_XX_<slug>) — Source: [URL]
- Day [NN+1] — [topic] (<track>, day_XX_<slug>) — Source: [URL]

CRITICAL: For each day, cover ALL A-Z Concept Checklist items.
Follow all Structure Templates. Validate G1–G8 per day.
End with combined self-check commands.
```

---

## Rework (after evaluation fails)

```
@.agent.md @docs/RUBRIC.md

Fix these issues from Day [NN] evaluation:
1. [paste issue]
2. [paste issue]
Files: exercise/<track>/day_XX_<slug>/exNN_*.py
Fix only listed issues. Maintain G1–G8. Re-run ruff + asserts.
```

---

## CODE.md Structure Template

> Every generated `CODE.md` MUST follow this structure. The Concepts table must have **one row per A-Z Checklist item** from `study_plan/<track>.md`.

### Required sections (in order):

```markdown
# Day [NN] — [Topic]

> **TL;DR:** 2–3 sentence overview. What does this topic do? Why does it matter
> in production Python? What style does `code.py` demonstrate?

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|-------------|----------------|---------------|---------------|
| 1 | [from checklist] | `code` | explanation | rationale | real-world use case | function name |
| 2 | ... | ... | ... | ... | ... | ... |
(One row per A-Z checklist item — no concept left uncovered)

## Snippets

(One snippet per major concept group. Minimum 8 for Python days, 6 for DSA weeks.)

### N. [Concept Group Name]

[Brief context sentence.]

```python
# Actual code snippet (3–15 lines)
```

Expected output:
```text
...
```

> 💡 One-line insight or warning callout.

(Repeat for each concept group)

## Anti-patterns

(Minimum 2 anti-pattern → corrected pairs per day)

### Anti-pattern: [Name]
```python
# ❌ Bad
...

# ✅ Corrected
...
```
> Why it's wrong and what breaks in production.

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| [pattern name] | `code snippet` | scenario description |
(2–4 rows of real-world patterns using this topic)

## Pitfalls

- Pitfall 1 — what happens and how to avoid it.
- Pitfall 2 — ...
(3–5 common mistakes)

## Why this design

1–2 sentences: why `code.py` uses this particular function design, typing, and
validation style.

## Further reading

- [Official docs link](url) — one-line description
- [Real Python / PEP link](url) — one-line description
- [Additional reference](url) — one-line description
(3–5 links from SOURCE_REGISTRY.md)
```

### DSA CODE.md additions

DSA `CODE.md` files include all sections above PLUS:

```markdown
## Visuals

(ASCII/Mermaid step-by-step diagrams for each core algorithm. Minimum 2 per week.)

### Visual: [Algorithm Name]
```text
Step 1: [state]
Step 2: [state]
...
```

## Complexity Summary

| Problem / Pattern | Time | Space | Notes |
|-------------------|------|-------|-------|
| [name] | O(?) | O(?) | [note] |
(One row per major pattern in this week)
```

---

## code.py Structure Template

> Every generated `code.py` MUST follow this structure. There must be **at least one function per major concept group** from the A-Z Checklist.

### Required structure:

```python
# code.py — Day [NN]: [Topic]

"""
[Topic] — production-style reference implementations.

Covers: [list key concepts from A-Z checklist].
Style: typed signatures, Google docstrings, explicit validation, inline asserts.
"""

from __future__ import annotations
# (imports as needed — typing, collections, etc.)


# ─── Section 1: [Concept Group — e.g., Creation & Access] ───

def function_name(param: Type, ...) -> ReturnType:
    """One-line summary.

    Args:
        param: Description.

    Returns:
        Description of return value.

    Raises:
        ValueError: When input violates rules.

    Examples:
        >>> function_name(sample_input)
        expected_output
    """
    # Input validation
    if not valid:
        raise ValueError(f"descriptive message, got {param!r}")
    # Implementation
    return result


# ─── Section 2: [Next Concept Group] ───

# ... (one function per concept group, 8–12 functions total for Python days)


# ─── Industrial Patterns ───

def industrial_pattern_1(...) -> ...:
    """Real-world usage pattern (e.g., config merge, inverted index)."""
    ...

def industrial_pattern_2(...) -> ...:
    """Another real-world pattern."""
    ...


# ─── Self-checks ───

if __name__ == "__main__":
    # One assert block per function above
    assert function_name(input) == expected, "description"
    # ... (cover every function)
    print("code.py: all asserts passed ✓")
```

### Required quality bars:

- **Type hints** on ALL function signatures (params + return)
- **Google-style docstrings** on ALL public functions (Args/Returns/Raises/Examples)
- **Input validation** with descriptive `ValueError` messages on ALL functions
- **8–12 functions minimum** for Python days, **6–10 for DSA weeks**
- **2–3 industrial pattern functions** showing real-world usage
- **Complete assert coverage** in `__main__` — every function tested
- **`from __future__ import annotations`** for modern type hint syntax

---

## Exercise Structure Template

> Every generated exercise set MUST follow this structure. Exercises must collectively cover ALL A-Z Checklist concepts.

### EXERCISE.md structure:

```markdown
# Day [NN] — [Topic]: Exercises

## Learning objectives

After completing these exercises you will be able to:
1. [objective mapped to checklist concepts 1–N]
2. [objective mapped to checklist concepts N+1–M]
3. [objective mapped to remaining concepts]

## Skills assessed

| Skill ID | Skill | Exercise | Proficiency target |
|----------|-------|----------|-------------------|
| PY-XX | [from RUBRIC.md §1] | ex01/ex02/ex03 | developing/proficient |
(Map to RUBRIC.md skill IDs)

## Concept coverage map

| Checklist # | Concept | Covered in |
|-------------|---------|------------|
| 1 | [concept] | ex01 — function_name |
| 2 | [concept] | ex01 — function_name |
| ... | ... | ... |
(Every A-Z checklist item must appear here)

---

## ex01_basic.py — [Title] (Checklist items #1–#N)

**Must-pass behaviors:**
- [behavior 1]
- [behavior 2]

**Stretch behaviors:**
- [optional harder behavior]

### Functions to implement:
1. `func_a(...)` — [one-line description]
2. `func_b(...)` — [one-line description]
(4–6 functions covering basic concepts)

---

## ex02_intermediate.py — [Title] (Checklist items #N+1–#M)

**Must-pass behaviors:**
- [behavior 1]
- [behavior 2]

**Stretch behaviors:**
- [optional harder behavior]

### Functions to implement:
1. `func_c(...)` — [one-line description]
2. `func_d(...)` — [one-line description]
(4–6 functions covering intermediate concepts)

---

## ex03_advanced.py — [Title] (Checklist items #M+1–end + industrial)

**Must-pass behaviors:**
- [behavior 1]
- [behavior 2]

**Stretch behaviors:**
- [optional harder behavior]

### Functions to implement:
1. `func_e(...)` — [one-line description]
2. `func_f(...)` — [one-line description]
(3–4 functions covering advanced + industrial concepts)

---

## Failure modes to watch for
- [common mistake 1]
- [common mistake 2]

## Scoring

| Criterion | Max | ex01 | ex02 | ex03 |
|-----------|-----|------|------|------|
| Must-pass behaviors | 40 | | | |
| Stretch behaviors | 15 | | | |
| Inline asserts + AI-verified | 25 | | | |
| Style (types, ruff, docstrings) | 20 | | | |
| **Total** | **100** | | | |

## Suggested practice
- [LeetCode / NeetCode / Exercism link] — [description]
- [Another link] — [description]

## Self-check commands
\```bash
ruff check exercise/<track>/day_XX_<slug>/
python exercise/<track>/day_XX_<slug>/ex01_basic.py
python exercise/<track>/day_XX_<slug>/ex02_intermediate.py
python exercise/<track>/day_XX_<slug>/ex03_advanced.py
\```
```

### Exercise file (ex01/ex02/ex03) structure:

```python
# ex[NN]_[level].py — Day [NN]: [Topic] — [Level]

"""
[Level] exercises for [Topic].
Covers checklist items: #X–#Y.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex[NN]_[level].py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations


def function_stub(param: Type) -> ReturnType:
    """One-line description of what to implement.

    Args:
        param: Description.

    Returns:
        Description.

    Raises:
        ValueError: When [condition].

    Examples:
        >>> function_stub("input")
        "expected_output"
    """
    # TODO: Implement this function
    # Sample input: ...
    # Expected output: ...
    ...


# (4–6 stubs for ex01, 4–6 for ex02, 3–4 for ex03)


if __name__ == "__main__":
    # ─── function_stub checks ───
    assert function_stub("input") == "expected", "description"
    assert function_stub("edge") == "edge_result", "edge case"

    # (assert blocks for every function in this file)
    print("ex[NN]_[level].py: all asserts passed ✓")
```

### Required quality bars for exercises:

- **4–6 functions per basic/intermediate file**, **3–4 per advanced file** (total 11–16 functions)
- Every function has: **typed signature + docstring + TODO + Examples**
- Every function tested with **3+ assert statements** (normal + edge cases)
- Exercises collectively cover **every A-Z checklist concept** (verified via Concept Coverage Map)
- ex01 = creation/access/basics, ex02 = mutation/patterns/iteration, ex03 = industrial/advanced/anti-pattern fixes
- **Difficulty ladder**: ex01 exercises solvable in 5–10 min each, ex02 in 10–15 min, ex03 in 15–25 min
