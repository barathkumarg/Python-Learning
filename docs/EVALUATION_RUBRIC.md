# Evaluation metrics & exercise evaluation mechanism

This repo uses a **fixed rubric** for every generated day module. The agent must generate matching artifacts; you use the **gates** and **scores** below for self-review and for asking the agent to grade your work.

**Copy-paste prompts** (generate → exercise → evaluate): [PROMPT_TEMPLATES.md](./PROMPT_TEMPLATES.md).

---
## 0. Skills taxonomy (master reference)

Every exercise maps to one or more **skills** from this canonical list. Any AI agent reading this file can tag, track, and report on skill progression.

### Python core skills

| Skill ID | Skill | Phases |
|----------|-------|--------|
| PY-01 | Variables, types, naming | 1 |
| PY-02 | String operations & formatting | 1 |
| PY-03 | Input validation & error handling | 1, 2 |
| PY-04 | Control flow (if/match/loops) | 1 |
| PY-05 | Functions, args, kwargs, lambda | 1 |
| PY-06 | Data structures (list, dict, set, tuple) | 1 |
| PY-07 | File I/O, pathlib, CSV, JSON | 1 |
| PY-08 | Modules & packages | 1 |
| PY-09 | Comprehensions & generators | 1, 2 |
| PY-10 | OOP — classes, dunder, inheritance | 2 |
| PY-11 | Abstract classes & protocols | 2 |
| PY-12 | Dataclasses | 2 |
| PY-13 | Decorators & closures | 2 |
| PY-14 | Context managers | 2 |
| PY-15 | functools & itertools | 2 |
| PY-16 | Type hints & mypy | 2 |
| PY-17 | Threading & multiprocessing | 3 |
| PY-18 | Asyncio & aiohttp | 3 |
| PY-19 | Descriptors, metaclasses, slots | 4 |
| PY-20 | Profiling & optimization | 4 |
| PY-21 | Testing (pytest, fixtures, mocking) | 3, 4 |
| PY-22 | Design patterns | 4 |
| PY-23 | Packaging & tooling (uv, pyproject) | 1, 4 |

### FastAPI & DevOps skills

| Skill ID | Skill | Phases |
|----------|-------|--------|
| FA-01 | Routing, Pydantic, dependencies | 5 |
| FA-02 | Auth (JWT, OAuth2) | 5 |
| FA-03 | DB integration (SQLAlchemy, Alembic) | 5 |
| FA-04 | Testing APIs (TestClient) | 5 |
| DO-01 | Docker & compose | 5, 6 |
| DO-02 | CI/CD (GitHub Actions) | 6 |
| DO-03 | Observability (logging, metrics, tracing) | 6 |
| DO-04 | Subprocess & automation | 6 |

### DSA skills

| Skill ID | Skill | Weeks |
|----------|-------|-------|
| DSA-01 | Big-O analysis | 1–20 |
| DSA-02 | Arrays & hashing | 1–2 |
| DSA-03 | Two pointers | 3 |
| DSA-04 | Sliding window | 4 |
| DSA-05 | Stack | 5 |
| DSA-06 | Binary search | 6 |
| DSA-07 | Linked lists | 7 |
| DSA-08 | Trees (BT, BST) | 8–9 |
| DSA-09 | Heaps | 10 |
| DSA-10 | Backtracking | 11 |
| DSA-11 | Graphs (BFS, DFS, topo) | 12–13 |
| DSA-12 | Union-Find | 14 |
| DSA-13 | Greedy | 15 |
| DSA-14 | Dynamic programming (1D, 2D) | 16–17 |
| DSA-15 | Shortest paths | 18 |
| DSA-16 | Tries & bit manipulation | 19 |
| DSA-17 | Recursion fundamentals (base case, processed/unprocessed) | 11 |
| DSA-18 | Monotonic deque patterns | 4–5 |
| DSA-19 | Intervals (merge, overlap, scheduling) | 15 |
| DSA-20 | String operations & algorithms (substring/consecutive string, KMP `k-map` idea, Rabin-Karp) | 4, 19 |
| DSA-21 | Matrix traversal patterns (grid BFS/DFS, row/col scans) | 12, 17 |
| DSA-22 | Math & number theory basics | 20 |
| DSA-23 | Kadane / max-subarray reasoning | 2, 16 |
| DSA-24 | Subsequence and subset-sum reasoning | 11, 16 |
| DSA-25 | Pattern printing (loop + recursion warm-up) | Prep, 11 |
| DSA-26 | Sorting algorithms (merge/quick/heap/counting) | 20 |

