# Daily Python + DSA Study Plan (Checkbox)

> **Role:** Professional backend Python + DSA tutor track — industrial exercises, parallel DSA from fundamentals.  
> **Companions:** [README.md](./README.md) · [.agent.md](./.agent.md) · this file is your **single checklist**.

---

## Repository layout (canonical paths)

Use **one pair of folders per day** (Python) or **per DSA week** (parallel track). Spelling is **`exercise/`** (not `execise`).

```
src/
  python_basic/           # study days 1–14
    day_01_syntax_variables/
    day_02_control_flow/
    …
  python_intermediate/    # days 15–34
  python_concurrency/     # days 35–50
  python_advanced/        # days 51–70
  fastapi_track/          # days 71–86
  devops_track/           # days 87–100
  dsa/                    # parallel DSA — see § Parallel DSA
    week01_big_o_arrays_hashing/
    week02_arrays_hashing_ii/
    …

exercise/
  python_basic/
    day_01_syntax_variables/
    day_02_control_flow/
    …
  python_intermediate/
  python_concurrency/
  python_advanced/
  fastapi_track/
  devops_track/
  dsa/
    week_01_big_o_arrays_hashing/
    …
```

**Naming rules**

| Location | Pattern | Example |
|----------|---------|---------|
| `src/` | `day_NN_short_topic` | `src/python_basic/day_08_strings/` |
| `exercise/` | `day_NN_short_topic` | `exercise/python_basic/day_08_strings/` |

**Where files go (avoid misconfiguration):**

| Content | Path |
|---------|------|
| Code explanation (theory) | `src/<track>/day_NN_topic/CODE.md` |
| Teaching / reference code | `src/<track>/day_NN_topic/code.py` |
| Learner tasks + evaluation | `exercise/<track>/day_NN_topic/` (EXERCISE.md + EVALUATION.md + ex files + `test_exercises.py`) |

Do **not** put `ex01`/`ex02`/`ex03` only under `src/.../` with no tests. Do **not** duplicate an `exercise/` subfolder inside `src/.../dayNN/` for day-to-day work — the canonical learner tree is `exercise/<track>/...` as above.

---

## Suggested additions (optional but strong)

| Addition | Why |
|----------|-----|
| [docs/EVALUATION_RUBRIC.md](docs/EVALUATION_RUBRIC.md) | **Normative** gates, dimension scores, per-exercise 0–100, evaluation prompt template |
| **`.cursor/rules`** or project rule | Point to `.agent.md` + `docs/EVALUATION_RUBRIC.md` so every chat inherits the bar |
| **`pyproject.toml`** with `ruff`, `pytest`, optional `mypy` | Same gates as CI in real teams |
| **`pre-commit`** | Optional; runs `ruff` + `pytest` on commit (see rubric §7) |

---

## Misconfiguration analysis (checklist)

| Issue | Symptom | Fix |
|-------|---------|-----|
| Exercises without tests | “Done” is subjective | Require `test_exercises.py` in every generation prompt ([.agent.md](./.agent.md)) |
| Evaluation rubric missing | Agent forgets weights next time | Use `exercise/.../EVALUATION.md` per day |
| Reference code = exercise answers | No learning gap | `src/.../code.py` teaches patterns; learner fills `exercise/.../exNN` stubs |
| Wrong file paths | Import/tests fail | Use `src/<track>/day_NN_topic/code.py` and `exercise/<track>/day_NN_topic/test_exercises.py` |
| `applyTo: "*.md"` only | Rules may not attach to `.py` | Add Cursor **project rules** or `@.agent` in prompts when you generate code |
| No `docs/EVALUATION_RUBRIC.md` in prompt | Drift from industrial bar | Paste “Read docs/EVALUATION_RUBRIC.md” in every generation request |

---

## Agentic systems (how you generate code & exercises)

**Ready-made prompts:** [docs/PROMPT_TEMPLATES.md](docs/PROMPT_TEMPLATES.md) (full module, content-only, exercise-only, evaluation).

Use these **in order** whenever you start a new day or DSA week.

1. **Cursor + [.agent.md](./.agent.md) + [docs/EVALUATION_RUBRIC.md](docs/EVALUATION_RUBRIC.md)**  
   The agent must emit: `CODE.md`, `code.py`, `EXERCISE.md`, `EVALUATION.md`, `ex01`–`ex03` (stubs/TODOs only), and `test_exercises.py`. Rubric weights and evaluation steps live in `docs/EVALUATION_RUBRIC.md` — not optional for “industrial” runs.

