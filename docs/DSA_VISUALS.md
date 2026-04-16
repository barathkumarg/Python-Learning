# DSA Visuals Guide — ASCII, Mermaid, Flowcharts & Optional GIF

> **Purpose:** Reference-only lookup for Mermaid templates and visual suggestions per DSA week. Not required reading — `.agent.md §4` contains all the rules you need for generation.  
> **Companion:** [.agent.md](../.agent.md) · [RUBRIC.md](./RUBRIC.md)

---

## §1 — Baseline Requirements (Mandatory)

Every DSA `CODE.md` must include:

| Visual Type | Where | Format | Required |
|------------|-------|--------|----------|
| Traversal block | Under each snippet's expected output | ASCII step-by-step | ✅ Always |
| Algorithm-decision flowchart | Visual/Diagram section | Mermaid `flowchart` | ✅ Always |
| Step-by-step traversal diagram | Visual/Diagram section | Mermaid or ASCII | ✅ Always |
| Complexity comparison chart | Visual/Diagram section | ASCII table | ✅ Always |
| Section-level structure diagram | Visual/Diagram section | ASCII or Mermaid | ✅ Always |
| GIF animation | Visual/Diagram section | `.gif` with caption | ⭐ Optional |

**Minimum per DSA `CODE.md`:** 3 diagrams in the Visual/Diagram section:
1. One **algorithm-decision flowchart** (when to use which approach)
2. One **step-by-step traversal** (how the algorithm processes data)
3. One **complexity comparison chart** (brute vs optimal)

---

## §2 — Mermaid Rendering Notes

Mermaid renders natively on **GitHub**, **GitLab**, **Notion**, and **VS Code** (with extensions).

### Flowchart Syntax Quick Reference

```mermaid
flowchart TD
    A[Start] --> B{Decision?}
    B -- Yes --> C[Action A]
    B -- No --> D[Action B]
    C --> E[End]
    D --> E
```

### Style Guide for DSA Flowcharts

| Node Type | Shape | Color | Example |
|-----------|-------|-------|---------|
| Start/Input | `[rectangle]` | Default | `A[Read array]` |
| Decision | `{diamond}` | Default | `B{Element in set?}` |
| Success/Return | `[rectangle]` | Green `fill:#2d6` | `C[Return result]` |
| Failure/Error | `[rectangle]` | Red `fill:#d44` | `D[Raise error]` |
| Process step | `[rectangle]` | Default | `E[Update pointer]` |
| Data structure | `([rounded])` | Blue `fill:#26d` | `F([Hash Map])` |

### ASCII Fallback Rule

Every Mermaid diagram must have an ASCII fallback **above or below** it for portability:

```text
[ASCII version of the same diagram]
```

```mermaid
flowchart ...
[Mermaid version]
```

---

## §3 — Snippet-Level Traversal Template

Place this under every DSA snippet's expected output:

````markdown
**`function_name`** — one-line description.
```python
# code snippet
```
Expected output:
```text
function_name([input]) -> output
```
Complexity: `Time O(...)`, `Space O(...)`.
Traversal (graphical):
```text
input = [...]
state = {}
step1: read X -> action -> state={...}
step2: read Y -> action -> state={...}
...
stepN: condition met -> return result
```
> One-line insight about this pattern.
````

---

## §4 — Visual/Diagram Section Template

Place this section after all snippets, before Pitfalls:

````markdown
## Visual / Diagram

### Algorithm Decision Flowchart — [Topic Name]

```text
[ASCII decision tree fallback]
```

```mermaid
flowchart TD
    A[Problem type?] --> B{Characteristic?}
    B -- Option 1 --> C[Approach 1 — O'...']
    B -- Option 2 --> D[Approach 2 — O'...']
    style C fill:#2d6,stroke:#333
    style D fill:#26d,stroke:#333
```

### Step-by-Step Traversal — [Algorithm Name]

```text
[ASCII step-by-step walkthrough]
```

```mermaid
flowchart LR
    A[Step 1] --> B[Step 2] --> C{Check} --> D[Step 3]
```

### Complexity Comparison Chart

```text
┌─────────────┬──────────┬──────────┬──────────────────┐
│ Problem      │ Brute    │ Optimal  │ Key insight       │
├─────────────┼──────────┼──────────┼──────────────────┤
│ Problem 1    │ O(n²)    │ O(n)     │ Insight here      │
│ Problem 2    │ O(n²)    │ O(n lg)  │ Insight here      │
└─────────────┴──────────┴──────────┴──────────────────┘
```
````

---

## §5 — Optional GIF Support

GIFs are optional and should only be used when they improve understanding (pointer movement, window shift, traversal order).

