# Daily Python + DSA Study Plan

> **Role:** Professional backend Python + DSA tutor track.  
> **Companions:** [README.md](./README.md) · [.agent.md](./.agent.md) · [docs/RUBRIC.md](./docs/RUBRIC.md) · [docs/PROMPT_TEMPLATES.md](./docs/PROMPT_TEMPLATES.md) · [docs/SOURCE_REGISTRY.md](./docs/SOURCE_REGISTRY.md)

---

## Purpose

This file is the **master index**. Detailed day tables, concept checklists, and exercise directions live in the track files under `study_plan/`.

---

## Artifacts Per Day

| Artifact | Purpose |
|----------|---------|
| `CODE.md` | Concept map + snippets + anti-patterns + industrial practices |
| `code.py` | Production-style reference with type hints and asserts |
| `EXERCISE.md` | Objectives, scoring, failure modes |
| `ex01_basic.py` | Foundational stubs |
| `ex02_intermediate.py` | Applied stubs |
| `ex03_advanced.py` | Design / edge-case stubs |

---

## Repository Layout

```text
src/<track>/day_NN_topic/     → CODE.md + code.py
exercise/<track>/day_NN_topic/ → EXERCISE.md + ex01/02/03
src/dsa/week_WW_topic/        → CODE.md + code.py
exercise/dsa/week_WW_topic/   → EXERCISE.md + ex01/02/03
study_plan/                    → Track files with concept checklists
```

---

## Phase Overview

| Phase | Days | Track | Study Plan |
|-------|------|-------|------------|
| 1 | 01–14 | `python_basic` | [study_plan/python_basic.md](./study_plan/python_basic.md) |
| 2 | 15–34 | `python_intermediate` | [study_plan/python_intermediate.md](./study_plan/python_intermediate.md) |
| 3 | 35–50 | `python_concurrency` | [study_plan/python_concurrency.md](./study_plan/python_concurrency.md) |
| 4 | 51–70 | `python_advanced` | [study_plan/python_advanced.md](./study_plan/python_advanced.md) |
| 5 | 71–86 | `fastapi_track` | [study_plan/fastapi_track.md](./study_plan/fastapi_track.md) |
| 6 | 87–100 | `devops_track` | [study_plan/devops_track.md](./study_plan/devops_track.md) |
| DSA | Weeks 01–20 | `dsa` | [study_plan/dsa.md](./study_plan/dsa.md) |

---

## Generation Workflow

1. Open the track file for the day/week you're generating.
2. Use [docs/SOURCE_REGISTRY.md](./docs/SOURCE_REGISTRY.md) for teaching sources.
3. Generate using [docs/PROMPT_TEMPLATES.md](./docs/PROMPT_TEMPLATES.md).
4. Validate with [.agent.md](./.agent.md) gates G1–G8 and [docs/RUBRIC.md](./docs/RUBRIC.md).

---

## Time Budget

| Block | Time |
|-------|------|
| Python day | 60–90 min |
| DSA week | 45–90 min |
| Sunday lab | 90–120 min |
| Quality pass | 15 min |

---

## High-Value References

| Area | Sources |
|------|---------|
| Python | [Python Tutorial](https://docs.python.org/3/tutorial/) · [Real Python](https://realpython.com/) |
| Typing | [typing docs](https://docs.python.org/3/library/typing.html) |
| Async | [asyncio docs](https://docs.python.org/3/library/asyncio.html) |
| FastAPI | [FastAPI docs](https://fastapi.tiangolo.com/) · [Pydantic docs](https://docs.pydantic.dev/) |
| DevOps | [GitHub Actions](https://docs.github.com/actions) · [Docker](https://docs.docker.com/) |
| DSA | [NeetCode](https://neetcode.io/roadmap) · [LeetCode](https://leetcode.com/) |

---

## Industrial Bar

- Type hints on all public APIs.
- `CODE.md` follows [.agent.md](./.agent.md) §3.
- Exercises use [docs/RUBRIC.md](./docs/RUBRIC.md) scoring and gate system (G1–G8).
- Every exercise file contains inline assert self-checks.
- DSA files include visuals + time/space complexity.
- Never copy proprietary text. Rewrite in repo style per [docs/SOURCE_REGISTRY.md](./docs/SOURCE_REGISTRY.md).

---

## Scheduling

- DSA Week `n` maps to Python days `5n-4` through `5n` (strict) or same phase (flexible).
- Sunday labs: finish before next phase milestone.
- This file is the planning source of truth.
