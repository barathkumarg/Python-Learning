# Daily Study Plan

> **This is the single entry point.** It answers one question: *what do I do each day?*
> Everything else is reference — see **Where things live** below.

---

## The Daily Loop (4 steps)

Do these in order. Study before you practise. Practise closed-book.

### 1. Generate

- Open the day in the track file → `study_plan/<track>.md`.
  Read its **Prerequisites, Real-world use, Production example, Sources**, and the
  A-Z **Concept Checklist**.
- Run the **generate prompt** from [docs/PROMPT_TEMPLATES.md](./docs/PROMPT_TEMPLATES.md).
- Output: 6 files —
  `src/<track>/<unit>/{CODE.md, code.py}` and
  `exercise/<track>/<unit>/{EXERCISE.md, ex01_basic.py, ex02_intermediate.py, ex03_advanced.py}`.

### 2. Study

- Read `src/<track>/<unit>/CODE.md`, then `code.py`.
- Run it and confirm output matches the `# Expected output:` comments:
  ```bash
  python src/<track>/<unit>/code.py
  ```

### 3. Practise

- Solve `ex01 → ex02 → ex03` **closed-book** (don't peek at `code.py`).
- Each file must pass its inline asserts and lint before you move on:
  ```bash
  ruff check exercise/<track>/<unit>/
  python exercise/<track>/<unit>/ex01_basic.py
  python exercise/<track>/<unit>/ex02_intermediate.py
  python exercise/<track>/<unit>/ex03_advanced.py
  ```

### 4. Evaluate & Record

- Run the **evaluate prompt** from [docs/RUBRIC.md §4](./docs/RUBRIC.md). It grades
  against gates G1–G8 and dimensions D1–D7, appends an evaluation report to
  `EXERCISE.md`, and updates [docs/SCORE_TRACKER.md](./docs/SCORE_TRACKER.md).
- **Gate:** `< 75` on any file or any gate fail → **rework** (max 3 cycles).
  `≥ 75` on all → advance to the next day.

---

## Where things live

| Question | File |
|----------|------|
| What do I do each day? | **this file** |
| What / how deep to learn per topic? | `study_plan/<track>.md` (checklists, prereqs, production example, sources) |
| Prompts to generate & evaluate | [docs/PROMPT_TEMPLATES.md](./docs/PROMPT_TEMPLATES.md) |
| Where content comes from (source URLs) | [docs/SOURCE_REGISTRY.md](./docs/SOURCE_REGISTRY.md) |
| How content is generated (rules) | [.agent.md](./.agent.md) |
| How it's graded — gates G1–G8, scoring | [docs/RUBRIC.md](./docs/RUBRIC.md) *(single source)* |
| My recorded progress | [docs/SCORE_TRACKER.md](./docs/SCORE_TRACKER.md) |
| DSA diagram templates | [docs/DSA_VISUALS.md](./docs/DSA_VISUALS.md) |

---

## Industrial learning bar

- **Study before practise** — read the reference, then solve from memory.
- **Closed-book practice** — active recall; don't copy `code.py`.
- **Everything runs green** — every file passes `ruff` + asserts before evaluation.
- **Grade to advance** — `≥ 75` all files, all gates; rework weak days (3-cycle cap).
- **Production-anchored** — each day builds the topic's real-world Production
  example, not toy snippets.

---

## Phases & tracks

| Phase | Days | Track | Study plan |
|-------|------|-------|------------|
| 1 | 01–14 | `python_basic` | [study_plan/python_basic.md](./study_plan/python_basic.md) |
| 2 | 15–34 | `python_intermediate` | [study_plan/python_intermediate.md](./study_plan/python_intermediate.md) |
| 3 | 35–50 | `python_concurrency` | [study_plan/python_concurrency.md](./study_plan/python_concurrency.md) |
| 4 | 51–70 | `python_advanced` | [study_plan/python_advanced.md](./study_plan/python_advanced.md) |
| 5 | 71–86 | `fastapi_track` | [study_plan/fastapi_track.md](./study_plan/fastapi_track.md) |
| 6 | 87–100 | `devops_track` | [study_plan/devops_track.md](./study_plan/devops_track.md) |
| DSA | Weeks 01–20 | `dsa` | [study_plan/dsa.md](./study_plan/dsa.md) |

**Layout:** `src/<track>/day_NN_slug/` (reference) · `exercise/<track>/day_NN_slug/`
(practice). DSA uses `week_WW_slug/`.

---

## Time budget & scheduling

| Block | Time |
|-------|------|
| Python day | 60–90 min |
| DSA week | 45–90 min |
| Sunday lab | 90–120 min |
| Quality pass (ruff + asserts) | 15 min |

- **DSA scheduling:** Week `n` runs parallel to Python days `5n-4` … `5n`.
- **Sunday labs:** finish before the next phase milestone.
