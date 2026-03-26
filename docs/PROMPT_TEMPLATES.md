# Prompt Templates — Generate → Study → Solve → Evaluate

Your **copy-paste playbook** for daily workflow. Normative references:

- [.agent.md](../.agent.md) — what to generate
- [docs/CODE_TEMPLATE.md](./CODE_TEMPLATE.md) — CODE.md structure
- [docs/EVALUATION_RUBRIC.md](./EVALUATION_RUBRIC.md) — gates G1–G7, scoring
- [docs/AI_EVAL_FRAMEWORK.md](./AI_EVAL_FRAMEWORK.md) — evaluation protocol
- [DAILY_STUDY_PLAN.md](../DAILY_STUDY_PLAN.md) — day/week + track + slugs

**Fill in:** `[NN]`, `[topic]`, `<track>`, `day_XX_<slug>` from your study plan.

---

## §1 Quick-fire one-liners (daily use — copy and go)

These are the prompts you'll fire most often. Copy, fill in the blanks, paste into your AI agent.

**Generate a Python day:**
```
@.agent.md @docs/CODE_TEMPLATE.md @docs/EVALUATION_RUBRIC.md @DAILY_STUDY_PLAN.md
Generate Day [NN] — [topic] (<track>, day_XX_<slug>). 5-file output.
```

**Generate a DSA week:**
```
@.agent.md @docs/CODE_TEMPLATE.md @docs/EVALUATION_RUBRIC.md @DAILY_STUDY_PLAN.md
Generate DSA Week [WW] — [topic] (dsa, week_WW_<slug>). Include ASCII/Mermaid diagrams in CODE.md.
```

**Evaluate your solution:**
```
@docs/AI_EVAL_FRAMEWORK.md @docs/EVALUATION_RUBRIC.md
Grade my Day [NN] at exercise/<track>/day_XX_<slug>/.
```

---

## §2 Full Day module — Python

Use when starting a **new Python day**. Generates all 5 files.

````
You are following .agent.md, docs/CODE_TEMPLATE.md, and docs/EVALUATION_RUBRIC.md for this repo.

Generate the complete module for:
- Day: [NN]
- Topic: [topic]
- Track: <track>
- Slug: day_XX_<content>

Read README.md, DAILY_STUDY_PLAN.md (this day's row), and docs/EVALUATION_RUBRIC.md before writing.

Create exactly these artifacts:

1) src/<track>/day_XX_<content>/CODE.md
   - Follow docs/CODE_TEMPLATE.md structure exactly (≤120 lines).
   - TL;DR → Concepts table → Snippets (3–5 key concepts, each: short code block + 1–2 line explanation) → Pitfalls → Why this design → Further reading.

2) src/<track>/day_XX_<content>/code.py
   - Module docstring explaining design choices.
   - 3–5 production-quality reference examples with type hints and docstrings.

3) exercise/<track>/day_XX_<content>/EXERCISE.md
   - Learning objectives (2–4 bullets).
   - Skills assessed: list Skill IDs from docs/EVALUATION_RUBRIC.md §0 with exercise mapping.
   - Per-exercise specs: must-pass, stretch, failure modes.
   - Scoring section: 0–100 breakdown per file + dimension weights from docs/EVALUATION_RUBRIC.md.
   - Suggested Practice section: 1–2 external links (LeetCode/NeetCode/docs) related to the day's topic.

4) exercise/<track>/day_XX_<content>/ex01_basic.py
5) exercise/<track>/day_XX_<content>/ex02_intermediate.py
6) exercise/<track>/day_XX_<content>/ex03_advanced.py
   - Starter stubs: function/class skeletons + TODO comments.
   - Do NOT provide full implementations.
   - Module docstring with: problem statement, signature, constraints, 2+ examples.
   - Each TODO includes sample input → expected output.
   - if __name__ == "__main__": block with 2–3 inline assert statements for self-check.
   - Use raise NotImplementedError() for unimplemented bodies.

Industrial checklist: enforce docs/EVALUATION_RUBRIC.md §1 gates G1–G7.

End with: file list and self-check commands:
  python ex01_basic.py && python ex02_intermediate.py && python ex03_advanced.py
  ruff check exercise/<track>/day_XX_<content>/
````

---

## §3 Full DSA week module

Use when starting a **new DSA week**. Generates all 5 files with mandatory visual diagrams.

````
You are following .agent.md, docs/CODE_TEMPLATE.md, and docs/EVALUATION_RUBRIC.md for this repo.