2. **Context bundle (paste at top of your prompt)**  
   ```
   Repo: Python-Learning. Read README.md, DAILY_STUDY_PLAN.md, and docs/EVALUATION_RUBRIC.md.
   Day: [NN] — Track: [<track>] — Slug: day_XX_<content>
   Paths:
   - src/<track>/day_XX_<content>/
   - exercise/<track>/day_XX_<content>/
   Follow .agent.md: CODE.md, code.py, EXERCISE.md, EVALUATION.md, ex01–ex03 stubs, test_exercises.py (pytest).
   Enforce gates G1–G7 from docs/EVALUATION_RUBRIC.md §1.
   ```

3. **Standard generation prompt (Python day)**  
   ```
   Generate the full module for Day [NN] — [topic] per DAILY_STUDY_PLAN.md.
   Output under:
   - src/<track>/day_XX_<content>/ (CODE.md + code.py)
   - exercise/<track>/day_XX_<content>/ (EXERCISE.md + EVALUATION.md + ex01–ex03 stubs + test_exercises.py)
   Industrial: type hints, ruff-clean, pytest must-pass behaviors.
   Read docs/EVALUATION_RUBRIC.md and ensure EVALUATION.md matches §§1–3.
   ```

4. **Standard generation prompt (DSA week)**  
   ```
   Generate DSA week [WW] per DAILY_STUDY_PLAN: Notes.md, src/dsa/weekWW_slug/src/code.py,
   exercise/dsa/week_WW_slug/ with ex01–ex03, RUBRIC.md, test_exercises.py.
   Complexity in docstrings; optional LeetCode-style names as practice targets only.
   ```

5. **Evaluation pass (same session or next)**  
   Use the **verbatim template** in [docs/EVALUATION_RUBRIC.md](docs/EVALUATION_RUBRIC.md) §5.2 — gates, D1–D7, per-file 0–100, top 3 fixes.  
   Attach paths or paste your solution files.

6. **Git as progress journal**  
   Commit after each checked day: `study: day 07 python_basic sets`.

---

## Time budget

| Block | Time | Notes |
|-------|------|--------|
| Python weekday | 60–90 min | One checklist “day” below |
| DSA parallel | 45–90 min | Same calendar week’s DSA § + problems |
| Sunday | 90–120 min | **Intermediate integrative** lab (below) |
| Quality | 15 min | `uv run ruff check .`, `uv run pytest`, `uv run mypy` where set up |

---

## Phase 1 — Python basics (days 1–14) · `python_basic/`

**Track folder:** `src/python_basic/` · `exercise/python_basic/`

- [ ] **Day 01** — Syntax, types, f-strings · `day01_syntax_variables` / `day_01_syntax_variables`  
  - [ ] Study: README Basic — Syntax & Variables  
  - [ ] Exercise theme: CLI argv, validation, exit codes  

- [ ] **Day 02** — Control flow, `match` · `day02_control_flow` / `day_02_control_flow`  
  - [ ] Exercise theme: order status state machine  

- [ ] **Day 03** — Functions, `*args`, `**kwargs`, lambda · `day03_functions` / `day_03_functions`  
  - [ ] Exercise theme: pluggable validators for a form dict  

- [ ] **Day 04** — Lists, sorting · `day04_lists` / `day_04_lists`  
  - [ ] Exercise theme: leaderboard, tie-break, top-k  

- [ ] **Day 05** — Tuples, `NamedTuple` · `day05_tuples` / `day_05_tuples`  
  - [ ] Exercise theme: CSV rows as immutable DTOs  

- [ ] **Day 06** — Dicts, comprehensions · `day06_dictionaries` / `day_06_dictionaries`  
  - [ ] Exercise theme: inverted index word → line numbers  

- [ ] **Day 07** — Sets, frozenset · `day07_sets` / `day_07_sets`  
  - [ ] Exercise theme: dedupe logs; allow/deny tag sets  

- [ ] **Day 08** — Strings, encoding · `day08_strings` / `day_08_strings`  
  - [ ] Exercise theme: normalizer, slugify for URLs  

- [ ] **Day 09** — File I/O, `pathlib`, CSV, JSON · `day09_file_io` / `day_09_file_io`  
  - [ ] Exercise theme: CSV → validate → JSON lines ETL stub  

- [ ] **Day 10** — Exceptions, custom errors · `day10_exceptions` / `day_10_exceptions`  
  - [ ] Exercise theme: domain errors; retry sketch  