**Usage:** Every `EXERCISE.md` must list which skill IDs each exercise targets. Evaluation reports must echo these IDs so progress is trackable across agents and sessions.

---
## 1. What “industrial level” means (generation checklist)

When you ask the agent to generate **Day N**, the output must satisfy **all** of these unless the day explicitly scopes down (e.g. “stdlib only”):

| # | Requirement | Verify |
|---|-------------|--------|
| G1 | **Type hints** on public functions and module-level constants where useful | `mypy` (if configured) or manual |
| G2 | **Explicit errors** — no bare `except:`; domain or `ValueError`/`TypeError` with message | Code review |
| G3 | **Behavioral verification** — inline `assert` checks in `__main__` + AI behavioral review (see [AI_EVAL_FRAMEWORK.md](./AI_EVAL_FRAMEWORK.md)) | Run each `exNN.py`; AI evaluation |
| G4 | **Lint/format** — Ruff-clean (or documented noqa with reason) | `ruff check` |
| G5 | **Docstrings** — Google or NumPy style on public APIs; exercise files include a clear problem docstring (prompt, signature, examples, constraints) | Spot check |
| G6 | **Security** — no secrets in code; validate external paths/inputs | Review |
| G7 | **Observability** (where relevant: CLI, services) — structured logging or clear exit codes | Review |

**DSA weeks:** G3 includes complexity coverage in `CODE.md`, `EXERCISE.md`, and DSA function docstrings (`code.py` and `exNN_*.py`); G7 may be N/A for pure algorithms.

---

## 2. Universal scoring dimensions (weighted)

Use a **1–5** score per dimension. **Passing** for a professional bar: **average ≥ 3.5** and **no dimension below 2**.

| Dimension | Weight | What to look for |
|-----------|--------|------------------|
| **D1 Correctness** | 0.30 | Matches spec; edge cases; tests green |
| **D2 Reliability** | 0.15 | Errors handled; no silent failures; timeouts where I/O |
| **D3 Maintainability** | 0.15 | Clear names; small functions; no duplication |
| **D4 API & typing** | 0.10 | Sensible signatures; `Optional`/`Union` used honestly |
| **D5 Performance** | 0.10 | Appropriate structures; no accidental O(n²); async where I/O bound |
| **D6 Security & safety** | 0.10 | Injection-safe; path traversal considered; subprocess safe |
| **D7 Test quality** | 0.10 | Meaningful assertions; edge cases; not only happy path |

**Weighted score:**  
`sum(score_i × weight_i)` over dimensions, scores 1–5.

---

## 3. Per-exercise rubric (ex01 / ex02 / ex03)

Each exercise file should declare **in module docstring** or in **`EXERCISE.md`** (same folder):

| Field | Description |
|-------|-------------|
| **Learning objectives** | 2–4 bullet outcomes |
| **Must pass** | List of behaviors (given/when/then style ok) |
| **Stretch** | Optional harder behaviors |
| **Time/space** | For DSA: explicit big-O per problem in `EXERCISE.md` and exercise docstrings; for Python I/O: streaming vs load-all |
| **Failure modes** | What must not happen (e.g. crash on empty input) |

**Scoring per file (ex01_basic, ex02_intermediate, ex03_advanced):**

| Criterion | Points (max) |
|-----------|----------------|
| All **must pass** behaviors implemented | 40 |
| **Stretch** (partial credit ok) | 15 |
| **Inline asserts + AI-verified** behavior coverage | 25 |
| **Style** (types, ruff, docstrings) | 20 |
| **Total** | **100** |

**Pass:** ≥ **75** and all gates G1–G4 for that file.

---

## 4. Verification mechanism (required layout)

For each day folder `exercise/<track>/day_NN_topic/`:

