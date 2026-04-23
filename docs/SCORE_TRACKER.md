# Score Tracker — Unified Evaluation Dashboard

> **Purpose:** Single source of truth for all evaluation scores, skill progression, gate compliance, and rework history across every Python day and DSA week.  
> **Companions:** [RUBRIC.md](./RUBRIC.md) · [PROMPT_TEMPLATES.md](./PROMPT_TEMPLATES.md)

---

## §0 — How to Use This File

1. **After every AI evaluation**, append a row to the Master Progress Table (§1).
2. **After every evaluation**, update the Skills Heatmap (§2) with tested skill IDs.
3. **On rework cycles**, log the attempt in the Rework Log (§3).
4. **Weekly**, review the Gate Compliance Summary (§4) for systemic gaps.
5. **Agents**: After generating an evaluation report in `EXERCISE.md`, copy the summary row here.

---

## §1 — Master Progress Table

| Day/Week | Track | Topic | ex01 | ex02 | ex03 | Weighted Avg | Verdict | Date | Notes |
|----------|-------|-------|------|------|------|-------------|---------|------|-------|
| Day 01 | python_basic | Syntax, types, variables | 81 | 79 | 79 | 3.80 | ✅ PASS | 2026-03-26 | First pass |
| Day 02 | python_basic | Control flow | 95 | 95 | 96 | 4.10 | 🔁 REWORK | 2026-03-28 | G4 ruff not run, order-id validation gap |
| Day 03 | python_basic | Functions | — | — | — | — | ⏳ PENDING | — | Exercises done, awaiting evaluation |
| Day 06 | python_basic | Dictionaries | 74 | 85 | 89 | 3.50 | 🔁 REWORK | 2026-04-23 | ex01 < 75: missing TypeError, no lowercase; merge_configs and/or guard broken |
| Day 07 | python_basic | Sets and frozenset | 96 | 100 | 100 | 4.90 | 🌟 STRONG | 2026-04-23 | Clean solutions; minor: leftover comments in ex01 |
| Week 01 | dsa | Big-O, arrays, hashing | 86 | 82 | 90 | 4.10 | ✅ PASS | 2026-04-23 | Clean solutions, needs more edge-case asserts + full docstrings |

### Legend

| Symbol | Meaning |
|--------|---------|
| ✅ PASS | Weighted avg ≥ 3.5, all files ≥ 75, all gates met |
| 🌟 STRONG | Weighted avg ≥ 4.5, all files ≥ 90 |
| 🔁 REWORK | One or more gates failed, or weighted avg < 3.5 |
| ⏳ PENDING | Exercises completed but not yet evaluated |
| — | Not yet generated |

### Score Formulas (from RUBRIC.md §2–§3)

**Per-file score (0–100):**

| Component | Weight | What it measures |
|-----------|--------|------------------|
| Must-pass requirements | 40 | Core logic, correct return type, handles specified inputs |
| Stretch goals | 15 | Optional enhancements attempted and correct |
| Inline asserts + AI-verified behavior | 25 | Self-check coverage and behavioral correctness |
| Style (type hints, naming, docstrings, lint) | 20 | Industrial code quality |

**Weighted dimension average (1–5):**

| Dimension | Weight | Key criteria |
|-----------|--------|-------------|
| D1 — Correctness | 0.30 | Handles all specified cases, edge cases |
| D2 — Reliability | 0.15 | Explicit errors, no silent failures |
| D3 — Maintainability | 0.15 | Naming, structure, readability |
| D4 — API & typing | 0.10 | Type hints, signatures, contracts |
| D5 — Performance | 0.10 | Appropriate complexity, no wasteful patterns |
| D6 — Security | 0.10 | No injection, no hardcoded secrets, safe defaults |
| D7 — Code quality | 0.10 | Lint-clean, consistent style, docstrings |

**Pass thresholds:** Per-file ≥ 75 · Weighted avg ≥ 3.5 · No dimension below 2.

---

## §2 — Skills Heatmap

Track which skills have been tested and passed across all evaluated modules.

### Python Core Skills (PY-01 to PY-23)