**If you add a GIF:**
- Keep ASCII/Mermaid fallback in the same section (mandatory).
- Add a one-line caption explaining what to observe.
- Prefer repo-local assets: `docs/assets/dsa_gifs/week_XX_topic.gif`.
- If using an external URL, include a stable source link in "Further reading".

```markdown
![Optional: pointer movement GIF](../../docs/assets/dsa_gifs/week_XX_topic.gif)

Caption: Observe how the pointer/window/traversal state changes each step.
Complexity tie-in: Time `O(...)`, Space `O(...)`.
```

---

## §6 — Per-Topic Flowchart Templates

Use these Mermaid templates as starting points for each DSA week's Visual/Diagram section.

### Week 01 — Arrays & Hashing: Data Structure Selection

```mermaid
flowchart TD
    A[What operation do you need?] --> B{Membership check?}
    B -- Yes --> C["Hash Set — O(1) avg"]
    A --> D{Key-value lookup?}
    D -- Yes --> E["Hash Map — O(1) avg"]
    A --> F{Count occurrences?}
    F -- Yes --> E
    A --> G{Group by property?}
    G -- Yes --> H["Hash Map + computed key"]
```

### Week 03 — Two Pointers: Pointer Movement

```mermaid
flowchart LR
    A["left=0, right=n-1"] --> B{sum == target?}
    B -- Yes --> C[Return pair]
    B -- "sum < target" --> D["left++ (need larger)"]
    B -- "sum > target" --> E["right-- (need smaller)"]
    D --> B
    E --> B
```

### Week 04 — Sliding Window: Window Expansion/Shrink

```mermaid
flowchart TD
    A[Initialize window start=0] --> B[Expand: add right element]
    B --> C{Window valid?}
    C -- Yes --> D[Update best answer]
    D --> E[Move right pointer]
    E --> B
    C -- No --> F[Shrink: remove left element]
    F --> G[Move left pointer]
    G --> C
```

### Week 05 — Stack: Monotonic Stack Pattern

```mermaid
flowchart TD
    A[Scan array left to right] --> B{Stack empty or current > top?}
    B -- Yes --> C[Push current index]
    B -- No --> D[Pop: current is 'next greater' for popped]
    D --> E[Record result for popped index]
    E --> B
    C --> F{More elements?}
    F -- Yes --> A
    F -- No --> G[Remaining stack items have no next greater]
```

### Week 06 — Binary Search: Search Space Halving

```mermaid
flowchart TD
    A["lo=0, hi=n-1"] --> B{lo <= hi?}
    B -- Yes --> C["mid = (lo+hi)//2"]
    C --> D{"arr[mid] == target?"}
    D -- Yes --> E[Return mid]
    D -- "arr[mid] < target" --> F["lo = mid+1"]
    D -- "arr[mid] > target" --> G["hi = mid-1"]
    F --> B
    G --> B
    B -- No --> H[Return -1 — not found]
```

### Week 08 — Binary Tree: DFS vs BFS Decision

```mermaid
flowchart TD
    A[Tree problem] --> B{Need level-by-level?}
    B -- Yes --> C["BFS with queue — O(n)"]
    B -- No --> D{Need path/depth?}
    D -- Yes --> E["DFS recursive — O(n)"]
    D -- No --> F{Need ordered output?}
    F -- Yes --> G["Inorder DFS — O(n)"]
    F -- No --> H["Any traversal works"]
```

### Week 11 — Backtracking: Include/Exclude Tree

```mermaid
flowchart TD
    A["f(index, current)"] --> B{Base case: index == n?}
    B -- Yes --> C[Record current as result]
    B -- No --> D["Include: f(index+1, current + [item])"]
    B -- No --> E["Exclude: f(index+1, current)"]
    D --> F{Pruning condition?}
    F -- Prune --> G[Backtrack early]
    F -- Continue --> A
```

### Week 12 — Graphs: BFS/DFS Traversal

```mermaid
flowchart TD
    A[Start from source node] --> B[Mark as visited]
    B --> C[Process neighbors]
    C --> D{Neighbor visited?}
    D -- Yes --> E[Skip]
    D -- No --> F[Add to queue/stack]
    F --> G{Queue/stack empty?}
    G -- No --> H[Pop next node]
    H --> B
    G -- Yes --> I[Traversal complete]
```

### Week 16 — DP: Memoization vs Tabulation

```mermaid
flowchart TD
    A[DP problem identified] --> B{Subproblem overlap?}
    B -- Yes --> C{Top-down natural?}
    C -- Yes --> D["Memoization (recursion + cache)"]
    C -- No --> E["Tabulation (iterative + table)"]
    B -- No --> F[Not a DP problem — use greedy/divide-conquer]
    D --> G["Space optimization possible?"]
    E --> G
    G -- Yes --> H["Reduce to O(1) or O(n) space"]
```