- [ ] **Day 11** — Modules, packages · `day11_modules` / `day_11_modules`  
  - [ ] Exercise theme: `src` layout, runnable `__main__`  

- [ ] **Day 12** — Built-ins: `enumerate`, `zip`, `map`, `filter` · `day12_builtins` / `day_12_builtins`  
  - [ ] Exercise theme: parse → map → filter → aggregate pipeline  

- [ ] **Day 13** — Comprehensions + generator preview · `day13_comprehensions` / `day_13_comprehensions`  
  - [ ] Exercise theme: generator yielding last N lines of a file  

- [ ] **Day 14** — `venv`, `uv`, `pyproject` / deps · `day14_tooling` / `day_14_tooling`  
  - [ ] Exercise theme: reproducible env + README install snippet  

---

## Phase 2 — Intermediate (days 15–34) · `python_intermediate/`

- [ ] **Day 15** — Classes, `__init__` · `day15_classes`  
- [ ] **Day 16** — `__repr__`, `__eq__`, `__hash__` · `day16_dunder_value_objects`  
- [ ] **Day 17** — `@property`, validation · `day17_properties`  
- [ ] **Day 18** — Inheritance, MRO · `day18_inheritance`  
- [ ] **Day 19** — `abc`, abstract classes · `day19_abstract_base`  
- [ ] **Day 20** — `@dataclass` · `day20_dataclasses`  
- [ ] **Day 21** — `@classmethod`, `@staticmethod` · `day21_class_static`  
- [ ] **Day 22** — Iterators · `day22_iterators`  
- [ ] **Day 23** — Generators, pipelines · `day23_generators`  
- [ ] **Day 24** — Generator expressions · `day24_generator_expressions`  
- [ ] **Day 25** — Decorators, `@wraps` · `day25_decorators`  
- [ ] **Day 26** — Parametric decorators · `day26_decorators_advanced`  
- [ ] **Day 27** — Context managers · `day27_context_managers`  
- [ ] **Day 28** — `@contextmanager` · `day28_contextmanager`  
- [ ] **Day 29** — `functools` · `day29_functools`  
- [ ] **Day 30** — `itertools` · `day30_itertools`  
- [ ] **Day 31** — Type hints, `Optional`, `Union` · `day31_typing_basics`  
- [ ] **Day 32** — `TypedDict`, `Literal` · `day32_typing_advanced`  
- [ ] **Day 33** — Generics, `TypeVar` · `day33_generics`  
- [ ] **Day 34** — `mypy` strictness · `day34_mypy`  

*(Mirror each `dayNN_*` under `exercise/python_intermediate/day_NN_*`.)*

---

## Phase 3 — Concurrency (days 35–50) · `python_concurrency/`

- [ ] **Day 35** — Threading, locks · `day35_threading`  
- [ ] **Day 36** — GIL, CPU vs I/O · `day36_gil`  
- [ ] **Day 37** — `multiprocessing.Pool` · `day37_multiprocessing`  
- [ ] **Day 38** — `concurrent.futures` · `day38_futures`  
- [ ] **Day 39** — `asyncio` basics · `day39_asyncio`  
- [ ] **Day 40** — `aiohttp` · `day40_aiohttp`  
- [ ] **Day 41** — Async errors, `gather` · `day41_async_errors`  
- [ ] **Day 42** — Executors from async · `day42_sync_async_bridge`  
- [ ] **Day 43** — Service boundaries · `day43_concurrency_design`  
- [ ] **Day 44** — Consolidate refactor · `day44_refactor`  
- [ ] **Day 45** — **Milestone** mini-project · `day45_milestone`  
- [ ] **Day 46** — `pyproject` package split · `day46_packaging`  
- [ ] **Day 47** — `pytest` concurrency · `day47_pytest_async`  
- [ ] **Day 48** — Mocking I/O · `day48_mocking`  
- [ ] **Day 49** — `logging` · `day49_logging`  
- [ ] **Day 50** — Phase review doc · `day50_review`  

---

## Phase 4 — Advanced (days 51–70) · `python_advanced/`

