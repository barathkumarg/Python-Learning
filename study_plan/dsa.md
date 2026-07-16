# Parallel DSA Track (Weeks 01–20)

> Track: `dsa` · Outcome: arrays, hashing, trees, graphs, DP, greedy, string algorithms

## Week Plan

| Week | Topic | Slug | Primary Source |
|------|-------|------|----------------|
| 01 | Big-O, arrays, hashing basics | `week_01_big_o_arrays_hashing` | [NeetCode — Arrays & Hashing](https://neetcode.io/roadmap) |
| 02 | Arrays, hashing, Kadane | `week_02_arrays_hashing_ii` | [NeetCode — Arrays & Hashing](https://neetcode.io/roadmap) |
| 03 | Two pointers | `week_03_two_pointers` | [NeetCode — Two Pointers](https://neetcode.io/roadmap) |
| 04 | Sliding window, monotonic deque | `week_04_sliding_window` | [NeetCode — Sliding Window](https://neetcode.io/roadmap) |
| 05 | Stack, monotonic structures | `week_05_stack` | [NeetCode — Stack](https://neetcode.io/roadmap) |
| 06 | Binary search | `week_06_binary_search` | [NeetCode — Binary Search](https://neetcode.io/roadmap) |
| 07 | Linked list | `week_07_linked_list` | [NeetCode — Linked List](https://neetcode.io/roadmap) |
| 08 | Binary trees I | `week_08_binary_tree` | [NeetCode — Trees](https://neetcode.io/roadmap) |
| 09 | Binary search trees | `week_09_bst` | [NeetCode — Trees](https://neetcode.io/roadmap) |
| 10 | Heap and priority queue | `week_10_heap` | [NeetCode — Heap](https://neetcode.io/roadmap) |
| 11 | Recursion and backtracking | `week_11_backtracking` | [NeetCode — Backtracking](https://neetcode.io/roadmap) |
| 12 | Graphs I | `week_12_graphs_i` | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 13 | Graphs II, topo sort | `week_13_graphs_ii_topo` | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 14 | Union-Find | `week_14_union_find` | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 15 | Intervals and greedy | `week_15_greedy` | [NeetCode — Greedy](https://neetcode.io/roadmap) |
| 16 | 1D dynamic programming | `week_16_dp_1d` | [NeetCode — DP](https://neetcode.io/roadmap) |
| 17 | 2D dynamic programming | `week_17_dp_2d` | [NeetCode — DP](https://neetcode.io/roadmap) |
| 18 | Shortest paths | `week_18_shortest_path` | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 19 | Tries, strings, bit tricks | `week_19_tries_bits` | [NeetCode — Roadmap](https://neetcode.io/roadmap) |
| 20 | Mixed review, sorting, math | `week_20_mixed_review` | [NeetCode Practice](https://neetcode.io/practice) |

---

## Concept Checklists

> Gate G8: every concept must appear in CODE.md table + at least one of: visual/diagram, code.py function, or exercise stub. Concept counts are sized to each pattern's scope — expanded past the earlier 15–20 guide where a topic genuinely needs it; no trivia.
>
> **How to read this file:** each week has a knowledge-base block
> (Prerequisites · Real-world use · Production example · Sources) followed by its
> **Concept Checklist**. The checklist is the Gate G8 contract — every concept
> must appear in `CODE.md` + at least one of visual / `code.py` function /
> exercise stub. The **Production example** is what `code.py` must implement.

### Week 01 — Big-O, Arrays, Hashing (21)

**Prerequisites:** none — this is the entry point for the DSA track.
**Real-world use:** complexity budgeting and O(1) lookups underpin every hot path — deduping records, counting events, and joining data by key.
**Production example (code.py):** an order-log analyzer — detect duplicate order IDs with a `set`, count events per user with `Counter`, and solve a Two-Sum-style complement lookup in a single O(n) pass.
**Sources:** [NeetCode — Arrays & Hashing](https://neetcode.io/roadmap) · [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/) · [LeetCode: Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | What Big-O measures | Worst-case growth rate |
| 2 | Common complexities | O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) |
| 3 | Amortized analysis | `list.append()` O(1) amortized |
| 4 | Space complexity | Extra space vs input space |
| 5 | Python `list` as array | O(1) index, O(n) insert at 0 |
| 6 | Array traversal patterns | Forward, backward, two-pass |
| 7 | Hash map fundamentals | Key → hash → bucket, O(1) avg |
| 8 | Hash collisions | Chaining vs open addressing |
| 9 | Python `dict` internals | Compact dict, insertion order |
| 10 | `set` for O(1) membership | `in` operator, dedupe |
| 11 | Two-Sum pattern | Hash map complement lookup |
| 12 | Duplicate detection | `set()` seen tracker |
| 13 | Anagram grouping | Sorted-key or frequency-key |
| 14 | Frequency map / Counter | `Counter`, manual counting |
| 15 | `defaultdict` for grouping | `defaultdict(list)` |
| 16 | Time/space labeling | O() on every function |
| 17 | Visual: hash map flow | Insert/lookup diagram |
| 18 | Array vs hash map choice | Memory vs speed tradeoff |
| 19 | Best/average/worst case | Not all inputs cost the same |
| 20 | Big-O simplification rules | Drop constants, keep dominant term |
| 21 | Hashable key requirements | Immutable keys, tuple composite keys |

### Week 02 — Arrays, Hashing, Kadane (21)

**Prerequisites:** Week 01 (Big-O, arrays, hash maps).
**Real-world use:** range aggregates, streaming maxima, and O(n) reshaping power analytics dashboards, billing rollups, and ETL transforms.
**Production example (code.py):** a revenue-window analyzer — build product-except-self for contribution scoring and run a Kadane scan that returns the best contiguous revenue window with its start/end indices.
**Sources:** [NeetCode — Arrays & Hashing](https://neetcode.io/roadmap) · [LeetCode: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · [LeetCode: Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Prefix sum array | `prefix[i] = prefix[i-1] + arr[i]` |
| 2 | Range sum query | `sum(l,r) = prefix[r] - prefix[l-1]` |
| 3 | Suffix sum / product | Right-to-left accumulation |
| 4 | Product except self | Left × right without division |
| 5 | Frequency map apps | Top-K, mode finding |
| 6 | Bucket sort for frequency | O(n) ranking via buckets |
| 7 | Kadane's algorithm | `max(num, max_ending + num)` |
| 8 | Kadane's all-negatives | Track global max separately |
| 9 | Kadane's subarray bounds | Record start/end during scan |
| 10 | Subsequence-sum intro | Precursor to DP |
| 11 | Array rotation | Reversal algorithm |
| 12 | Dutch National Flag | Three-way partition |
| 13 | In-place operations | Swap, reverse, partition |
| 14 | String-as-array ops | Char frequency, anagram check |
| 15 | Encode/decode strings | Length-prefix or delimiter |
| 16 | Visual: prefix sum | Accumulation diagram |
| 17 | Visual: Kadane trace | Step-by-step max tracking |
| 18 | Complexity table | O(n) vs O(n²) per variant |
| 19 | Subarray sum equals K | Prefix sum + hash map of counts |
| 20 | Maximum product subarray | Track running min & max (sign flips) |
| 21 | 2D prefix sum | Range sum on a matrix in O(1) |

### Week 03 — Two Pointers (20)

**Prerequisites:** Week 01 (arrays), Week 02 (in-place scans).
**Real-world use:** pair/triple matching, in-place compaction of buffers, palindrome/validation checks on sorted or scannable data.
**Production example (code.py):** 3Sum with full duplicate suppression — sort, fix one index, converge two pointers, and skip duplicate values to return only unique triplets.
**Sources:** [NeetCode — Two Pointers](https://neetcode.io/roadmap) · [LeetCode: 3Sum](https://leetcode.com/problems/3sum/) · [LeetCode: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Opposite-end pointers | `left=0, right=len-1` |
| 2 | Same-direction pointers | Fast/slow pattern |
| 3 | Sorted pair sum | Move based on sum |
| 4 | 3Sum approach | Fix one + two-pointer |
| 5 | 3Sum dedupe | Skip duplicate values |
| 6 | Container with most water | Greedy pointer move |
| 7 | Valid palindrome | Skip non-alnum, compare |
| 8 | Two-pointer on strings | Character comparison |
| 9 | Trapping rain water | Left-max / right-max |
| 10 | Remove duplicates in-place | Slow/fast writer |
| 11 | Move zeroes | Two-pointer partition |
| 12 | Sort colors | Three-pointer partition |
| 13 | When to sort first | O(n log n) enables O(n) scan |
| 14 | Movement invariant | Why correct pointer moves |
| 15 | Visual: convergence | Step-by-step pointers |
| 16 | Visual: 3Sum dedup | Skip logic diagram |
| 17 | Complexity analysis | O(n²) 3Sum, O(n) pair |
| 18 | Two Sum II (sorted input) | Opposite-end pointers on sorted array |
| 19 | kSum generalization | Recurse fixing outer + two-pointer base |
| 20 | Merge sorted arrays in-place | Fill from the back |

### Week 04 — Sliding Window, Monotonic Deque (21)

**Prerequisites:** Week 03 (two pointers), Week 01 (hash maps for frequency).
**Real-world use:** rate limiting, streaming metrics over a moving window, and finding the longest/shortest qualifying span in a stream.
**Production example (code.py):** minimum window substring — expand right to cover all required characters, then shrink left to the smallest valid window using a frequency-satisfaction counter.
**Sources:** [NeetCode — Sliding Window](https://neetcode.io/roadmap) · [LeetCode: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) · [LeetCode: Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Fixed-size window | Sum/max of k elements |
| 2 | Variable-size window | Expand right, shrink left |
| 3 | Window invariant | Valid window condition |
| 4 | Frequency map in window | Track counts on slide |
| 5 | Longest substring no repeat | `set`/`dict` last-seen |
| 6 | Longest repeating char replacement | `max_freq` + window size |
| 7 | Minimum window substring | Shrink for minimum |
| 8 | Permutation in string | Fixed-size freq match |
| 9 | `deque` basics | O(1) both ends |
| 10 | Monotonic decreasing deque | Pop smaller on push |
| 11 | Sliding window maximum | Deque indices, front=max |
| 12 | Monotonic increasing deque | Min in window |
| 13 | Deque vs heap for window | O(n) vs O(n log n) |
| 14 | Substring frequency | Count-based conditions |
| 15 | Two-pointer vs sliding window | Naming overlap |
| 16 | Visual: window slide | Expansion/contraction |
| 17 | Visual: deque state | Contents at each step |
| 18 | Complexity: O(n) amortized | Each elem enters/leaves once |
| 19 | At-most-K → exactly-K trick | `atMost(k) - atMost(k-1)` |
| 20 | Best time to buy/sell stock | Min-so-far window over prices |
| 21 | Window-validity via counter | Track satisfied counts to shrink |

### Week 05 — Stack, Monotonic Structures (20)

**Prerequisites:** Week 01 (arrays/lists), Week 04 (monotonic deque intuition).
**Real-world use:** expression parsers, bracket/undo stacks, and next-greater queries over stock prices or temperature series.
**Production example (code.py):** largest rectangle in histogram — maintain a monotonic increasing stack of bar indices and compute the maximal area by popping when a shorter bar arrives.
**Sources:** [NeetCode — Stack](https://neetcode.io/roadmap) · [LeetCode: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · [LeetCode: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Stack ADT | LIFO: push, pop, peek |
| 2 | `list` as stack | `.append()`, `.pop()`, `[-1]` |
| 3 | Bracket matching | Push open, pop on close |
| 4 | Nested brackets | Multiple types, ordering |
| 5 | Monotonic stack (decreasing) | Pop smaller on push |
| 6 | Monotonic stack (increasing) | Pop larger on push |
| 7 | Next greater element | Right-to-left mono stack |
| 8 | Next smaller element | Symmetric pattern |
| 9 | Daily temperatures | Days until warmer |
| 10 | Histogram rectangle | Left/right boundaries |
| 11 | Expression evaluation | Postfix, precedence |
| 12 | Min-stack | Auxiliary min tracker |
| 13 | Stack vs deque choice | When to use which |
| 14 | `deque` as stack | Explicit intent |
| 15 | Visual: mono stack build | State at each step |
| 16 | Visual: histogram | Boundary detection |
| 17 | Complexity: O(n) | Each elem pushed/popped once |
| 18 | Trapping rain water (stack) | Pop and fill by left/right boundaries |
| 19 | Asteroid collision | Resolve survivors via stack pops |
| 20 | Car fleet | Sort by position + monotonic stack of times |

### Week 06 — Binary Search (20)

**Prerequisites:** Week 01 (Big-O, arrays), Week 02 (sorted-array reasoning).
**Real-world use:** log/index lookup, capacity planning by feasibility search, and versioned or time-based queries.
**Production example (code.py):** search in a rotated sorted array — locate the sorted half at each step and recurse/narrow to find a target in O(log n) with no full scan.
**Sources:** [NeetCode — Binary Search](https://neetcode.io/roadmap) · [LeetCode: Binary Search](https://leetcode.com/problems/binary-search/) · [LeetCode: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Binary search template | `while left <= right` |
| 2 | Lower bound `bisect_left` | First insertion point |
| 3 | Upper bound `bisect_right` | After existing elements |
| 4 | `bisect` module | `bisect_left`, `insort` |
| 5 | Rotated sorted array | Find pivot, search half |
| 6 | Find min in rotated | Binary search on rotation |
| 7 | Search 2D matrix | Flattened sorted view |
| 8 | Answer-space search | Search on value, not index |
| 9 | Koko eating bananas | Binary search on speed |
| 10 | First/last occurrence | Don't stop at first find |
| 11 | Square root | Integer sqrt via search |
| 12 | Peak element | Binary search non-sorted |
| 13 | Off-by-one pitfalls | `<=` vs `<`, mid calc |
| 14 | Overflow prevention | `left + (right-left)//2` |
| 15 | Visual: narrowing | left/mid/right movement |
| 16 | Visual: rotated search | Pivot + half selection |
| 17 | Complexity: O(log n) | Halving each step |
| 18 | Capacity/ship-within-days | Feasibility predicate + search on answer |
| 19 | Median of two sorted arrays | Partition-based binary search |
| 20 | Monotonic-predicate boundary | Find first True in a T/F space |

### Week 07 — Linked List (20)

**Prerequisites:** Week 01 (references/objects), Week 03 (fast/slow two-pointer).
**Real-world use:** LRU caches, streaming buffers, and pointer manipulation in allocators, queues, and adjacency structures.
**Production example (code.py):** reverse a singly linked list both iteratively (prev/curr/next) and recursively, plus Floyd's cycle detection returning the cycle start.
**Sources:** [NeetCode — Linked List](https://neetcode.io/roadmap) · [LeetCode: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) · [LeetCode: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Node class | `val`, `next` |
| 2 | Traversal | `while curr:` |
| 3 | Dummy/sentinel | Simplify edge cases |
| 4 | Reverse iterative | prev/curr/next pointers |
| 5 | Reverse recursive | Re-link on return |
| 6 | Fast/slow (Floyd's) | Cycle detection |
| 7 | Find middle | Slow=1, fast=2 |
| 8 | Merge two sorted | Compare heads |
| 9 | Remove nth from end | n-gap two-pointer |
| 10 | Detect cycle start | Phase 2: reset to head |
| 11 | Intersection | Length diff alignment |
| 12 | Palindrome LL | Reverse second half |
| 13 | Add two numbers | Digit carry |
| 14 | Doubly linked list | `prev`+`next`, LRU |
| 15 | Visual: reversal | Pointer reassignment |
| 16 | Visual: fast/slow | Positions each step |
| 17 | Complexity: O(n), O(1) space | In-place manipulation |
| 18 | Reorder list | Find mid + reverse half + merge |
| 19 | Swap nodes in pairs | Pointer surgery or recursion |
| 20 | Copy list with random pointer | Interleave clones or hash map |

### Week 08 — Binary Trees I (26)

**Prerequisites:** Week 07 (nodes/pointers), Week 11 preview (recursion).
**Real-world use:** file systems, DOM/AST trees, and traversing any hierarchical data (org charts, category trees).
**Production example (code.py):** serialize/deserialize a binary tree via preorder encoding, plus LCA and diameter computed in a single recursive pass.
**Sources:** [NeetCode — Trees](https://neetcode.io/roadmap) · [LeetCode: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) · [LeetCode: Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | TreeNode class | `val`, `left`, `right` |
| 2 | Tree from list/array | Level-order construction |
| 3 | DFS inorder | Left → Root → Right |
| 4 | DFS preorder | Root → Left → Right |
| 5 | DFS postorder | Left → Right → Root |
| 6 | BFS level-order | Queue-based |
| 7 | Recursive DFS template | Base case + recurse |
| 8 | Iterative DFS | Explicit stack |
| 9 | Max depth | `1 + max(left, right)` |
| 10 | Min depth | Shortest root-to-leaf |
| 11 | Path sum | Root-to-leaf check |
| 12 | Diameter | Longest any-two-node path |
| 13 | LCA | Recursive match |
| 14 | Same tree / subtree | Recursive equality |
| 15 | Invert binary tree | Swap left/right |
| 16 | Zigzag traversal | Alternating direction |
| 17 | Vertical order | Column-based grouping |
| 18 | Serialize/deserialize | Preorder encoding |
| 19 | Visual: DFS order | Numbered visit order |
| 20 | Visual: BFS levels | Queue state per level |
| 21 | Balanced tree check | Height + early exit on imbalance |
| 22 | Symmetric tree | Mirror comparison of subtrees |
| 23 | Construct from preorder+inorder | Root split via index map |
| 24 | Right side view | Last node per BFS level |
| 25 | Binary tree max path sum | Gain from children, track global max |
| 26 | Complexity: O(n), O(h) space | Visit each node once, recursion stack O(h) |

### Week 09 — BST (19)

**Prerequisites:** Week 08 (binary trees, traversals, recursion).
**Real-world use:** ordered indexes, range queries, and the self-balancing maps behind database indexes and ordered sets.
**Production example (code.py):** validate a BST with min/max range recursion and find the kth smallest element via a controlled (stack-based) inorder walk.
**Sources:** [NeetCode — Trees](https://neetcode.io/roadmap) · [LeetCode: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) · [LeetCode: Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | BST property | Left < Root < Right |
| 2 | BST validation | In-range recursive |
| 3 | BST search | O(h) left/right |
| 4 | BST insert | Find leaf, create |
| 5 | BST delete | Leaf/one-child/two-child |
| 6 | Inorder = sorted | BST traversal property |
| 7 | Kth smallest | Inorder + counter |
| 8 | Successor/predecessor | Next larger/smaller |
| 9 | BST from sorted array | Mid-point recursion |
| 10 | LCA in BST | Use BST property |
| 11 | BST iterator | Controlled inorder via stack |
| 12 | Balanced BST concepts | AVL/RB awareness |
| 13 | BST vs hash map | Ordered ops vs O(1) |
| 14 | Visual: insert sequence | Tree growth |
| 15 | Visual: delete cases | Three cases |
| 16 | Complexity: O(h) | log n balanced, n worst |
| 17 | Range sum of BST | Prune subtrees outside range bounds |
| 18 | Trim BST to range | Recursive prune of out-of-range nodes |
| 19 | Two-Sum in BST | Inorder + two-pointer or seen-set |

### Week 10 — Heap (19)

**Prerequisites:** Week 08 (tree/array indexing), Week 01 (Big-O).
**Real-world use:** task schedulers, top-K dashboards, streaming medians, and k-way merges in log/DB systems.
**Production example (code.py):** merge K sorted lists using a min-heap of `(value, list_index, node)` tuples, always popping the global minimum next.
**Sources:** [NeetCode — Heap / Priority Queue](https://neetcode.io/roadmap) · [LeetCode: Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · [LeetCode: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Heap property | Parent ≤ children (min) |
| 2 | `heapq` module | `heappush`, `heappop`, `heapify` |
| 3 | Min-heap default | Python only min-heap |
| 4 | Max-heap via negation | Push `-val` |
| 5 | `heapify` O(n) | In-place conversion |
| 6 | `nlargest`/`nsmallest` | Top-N |
| 7 | Kth largest | Min-heap size k |
| 8 | Top-K frequent | Heap + freq map |
| 9 | Merge K sorted lists | Heap of tuples |
| 10 | Running median | Two heaps |
| 11 | Priority queue | `(priority, item)` |
| 12 | Heap sort concept | Build + extract |
| 13 | Lazy deletion | Mark + skip |
| 14 | Visual: array layout | Parent/children indices |
| 15 | Visual: heapify | Sift-down trace |
| 16 | Complexity | O(log n) push/pop |
| 17 | K closest points to origin | Max-heap of size k by distance |
| 18 | Task scheduler | Greedy heap of counts + cooldown |
| 19 | Reorganize string | Heap of counts, avoid adjacency |

### Week 11 — Recursion and Backtracking (26)

**Prerequisites:** Week 03 (choice/decision framing), Week 08 (recursion on trees).
**Real-world use:** config permutations, constraint solvers (schedulers, puzzles), and search over combinatorial spaces.
**Production example (code.py):** subsets and combination sum via the choose → explore → unchoose template, with duplicate-skipping and sum-bound pruning.
**Sources:** [NeetCode — Backtracking](https://neetcode.io/roadmap) · [LeetCode: Subsets](https://leetcode.com/problems/subsets/) · [LeetCode: Combination Sum](https://leetcode.com/problems/combination-sum/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Base case | Termination + return |
| 2 | Recursive case | Reduce + trust |
| 3 | Processed/unprocessed | Decided vs remaining |
| 4 | Include/exclude tree | Binary choice per element |
| 5 | Subsets | Include/exclude, collect at leaf |
| 6 | Subsets with duplicates | Sort + skip duplicates |
| 7 | Subsequence by character | String include/exclude |
| 8 | Subsequence-sum / subset-sum | Sum constraint pruning |
| 9 | Combination sum | Reuse elements |
| 10 | Permutations | Swap or used-set |
| 11 | Backtracking template | Choose → Explore → Unchoose |
| 12 | Pruning | Early termination |
| 13 | N-Queens | Column/diagonal constraints |
| 14 | Word search | Grid DFS + visited |
| 15 | Pattern printing recursion | Triangle/diamond |
| 16 | Call stack visualization | Stack frame diagram |
| 17 | Recursion vs iteration | Stack overflow risk |
| 18 | Memoization preview | Cache → DP connection |
| 19 | Visual: recursion tree | Include/exclude branches |
| 20 | Visual: pruning | Pruned vs explored |
| 21 | Combinations (n choose k) | Start-index pruning |
| 22 | Permutations with duplicates | Sort + skip used duplicates |
| 23 | Palindrome partitioning | Cut + recurse on valid suffix |
| 24 | Letter combinations of phone | Digit → letters cartesian build |
| 25 | Generate parentheses | Open/close count constraints |
| 26 | Complexity: exponential | Branching^depth; pruning cuts the tree |

### Week 12 — Graphs I (22)

**Prerequisites:** Week 07 (traversal), Week 11 (DFS recursion), Week 10 preview (BFS queue).
**Real-world use:** social graphs, dependency maps, grid/maze pathfinding, and network reachability.
**Production example (code.py):** number of islands — flood each unvisited land cell with DFS/BFS over 4-directional neighbors, marking visited to count connected components.
**Sources:** [NeetCode — Graphs](https://neetcode.io/roadmap) · [LeetCode: Number of Islands](https://leetcode.com/problems/number-of-islands/) · [LeetCode: Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Adjacency list | `dict[node, list[node]]` |
| 2 | Adjacency matrix | `matrix[u][v]` |
| 3 | Edge list | `[(u, v, w)]` |
| 4 | BFS | Queue-based, level-by-level |
| 5 | DFS | Stack/recursion |
| 6 | Visited set | Prevent revisit |
| 7 | Connected components | Count via BFS/DFS |
| 8 | Number of islands | Grid DFS/BFS |
| 9 | Grid as graph | 4-direction neighbors |
| 10 | Flood fill | Fill connected region |
| 11 | Rotting oranges | Multi-source BFS |
| 12 | Clone graph | `{old: new}` mapping |
| 13 | Surrounded regions | Border DFS + flip |
| 14 | Pacific Atlantic | Reverse-flow BFS |
| 15 | BFS shortest (unweighted) | Level = distance |
| 16 | Directed vs undirected | Edge semantics |
| 17 | Visual: BFS wave | Level-by-level fill |
| 18 | Visual: DFS stack | Stack + visited |
| 19 | Max area of island | DFS returning region area |
| 20 | Walls and gates / 01 matrix | Multi-source BFS distance |
| 21 | Word ladder | BFS over word transformations |
| 22 | Complexity: O(V+E) | Each node and edge visited once |

### Week 13 — Graphs II, Topo Sort (19)

**Prerequisites:** Week 12 (graph representations, BFS/DFS).
**Real-world use:** build systems, task/job scheduling, course and dependency ordering, and deadlock (cycle) detection.
**Production example (code.py):** course schedule II — build an indegree map and run Kahn's algorithm to return a valid topological order, or detect a cycle when not all nodes are processed.
**Sources:** [NeetCode — Graphs](https://neetcode.io/roadmap) · [LeetCode: Course Schedule](https://leetcode.com/problems/course-schedule/) · [LeetCode: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | DAG | No cycles |
| 2 | Topological sort | Linear ordering |
| 3 | Kahn's algorithm | Indegree + queue |
| 4 | DFS-based topo | Post-order reverse |
| 5 | Cycle detection (directed) | Kahn's: processed < total |
| 6 | DFS coloring | White/gray/black |
| 7 | Course schedule I | Cycle check |
| 8 | Course schedule II | Valid ordering |
| 9 | Dependency resolution | Build order |
| 10 | Indegree construction | Count incoming edges |
| 11 | Multi-source start | All zero-indegree |
| 12 | Alien dictionary | Word comparison → topo |
| 13 | Cycle in undirected | Parent tracking / UF |
| 14 | Bipartite check | 2-coloring |
| 15 | Visual: Kahn's | Indegree + queue |
| 16 | Visual: DFS coloring | State transitions |
| 17 | Longest path in DAG | Topo order + DP relaxation |
| 18 | Reconstruct itinerary | Hierholzer / Eulerian path |
| 19 | Complexity: O(V+E) | Topo sort linear in graph size |

### Week 14 — Union-Find (18)

**Prerequisites:** Week 12 (graphs, components).
**Real-world use:** dynamic connectivity queries, network partitioning, account/dedup merging, and Kruskal's MST.
**Production example (code.py):** a DSU class with path compression and union by rank used to detect the redundant connection (the edge that creates a cycle) in a graph.
**Sources:** [NeetCode — Graphs](https://neetcode.io/roadmap) · [LeetCode: Redundant Connection](https://leetcode.com/problems/redundant-connection/) · [LeetCode: Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | DSU concept | Connected components |
| 2 | `find()` | Trace to root |
| 3 | `union()` | Link roots |
| 4 | Path compression | Direct to root |
| 5 | Union by rank | Shorter under taller |
| 6 | Union by size | Smaller under larger |
| 7 | DSU class | `parent[]`, `rank[]` |
| 8 | Component counting | Decrement on union |
| 9 | Redundant connection | Cycle-causing edge |
| 10 | Components via DSU | Alternative to BFS/DFS |
| 11 | DSU vs BFS/DFS | Dynamic vs traversal |
| 12 | Accounts merge | Union by shared email |
| 13 | Graph valid tree | n-1 edges + connected |
| 14 | Visual: union ops | Parent array changes |
| 15 | Complexity: ~O(1) | Inverse Ackermann |
| 16 | Number of connected components | Union all edges, count roots |
| 17 | Most stones removed | Union by shared row/col |
| 18 | Number of islands II | Dynamic union as cells are added |

### Week 15 — Intervals and Greedy (21)

**Prerequisites:** Week 04 (sorting/scanning), Week 01 (Big-O).
**Real-world use:** calendar/booking overlap, resource allocation, scheduling, and greedy optimization of ordering problems.
**Production example (code.py):** merge overlapping intervals (sort by start, coalesce) and compute the minimum removals to make the rest non-overlapping (sort by end, greedy keep).
**Sources:** [NeetCode — Greedy](https://neetcode.io/roadmap) · [LeetCode: Merge Intervals](https://leetcode.com/problems/merge-intervals/) · [LeetCode: Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Interval representation | `[start, end]` |
| 2 | Sort by start | `key=lambda x: x[0]` |
| 3 | Sort by end | Activity selection |
| 4 | Merge overlapping | Compare start vs prev end |
| 5 | Insert interval | Find + merge |
| 6 | Non-overlapping | Min removals |
| 7 | Meeting rooms | Check overlaps |
| 8 | Meeting rooms II | Sweep/heap for concurrency |
| 9 | Greedy concept | Local → global optimal |
| 10 | Greedy proof | Exchange argument |
| 11 | Jump game I | Max-reach |
| 12 | Jump game II | BFS-style min jumps |
| 13 | Activity selection | Sort end, pick |
| 14 | Gas station | Deficit tracking |
| 15 | Greedy vs DP | No backtrack vs all subproblems |
| 16 | Visual: interval merge | Timeline diagram |
| 17 | Visual: jump game | Max-reach trace |
| 18 | Minimum arrows to burst balloons | Sort by end, count groups |
| 19 | Partition labels | Last-occurrence greedy cuts |
| 20 | Hand of straights / groups | Greedy consecutive grouping |
| 21 | Complexity: O(n log n) | Dominated by the initial sort |

### Week 16 — 1D DP (22)

**Prerequisites:** Week 11 (recursion, memoization preview).
**Real-world use:** resource optimization, planning with reused subresults, and sequence problems (pricing, scheduling, counting).
**Production example (code.py):** coin change (minimum coins for an amount) solved both top-down with memoization and bottom-up with a 1D table, returning -1 when unreachable.
**Sources:** [NeetCode — Dynamic Programming](https://neetcode.io/roadmap) · [LeetCode: Coin Change](https://leetcode.com/problems/coin-change/) · [LeetCode: House Robber](https://leetcode.com/problems/house-robber/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Overlapping subproblems | Same subproblem repeated |
| 2 | Optimal substructure | Contains optimal sub-solutions |
| 3 | Memoization (top-down) | Recursion + cache |
| 4 | Tabulation (bottom-up) | Iterative table fill |
| 5 | State definition | What `dp[i]` means |
| 6 | Recurrence relation | `dp[i] = f(dp[i-1], ...)` |
| 7 | Base cases | Initial values |
| 8 | Climbing stairs | Fibonacci variant |
| 9 | House robber | Skip or take |
| 10 | Coin change | Min coins for amount |
| 11 | LIS | Longest increasing subsequence |
| 12 | Max subarray as DP | Kadane reinforcement |
| 13 | Subset sum / partition | Boolean DP |
| 14 | Space optimization | Rolling variables |
| 15 | State compression | Reduce dimensions |
| 16 | Decode ways | Single/double digit |
| 17 | Visual: DP table | Cell-by-cell fill |
| 18 | Visual: memo tree | Eliminated repeats |
| 19 | Min cost climbing stairs | dp = cost + min of two prev |
| 20 | Word break | dp over dictionary segments |
| 21 | Coin change II (count ways) | Unbounded combinations, order-free |
| 22 | Complexity: O(states × transition) | States × per-state work |

### Week 17 — 2D DP (20)

**Prerequisites:** Week 16 (1D DP states, recurrences).
**Real-world use:** diffing, spell correction (edit distance), grid routing, and image/matrix transforms.
**Production example (code.py):** longest common subsequence and edit distance on a 2D `dp[i][j]` table, with a backtrack that reconstructs the aligning sequence.
**Sources:** [NeetCode — Dynamic Programming](https://neetcode.io/roadmap) · [LeetCode: Unique Paths](https://leetcode.com/problems/unique-paths/) · [LeetCode: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | 2D state definition | `dp[i][j]` meaning |
| 2 | Grid path counting | Unique paths |
| 3 | Grid with obstacles | Skip blocked |
| 4 | Minimum path sum | Min cost grid |
| 5 | LCS | Longest common subsequence |
| 6 | Edit distance | Insert/delete/replace |
| 7 | 0/1 Knapsack | Items + capacity |
| 8 | Table fill order | Row/col/diagonal |
| 9 | Matrix traversal | Row/col/spiral/diagonal |
| 10 | Set matrix zeroes | First row/col flags |
| 11 | Rotate image | Transpose + reverse |
| 12 | Spiral matrix | Layer boundaries |
| 13 | Space optimization | Two rows |
| 14 | Palindrome partition DP | `dp[i][j]` palindrome? |
| 15 | Visual: 2D table | Dependencies + fill |
| 16 | Visual: LCS backtrack | Trace through table |
| 17 | Maximal square | dp = min of 3 neighbors + 1 |
| 18 | Interleaving string | 2D boolean reachability |
| 19 | Interval DP (burst balloons) | dp over subrange endpoints |
| 20 | Complexity: O(m×n) | Fill each table cell once |

### Week 18 — Shortest Paths (19)

**Prerequisites:** Week 12 (graphs), Week 10 (heap for Dijkstra).
**Real-world use:** routing and navigation, network latency, logistics/least-cost paths, and negative-cycle (arbitrage) detection.
**Production example (code.py):** network delay time via Dijkstra with a `heapq` of `(dist, node)` tuples, returning the max shortest-distance (or -1 if unreachable).
**Sources:** [NeetCode — Graphs](https://neetcode.io/roadmap) · [LeetCode: Network Delay Time](https://leetcode.com/problems/network-delay-time/) · [LeetCode: Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Weighted graph | `dict[node, list[(node, w)]]` |
| 2 | Dijkstra's | Greedy BFS + heap |
| 3 | Dijkstra with `heapq` | `(dist, node)` tuples |
| 4 | Relaxation | If new_dist < known, update |
| 5 | No negative weights | Dijkstra limitation |
| 6 | Network delay time | Max shortest distance |
| 7 | Cheapest flights K stops | Modified BFS/Bellman |
| 8 | Bellman-Ford | V-1 iterations |
| 9 | Negative cycle detection | Nth iteration relaxes |
| 10 | BFS unweighted (review) | Level = distance |
| 11 | 0-1 BFS | Deque: 0-front, 1-back |
| 12 | Floyd-Warshall | All-pairs O(V³) |
| 13 | Path reconstruction | `prev[]` backtrack |
| 14 | Multi-source shortest | All sources in initial heap |
| 15 | Visual: Dijkstra | Heap + distance updates |
| 16 | Visual: Bellman-Ford | Rounds of relaxation |
| 17 | Minimum spanning tree | Prim (heap) / Kruskal (DSU) |
| 18 | Swim in rising water / min-max path | Dijkstra on max edge weight |
| 19 | Complexity comparison | Dijkstra O(E log V) · Bellman-Ford O(V·E) |

### Week 19 — Tries, Strings, Bits (25)

**Prerequisites:** Week 08 (tree structure), Week 01 (hash maps, Big-O).
**Real-world use:** autocomplete/prefix search, plagiarism and substring search, DNA/log scanning, and permission bitmasks or low-level flags.
**Production example (code.py):** implement a Trie (`insert`, `search`, `startsWith`) backed by per-node child dicts and an `is_end` flag, ready for autocomplete lookups.
**Sources:** [NeetCode — Trie / Strings / Bit Manipulation](https://neetcode.io/roadmap) · [LeetCode: Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) · [LeetCode: Single Number](https://leetcode.com/problems/single-number/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Trie node | `children: dict`, `is_end` |
| 2 | Trie insert | Walk/create per char |
| 3 | Trie search | Walk, check `is_end` |
| 4 | Trie prefix search | Walk, no `is_end` check |
| 5 | Trie applications | Autocomplete, spell check |
| 6 | Palindrome expansion | Expand around center |
| 7 | Rabin-Karp rolling hash | Slide hash window |
| 8 | KMP prefix function | LPS array |
| 9 | KMP matching | Skip via LPS |
| 10 | Repeated DNA sequences | 10-char window set |
| 11 | String normalization | Lower, strip, filter |
| 12 | Consecutive-string patterns | Run-length, grouping |
| 13 | Bit basics | `&`, `|`, `^`, `~`, `<<`, `>>` |
| 14 | Single number (XOR) | `a ^ a = 0` |
| 15 | Counting bits | `bin(n).count('1')` |
| 16 | Bit masking subsets | `1 << i` |
| 17 | Power of two | `n & (n-1) == 0` |
| 18 | Reverse bits | Bit-by-bit |
| 19 | Visual: trie tree | Word insertions |
| 20 | Visual: KMP LPS | Prefix function build |
| 21 | Word search II | Trie + grid DFS pruning |
| 22 | Add & search word (wildcard) | Trie DFS branching on `.` |
| 23 | Sum of two integers (no `+`) | XOR sum + carry shift |
| 24 | Missing number | XOR trick or Gauss sum |
| 25 | Complexity: trie O(L) | Per-op linear in word length |

### Week 20 — Mixed Review, Sorting, Math (24)

**Prerequisites:** all prior weeks (01–19).
**Real-world use:** interview-day breadth — choosing the right sort, applying number theory, and consolidating every pattern under time pressure.
**Production example (code.py):** implement merge sort and quickselect (kth element in O(n) average), plus a Sieve of Eratosthenes prime counter, each with complexity labels.
**Sources:** [NeetCode — Practice](https://neetcode.io/practice) · [LeetCode: Sort an Array](https://leetcode.com/problems/sort-an-array/) · [LeetCode: Count Primes](https://leetcode.com/problems/count-primes/)

| # | Concept | Key Pattern / API |
|---|---------|------------------|
| 1 | Merge sort | Divide + merge, O(n log n) |
| 2 | Quick sort | Pivot partition |
| 3 | Heap sort | Build + extract |
| 4 | Counting sort | O(n+k), integer keys |
| 5 | Radix sort | Digit-by-digit |
| 6 | Sorting stability | Preserves equal order |
| 7 | Timsort | Python's `sorted()` |
| 8 | Sort comparison table | Time/space/stability |
| 9 | GCD | `math.gcd()`, Euclidean |
| 10 | LCM | `math.lcm()` |
| 11 | Prime checking | Trial division √n |
| 12 | Sieve of Eratosthenes | O(n log log n) |
| 13 | Fast power | `pow(base, exp, mod)` |
| 14 | Modular arithmetic | Overflow prevention |
| 15 | Fibonacci variants | Matrix, DP |
| 16 | Combinatorics | `math.comb()`, Pascal's |
| 17 | Template consolidation | Unify all weeks |
| 18 | Timed practice | Interview simulation |
| 19 | Verbal explanation | Explain before code |
| 20 | Weak-area diagnosis | Log personal gaps |
| 21 | Quickselect | Partition to find kth in O(n) avg |
| 22 | Next permutation | In-place lexicographic step |
| 23 | Visual: partition trace | Merge/quick partition step-by-step |
| 24 | Complexity: sort/math cheat | O(n log n) sorts · O(√n) primality |

---

## MAANG Depth Coverage

| Concept | Week |
|---------|------|
| Kadane's algorithm | 02, reinforced 16 |
| 3Sum dedupe | 03 |
| Recursion foundation | 11 |
| Processed/unprocessed state | 11 |
| Subsequence generation | 11 |
| Subset-sum | 11, 16 |
| Pattern printing (recursion) | 11 |
| Binary tree: construction, LCA, diameter, traversals | 08 |
| Monotonic deque | 04, 05 |
| Intervals | 15 |
| String algorithms (palindromes, KMP, Rabin-Karp) | 03, 04, 19 |
| Substring/consecutive patterns | 04, 19 |
| Sorting algorithms | 20 |
| Matrix traversal | 12, 17 |
| Math/number theory | 20 |

---

## Folder Slugs

| Week | Folder |
|------|--------|
| 01–20 | `week_{NN}_{slug}/` under `src/dsa/` and `exercise/dsa/` |
