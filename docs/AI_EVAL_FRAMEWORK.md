# AI Evaluation Framework

This repo uses **AI-based evaluation** instead of pytest for grading exercise solutions. The AI agent reviews your code against the day's `EXERCISE.md` specs and the universal rubric in [EVALUATION_RUBRIC.md](./EVALUATION_RUBRIC.md).

---

## §1 When to evaluate

Trigger an AI evaluation **after** you have:

1. Completed all 3 exercise files (`ex01_basic.py`, `ex02_intermediate.py`, `ex03_advanced.py`).
2. Run each file — `python exNN.py` — and confirmed inline asserts pass.
3. Run `ruff check exercise/<track>/day_NN_topic/` with no errors.

---

## §2 Submission prompt template

Copy-paste this into your AI agent (Cursor / Copilot / CLI) after completing a day:

```
@docs/AI_EVAL_FRAMEWORK.md @docs/EVALUATION_RUBRIC.md

Grade my solution for:
- Day: [NN]
- Topic: [topic]
- Track: <track>
- Folder: exercise/<track>/day_XX_<content>/

Read the EXERCISE.md in that folder for must-pass, stretch, and scoring criteria.

My solution files:
- ex01_basic.py: [attach or path]
- ex02_intermediate.py: [attach or path]
- ex03_advanced.py: [attach or path]

Deliver exactly:
1) Gate table: G1–G7 — pass/fail with one-line evidence each.
   (G3 = inline asserts pass + AI behavioral review, NOT pytest.)
   For DSA submissions, include evidence that time/space complexity is present in `CODE.md`, `EXERCISE.md`, and DSA function docstrings.
   For DSA submissions, also confirm the week's advanced subtopics from `DAILY_STUDY_PLAN.md` are actually covered.
2) Dimension scores D1–D7 (1–5) + weighted total per docs/EVALUATION_RUBRIC.md §2.
3) Per-file scores for ex01, ex02, ex03 (0–100) with breakdown per EXERCISE.md scoring section.
4) Skills assessed: list each Skill ID from EXERCISE.md, rate proficiency (learning / developing / proficient / strong).
5) Top 3 concrete improvements (code-level, with file:line references).
6) One rewritten snippet fixing the worst issue found.
7) Verdict: PASS (≥75 all files) or REWORK (which file + criterion to fix).

Append the full report to the EXERCISE.md under an ## Evaluation report heading.
```

---

## §3 Expected AI output format

The evaluating agent must produce:

### 3a. Gate checklist

| Gate | Pass/Fail | Evidence |
|------|-----------|----------|
| G1 Type hints | ✅/❌ | one-line proof |
| G2 Explicit errors | ✅/❌ | one-line proof |
| G3 Inline asserts + behavior coverage | ✅/❌ | "all asserts pass; AI confirms must-pass behaviors X, Y, Z are implemented" |
| G4 Ruff-clean | ✅/❌ | one-line proof |
| G5 Docstrings | ✅/❌ | one-line proof |
| G6 Security | ✅/❌ | one-line proof |
| G7 Observability | ✅/❌ | one-line proof or N/A |

For DSA evaluations, G3 evidence must also confirm:
- complexity is stated for each discussed problem in `EXERCISE.md`
- complexity is present in DSA function docstrings (`code.py` and `exNN_*.py`)
- row-listed weekly DSA subtopics are not skipped in generated artifacts
- snippet-level traversal visuals are present for DSA `CODE.md` examples

### 3b. Dimension scores

| Dimension | Score (1–5) | Notes |
|-----------|-------------|-------|
| D1 Correctness (0.30) | | |
| D2 Reliability (0.15) | | |
| D3 Maintainability (0.15) | | |
| D4 API & typing (0.10) | | |
| D5 Performance (0.10) | | |
| D6 Security (0.10) | | |
| D7 Code quality (0.10) | | |
| **Weighted total** | | |

### 3c. Per-file scores (0–100)

| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | | | |
| Stretch behaviors (15) | | | |
| Inline asserts + AI behavior coverage (25) | | | |
| Style — types, ruff, docstrings (20) | | | |
| **Total** | | | |

### 3d. Top 3 improvements

Numbered list with `file:line` references and concrete fix descriptions.

### 3e. Rewritten snippet

Minimal code showing the best-practice fix for the worst issue.

---

## §4 Feedback loop