- [ ] **Day 51** — Descriptors · `day51_descriptors`  
- [ ] **Day 52** — `__slots__` · `day52_slots`  
- [ ] **Day 53** — Metaclasses (read-heavy) · `day53_metaclasses`  
- [ ] **Day 54** — `__init_subclass__` · `day54_init_subclass`  
- [ ] **Day 55** — Bytecode `dis` · `day55_bytecode`  
- [ ] **Day 56** — Import system · `day56_importlib`  
- [ ] **Day 57** — `cProfile` · `day57_cprofile`  
- [ ] **Day 58** — `timeit` · `day58_timeit`  
- [ ] **Day 59** — `pytest` fixtures · `day59_pytest_fixtures`  
- [ ] **Day 60** — Coverage · `day60_coverage`  
- [ ] **Day 61** — `ruff`, `pre-commit` · `day61_ruff_precommit`  
- [ ] **Day 62** — `bandit` · `day62_bandit`  
- [ ] **Day 63** — Strategy + Factory · `day63_patterns_creational`  
- [ ] **Day 64** — Repository + DI · `day64_patterns_architecture`  
- [ ] **Day 65** — `pyproject` library · `day65_packaging_library`  
- [ ] **Day 66** — `uv` workflow · `day66_uv`  
- [ ] **Day 67** — **Milestone** library CI · `day67_milestone`  
- [ ] **Day 68** — Metaprogramming review · `day68_review_meta`  
- [ ] **Day 69** — Testing strategy · `day69_review_testing`  
- [ ] **Day 70** — Retrospective · `day70_retrospective`  

---

## Phase 5 — FastAPI (days 71–86) · `fastapi_track/`

- [ ] **Day 71** — App, routing, OpenAPI · `day71_fastapi_intro`  
- [ ] **Day 72** — Pydantic v2, bodies · `day72_pydantic`  
- [ ] **Day 73** — Dependencies · `day73_dependencies`  
- [ ] **Day 74** — Exception handlers · `day74_errors`  
- [ ] **Day 75** — OAuth2 + JWT · `day75_security_jwt`  
- [ ] **Day 76** — Middleware, CORS · `day76_middleware`  
- [ ] **Day 77** — Background tasks · `day77_background`  
- [ ] **Day 78** — SQLAlchemy async, Alembic · `day78_db_alembic`  
- [ ] **Day 79** — Repository in API · `day79_repository`  
- [ ] **Day 80** — TestClient / AsyncClient · `day80_testing`  
- [ ] **Day 81** — WebSockets (optional) · `day81_websockets`  
- [ ] **Day 82** — Docker · `day82_docker`  
- [ ] **Day 83** — `pydantic-settings` · `day83_settings`  
- [ ] **Day 84** — **Milestone** service · `day84_milestone`  
- [ ] **Day 85** — Health / readiness · `day85_probes`  
- [ ] **Day 86** — API checklist · `day86_review`  

---

## Phase 6 — DevOps + capstone (days 87–100) · `devops_track/`

- [ ] **Day 87** — `pdb` · `day87_pdb`  
- [ ] **Day 88** — `structlog` · `day88_structlog`  
- [ ] **Day 89** — OpenTelemetry · `day89_otel`  
- [ ] **Day 90** — `subprocess` · `day90_subprocess`  
- [ ] **Day 91** — Boto3 or Docker SDK · `day91_cloud_sdk`  
- [ ] **Day 92** — GitHub Actions · `day92_actions`  
- [ ] **Day 93** — Prometheus · `day93_prometheus`  
- [ ] **Day 94** — **Capstone** deploy · `day94_capstone`  
- [ ] **Day 95** — Runbook · `day95_runbook`  
- [ ] **Day 96** — DSA timed practice · `day96_dsa_timed`  
- [ ] **Day 97** — DSA explain-aloud · `day97_dsa_verbal`  
- [ ] **Day 98** — Portfolio README · `day98_portfolio`  
- [ ] **Day 99** — README tracker sync · `day99_full_review`  
- [ ] **Day 100** — Next 30 days plan · `day100_graduation`  

---

## Sunday labs — intermediate (every 5 study days)

Complete **after** the fifth day of each block (e.g. after day 5, 10, …). These are **integrative**: combine the week’s topics, industrial quality, tests.

