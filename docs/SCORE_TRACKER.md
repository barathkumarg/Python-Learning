# Score Tracker — Unified Evaluation Dashboard

> **Purpose:** Single source of truth for all evaluation scores, skill progression, gate compliance, and rework history across every Python day and DSA week.  
> **Companions:** [RUBRIC.md](./RUBRIC.md) · [.agent.md](../.agent.md)

---

## §0 — How to Use This File

1. **After every AI evaluation**, append a row to the Master Progress Table (§1).
2. **After every evaluation**, update the Skills Heatmap (§2) with tested skill IDs.
3. **On rework cycles**, log the attempt in the Rework Log (§3).
4. **Weekly**, review the Gate Compliance Summary (§4) for systemic gaps.
5. **Agents**: After writing an `EVALUATION.md` for a day/week, copy the summary row here.

---

## §1 — Master Progress Table

| Day/Week | Track | Topic | ex01 | ex02 | ex03 | Weighted Avg | Verdict | Date | Notes |
|----------|-------|-------|------|------|------|-------------|---------|------|-------|
| Day 01 | python_basic | Syntax, types, variables | 81 | 79 | 79 | 3.80 | ✅ PASS | 2026-03-26 | First pass |
| Day 02 | python_basic | Control flow | 95 | 95 | 96 | 4.10 | 🔁 REWORK | 2026-03-28 | G4 ruff not run, order-id validation gap |
| Day 03 | python_basic | Functions | — | — | — | — | ⏳ PENDING | — | Exercises done, awaiting evaluation |
| Day 06 | python_basic | Dictionaries | 74 | 85 | 89 | 3.50 | 🔁 REWORK | 2026-04-23 | ex01 < 75: missing TypeError, no lowercase; merge_configs and/or guard broken |
| Day 07 | python_basic | Sets and frozenset | 96 | 100 | 100 | 4.90 | 🌟 STRONG | 2026-04-23 | Clean solutions; minor: leftover comments in ex01 |
| Day 08 | python_basic | Strings and encoding | 73 | 84 | 84 | 3.05 | 🔁 REWORK | 2026-04-28 | G2 fail: no ValueError guards; safe_replace_char logic bug; debug prints left in |
| Day 09 | python_basic | File I/O | 89 | 87 | 86 | 3.95 | ✅ PASS | 2026-04-30 | JSONL format semantically wrong (writes list not per-line); inconsistent error types; missing newline="" in CSV read |
| Day 10 | python_basic | Exceptions | 74 | 82 | 88 | 3.45 | 🔁 REWORK | 2026-05-11 | G3 fail (7 ruff errors); ex01 < 75; weighted 3.45 < 3.5; describe_error format bug; classify_exception incomplete; read_first_line missing finally |
| Day 11 | python_basic | Modules and packages | 82 | — | — | 3.80 | ✅ PASS | 2026-05-13 | Single-file format; classify_import_statement logic bug (. vs from .); unnecessary print in check_name_guard |
| Week 01 | dsa | Big-O, arrays, hashing | 86 | 82 | 90 | 4.10 | ✅ PASS | 2026-04-23 | Clean solutions, needs more edge-case asserts + full docstrings |

### Legend

| Symbol | Meaning |
|--------|---------|
| ✅ PASS | Weighted avg ≥ 3.5, all files ≥ 75, all gates met |
| 🌟 STRONG | Weighted avg ≥ 4.5, all files ≥ 90 |
| 🔁 REWORK | One or more gates failed, or weighted avg < 3.5 |
| ⏳ PENDING | Exercises completed but not yet evaluated |
| — | Not yet generated |

### Score Formulas

Gates (G1–G8), per-file scoring (40/15/25/20), dimensions (D1–D7), and pass
thresholds are defined once in **[RUBRIC.md](./RUBRIC.md)** (§0, §2, §3). This
tracker only records the resulting scores — see RUBRIC for how they're computed.

---

## §2 — Skills Heatmap

Track which skills have been tested and passed across all evaluated modules.

### Python Core Skills (PY-01 to PY-23)

> Skill IDs and names are the canonical taxonomy from [RUBRIC.md §1](./RUBRIC.md).

