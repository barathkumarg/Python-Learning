# Python-Learning

A 100-day Python + 20-week DSA self-study repository with code-first teaching,
graded exercises, and industrial-quality reference code. **This README is the
single entry point** — it documents the full workflow and where everything lives.

## What's Inside

```
study_plan/   ← THE PLAN: every Python + DSA concept, basic→advanced, per day/week
              (prerequisites, production example, A-Z checklist, inline sources)
src/          ← generated study material: CODE.md (teaches) + code.py (reference)
exercise/     ← generated practice: EXERCISE.md + ex01/02/03 stubs + EVALUATION.md
.agent.md     ← the agentic spec: generation rules, gates, and the prompts
docs/         ← RUBRIC (grading), SCORE_TRACKER (results), SOURCE_REGISTRY, DSA_VISUALS
```

## The Workflow (4 steps)

Study before you practise. Practise closed-book. One day (or DSA week) at a time.

### 0. Reference
Pick the day in **`study_plan/<track>.md`**. It is the source of truth for what to
learn: the A-Z concept checklist, prerequisites, the day's **Production example**,
and the inline **Sources** to read.

### 1. Generate
Run the **generate prompt** from **[.agent.md](.agent.md)**. It produces 6 files:
```
src/<track>/<unit>/{CODE.md, code.py}
exercise/<track>/<unit>/{EXERCISE.md, ex01_basic.py, ex02_intermediate.py, ex03_advanced.py}
```
(`<unit>` = `day_NN_slug`, or `week_WW_slug` for DSA.)

### 2. Study
Read `src/<track>/<unit>/CODE.md`, then `code.py`. Run it and confirm output
matches the `# Expected output:` comments:
```bash
python src/<track>/<unit>/code.py
```

### 3. Practise
Solve `ex01 → ex02 → ex03` **closed-book** (don't peek at `code.py`). Each file
must pass its inline asserts and lint before you move on:
```bash
ruff check exercise/<track>/<unit>/
python exercise/<track>/<unit>/ex01_basic.py
python exercise/<track>/<unit>/ex02_intermediate.py
python exercise/<track>/<unit>/ex03_advanced.py
```

### 4. Evaluate & Record
Run the **evaluate prompt** from **[.agent.md](.agent.md)** (grading rules in
[docs/RUBRIC.md](docs/RUBRIC.md)). It grades against gates G1–G8 and dimensions
D1–D7, then:
- writes the graded report to **`exercise/<track>/<unit>/EVALUATION.md`**, and
- adds a row to **[docs/SCORE_TRACKER.md](docs/SCORE_TRACKER.md)**.

**Gate:** `< 75` on any file or any gate fail → **rework** (max 3 cycles).
`≥ 75` on all → advance to the next day.

## Where Things Live

| Question | File |
|----------|------|
| What do I do? (the workflow) | **this README** |
| What / how deep to learn per topic? | `study_plan/<track>.md` |
| The generate / evaluate / rework prompts | [.agent.md](.agent.md) |
| How content is generated (rules, gates) | [.agent.md](.agent.md) |
| How it's graded — gates G1–G8, scoring | [docs/RUBRIC.md](docs/RUBRIC.md) *(single source)* |
| My recorded progress | [docs/SCORE_TRACKER.md](docs/SCORE_TRACKER.md) |
| Curated source catalog | [docs/SOURCE_REGISTRY.md](docs/SOURCE_REGISTRY.md) |
| DSA diagram templates | [docs/DSA_VISUALS.md](docs/DSA_VISUALS.md) |

## Phases & Tracks

| Phase | Days | Track | Study plan |
|-------|------|-------|------------|
| 1 | 01–14 | Python Basics | [study_plan/python_basic.md](study_plan/python_basic.md) |
| 2 | 15–34 | Python Intermediate | [study_plan/python_intermediate.md](study_plan/python_intermediate.md) |
| 3 | 35–50 | Python Concurrency | [study_plan/python_concurrency.md](study_plan/python_concurrency.md) |
| 4 | 51–70 | Advanced Python | [study_plan/python_advanced.md](study_plan/python_advanced.md) |
| 5 | 71–86 | FastAPI | [study_plan/fastapi_track.md](study_plan/fastapi_track.md) |
| 6 | 87–100 | DevOps & Capstone | [study_plan/devops_track.md](study_plan/devops_track.md) |
| ∥ | Weeks 01–20 | DSA | [study_plan/dsa.md](study_plan/dsa.md) — arrays → graphs → DP → tries |

**DSA scheduling:** Week `n` runs parallel to Python days `5n-4` … `5n`.

## Quick Start

```bash
git clone <repo-url> && cd Python-Learning
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Then open [study_plan/python_basic.md](study_plan/python_basic.md) and run the
workflow above for Day 01.

## Industrial Learning Bar

- **Study before practise** — read the reference, then solve from memory.
- **Closed-book practice** — active recall; don't copy `code.py`.
- **Everything runs green** — every file passes `ruff` + asserts before evaluation.
- **Grade to advance** — `≥ 75` all files, all gates; rework weak days (3-cycle cap).
- **Production-anchored** — each day builds the topic's real-world Production example.

## Time Budget

| Block | Time |
|-------|------|
| Python day | 60–90 min |
| DSA week | 45–90 min |
| Sunday lab | 90–120 min |
| Quality pass (ruff + asserts) | 15 min |

## License

For personal learning use.