- [ ] **Sunday 1** (after day 5): Mini service — **config + CLI + CSV leaderboard** using days 1–5 (typed dict rows, sorted output, file error handling).  
- [ ] **Sunday 2** (after day 10): **Log pipeline** — read mixed logs, dedupe (sets), normalize strings, write JSONL + structured errors.  
- [ ] **Sunday 3** (after day 14): **Tooling handoff** — package skeleton with `pyproject.toml`, `uv`, one console entrypoint, README “how to run”.  
- [ ] **Sunday 4** (after day 19): **Plugin system** — ABC storage + two backends + dataclass events + tests.  
- [ ] **Sunday 5** (after day 24): **Lazy ETL** — generators + iterators; memory-bounded processing from large fixture file.  
- [ ] **Sunday 6** (after day 29): **Cross-cutting concerns** — decorators for timing + retry; context manager for atomic file; `functools` cache on pure parser.  
- [ ] **Sunday 7** (after day 34): **Typed library slice** — `mypy` clean module + `pytest` + one `Protocol`.  
- [ ] **Sunday 8** (after day 39): **Concurrent fetch** — thread pool OR asyncio (pick one) with timeouts; document tradeoff.  
- [ ] **Sunday 9** (after day 44): **Refactor milestone** — unify async/sync boundaries; add logging.  
- [ ] **Sunday 10** (after day 50): **Concurrency retrospective** — short design doc + diagram (ASCII ok).  
- [ ] **Sunday 11** (after day 55): **Profile & fix** — take day 45 code, profile, one evidence-based optimization.  
- [ ] **Sunday 12** (after day 60): **Quality gate** — `ruff` + `pytest --cov` + `pre-commit` config in repo.  
- [ ] **Sunday 13** (after day 65): **Patterns** — Strategy + Repository for a fake “billing” module with tests.  
- [ ] **Sunday 14** (after day 70): **Library release dry-run** — editable install, version bump story, tag in git.  
- [ ] **Sunday 15** (after day 75): **Auth slice** — JWT issue/verify in isolation + pytest.  
- [ ] **Sunday 16** (after day 80): **Integration tests** — FastAPI app with dependency overrides + fake DB.  
- [ ] **Sunday 17** (after day 86): **Docker + API** — one `docker compose` with API + healthcheck.  
- [ ] **Sunday 18** (after day 91): **Automation script** — safe `subprocess` + structured logs + exit codes.  
- [ ] **Sunday 19** (after day 96): **DSA + API** — one endpoint that runs a pure DSA routine (e.g. validate parentheses) with unit tests.  
- [ ] **Sunday 20** (after day 100): **Capstone review** — demo script, architecture notes, backlog of 5 improvements.  

**Folder suggestion for Sundays:** `exercise/sunday_labs/week_01_integrated/` … `week_20_integrated/` (optional `Notes.md` only).

---

## Parallel DSA — fundamentals → advanced