| Skill ID | Skill Name | Phase | Tested | Pass | Days/Weeks |
|----------|-----------|-------|--------|------|------------|
| PY-01 | Variables, types, naming | 1 | ✅ | ✅ | Day 01 |
| PY-02 | String operations & formatting | 1 | ✅ | 🔁 | Days 01, 08 |
| PY-03 | Input validation & error handling | 1–2 | ✅ | 🔁 | Days 01, 10 |
| PY-04 | Control flow (if/match/loops) | 1 | ✅ | 🔁 | Day 02 |
| PY-05 | Functions, args, kwargs, lambda | 1 | ⏳ | — | Day 03 |
| PY-06 | Data structures (list, dict, set, tuple) | 1 | ✅ | 🔁 | Days 06, 07 |
| PY-07 | File I/O, pathlib, CSV, JSON | 1 | ✅ | ✅ | Day 09 |
| PY-08 | Modules & packages | 1 | ✅ | ✅ | Day 11 |
| PY-09 | Comprehensions & generators | 1–2 | — | — | — |
| PY-10 | OOP — classes, dunder, inheritance | 2 | — | — | — |
| PY-11 | Abstract classes & protocols | 2 | — | — | — |
| PY-12 | Dataclasses | 2 | — | — | — |
| PY-13 | Decorators & closures | 2 | — | — | — |
| PY-14 | Context managers | 2 | — | — | — |
| PY-15 | functools & itertools | 2 | — | — | — |
| PY-16 | Type hints & mypy | 2 | — | — | — |
| PY-17 | Threading & multiprocessing | 3 | — | — | — |
| PY-18 | Asyncio & aiohttp | 3 | — | — | — |
| PY-19 | Descriptors, metaclasses, slots | 4 | — | — | — |
| PY-20 | Profiling & optimization | 4 | — | — | — |
| PY-21 | Testing (pytest, fixtures, mocking) | 3–4 | — | — | — |
| PY-22 | Design patterns | 4 | — | — | — |
| PY-23 | Packaging & tooling (uv, pyproject) | 1, 4 | — | — | — |

### DSA Skills (DSA-01 to DSA-26)

| Skill ID | Skill Name | Week | Tested | Pass | Weeks |
|----------|-----------|------|--------|------|-------|
> Skill IDs and names are the canonical taxonomy from [RUBRIC.md §1](./RUBRIC.md).

| DSA-01 | Big-O analysis | 1–20 | ✅ | ✅ | Week 01 |
| DSA-02 | Arrays & hashing | 1–2 | ✅ | ✅ | Week 01 |
| DSA-03 | Two pointers | 3 | — | — | — |
| DSA-04 | Sliding window | 4 | — | — | — |
| DSA-05 | Stack | 5 | — | — | — |
| DSA-06 | Binary search | 6 | — | — | — |
| DSA-07 | Linked lists | 7 | — | — | — |
| DSA-08 | Trees (BT, BST) | 8–9 | — | — | — |
| DSA-09 | Heaps | 10 | — | — | — |
| DSA-10 | Backtracking | 11 | — | — | — |
| DSA-11 | Graphs (BFS, DFS, topo) | 12–13 | — | — | — |
| DSA-12 | Union-Find | 14 | — | — | — |
| DSA-13 | Greedy | 15 | — | — | — |
| DSA-14 | DP (1D, 2D) | 16–17 | — | — | — |
| DSA-15 | Shortest paths | 18 | — | — | — |
| DSA-16 | Tries & bit manipulation | 19 | — | — | — |
| DSA-17 | Recursion fundamentals | 11 | — | — | — |
| DSA-18 | Monotonic deque patterns | 4–5 | — | — | — |
| DSA-19 | Intervals | 15 | — | — | — |
| DSA-20 | String algorithms (KMP, Rabin-Karp) | 4, 19 | — | — | — |
| DSA-21 | Matrix traversal (grid BFS/DFS) | 12, 17 | — | — | — |
| DSA-22 | Math & number theory | 20 | — | — | — |
| DSA-23 | Kadane / max-subarray | 2, 16 | — | — | — |
| DSA-24 | Subsequence & subset-sum | 11, 16 | — | — | — |
| DSA-25 | Pattern printing | Prep, 11 | — | — | — |
| DSA-26 | Sorting algorithms | 20 | — | — | — |

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
| Day 08 | 1 | G2 fail (no ValueError), ex01 < 75, weighted 3.05 | Add ValueError guards to all fns; fix safe_replace_char slicing; remove debug prints; fix normalize_and_compare | ⏳ Open | 2026-04-28 |
| Day 10 | 1 | G3 fail (7 ruff), ex01 < 75, weighted 3.45 | Fix 7 ruff errors (unused `as` aliases, E701, F821); fix describe_error space; add finally to read_first_line; complete classify_exception hierarchy; fix withdraw amount<=0 | ⏳ Open | 2026-05-11 |

### Rework Rules (from RUBRIC.md §4)