| Score | Action |
|-------|--------|
| **< 75 on any file** | AI suggests targeted rework on the weakest criterion. Fix and re-evaluate. |
| **≥ 75 on all files** | Day passes. Proceed to next day. |
| **≥ 90 on all files** | Strong pass. Skip remaining stretch goals if desired. Move on. |

**Iteration cap:** If a file stays < 75 after 3 rework cycles, log the gap in your commit message and move on — revisit during the next Sunday lab.

---

## §5 Quick self-check (before AI eval)

Run these before submitting to the AI — catches 80% of issues:

```bash
# Lint check
ruff check exercise/<track>/day_XX_<content>/

# Run inline asserts in each exercise
python exercise/<track>/day_XX_<content>/ex01_basic.py
python exercise/<track>/day_XX_<content>/ex02_intermediate.py
python exercise/<track>/day_XX_<content>/ex03_advanced.py
```

All 3 scripts must exit cleanly (no `AssertionError`, no traceback) before requesting AI evaluation.

---

## §6 Progress logging

Use this commit message format after a passing evaluation:

```
study: day [NN] <track> weighted [X.X] ex01 [YY]/100 ex02 [YY]/100 ex03 [YY]/100
```

Example:
```
study: day 08 python_basic weighted 4.1 ex01 88/100 ex02 82/100 ex03 76/100
```

For DSA weeks:
```
study: dsa week [WW] weighted [X.X] ex01 [YY]/100 ex02 [YY]/100 ex03 [YY]/100
```

---

## §7 Agent compatibility

This framework is designed to work with **any AI agent** (Cursor, GitHub Copilot, ChatGPT, Claude, Gemini, local LLMs, etc.).

### How any agent can evaluate

1. **Context required:** The agent needs access to these files (paste, attach, or `@`-reference):
   - `docs/AI_EVAL_FRAMEWORK.md` (this file) — evaluation protocol
   - `docs/EVALUATION_RUBRIC.md` — gates, dimensions, skills taxonomy
   - `exercise/<track>/day_NN_topic/EXERCISE.md` — day-specific specs + skills
   - The 3 solution files (`ex01`, `ex02`, `ex03`)

2. **No tool dependencies:** The evaluation does not require pytest, mypy, or any tooling. The agent reviews code against specs and produces a structured report. Optional: ask the learner to paste `ruff check` output.

3. **Output contract:** Every agent must produce the report in the **exact structure** defined in §3 (gate table → dimensions → per-file scores → improvements → snippet). This ensures reports are comparable across agents and sessions.

### Agent-agnostic evaluation prompt (universal)

This prompt works in **any** AI chat interface — no `@`-references needed:

```
You are evaluating Python exercises for an industrial-level learning repo.

Context files (pasted below or attached):
- EXERCISE.md: contains exercise specs, skills assessed, and scoring criteria
- EVALUATION_RUBRIC.md: contains gate checklist G1–G7, dimension weights D1–D7, and skills taxonomy
- AI_EVAL_FRAMEWORK.md: contains the output format you must follow

Student solution files (pasted below or attached):
- ex01_basic.py
- ex02_intermediate.py
- ex03_advanced.py

Produce your evaluation in this exact order:
1. Gate checklist: G1–G7, pass/fail, one-line evidence each.
2. Dimension scores: D1–D7, score 1–5, weighted total.
3. Per-file scores: 0–100 with criterion breakdown.
4. Skills assessed: list each skill ID from EXERCISE.md and rate proficiency (learning / developing / proficient / strong).
5. Top 3 improvements with file:line references.
6. One rewritten snippet for the worst issue.
7. Verdict: PASS (≥75 all files) or REWORK (file + criterion to fix).
```

### Report persistence

After evaluation, the report is **appended to the day's `EXERCISE.md`** under an `## Evaluation report` heading. This makes the report:
- Portable — lives with the exercise, not in chat history
- Diffable — tracked by git
- Readable by any future agent — next session can read prior scores

---

## §8 Structured report schema

For machine-parseability across agents, evaluation reports in `EXERCISE.md` should follow this structure:

```markdown
## Evaluation report — YYYY-MM-DD

### Skills assessed
| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| PY-XX | ... | ex01/ex02/ex03 | learning / developing / proficient / strong |

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
| **Status** | ✅/❌ | ✅/❌ | ✅/❌ |

### Action items
1. ...

### Verdict
PASS / REWORK — commit message
```

Any agent reading a prior `EXERCISE.md` can parse this to understand:
- What skills were tested and at what proficiency
- What the scores were
- What needs rework before the next day
