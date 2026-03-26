# Prompt templates (generate → implement → evaluate)

Use this file as your **copy-paste playbook**. Normative rules:
1. [.agent.md](../.agent.md) (what to generate)
2. [docs/EVALUATION_RUBRIC.md](./EVALUATION_RUBRIC.md) (gates + scoring dimensions)
3. [DAILY_STUDY_PLAN.md](../DAILY_STUDY_PLAN.md) (day/week + track + slugs)

**Fill in:** `[NN]`, `[topic]`, `<track>`, `day_<NN>_slug` / `dayNN_slug` from your study plan.

---

## 1. Generate full Day module (CODE + EXERCISES + EVALUATION + tests)

Use when starting a **new day**.

```
You are following .agent.md and docs/EVALUATION_RUBRIC.md for this repo.

Generate the complete module for:
- Day: [NN]
- Topic: [topic]
- Track: <track>
- Day slug: day_XX_<content>   (used for both src and exercise folders)

Read README.md, DAILY_STUDY_PLAN.md (this day’s row), and docs/EVALUATION_RUBRIC.md before writing files.

Create exactly these artifacts:

1) src/<track>/day_XX_<content>/CODE.md
2) src/<track>/day_XX_<content>/code.py
   - Put concept explanation in the module docstring.
   - Include 3–5 industrial examples as reference code.

3) exercise/<track>/day_XX_<content>/EXERCISE.md
4) exercise/<track>/day_XX_<content>/EVALUATION.md

5) exercise/<track>/day_XX_<content>/ex01_basic.py
6) exercise/<track>/day_XX_<content>/ex02_intermediate.py
7) exercise/<track>/day_XX_<content>/ex03_advanced.py
   - These must be starter stubs: function/class skeletons + TODO comments.
   - Do NOT provide the full implementation.
   - Use "complete the function logic" style.
   - Each file must start with a module docstring containing: problem statement, function signature, constraints, and at least 2 examples.
   - Each TODO comment must include at least one sample input → expected output line in the same comment block.
   - Add a minimal `if __name__ == "__main__":` runner so learners can execute sample cases interactively.

8) exercise/<track>/day_XX_<content>/test_exercises.py
   - pytest tests for the must-pass behaviors. Tests should fail until the learner implements the stubs.

Industrial checklist: enforce docs/EVALUATION_RUBRIC.md §1 gates G1–G7.

End with: file list, `pytest` command, and the “done” threshold taken from exercise/<track>/.../EVALUATION.md.
```

---

## 2. Generate only CODE (no exercises yet)

Use if you want to learn first.

```
Generate ONLY:
- src/<track>/day_XX_<content>/CODE.md
- src/<track>/day_XX_<content>/code.py

Follow .agent.md and keep the content as reference/teaching code.
Do NOT create exercise/ files in this pass.
```

---

## 3. Generate only exercises (stubs + EXERCISE.md + EVALUATION.md + tests)

Use after CODE is done or to regenerate exercises.

```
Generate ONLY under:
exercise/<track>/day_XX_<content>/

Create:
- EXERCISE.md
- EVALUATION.md (aligned with docs/EVALUATION_RUBRIC.md)
- ex01_basic.py, ex02_intermediate.py, ex03_advanced.py (stubs/TODOs; no full implementations)
  - platform style: docstring problem + function signature + examples + minimal interactive runner
- test_exercises.py (pytest)

Do NOT duplicate the full reference code as learner implementations.
```

---

## 4. After you implement exercises — self-check

Run:
```bash
ruff check exercise/<track>/day_XX_<content>/
pytest exercise/<track>/day_XX_<content>/test_exercises.py -v
```

Then score locally using `exercise/.../EVALUATION.md` thresholds (your agent rubric for that day).
If you want deeper inspection: run `mypy` if configured.

---

## 5. Agent evaluation (after your solution is implemented)

Paste your files/solutions and use:

```
You are grading per docs/EVALUATION_RUBRIC.md and exercise/<track>/day_XX_<content>/EVALUATION.md.

Context:
- Day: [NN]
- Topic: [topic]
- Track: <track>
- Folder: exercise/<track>/day_XX_<content>/

My solution:
- ex01_basic.py: [attach or path]
- ex02_intermediate.py: [attach or path]
- ex03_advanced.py: [attach or path]

Deliver exactly:
1) Gate table: G1–G7 pass/fail with one-line evidence each.
2) Dimension scores D1–D7 (1–5) + weighted total (from docs/EVALUATION_RUBRIC.md).
3) Per-file scores for ex01, ex02, ex03 (0–100) with breakdown.
4) Top 3 concrete improvements (code-level).
5) Optional: minimal rewritten snippet fixing the worst issue.
```

---

## 6. Minimal “daily” one-liners

Generate:
```
@.agent.md @docs/EVALUATION_RUBRIC.md @DAILY_STUDY_PLAN.md
Full module for Day [NN] (<track>, day_XX_<content>).
```

Evaluate:
```
@docs/EVALUATION_RUBRIC.md
Grade my Day [NN] at exercise/<track>/day_XX_<content>/.
```