- **< 75 weighted or any gate fail** → REWORK required.
- **≥ 75 weighted, all gates pass** → PASS.
- **≥ 90 weighted, all gates pass** → STRONG PASS.
- **3-cycle cap**: If still failing after 3 rework cycles, mark as blocked and move on.

---

## §4 — Gate Compliance Summary

Aggregate gate pass/fail across all evaluated modules for systemic pattern detection.

| Gate | Description | Day 01 | Day 02 | Day 03 | Day 08 | Day 09 | Day 10 | Day 11 | W01 | Pass Rate |
|------|-------------|--------|--------|--------|--------|--------|--------|--------|-----|-----------|
| G1 | Type hints on public APIs | ✅ | ✅ | ⏳ | ✅ | ✅ | ✅ | ✅ | ⏳ | 6/6 |
| G2 | Explicit errors (no bare except) | ⚠️ | ✅ | ⏳ | ❌ | ⚠️ | ⚠️ | ✅ | ⏳ | 2/6 |
| G3 | Behavioral verification (asserts + AI) | ✅ | ✅ | ⏳ | ✅ | ✅ | ✅ | ✅ | ⏳ | 6/6 |
| G4 | Lint clean (`ruff check`) | ✅ | ❌ | ⏳ | ✅ | ✅ | ❌ | ✅ | ⏳ | 4/6 |
| G5 | Docstrings on public functions | ✅ | ✅ | ⏳ | ✅ | ✅ | ✅ | ✅ | ⏳ | 6/6 |
| G6 | Security (no hardcoded secrets) | ✅ | ✅ | ⏳ | ✅ | ✅ | ✅ | ✅ | ⏳ | 6/6 |
| G7 | Observability (clear error messages) | ⚠️ | ⚠️ | ⏳ | ❌ | ⚠️ | ⚠️ | ✅ | ⏳ | 1/6 |
| G8 | Concept completeness (A-Z checklist) | — | — | ⏳ | ✅ | ✅ | ⚠️ | ✅ | ⏳ | 3/4 |

### Systemic Patterns

- **G2 (Explicit errors):** Day 01 ex02 uses bare `except:` — a recurring risk in early exercises. Fix: always catch specific exception types.
- **G4 (Lint clean):** Day 02 evaluation flagged ruff not run. Fix: add `ruff check` to every pre-evaluation self-check.
- **G7 (Observability):** Error messages in Days 01–02, 08 are vague or absent. Day 08 has debug `print()` in 3 functions. Fix: include the invalid value and expected range in every error message; remove debug prints.
- **G2 (Explicit errors — Day 08):** All 19 functions document `Raises: ValueError` but none actually raise. Recurring pattern — validation docstrings written but guards not implemented.

---

## §5 — Completion Dashboard

| Phase | Total Days | Generated | Evaluated | Passed | Remaining |
|-------|-----------|-----------|-----------|--------|-----------|
| Phase 1 — Python Basics | 14 | 6 | 6 | 3 | 8 |
| Phase 2 — Python Intermediate | 20 | 0 | 0 | 0 | 20 |
| Phase 3 — Python Concurrency | 16 | 0 | 0 | 0 | 16 |
| Phase 4 — Python Advanced | 20 | 0 | 0 | 0 | 20 |
| Phase 5 — FastAPI Track | 16 | 0 | 0 | 0 | 16 |
| Phase 6 — DevOps & Capstone | 14 | 0 | 0 | 0 | 14 |
| **Python Total** | **100** | **6** | **6** | **3** | **94** |
| DSA Weeks | 20 | 1 | 0 | 0 | 19 |
| **Grand Total** | **120** | **7** | **6** | **3** | **113** |

---

## §6 — Agent Update Protocol

Any AI agent performing evaluation must follow this protocol:

1. **Run** the evaluation using the evaluate prompt in [.agent.md §8](../.agent.md), following the [RUBRIC.md §4](./RUBRIC.md) protocol.
2. **Write** the detailed evaluation report to `exercise/<track>/<unit>/EVALUATION.md`.
3. **Add a row** to the Master Progress Table (§1) with scores, verdict, and date.
4. **Update** the Skills Heatmap (§2) for each skill ID tested.
5. **Update** the Gate Compliance Summary (§4) for each gate checked.
6. **If REWORK**, add a row to the Rework Log (§3).
7. **Update** the Completion Dashboard (§5) counts.
8. **Commit** with format: `eval: day [NN] <track> weighted [X.X] ex01 [YY]/100 ex02 [YY]/100 ex03 [YY]/100`
