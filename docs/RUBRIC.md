# Rubric — Gates, Scoring, Skills & Evaluation Protocol

> Single source of truth for grading. Referenced by `.agent.md` and `docs/PROMPT_TEMPLATES.md`.

---

## §1 Skills taxonomy

### Python core (PY-01 to PY-23)

| ID | Skill | Phase |
|----|-------|-------|
| PY-01 | Variables, types, naming | 1 |
| PY-02 | String operations & formatting | 1 |
| PY-03 | Input validation & error handling | 1–2 |
| PY-04 | Control flow (if/match/loops) | 1 |
| PY-05 | Functions, args, kwargs, lambda | 1 |
| PY-06 | Data structures (list, dict, set, tuple) | 1 |
| PY-07 | File I/O, pathlib, CSV, JSON | 1 |
| PY-08 | Modules & packages | 1 |
| PY-09 | Comprehensions & generators | 1–2 |
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
| PY-21 | Testing (pytest, fixtures, mocking) | 3–4 |
| PY-22 | Design patterns | 4 |
| PY-23 | Packaging & tooling (uv, pyproject) | 1, 4 |

### FastAPI & DevOps (FA-01 to DO-04)

| ID | Skill | Phase |
|----|-------|-------|
| FA-01 | Routing, Pydantic, dependencies | 5 |
| FA-02 | Auth (JWT, OAuth2) | 5 |
| FA-03 | DB integration (SQLAlchemy, Alembic) | 5 |
| FA-04 | Testing APIs (TestClient) | 5 |
| DO-01 | Docker & compose | 5–6 |
| DO-02 | CI/CD (GitHub Actions) | 6 |
| DO-03 | Observability (logging, metrics) | 6 |
| DO-04 | Subprocess & automation | 6 |

### DSA (DSA-01 to DSA-26)

| ID | Skill | Weeks |
|----|-------|-------|
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
| DSA-14 | DP (1D, 2D) | 16–17 |
| DSA-15 | Shortest paths | 18 |
| DSA-16 | Tries & bit manipulation | 19 |
| DSA-17 | Recursion fundamentals | 11 |
| DSA-18 | Monotonic deque patterns | 4–5 |
| DSA-19 | Intervals | 15 |
| DSA-20 | String algorithms (KMP, Rabin-Karp) | 4, 19 |
| DSA-21 | Matrix traversal (grid BFS/DFS) | 12, 17 |
| DSA-22 | Math & number theory | 20 |
| DSA-23 | Kadane / max-subarray | 2, 16 |
| DSA-24 | Subsequence & subset-sum | 11, 16 |
| DSA-25 | Pattern printing | Prep, 11 |
| DSA-26 | Sorting algorithms | 20 |

---

## §2 Scoring dimensions (D1–D7, weighted 1–5)

| Dim | Weight | What to check |
|-----|--------|---------------|
| D1 Correctness | 0.30 | Matches spec, edge cases, tests green |
| D2 Reliability | 0.15 | Errors handled, no silent failures |
| D3 Maintainability | 0.15 | Clear names, small functions, no duplication |
| D4 API & typing | 0.10 | Sensible signatures, `Optional`/`Union` used correctly |
| D5 Performance | 0.10 | Right data structures, no accidental O(n²) |
| D6 Security | 0.10 | Injection-safe, no secrets, safe defaults |
| D7 Code quality | 0.10 | Lint-clean, consistent style, docstrings |

**Weighted total** = `sum(score_i × weight_i)`. Pass: **avg ≥ 3.5**, no dimension below 2.

---

## §3 Per-file scoring (0–100)

| Criterion | Max |
|-----------|-----|
| Must-pass behaviors | 40 |
| Stretch behaviors | 15 |
| Inline asserts + AI-verified behavior | 25 |
| Style (types, ruff, docstrings) | 20 |
| **Total** | **100** |

**Pass:** ≥ 75 per file + gates G1–G4.

---

## §4 Evaluation protocol

### When to evaluate

1. All 3 exercises completed.
2. Each runs cleanly: `python exNN.py` — no errors.
3. `ruff check exercise/<track>/day_NN_*/` — no errors.

### Evaluation prompt (copy-paste into any AI agent)

```
@.agent.md @docs/RUBRIC.md

Grade my solution for Day [NN] — [topic] at exercise/<track>/day_XX_<slug>/.
Read EXERCISE.md for specs and scoring.

Deliver exactly:
1. Gate table G1–G7 — pass/fail + one-line evidence.
2. Dimension scores D1–D7 (1–5) + weighted total.
3. Per-file scores ex01/ex02/ex03 (0–100) with criterion breakdown.
4. Skills assessed — Skill ID + proficiency (learning/developing/proficient/strong).
5. Top 3 improvements with file:line references.
6. One rewritten snippet for the worst issue.
7. Verdict: PASS (≥75 all) or REWORK (file + criterion).

Append the report to EXERCISE.md under ## Evaluation report.
```

### Feedback loop

| Score | Action |
|-------|--------|
| < 75 any file | REWORK — fix weakest criterion, re-evaluate |
| ≥ 75 all files | PASS — proceed to next day |
| ≥ 90 all files | STRONG PASS — skip stretch if desired |

**3-cycle cap:** if still failing after 3 rework cycles, log the gap and move on.

### Report format (append to EXERCISE.md)

```markdown
## Evaluation report — YYYY-MM-DD

### Gate checklist
| Gate | Result | Evidence |
|------|--------|----------|

### Dimension scores
| Dimension | Score | Notes |
|-----------|-------|-------|
| **Weighted total** | X.XX | |

### Per-file scores
| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| **Total** | | | |

### Skills assessed
| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|

### Action items
1. ...

### Verdict
PASS / REWORK — commit message: `study: day [NN] <track> weighted [X.X] ex01 [YY]/100 ex02 [YY]/100 ex03 [YY]/100`
```

---

## §5 Self-check commands (before evaluation)

```bash
ruff check exercise/<track>/day_XX_<content>/
python exercise/<track>/day_XX_<content>/ex01_basic.py
python exercise/<track>/day_XX_<content>/ex02_intermediate.py
python exercise/<track>/day_XX_<content>/ex03_advanced.py
```
