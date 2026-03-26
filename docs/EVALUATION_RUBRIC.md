# Evaluation metrics & exercise evaluation mechanism

This repo uses a **fixed rubric** for every generated day module. The agent must generate matching artifacts; you use the **gates** and **scores** below for self-review and for asking the agent to grade your work.

**Copy-paste prompts** (generate → exercise → evaluate): [PROMPT_TEMPLATES.md](./PROMPT_TEMPLATES.md).

---

## 1. What “industrial level” means (generation checklist)

When you ask the agent to generate **Day N**, the output must satisfy **all** of these unless the day explicitly scopes down (e.g. “stdlib only”):

| # | Requirement | Verify |
|---|-------------|--------|
| G1 | **Type hints** on public functions and module-level constants where useful | `mypy` (if configured) or manual |
| G2 | **Explicit errors** — no bare `except:`; domain or `ValueError`/`TypeError` with message | Code review |
| G3 | **Tests** — `pytest` tests for exercise behavior (see §3) | `pytest` passes |
| G4 | **Lint/format** — Ruff-clean (or documented noqa with reason) | `ruff check` |
| G5 | **Docstrings** — Google or NumPy style on public APIs; exercise files include a clear problem docstring (prompt, signature, examples, constraints) | Spot check |
| G6 | **Security** — no secrets in code; validate external paths/inputs | Review |
| G7 | **Observability** (where relevant: CLI, services) — structured logging or clear exit codes | Review |

**DSA weeks:** G3 includes complexity stated in docstrings; G7 may be N/A for pure algorithms.

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

Each exercise file should declare **in module docstring** or in **`EVALUATION.md`** (same folder):

| Field | Description |
|-------|-------------|
| **Learning objectives** | 2–4 bullet outcomes |
| **Must pass** | List of behaviors (given/when/then style ok) |
| **Stretch** | Optional harder behaviors |
| **Time/space** | For DSA: big-O; for Python I/O: streaming vs load-all |
| **Failure modes** | What must not happen (e.g. crash on empty input) |

**Scoring per file (ex01_basic, ex02_intermediate, ex03_advanced):**

| Criterion | Points (max) |
|-----------|----------------|
| All **must pass** behaviors implemented | 40 |
| **Stretch** (partial credit ok) | 15 |
| **Tests** cover must-pass + one edge case | 25 |
| **Style** (types, ruff, docstrings) | 20 |
| **Total** | **100** |

**Pass:** ≥ **75** and all gates G1–G4 for that file.

---

## 4. Test mechanism (required layout)

For each day folder `exercise/<track>/day_NN_topic/`:

| Artifact | Purpose |
|----------|---------|
| `ex01_basic.py`, `ex02_intermediate.py`, `ex03_advanced.py` | Learner implementation (or stubs + `TODO`) in "complete the function" format with problem docstring |
| `test_exercises.py` | `pytest` tests — **can** import from exercise modules or test pure functions |
| `conftest.py` | Optional fixtures (temp dirs, fake clock) |

**Rule:** The agent should either ship **reference tests** that fail until the learner completes the exercise, or ship **parametrized** tests with clear `xfail`/`skip` documented in comments.

---

## 5. Evaluation workflow

### 5.1 Self-evaluation (you)

1. Run gates: `ruff check`, `pytest`, `mypy` (if enabled).
2. Score dimensions D1–D7 (1–5) using §2.
3. Score each exercise 0–100 using §3.
4. Log in git commit message or a private note: `day 08: weighted 4.0, ex02 82/100`.

### 5.2 Agent evaluation (you paste solution + rubric)

Use this **verbatim template** in Cursor:

```
You are grading per docs/EVALUATION_RUBRIC.md.

Context: Day [NN], topic [topic], files: [paths].
My solution: [attach or path].

Deliver:
1. Gate table: G1–G7 pass/fail with one-line evidence each.
2. Dimension scores D1–D7 (1–5) + weighted total.
3. Per-file scores for ex01, ex02, ex03 (0–100) with breakdown.
4. Top 3 concrete improvements (code-level).
5. Optional: one rewritten snippet showing best-practice fix for the worst issue.
```

### 5.3 Regression prevention

After the agent suggests changes, re-run `pytest` and `ruff`; only then merge or commit.

---

## 6. Misconfiguration traps (avoid)

| Trap | Fix |
|------|-----|
| Exercises only in comments, no tests | Require `test_exercises.py` in generation prompt |
| `src/.../dayNN/` also contains `exercise/` subfolder | Exercises live only under `exercise/<track>/day_NN_*` |
| Two different “src” meanings | Module root: `src/python_basic/day_08_strings/`; production examples: `.../code.py` inside **that** day folder |
| Agent skips industrial checklist | Paste §1 table into every generation prompt until habit forms |
| No numeric score | Use §2 + §3 every time |

---

## 7. Optional: pre-commit hook

When the repo has `pre-commit`, add `ruff` + `pytest` on staged files or on `exercise/**` — not mandatory for solo learning but matches industry practice.

---

## 8. File the agent must generate per day (summary)

| Path | Content |
|------|---------|
| `src/<track>/day_NN_topic/CODE.md` | Code-learning explanation |
| `src/<track>/day_NN_topic/code.py` | 3–5 production examples |
| `exercise/<track>/day_NN_topic/EXERCISE.md` | Objectives, must-pass, expected I/O |
| `exercise/<track>/day_NN_topic/EVALUATION.md` | Rubric: objectives, must-pass, stretch, scoring |
| `exercise/<track>/day_NN_topic/ex01_*.py` … `ex03_*.py` | Exercises |
| `exercise/<track>/day_NN_topic/test_exercises.py` | pytest |

This list is **normative** for “industrial level” generation in this repo.
