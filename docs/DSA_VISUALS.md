# DSA Visuals Guide (ASCII, Mermaid, Optional GIF)

Use this guide when generating DSA `CODE.md` files.

## 1) Baseline requirement (always)

- Every core algorithm/topic in a DSA week must have a visual explanation.
- Every snippet/example in DSA `CODE.md` must have a mini traversal visual immediately below expected output.
- Baseline visuals must be plain markdown friendly:
  - ASCII diagrams
  - Mermaid diagrams

This baseline is mandatory even if GIFs are added.

## 2) Optional GIF support

GIFs are optional and should only be used when they improve understanding (pointer movement, window shift, traversal order).

If you add a GIF:
- Keep ASCII/Mermaid fallback in the same section.
- Add a one-line caption explaining what to observe.
- Prefer repo-local assets when available (for example `docs/assets/dsa_gifs/...`).
- If using an external GIF URL, include a stable source link in "Further reading".

## 3) Recommended placement in `CODE.md`

Place visuals in this order:

1. Snippet-level traversal visual under each example.
2. Section-level static visual (ASCII or Mermaid) for structure.
3. Optional GIF for dynamic behavior.
4. One-line interpretation + complexity tie-in.

## 4) Copy-paste template

````markdown
**`snippet_name`**
```python
# code
```
Expected output:
```text
# output
```
Traversal (graphical):
```text
# step-by-step states for this snippet
```

## Visual / Diagram

```text
[ASCII fallback diagram]
```

```mermaid
graph LR
...
```

![Optional: pointer movement GIF](../../docs/assets/dsa_gifs/week_XX_topic.gif)

Caption: Observe how the pointer/window/traversal state changes each step.
Complexity tie-in: Time `O(...)`, Space `O(...)`.
````

## 5) Week-specific suggestions

- Week 03 (Two pointers, 3Sum): show fixed `i` with `left/right` convergence and duplicate skipping.
- Week 04 (Sliding window): show window expansion/shrink and deque front eviction.
- Week 08 (Binary trees): show traversal order and path decisions (LCA/diameter intuition).
- Week 11 (Recursion): show processed/unprocessed recursion tree for subsequence generation.
- Week 19 (String algorithms): show rolling-hash window updates (Rabin-Karp) and prefix-map transitions (KMP `k-map` / LPS).
- Week 20 (Sorting): show partition steps (quick sort) or merge levels (merge sort).