| Artifact | Purpose |
|----------|---------|
| `EXERCISE.md` | Objectives, must-pass/stretch specs, scoring breakdown, suggested practice links |
| `ex01_basic.py`, `ex02_intermediate.py`, `ex03_advanced.py` | Learner implementation (or stubs + `TODO`) with inline `assert` checks in `__main__` |

**No `test_exercises.py` or `EVALUATION.md`.** Evaluation is AI-based — see [AI_EVAL_FRAMEWORK.md](./AI_EVAL_FRAMEWORK.md).

**Rule:** Each exercise stub must include 2–3 `assert` statements in its `if __name__ == "__main__":` block covering must-pass behaviors. The learner runs each file to self-check before requesting AI evaluation.

---

## 5. Evaluation workflow

See [docs/AI_EVAL_FRAMEWORK.md](./AI_EVAL_FRAMEWORK.md) for the full evaluation protocol.

### 5.1 Quick self-check (you)

1. Run `ruff check exercise/<track>/day_NN_topic/`.
2. Run each exercise file: `python ex01_basic.py`, `python ex02_intermediate.py`, `python ex03_advanced.py`.
3. All must exit cleanly (no `AssertionError`, no traceback).

### 5.2 AI evaluation

Use the **verbatim submission template** in [AI_EVAL_FRAMEWORK.md §2](./AI_EVAL_FRAMEWORK.md) — gates, D1–D7, per-file 0–100, top 3 fixes.

### 5.3 Regression prevention

After the agent suggests changes, re-run inline asserts and `ruff check`; only then commit.

---

## 6. Misconfiguration traps (avoid)

| Trap | Fix |
|------|-----|
| CODE.md too verbose / inconsistent | Follow [docs/CODE_TEMPLATE.md](./CODE_TEMPLATE.md) — ≤80 lines, concepts table format |
| `src/.../dayNN/` also contains `exercise/` subfolder | Exercises live only under `exercise/<track>/day_NN_*` |
| Two different "src" meanings | Module root: `src/python_basic/day_08_strings/`; production examples: `.../code.py` inside **that** day folder |
| Agent skips industrial checklist | Paste §1 table into every generation prompt until habit forms |
| No numeric score | Use §2 + §3 every time |
| DSA CODE.md without diagrams | Must include Visual/Diagram section per [docs/CODE_TEMPLATE.md](./CODE_TEMPLATE.md) diagram guide |
| DSA content missing Big-O usage explanation | Week 01 and other Big-O intros must explain what Big-O is used for in approach selection |
| DSA files missing time/space complexity | Add explicit complexity for each discussed problem in DSA `.md` and `.py` files |
| DSA week misses row-listed advanced subtopics | Read `DAILY_STUDY_PLAN.md` week row and ensure every listed subtopic appears in CODE.md or exercise specs |
| GIF included without fallback | If using GIF in DSA docs, keep ASCII/Mermaid fallback for plain markdown viewers |
| DSA snippets missing traversal visuals | Add a mini traversal block under each snippet/example expected output |

---

## 7. Optional: pre-commit hook

When the repo has `pre-commit`, add `ruff` on staged files or on `exercise/**` — not mandatory for solo learning but matches industry practice.

---

## 8. Files the agent must generate per day (summary)

| Path | Content |
|------|---------|
| `src/<track>/day_NN_topic/CODE.md` | Code-learning explanation (follow [docs/CODE_TEMPLATE.md](./CODE_TEMPLATE.md); DSA: include Visual/Diagram) |
| `src/<track>/day_NN_topic/code.py` | 3–5 production examples |
| `exercise/<track>/day_NN_topic/EXERCISE.md` | Objectives, must-pass/stretch, scoring 0–100, suggested practice links |
| `exercise/<track>/day_NN_topic/ex01_*.py` … `ex03_*.py` | Stubs with inline `assert` self-checks in `__main__` |

**5 files total.** No `EVALUATION.md`, no `test_exercises.py`. Evaluation is AI-based per [AI_EVAL_FRAMEWORK.md](./AI_EVAL_FRAMEWORK.md).

This list is **normative** for “industrial level” generation in this repo.