### Week 18 — Shortest Path: Algorithm Selection

```mermaid
flowchart TD
    A[Shortest path problem] --> B{Edge weights?}
    B -- Unweighted --> C["BFS — O(V+E)"]
    B -- Non-negative --> D["Dijkstra — O((V+E) log V)"]
    B -- Negative edges --> E{Negative cycles?}
    E -- No --> F["Bellman-Ford — O(V·E)"]
    E -- Yes --> G[No shortest path exists]
```

### Week 19 — Tries: Prefix Lookup

```mermaid
flowchart TD
    A[Start at root] --> B[Read next character]
    B --> C{Child exists?}
    C -- Yes --> D[Move to child node]
    D --> E{More characters?}
    E -- Yes --> B
    E -- No --> F{Is end-of-word?}
    F -- Yes --> G[Word found]
    F -- No --> H[Prefix exists, not a word]
    C -- No --> I[Not in trie]
```

### Week 20 — Sorting: Algorithm Comparison

```text
┌──────────────┬──────────┬──────────┬──────────┬─────────┬───────────┐
│ Algorithm    │ Best     │ Average  │ Worst    │ Space   │ Stable?   │
├──────────────┼──────────┼──────────┼──────────┼─────────┼───────────┤
│ Merge Sort   │ O(n lg)  │ O(n lg)  │ O(n lg)  │ O(n)    │ ✅ Yes    │
│ Quick Sort   │ O(n lg)  │ O(n lg)  │ O(n²)    │ O(lg n) │ ❌ No     │
│ Heap Sort    │ O(n lg)  │ O(n lg)  │ O(n lg)  │ O(1)    │ ❌ No     │
│ Counting     │ O(n+k)   │ O(n+k)   │ O(n+k)   │ O(k)    │ ✅ Yes    │
│ Python sort  │ O(n)     │ O(n lg)  │ O(n lg)  │ O(n)    │ ✅ Yes    │
└──────────────┴──────────┴──────────┴──────────┴─────────┴───────────┘
```

---

## §7 — Placement Order Checklist

When building a DSA `CODE.md`, place visuals in this order:

1. ✅ **Snippet-level traversal** — under each snippet's expected output (§3)
2. ✅ **Algorithm-decision flowchart** — first diagram in Visual/Diagram (§6)
3. ✅ **Step-by-step traversal diagram** — second in Visual/Diagram
4. ✅ **Complexity comparison chart** — third in Visual/Diagram
5. ⭐ **Optional GIF** — last in Visual/Diagram, with ASCII/Mermaid above (§5)
6. ✅ **One-line complexity tie-in** — after each diagram

---

## §8 — Week-Specific Visual Suggestions

| Week | Topic | Recommended Visuals |
|------|-------|--------------------|
| 01 | Big-O, Arrays, Hashing | Data structure selection flowchart, two-sum walkthrough, complexity comparison table |
| 02 | Kadane, Prefix Sums | Running sum state diagram, Kadane's max-so-far tracker, prefix sum build animation |
| 03 | Two Pointers, 3Sum | Fixed `i` with `left`/`right` convergence, duplicate skipping decision tree |
| 04 | Sliding Window | Window expansion/shrink flowchart, deque front eviction diagram, window state tracker |
| 05 | Stack | Monotonic stack push/pop sequence, bracket matching state machine |
| 06 | Binary Search | Search space halving per step, rotated array pivot detection |
| 07 | Linked List | Node pointer diagrams, reversal step-by-step, fast/slow pointer positions |
| 08 | Binary Trees | Tree structure (Mermaid `graph TD`), DFS/BFS path highlighting, level-order fill |
| 09 | BST | BST validation range narrowing, inorder traversal sequence |
| 10 | Heap | Heap insert/extract sift operations, array-to-heap mapping |
| 11 | Backtracking | Include/exclude recursion tree, pruning visualization, subset generation tree |
| 12 | Graphs I | Adjacency list structure, BFS queue state per step, DFS stack per step |
| 13 | Topo Sort | Indegree table, Kahn's algorithm queue progression, cycle detection |
| 14 | Union-Find | Path compression before/after, union by rank tree shapes |
| 15 | Greedy/Intervals | Interval timeline diagrams, greedy choice proof sketches |
| 16 | 1D DP | Recurrence arrow diagram, table fill progression, state compression |
| 17 | 2D DP | Grid fill order arrows, LCS alignment matrix, path counting grid |
| 18 | Shortest Paths | Dijkstra relaxation per step, priority queue state, weighted graph |
| 19 | Tries/Strings | Trie tree structure, KMP failure function build, Rabin-Karp rolling hash |
| 20 | Mixed Review | Sorting comparison table, algorithm selection decision tree |