Generate the complete DSA module for:
- Week: [WW]
- Topic: [topic]
- Slug: week_WW_<content>

Read DAILY_STUDY_PLAN.md (this week's section under "Parallel DSA") before writing.

Create exactly these artifacts:

1) src/dsa/week_WW_<content>/CODE.md
   - Follow docs/CODE_TEMPLATE.md structure (≤120 lines).
   - MUST include a Visual/Diagram section with ASCII art or Mermaid diagram
     showing the data structure and/or algorithm flow.
   - MUST include Snippets section: 3–5 key operations, each with a short code block + 1–2 line explanation.
   - Use the DSA diagram style guide in docs/CODE_TEMPLATE.md to pick the right visual.
   - Concepts table must include time/space complexity for each operation.

2) src/dsa/week_WW_<content>/code.py
   - Reference implementations with complexity stated in every docstring.
   - Use your own examples — do NOT copy proprietary problem text verbatim.

3) exercise/dsa/week_WW_<content>/EXERCISE.md
   - Learning objectives with complexity awareness.   - Skills assessed: list Skill IDs from docs/EVALUATION_RUBRIC.md §0 (DSA section) with exercise mapping.   - Per-exercise specs: must-pass, stretch, failure modes, expected big-O.
   - Scoring section: 0–100 breakdown per file + dimension weights.
   - Suggested Practice: link the specific LeetCode/NeetCode problems listed in DAILY_STUDY_PLAN.md for this week.

4) exercise/dsa/week_WW_<content>/ex01_basic.py
5) exercise/dsa/week_WW_<content>/ex02_intermediate.py
6) exercise/dsa/week_WW_<content>/ex03_advanced.py
   - Stubs with TODO comments including expected complexity.
   - Module docstring with problem statement, signature, constraints, 2+ examples.
   - if __name__ == "__main__": block with 2–3 inline assert statements.

Enforce gates G1–G7 (G3 = inline asserts + complexity in docstrings).

End with: file list and self-check commands.
````

---

## §4 Generate only CODE (study first, exercise later)

```
@.agent.md @docs/CODE_TEMPLATE.md
Generate ONLY:
- src/<track>/day_XX_<content>/CODE.md  (follow docs/CODE_TEMPLATE.md)
- src/<track>/day_XX_<content>/code.py

For DSA: include Visual/Diagram section in CODE.md with ASCII/Mermaid per the diagram style guide.
Do NOT create exercise/ files in this pass.
```

---

## §5 Generate only exercises (after CODE is done)

```
@.agent.md @docs/EVALUATION_RUBRIC.md
Generate ONLY under exercise/<track>/day_XX_<content>/:

- EXERCISE.md (objectives, per-exercise specs, scoring 0–100, suggested practice links)
- ex01_basic.py, ex02_intermediate.py, ex03_advanced.py
  (stubs with TODOs, inline assert runners in __main__, no full implementations)

Do NOT create CODE.md, code.py, EVALUATION.md, or test_exercises.py.
```

---

## §6 Self-check (after implementing exercises)

Run before requesting AI evaluation:

```bash
# Lint
ruff check exercise/<track>/day_XX_<content>/

# Inline assert checks
python exercise/<track>/day_XX_<content>/ex01_basic.py
python exercise/<track>/day_XX_<content>/ex02_intermediate.py
python exercise/<track>/day_XX_<content>/ex03_advanced.py
```

All 3 scripts must exit cleanly. Then score locally using `EXERCISE.md` scoring section.

---

## §7 Agent evaluation (after your solution is implemented)

Use the full template from [docs/AI_EVAL_FRAMEWORK.md §2](./AI_EVAL_FRAMEWORK.md):

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
2) Dimension scores D1–D7 (1–5) + weighted total.
3) Per-file scores for ex01, ex02, ex03 (0–100) with breakdown.
4) Skills assessed: list each Skill ID from EXERCISE.md, rate proficiency (learning/developing/proficient/strong).
5) Top 3 concrete improvements (code-level, with file:line references).
6) One rewritten snippet fixing the worst issue found.
7) Verdict: PASS (≥75 all files) or REWORK (which file + criterion to fix).
```

Feedback loop (from [AI_EVAL_FRAMEWORK.md §4](./AI_EVAL_FRAMEWORK.md)):
- **< 75** → fix weakest criterion and re-evaluate.
- **≥ 75** → pass, proceed to next day.
- **≥ 90** → strong pass, skip stretch if desired.