| Skill ID | Skill Name | Phase | Tested | Pass | Days/Weeks |
|----------|-----------|-------|--------|------|------------|
| PY-01 | Variables, types, literals | 1 | ✅ | ✅ | Day 01 |
| PY-02 | f-strings, formatting | 1 | ✅ | ✅ | Day 01 |
| PY-03 | Input parsing, validation | 1 | ✅ | ✅ | Day 01 |
| PY-04 | Control flow (if/match/loops) | 1 | ✅ | 🔁 | Day 02 |
| PY-05 | Functions, args, kwargs | 1 | ⏳ | — | Day 03 |
| PY-06 | Lists and sorting | 1 | — | — | — |
| PY-07 | Tuples and NamedTuple | 1 | — | — | — |
| PY-08 | Dictionaries | 1 | — | — | — |
| PY-09 | Sets and frozenset | 1 | — | — | — |
| PY-10 | Strings and encoding | 1 | — | — | — |
| PY-11 | File I/O | 1 | — | — | — |
| PY-12 | Exceptions and custom errors | 1 | — | — | — |
| PY-13 | Modules and packages | 1 | — | — | — |
| PY-14 | Built-ins (map, filter, zip) | 1 | — | — | — |
| PY-15 | Comprehensions | 1 | — | — | — |
| PY-16 | OOP (classes, inheritance) | 2 | — | — | — |
| PY-17 | Iterators and generators | 2 | — | — | — |
| PY-18 | Decorators | 2 | — | — | — |
| PY-19 | Context managers | 2 | — | — | — |
| PY-20 | Typing and generics | 2 | — | — | — |
| PY-21 | Concurrency (threads/async) | 3 | — | — | — |
| PY-22 | Testing and coverage | 4 | — | — | — |
| PY-23 | Packaging and tooling | 4 | — | — | — |

### DSA Skills (DSA-01 to DSA-26)

| Skill ID | Skill Name | Week | Tested | Pass | Weeks |
|----------|-----------|------|--------|------|-------|
| DSA-01 | Big-O analysis | 01 | ⏳ | — | Week 01 |
| DSA-02 | Array scan patterns | 01 | ⏳ | — | Week 01 |
| DSA-03 | Hash map/set usage | 01 | ⏳ | — | Week 01 |
| DSA-04 | Prefix sums, Kadane | 02 | — | — | — |
| DSA-05 | Two pointers | 03 | — | — | — |
| DSA-06 | Sliding window | 04 | — | — | — |
| DSA-07 | Stack / monotonic stack | 05 | — | — | — |
| DSA-08 | Binary search | 06 | — | — | — |
| DSA-09 | Linked list | 07 | — | — | — |
| DSA-10 | Binary tree traversals | 08 | — | — | — |
| DSA-11 | BST operations | 09 | — | — | — |
| DSA-12 | Heap / priority queue | 10 | — | — | — |
| DSA-13 | Recursion fundamentals | 11 | — | — | — |
| DSA-14 | Backtracking | 11 | — | — | — |
| DSA-15 | Graph BFS/DFS | 12 | — | — | — |
| DSA-16 | Topological sort | 13 | — | — | — |
| DSA-17 | Union-Find | 14 | — | — | — |
| DSA-18 | Greedy / intervals | 15 | — | — | — |
| DSA-19 | 1D DP | 16 | — | — | — |
| DSA-20 | 2D DP | 17 | — | — | — |
| DSA-21 | Shortest paths | 18 | — | — | — |
| DSA-22 | Tries | 19 | — | — | — |
| DSA-23 | String algorithms (KMP, Rabin-Karp) | 19 | — | — | — |
| DSA-24 | Bit manipulation | 19 | — | — | — |
| DSA-25 | Sorting algorithms | 20 | — | — | — |
| DSA-26 | Math / number theory | 20 | — | — | — |

### Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Tested and passed (score ≥ 75, gate compliant) |
| 🔁 | Tested but needs rework |
| ⏳ | Exercises exist, evaluation pending |
| — | Not yet generated |

---

## §3 — Rework Log