**Folders:** `src/dsa/weekNN_slug/` · `exercise/dsa/week_NN_slug/`  
**External practice:** [NeetCode roadmap](https://neetcode.io/roadmap) + [LeetCode](https://leetcode.com/) (solve **2–3 problems/week** minimum on platform; your repo holds **clean implementations** and **custom exercises**).

### Week 01 — Big-O, arrays, hashing basics

- [ ] Theory: Big-O, amortized, why hash maps are O(1) average  
- [ ] Implement: dynamic array behavior intuition (Python lists), hash map API drills  
- [ ] `exercise/dsa/week_01_.../`: ex01 two-sum variant, ex02 anagram buckets, ex03 longest without repeat (skeletons + tests)  
- [ ] Platform: 2 problems — e.g. Two Sum, Contains Duplicate  

### Week 02 — Arrays & hashing II

- [ ] Prefix sum, frequency maps, sorting tie-ins  
- [ ] Implement: prefix array builder; group-by key  
- [ ] Exercises: subarray sum equals k (concept), encode/decode lists (design)  
- [ ] Platform: Group Anagrams, Top K Frequent  

### Week 03 — Two pointers

- [ ] Sorted array pair sums, opposite ends, triplet patterns  
- [ ] Implement: `pair_sum`, `three_sum` (no duplicates) templates  
- [ ] Platform: 3Sum, Container With Most Water  

### Week 04 — Sliding window

- [ ] Fixed vs variable window, invariant maintenance  
- [ ] Implement: min window substring scaffold (tests for small inputs)  
- [ ] Platform: Longest Repeating Character Replacement, Minimum Window Substring  

### Week 05 — Stack

- [ ] Monotonic stack intuition, parentheses, daily temperatures pattern  
- [ ] Implement: stack ADT + next greater element  
- [ ] Platform: Valid Parentheses, Daily Temperatures  

### Week 06 — Binary search

- [ ] Bounds, lower/upper bound, rotated array  
- [ ] Implement: `bisect` mental model + custom binary search  
- [ ] Platform: Binary Search, Search in Rotated Sorted Array  

### Week 07 — Linked list

- [ ] Dummy node, fast/slow pointers, reversal  
- [ ] Implement: singly linked list class + cycle detection  
- [ ] Platform: Reverse Linked List, Merge Two Sorted Lists  

### Week 08 — Trees I (BT)

- [ ] DFS pre/in/post, BFS level order  
- [ ] Implement: tree from list (level-order), height, balanced check  
- [ ] Platform: Maximum Depth, Same Tree  

### Week 09 — Trees II (BST)

- [ ] BST validate, successor, kth smallest  
- [ ] Platform: Validate BST, Kth Smallest in BST  

### Week 10 — Heap / priority queue

- [ ] `heapq`, top-k, merge k lists concept  
- [ ] Implement: running median (two heaps) sketch  
- [ ] Platform: Kth Largest, Merge K Sorted Lists  

### Week 11 — Backtracking

- [ ] Subsets, permutations, pruning  
- [ ] Implement: subsets with duplicates template  
- [ ] Platform: Subsets, Combination Sum  

### Week 12 — Graphs I

- [ ] Adjacency list/matrix, BFS/DFS, island count  
- [ ] Implement: graph class + BFS shortest path unweighted  
- [ ] Platform: Number of Islands, Clone Graph  

### Week 13 — Graphs II

- [ ] Topo sort (Kahn), cycle detection  
- [ ] Platform: Course Schedule  

### Week 14 — Union-Find

- [ ] Path compression, union by rank  
- [ ] Implement: DSU class with tests  
- [ ] Platform: Redundant Connection, Number of Provinces  

### Week 15 — Greedy

- [ ] Intervals, scheduling, proof sketches  
- [ ] Platform: Non-overlapping Intervals, Jump Game  

### Week 16 — 1D DP

- [ ] Climbing stairs, house robber, coin change  
- [ ] Implement: bottom-up + top-down with memo  
- [ ] Platform: Coin Change, House Robber  

### Week 17 — 2D DP

- [ ] Grid paths, LCS, edit distance (concept)  
- [ ] Platform: Unique Paths, Longest Common Subsequence  

### Week 18 — Shortest paths

- [ ] Dijkstra (heap), Bellman-Ford awareness  
- [ ] Implement: Dijkstra on small graph with `heapq`  
- [ ] Platform: Network Delay Time  

### Week 19 — Advanced topics / review

- [ ] Tries (insert/search), bit tricks intro  
- [ ] Platform: Implement Trie, Single Number  

### Week 20 — Integration

- [ ] Timed mixed set (3 problems), explain solutions aloud  
- [ ] NeetCode blind revisit: pick by weak area from README  

---

## DSA folder slugs (reference)

| Week | `src/dsa/` folder |
|------|-------------------|
| 01 | `week01_big_o_arrays_hashing/` |
| 02 | `week02_arrays_hashing_ii/` |
| 03 | `week03_two_pointers/` |
| 04 | `week04_sliding_window/` |
| 05 | `week05_stack/` |
| 06 | `week06_binary_search/` |
| 07 | `week07_linked_list/` |
| 08 | `week08_binary_tree/` |
| 09 | `week09_bst/` |
| 10 | `week10_heap/` |
| 11 | `week11_backtracking/` |
| 12 | `week12_graphs_i/` |
| 13 | `week13_graphs_ii_topo/` |
| 14 | `week14_union_find/` |
| 15 | `week15_greedy/` |
| 16 | `week16_dp_1d/` |
| 17 | `week17_dp_2d/` |
| 18 | `week18_shortest_path/` |
| 19 | `week19_tries_bits/` |
| 20 | `week20_mixed_review/` |

Mirror under `exercise/dsa/week_01_big_o_arrays_hashing/` etc.

---

## Industrial bar (Python + DSA repo work)

- Types on public APIs; docstrings with complexity for DSA.  
- **`pytest`** + **`RUBRIC.md`** per day; no bare `except:`.  
- DSA: cite complexity in file header; avoid copying proprietary problem text verbatim—use your own examples in comments.

**Measurement:** Use [docs/EVALUATION_RUBRIC.md](docs/EVALUATION_RUBRIC.md) — gates, weighted dimensions, **0–100** per exercise file.

---

## Flexibility

- **1:1 calendar mapping:** Treat “DSA Week *n*” as the same calendar week as “Study days 5*n*−4 … 5*n*” if you want strict lockstep; otherwise finish DSA Week *n* within the same **phase** (basics vs intermediate).  
- **Missed Sunday:** Do the Sunday lab before starting the next phase milestone (day 45, 67, 84, 94).

Your full topic tables and links remain in [README.md](./README.md).
