# Python-Learning

A 100-day Python + 20-week DSA self-study repository with code-first teaching, graded exercises, and industrial-quality reference code.

## What's Inside

```
study_plan/          ← Day tables + A-Z concept checklists per topic
src/                 ← CODE.md (teaches) + code.py (reference implementation)
exercise/            ← EXERCISE.md + ex01/02/03 stubs with assert self-checks
docs/                ← Rubric, prompts, source registry, score tracker
```

## Tracks

| Phase | Days | Track | Focus |
|-------|------|-------|-------|
| 1 | 01–14 | Python Basics | Syntax, data structures, I/O, tooling |
| 2 | 15–34 | Python Intermediate | OOP, decorators, testing, typing |
| 3 | 35–50 | Concurrency | Async, threads, multiprocessing, profiling |
| 4 | 51–70 | Advanced Python | Metaprogramming, patterns, security, DB |
| 5 | 71–86 | FastAPI | REST APIs, auth, middleware, deployment |
| 6 | 87–100 | DevOps & Capstone | Docker, CI/CD, monitoring, final project |
| ∥ | Weeks 01–20 | DSA | Arrays → graphs → DP → tries (NeetCode-aligned) |

## Quick Start

```bash
git clone <repo-url> && cd Python-Learning
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Start with [study_plan/python_basic.md](study_plan/python_basic.md) → open the day's `CODE.md` → try the exercises.

## Structure Per Day

Each day generates 6 files:

| File | Purpose |
|------|---------|
| `CODE.md` | Concept table + 8+ snippets + anti-patterns + industrial practices |
| `code.py` | Runnable reference with type hints, docstrings, asserts |
| `EXERCISE.md` | Objectives, concept coverage map, scoring guide |
| `ex01_basic.py` | 4–6 basic stubs |
| `ex02_intermediate.py` | 4–6 intermediate stubs |
| `ex03_advanced.py` | 3–4 advanced stubs |

## Key Files

- [DAILY_STUDY_PLAN.md](DAILY_STUDY_PLAN.md) — Master index and workflow
- [study_plan/](study_plan/) — Track files with concept checklists
- [docs/RUBRIC.md](docs/RUBRIC.md) — Scoring rubric and gates (G1–G8)
- [docs/PROMPT_TEMPLATES.md](docs/PROMPT_TEMPLATES.md) — Generation templates
- [docs/SOURCE_REGISTRY.md](docs/SOURCE_REGISTRY.md) — Curated learning sources

## License

For personal learning use.