Track rework cycles per day/week. Max 3 cycles per the RUBRIC.md §4 rule.

| Day/Week | Cycle | Trigger | Action Items | Resolution | Date |
|----------|-------|---------|-------------|------------|------|
| Day 02 | 1 | G4 ruff not run, order-id validation gap | Run `ruff check`, add strict `id` format validation | ⏳ Open | 2026-03-28 |

### Rework Rules (from RUBRIC.md §4)

- **< 75 weighted or any gate fail** → REWORK required.
- **≥ 75 weighted, all gates pass** → PASS.
- **≥ 90 weighted, all gates pass** → STRONG PASS.
- **3-cycle cap**: If still failing after 3 rework cycles, mark as blocked and move on.

---

## §4 — Gate Compliance Summary

Aggregate gate pass/fail across all evaluated modules for systemic pattern detection.

| Gate | Description | Day 01 | Day 02 | Day 03 | W01 | Pass Rate |
|------|-------------|--------|--------|--------|-----|-----------|
| G1 | Type hints on public APIs | ✅ | ✅ | ⏳ | ⏳ | 2/2 |
| G2 | Explicit errors (no bare except) | ⚠️ | ✅ | ⏳ | ⏳ | 1/2 |
| G3 | Behavioral verification (asserts + AI) | ✅ | ✅ | ⏳ | ⏳ | 2/2 |
| G4 | Lint clean (`ruff check`) | ✅ | ❌ | ⏳ | ⏳ | 1/2 |
| G5 | Docstrings on public functions | ✅ | ✅ | ⏳ | ⏳ | 2/2 |
| G6 | Security (no hardcoded secrets) | ✅ | ✅ | ⏳ | ⏳ | 2/2 |
| G7 | Observability (clear error messages) | ⚠️ | ⚠️ | ⏳ | ⏳ | 0/2 |

### Systemic Patterns

- **G2 (Explicit errors):** Day 01 ex02 uses bare `except:` — a recurring risk in early exercises. Fix: always catch specific exception types.
- **G4 (Lint clean):** Day 02 evaluation flagged ruff not run. Fix: add `ruff check` to every pre-evaluation self-check.
- **G7 (Observability):** Error messages in Days 01–02 are vague (`"Conversion error"`, `"Value not accepted"`). Fix: include the invalid value and expected range in every error message.

---

## §5 — Completion Dashboard

| Phase | Total Days | Generated | Evaluated | Passed | Remaining |
|-------|-----------|-----------|-----------|--------|-----------|
| Phase 1 — Python Basics | 14 | 3 | 2 | 1 | 11 |
| Phase 2 — Python Intermediate | 20 | 0 | 0 | 0 | 20 |
| Phase 3 — Python Concurrency | 16 | 0 | 0 | 0 | 16 |
| Phase 4 — Python Advanced | 20 | 0 | 0 | 0 | 20 |
| Phase 5 — FastAPI Track | 16 | 0 | 0 | 0 | 16 |
| Phase 6 — DevOps & Capstone | 14 | 0 | 0 | 0 | 14 |
| **Python Total** | **100** | **3** | **2** | **1** | **97** |
| DSA Weeks | 20 | 1 | 0 | 0 | 19 |
| **Grand Total** | **120** | **4** | **2** | **1** | **116** |

---

## §6 — Agent Update Protocol

Any AI agent performing evaluation must follow this protocol:

1. **Run** the evaluation using the prompt from [RUBRIC.md §4](./RUBRIC.md).
2. **Append** the detailed evaluation report to the relevant `EXERCISE.md` file.
3. **Add a row** to the Master Progress Table (§1) with scores, verdict, and date.
4. **Update** the Skills Heatmap (§2) for each skill ID tested.
5. **Update** the Gate Compliance Summary (§4) for each gate checked.
6. **If REWORK**, add a row to the Rework Log (§3).
7. **Update** the Completion Dashboard (§5) counts.
8. **Commit** with format: `eval: day [NN] <track> weighted [X.X] ex01 [YY]/100 ex02 [YY]/100 ex03 [YY]/100`
