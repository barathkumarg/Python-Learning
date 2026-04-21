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

> Gate G8: every concept must appear in CODE.md table + at least one of: visual/diagram, code.py function, or exercise stub. Cap: 15–20 per week.

### Week 01 — Big-O, Arrays, Hashing (18)

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

### Week 02 — Arrays, Hashing, Kadane (18)

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

### Week 03 — Two Pointers (17)

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

### Week 04 — Sliding Window, Monotonic Deque (18)

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

### Week 05 — Stack, Monotonic Structures (17)

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

### Week 06 — Binary Search (17)

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

### Week 07 — Linked List (17)

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

### Week 08 — Binary Trees I (20)

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

### Week 09 — BST (16)

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

### Week 10 — Heap (16)

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

### Week 11 — Recursion and Backtracking (20)

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

### Week 12 — Graphs I (18)

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

### Week 13 — Graphs II, Topo Sort (16)

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

### Week 14 — Union-Find (15)

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

### Week 15 — Intervals and Greedy (17)

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

### Week 16 — 1D DP (18)

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

### Week 17 — 2D DP (16)

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

### Week 18 — Shortest Paths (16)

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

### Week 19 — Tries, Strings, Bits (20)

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

### Week 20 — Mixed Review, Sorting, Math (20)

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
