# Prompt Templates — Copy-Paste Playbook

> **Required files:** `.agent.md` (generation rules) · `docs/RUBRIC.md` (scoring & evaluation).
> **Look up first:** `DAILY_STUDY_PLAN.md` → day/week, slug, subtopics, primary source URL.

---

## Generate a Python day

```
@.agent.md @docs/RUBRIC.md @DAILY_STUDY_PLAN.md @docs/SOURCE_REGISTRY.md

Generate Day [NN] — [topic] (<track>, day_XX_<slug>).
Primary source: [URL from DAILY_STUDY_PLAN.md].
Create 5 files per .agent.md §3. Mirror the source's concept order.
Pass gates G1–G7. End with file list + self-check commands.
```

---

## Generate a DSA week

```
@.agent.md @docs/RUBRIC.md @DAILY_STUDY_PLAN.md @docs/SOURCE_REGISTRY.md

Generate DSA Week [WW] — [topic] (dsa, week_WW_<slug>).
Primary source: [URL]. LeetCode: [URLs from SOURCE_REGISTRY.md].
Create 5 files per .agent.md §3 + §4 (DSA extras).
Include Visual/Diagram section, traversal blocks, Big-O section.
Cover all subtopics from DAILY_STUDY_PLAN.md row.
Pass gates G1–G7. End with file list + self-check commands.
```

---

## Generate only CODE (study first)

```
@.agent.md @DAILY_STUDY_PLAN.md @docs/SOURCE_REGISTRY.md

Generate ONLY src/<track>/day_XX_<slug>/CODE.md + code.py.
Day [NN] — [topic]. Primary source: [URL].
Mirror source order. Do NOT create exercise files.
```

---

## Generate only exercises

```
@.agent.md @docs/RUBRIC.md @DAILY_STUDY_PLAN.md @docs/SOURCE_REGISTRY.md

Generate ONLY exercise/<track>/day_XX_<slug>/ (EXERCISE.md + ex01–ex03).
Day [NN] — [topic]. Do NOT create CODE.md or code.py.
```

---

## Evaluate your solution

```
@.agent.md @docs/RUBRIC.md

Grade Day [NN] at exercise/<track>/day_XX_<slug>/.
Follow docs/RUBRIC.md §4 evaluation protocol exactly.
```

---

## Batch generation

```
@.agent.md @docs/RUBRIC.md @DAILY_STUDY_PLAN.md @docs/SOURCE_REGISTRY.md

Generate these days as a batch (5 files each, per .agent.md §3):
- Day [NN] — [topic] (<track>, day_XX_<slug>) — Source: [URL]
- Day [NN+1] — [topic] (<track>, day_XX_<slug>) — Source: [URL]
Validate G1–G7 per day. End with combined self-check commands.
```

---

## Rework (after evaluation fails)

```
@.agent.md @docs/RUBRIC.md

Fix these issues from Day [NN] evaluation:
1. [paste issue]
2. [paste issue]
Files: exercise/<track>/day_XX_<slug>/exNN_*.py
Fix only listed issues. Maintain G1–G7. Re-run ruff + asserts.
```
