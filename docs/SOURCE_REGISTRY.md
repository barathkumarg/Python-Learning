# Source Registry for Industrial-Level Generation

This file records high-value learning sources that are safe to use as inputs for generating:

- `src/<track>/day_NN_topic/CODE.md`
- `src/<track>/day_NN_topic/code.py`
- `exercise/<track>/day_NN_topic/EXERCISE.md`
- `exercise/<track>/day_NN_topic/ex01_*.py` to `ex03_*.py`

Use this registry to keep content quality high and source usage intentional.

---

## Why this exists

Not every Python resource is good for every artifact.

- Some sources are best for **teaching flow**.
- Some are best for **production-style reference code**.
- Some are best for **exercise ideas and difficulty ladders**.
- Some are best for **DSA problem sourcing**, but not for production code style.

This registry helps future generation work use the right source for the right job.

---

## Source usage rules

When using any external source:

- Mirror the source's **concept progression**, not its exact wording.
- Do **not** copy proprietary explanations, large code blocks, or problem text verbatim.
- Rewrite examples in the repo's style: typed signatures, clear validation, explicit errors, concise docstrings, inline self-checks.
- Prefer official docs and production-oriented repos for `code.py`.
- Prefer challenge banks and practice repos for `EXERCISE.md` inspiration, not for answer-copying.
- If a source is beginner-friendly but not production-grade, use it for ordering and exercise shape, then raise the code quality to this repo's standard.
- **Always consult the day's inline `Sources:` line in `study_plan/<track>.md`** before generating — it names the primary + secondary source URL for that day. This file is the curated catalog to draw from for anything extra.

---

## Source buckets

| Bucket | Best use | Avoid using it for | Quality Tier |
|--------|----------|--------------------|-------------|
| Tutorial progression | `CODE.md` learning order and beginner examples | Copy-pasting long prose | T2 — Curated tutorial |
| Production examples | `code.py` reference implementations and style cues | Full exercise specs without adaptation | T1 — Official docs |
| Exercise bank | `EXERCISE.md` must-pass/stretch ideas | Direct solution copying | T3 — Community exercise |
| DSA problem archive | DSA practice links, stretch prompts, complexity framing | Production Python API design | T2 — Curated tutorial |
| Video resources | Concept reinforcement, visual walkthroughs | Primary teaching source (use docs first) | T2 — Curated tutorial |
| Interactive tools | Live code visualization, playground experimentation | Formal reference (use docs for that) | T3 — Community exercise |
| Books | Deep conceptual understanding, chapter-mapped study | Quick reference (use cheat sheets for that) | T1 — Authoritative |
| Cheat sheets | Quick lookup during generation, complexity tables | In-depth learning (use tutorials for that) | T3 — Quick reference |

### Quality Tier Legend

| Tier | Meaning | When to use |
|------|---------|-------------|
| T1 — Official/Authoritative | Official docs, language specs, published books | Ground truth for API behavior, complexity proofs |
| T2 — Curated tutorial | Vetted articles, established YouTube channels, maintained repos | Concept ordering, practical examples, video walkthroughs |
| T3 — Community/Quick-ref | Exercise banks, cheat sheets, playground tools | Exercise inspiration, quick lookup, interactive exploration |

---

## Curated external sources

### Tutorial progression sources

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| Asabeneh - 30 Days of Python | <https://github.com/Asabeneh/30-Days-Of-Python> | Day-scoped concept ordering for `CODE.md`, beginner-to-intermediate topic shapes | Good for concept progression and exercise layering. Raise examples to typed, production-style. |
| CodeWithHarry - Ultimate Python Course | <https://github.com/CodeWithHarry/The-Ultimate-Python-Course> | Chapter-level teaching flow, beginner-to-intermediate sequencing, project and problem-set inspiration | Useful when we need broader course structure around a topic. |
| CodeWithHarry - Python Handbook PDF | <https://github.com/CodeWithHarry/The-Ultimate-Python-Course/blob/main/The%20Ultimate%20Python%20Handbook.pdf> | Offline reading reference for concepts, summaries, and chapter coverage checks | Use for topic coverage verification, not for copying handbook prose. |

### Production-style reference sources

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| Real Python — Defining Functions | <https://realpython.com/defining-your-own-python-function/> | `CODE.md` teaching order + `code.py` style for Day 03 | Follow its progression: def -> call -> return -> defaults -> *args -> **kwargs |
| Real Python — Lists and Tuples | <https://realpython.com/python-lists-tuples/> | `CODE.md` + `code.py` for Days 04-05 | Covers indexing, slicing, mutation, sorting |
| Real Python — Dictionaries | <https://realpython.com/python-dicts/> | `CODE.md` + `code.py` for Day 06 | CRUD, comprehension, nesting, iteration patterns |
| Real Python — Sets | <https://realpython.com/python-sets/> | `CODE.md` + `code.py` for Day 07 | Uniqueness, set math, frozenset, membership |
| Real Python — Strings | <https://realpython.com/python-strings/> | `CODE.md` + `code.py` for Day 08 | Slicing, methods, formatting, encoding |
| Real Python — File I/O | <https://realpython.com/read-write-files-python/> | `CODE.md` + `code.py` for Day 09 | open, context managers, pathlib, CSV, JSON |
| Real Python — Exceptions | <https://realpython.com/python-exceptions/> | `CODE.md` + `code.py` for Day 10 | try/except/else/finally, custom errors, chaining |
| Real Python — Modules and Packages | <https://realpython.com/python-modules-packages/> | `CODE.md` + `code.py` for Day 11 | Imports, __name__, __main__, package layout |
| Real Python — Comprehensions | <https://realpython.com/list-comprehension-python/> | `CODE.md` + `code.py` for Day 13 | List/dict/set comprehensions, generator expressions |
| Real Python — Type Checking | <https://realpython.com/python-type-checking/> | `CODE.md` + `code.py` for Days 31-34 | Optional, Union, TypedDict, TypeVar, generics, mypy |
| Real Python — OOP | <https://realpython.com/python3-object-oriented-programming/> | `CODE.md` + `code.py` for Days 15-21 | Classes, inheritance, ABC, class/static methods |
| Real Python — Dataclasses | <https://realpython.com/python-data-classes/> | `CODE.md` + `code.py` for Day 20 | @dataclass, field, frozen, slots, __post_init__ |
| Real Python — Properties | <https://realpython.com/python-property/> | `CODE.md` + `code.py` for Day 17 | @property, setters, computed fields, validation gates |
| Real Python — Decorators | <https://realpython.com/primer-on-python-decorators/> | `CODE.md` + `code.py` for Days 25-26 | Wrappers, functools.wraps, factories, parametric |
| Real Python — Context Managers | <https://realpython.com/python-with-statement/> | `CODE.md` + `code.py` for Days 27-28 | __enter__/__exit__, @contextmanager, setup/teardown |
| Real Python — Generators | <https://realpython.com/introduction-to-python-generators/> | `CODE.md` + `code.py` for Days 23-24 | yield, lazy pipelines, yield from, memory savings |
| Real Python — Iterators | <https://realpython.com/python-iterators-iterables-iteration/> | `CODE.md` + `code.py` for Day 22 | Iterable protocol, iter, next, StopIteration |
| Real Python — functools | <https://realpython.com/python-functools/> | `CODE.md` + `code.py` for Day 29 | partial, lru_cache, reduce, singledispatch |
| Real Python — itertools | <https://realpython.com/python-itertools/> | `CODE.md` + `code.py` for Day 30 | chain, islice, groupby, product, combinations |
| Real Python — Threading | <https://realpython.com/intro-to-python-threading/> | `CODE.md` + `code.py` for Days 35-36 | Threads, locks, race conditions, GIL tradeoffs |
| Real Python — Asyncio | <https://realpython.com/async-io-python/> | `CODE.md` + `code.py` for Days 39-41 | Event loop, coroutines, await, gather, cancellation |
| Real Python — Multiprocessing | <https://realpython.com/python-multiprocessing/> | `CODE.md` + `code.py` for Day 37 | Process pool, serialization, fan-out workloads |
| Real Python — Descriptors | <https://realpython.com/python-descriptors/> | `CODE.md` + `code.py` for Day 51 | __get__, __set__, validation descriptors |
| Real Python — Metaclasses | <https://realpython.com/python-metaclasses/> | `CODE.md` + `code.py` for Day 53 | type, controlled class creation, limited use cases |
| Real Python — pytest | <https://realpython.com/pytest-python-testing/> | `CODE.md` + `code.py` for Days 47, 59-60 | Fixtures, scopes, parametrize, async testing |
| Real Python — Logging | <https://realpython.com/python-logging/> | `CODE.md` + `code.py` for Days 49, 88 | Structured logs, handlers, formatters, context |
| Real Python — subprocess | <https://realpython.com/python-subprocess/> | `CODE.md` + `code.py` for Day 90 | Argument lists, capture, timeouts, injection safety |
| Python official docs — Tutorial | <https://docs.python.org/3/tutorial/> | Ground truth for all Python basics (Days 01-14) | Use as the authoritative reference when explaining syntax or built-in behavior. |
| Python official docs — Library Reference | <https://docs.python.org/3/library/> | API truth for all standard library modules | Link to specific module sections in Further reading. |
| Python official docs — typing | <https://docs.python.org/3/library/typing.html> | API truth for type annotations (Days 31-34) | Use as ground truth for Optional, Union, TypeVar, Generic. |
| Python official docs — functools | <https://docs.python.org/3/library/functools.html> | API truth for Day 29 | partial, lru_cache, cache, reduce, singledispatch |
| Python official docs — itertools | <https://docs.python.org/3/library/itertools.html> | API truth for Day 30 | chain, islice, groupby, product, combinations |
| Python official docs — asyncio | <https://docs.python.org/3/library/asyncio.html> | API truth for Days 39-41 | Event loop, coroutines, tasks, gather |
| Python official docs — concurrent.futures | <https://docs.python.org/3/library/concurrent.futures.html> | API truth for Day 38 | ThreadPoolExecutor, ProcessPoolExecutor, as_completed |
| Python official docs — dataclasses | <https://docs.python.org/3/library/dataclasses.html> | API truth for Day 20 | @dataclass, field, frozen, slots |
| Python official docs — collections | <https://docs.python.org/3/library/collections.html> | API truth for Days 05-07 | namedtuple, defaultdict, Counter, deque |
| Python official docs — contextlib | <https://docs.python.org/3/library/contextlib.html> | API truth for Days 27-28 | @contextmanager, closing, suppress |
| Python official docs — abc | <https://docs.python.org/3/library/abc.html> | API truth for Day 19 | ABC, @abstractmethod |
| Python official docs — threading | <https://docs.python.org/3/library/threading.html> | API truth for Days 35-36 | Thread, Lock, Event, Condition |
| Python official docs — multiprocessing | <https://docs.python.org/3/library/multiprocessing.html> | API truth for Day 37 | Process, Pool, Queue, Pipe |
| Python official docs — pdb | <https://docs.python.org/3/library/pdb.html> | API truth for Day 87 | Breakpoints, stepping, inspecting state |
| Python official docs — pathlib | <https://docs.python.org/3/library/pathlib.html> | API truth for Day 09 | Path, read_text, write_text, glob |
| Python official docs — csv | <https://docs.python.org/3/library/csv.html> | API truth for Day 09 | Reader, writer, DictReader |
| Python official docs — json | <https://docs.python.org/3/library/json.html> | API truth for Day 09 | load, dump, loads, dumps |
| Python official docs — re | <https://docs.python.org/3/library/re.html> | API truth for Day 08 | Pattern matching, substitution, search |
| Python official docs — dis | <https://docs.python.org/3/library/dis.html> | API truth for Day 55 | Bytecode disassembly, stack inspection |
| Python official docs — logging | <https://docs.python.org/3/library/logging.html> | API truth for Days 49, 88 | Loggers, handlers, formatters, levels |
| Python official docs — subprocess | <https://docs.python.org/3/library/subprocess.html> | API truth for Day 90 | run, Popen, capture_output, timeout |
| Python official docs — unittest | <https://docs.python.org/3/library/unittest.html> | Reference for Day 59 | TestCase, fixtures, assertions |

### Key PEP references

| PEP | URL | Best use in this repo |
|-----|-----|-----------------------|
| PEP 484 — Type Hints | <https://peps.python.org/pep-0484/> | Further reading for Days 01, 31-34 |
| PEP 498 — f-strings | <https://peps.python.org/pep-0498/> | Further reading for Day 01 |
| PEP 557 — Dataclasses | <https://peps.python.org/pep-0557/> | Further reading for Day 20 |
| PEP 572 — Assignment Expressions | <https://peps.python.org/pep-0572/> | Further reading for Day 02 |
| PEP 634 — Structural Pattern Matching | <https://peps.python.org/pep-0634/> | Further reading for Day 02 |
| PEP 3103 — match/case | <https://peps.python.org/pep-0636/> | Tutorial-style examples for Day 02 |
| PEP 570 — Positional-Only Parameters | <https://peps.python.org/pep-0570/> | Further reading for Day 03 |
| PEP 3102 — Keyword-Only Arguments | <https://peps.python.org/pep-3102/> | Further reading for Day 03 |
| PEP 318 — Decorators | <https://peps.python.org/pep-0318/> | Further reading for Days 25-26 |
| PEP 343 — The with Statement | <https://peps.python.org/pep-0343/> | Further reading for Days 27-28 |

### Exercise and problem-bank sources

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| zhiwehu — Python programming exercises | <https://github.com/zhiwehu/Python-programming-exercises> | `EXERCISE.md` must-pass/stretch inspiration for Python basics and intermediate practice | Great for breadth and variety. Rewrite prompts into repo-specific, typed, industrial-style tasks. |
| MTrajK — coding problems | <https://github.com/MTrajK/coding-problems> | DSA exercise sourcing, topic mapping, complexity-aware practice prompts | Best for DSA week practice and stretch tasks. Not a model for production application structure. |
| exercism — Python Track | <https://exercism.org/tracks/python> | Exercise ideas with mentoring-style feedback, good difficulty ladder | Use for exercise shape and test-driven exercise design patterns. |

### DSA platform sources

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| NeetCode — Roadmap | <https://neetcode.io/roadmap> | DSA topic ordering, problem selection, difficulty progression | Primary DSA planning source. Follow its topic ordering. |
| NeetCode — YouTube | <https://www.youtube.com/@NeetCode> | Video explanations for algorithm patterns | Use for concept ordering, not for code copying. |
| LeetCode | <https://leetcode.com/> | Practice problem URLs for `EXERCISE.md` Suggested Practice sections | Link specific problems, not solutions. |
| LeetCode — NeetCode 150 list | <https://neetcode.io/practice> | Curated problem set mapped to topics | Best for selecting the right practice problem per week. |
| Visualgo | <https://visualgo.net/en> | Algorithm visualization for DSA diagrams | Use for understanding algorithm flows to create ASCII/Mermaid diagrams. |
| Big-O Cheat Sheet | <https://www.bigocheatsheet.com/> | Complexity reference for `CODE.md` Concepts table | Link in Further reading for quick reference. |

### FastAPI and web framework sources

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| FastAPI — Official docs | <https://fastapi.tiangolo.com/> | API truth for all FastAPI days (71-86) | Primary reference. Follow its tutorial progression. |
| FastAPI — Tutorial | <https://fastapi.tiangolo.com/tutorial/> | Step-by-step teaching flow for CODE.md | Good for concept ordering: path params -> query params -> body -> dependencies. |
| Pydantic — Official docs | <https://docs.pydantic.dev/> | API truth for Days 72, 83 | Model validation, field config, serialization. |
| SQLAlchemy — Official docs | <https://docs.sqlalchemy.org/> | API truth for Day 78 | Async sessions, ORM models, queries. |
| Alembic — Official docs | <https://alembic.sqlalchemy.org/> | API truth for Day 78 | Migration generation and application. |
| Uvicorn | <https://www.uvicorn.org/> | ASGI server reference for deployment | Use for running FastAPI apps locally and in containers. |
| Starlette | <https://www.starlette.io/> | Underlying framework reference | Useful for understanding middleware, requests, responses. |

### DevOps and infrastructure sources

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| Docker — Official docs | <https://docs.docker.com/> | Container concepts for Days 82, 91 | Dockerfile, compose, image layers. |
| GitHub Actions — Official docs | <https://docs.github.com/actions> | CI/CD pipeline design for Day 92 | Workflows, jobs, matrix, secrets. |
| OpenTelemetry — Python SDK | <https://opentelemetry.io/docs/languages/python/> | Instrumentation concepts for Day 89 | Traces, spans, metrics, exporters. |
| Prometheus — Python client | <https://prometheus.io/docs/guides/python/> | Metrics exposition for Day 93 | Counters, histograms, labels, registry. |
| Boto3 — AWS SDK | <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html> | Cloud automation for Day 91 | S3, EC2, client patterns. |
| structlog | <https://www.structlog.org/> | Structured logging for Day 88 | Event logs, context binding, processors. |

### Python packaging and tooling sources

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| uv — Official docs | <https://docs.astral.sh/uv/> | Package management for Days 14, 66 | Dependency management, scripts, reproducible workflows. |
| ruff — Official docs | <https://docs.astral.sh/ruff/> | Linting and formatting for Days 14, 61 | Configuration, rules, autofix, pre-commit. |
| mypy — Official docs | <https://mypy.readthedocs.io/> | Type checking for Days 31-34 | Strict mode, configuration, common errors. |
| pytest — Official docs | <https://docs.pytest.org/> | Testing framework for Days 47, 59-60 | Fixtures, marks, parametrize, plugins. |
| coverage — Official docs | <https://coverage.readthedocs.io/> | Coverage measurement for Day 60 | Branch coverage, configuration, reporting. |
| bandit — Official docs | <https://bandit.readthedocs.io/> | Security scanning for Day 62 | Rule set, configuration, severity levels. |
| pyproject.toml spec | <https://packaging.python.org/en/latest/specifications/pyproject-toml/> | Packaging metadata for Days 14, 65 | Project metadata, build systems, tool config. |

### Video resources (T2)

| Source | URL | Best use in this repo | Coverage |
|--------|-----|-----------------------|----------|
| Corey Schafer — Python | <https://www.youtube.com/@coreyms> | Visual walkthroughs for Python basics through intermediate (OOP, generators, decorators, file I/O) | Days 01–30 |
| ArjanCodes | <https://www.youtube.com/@ArjanCodes> | Design patterns, typing, testing, software architecture in Python | Days 15–70 |
| mCoding (James Murphy) | <https://www.youtube.com/@mCoding> | Advanced Python internals, metaclasses, performance, bytecode | Days 51–70 |
| sentdex | <https://www.youtube.com/@sentdex> | Practical Python projects, data manipulation, web scraping | General reinforcement |
| Tech With Tim | <https://www.youtube.com/@TechWithTim> | FastAPI tutorials, project-based learning | Days 71–86 |
| NeetCode — YouTube | <https://www.youtube.com/@NeetCode> | Algorithm pattern explanations, step-by-step DSA walkthroughs | DSA Weeks 01–20 |
| Abdul Bari — Algorithms | <https://www.youtube.com/@abdul_bari> | Theory-heavy algorithm explanations (DP, graphs, sorting) | DSA Weeks 06–20 |
| William Fiset — Data Structures | <https://www.youtube.com/@WilliamFiset-videos> | Detailed data structure implementations (trees, graphs, union-find) | DSA Weeks 07–14, 18 |
| Back To Back SWE | <https://www.youtube.com/@BackToBackSWE> | Interview-style DSA explanations with visual diagrams | DSA Weeks 01–20 |
| Reducible | <https://www.youtube.com/@Reducible> | Animated algorithm visualizations (sorting, graphs, DP) | DSA Weeks 12–20 |

### Interactive tools and playgrounds (T3)

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| Python Tutor | <https://pythontutor.com/> | Step-by-step execution visualization for Python code | Excellent for understanding recursion, closures, and variable scoping |
| LeetCode Playground | <https://leetcode.com/playground/> | Quick DSA code testing without local setup | Use for verifying exercise solutions and edge cases |
| Replit | <https://replit.com/languages/python3> | Shareable Python environments for practice | Use for sandbox experimentation |
| Visualgo | <https://visualgo.net/en> | Algorithm and data structure animations | Primary visual reference for DSA diagrams and traversal understanding |
| Algorithm Visualizer | <https://algorithm-visualizer.org/> | Interactive step-through of sorting, searching, graph algorithms | Supplement for DSA Weeks 01–20 |
| Python Playground (W3Schools) | <https://www.w3schools.com/python/trypython.asp?filename=demo_default> | Quick Python syntax testing | For Days 01–14 basics verification |

### Cheat sheets and quick references (T3)

| Source | URL | Best use in this repo | Notes |
|--------|-----|-----------------------|-------|
| Big-O Cheat Sheet | <https://www.bigocheatsheet.com/> | Complexity reference for `CODE.md` concepts tables | Link in DSA Further reading sections |
| Python Cheat Sheet (gto76) | <https://github.com/gto76/python-cheatsheet> | Comprehensive Python syntax quick-ref | Quick lookup during generation |
| Python `collections` Quick-Ref | <https://docs.python.org/3/library/collections.html> | Counter, defaultdict, deque, namedtuple | Days 05–07, DSA Weeks 04–05 |
| Type Hints Cheat Sheet (mypy) | <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html> | Quick type annotation reference | Days 01, 31–34 |
| Sorting Algorithm Comparison | <https://www.toptal.com/developers/sorting-algorithms> | Visual sorting comparison with animations | DSA Week 20 |
| Python Built-in Functions | <https://docs.python.org/3/library/functions.html> | Quick lookup for map, filter, zip, sorted, etc. | Day 12 |
| FastAPI Cheat Sheet | <https://fastapi.tiangolo.com/tutorial/> | Quick API pattern reference | Days 71–86 |

### Book references (T1)

| Book | Author | Best use in this repo | Chapter mapping |
|------|--------|-----------------------|-----------------|
| Fluent Python (2nd ed.) | Luciano Ramalho | Deep Python understanding — data model, iterators, generators, decorators, metaclasses | Ch 1–4: Days 01–14, Ch 5–7: Days 15–21, Ch 14–17: Days 22–30, Ch 22–24: Days 51–55 |
| Grokking Algorithms | Aditya Bhargava | Visual algorithm explanations — ideal for DSA concept intros | Ch 1: Week 01, Ch 4: Week 06, Ch 6: Weeks 12–13, Ch 7: Week 18, Ch 9: Weeks 16–17 |
| Python Cookbook (3rd ed.) | David Beazley & Brian K. Jones | Production Python patterns and recipes | Recipes per topic: data structures, strings, iterators, concurrency |
| Introduction to Algorithms (CLRS) | Cormen et al. | Formal algorithm proofs and complexity analysis | Ch 1–4: Week 01, Ch 6–9: Week 20, Ch 15: Weeks 16–17, Ch 22–26: Weeks 12–14, 18 |
| Effective Python (2nd ed.) | Brett Slatkin | Pythonic patterns, best practices, industrial style | 90 items mapped across all Python phases |
| Architecture Patterns with Python | Harry Percival & Bob Gregory | Repository pattern, DI, event-driven design | Days 63–64, 79 |
| Python Testing with pytest | Brian Okken | Testing patterns and fixtures | Days 47, 59–60 |

---

## Per-day source mapping

Per-day sources now live **inline** in each day/week block of
`study_plan/<track>.md` (the **Sources:** line) — that is the single source of
truth for which URL to open for a given day. The sections above are the curated
catalog (tiers, official docs, PEPs, books, platforms) to draw from for anything extra.

---

## Artifact mapping

### For `CODE.md`

Use:

- Official docs for correctness
- Day-scoped tutorials for learning order
- Real Python for concise, practical examples
- PEPs for Further reading links
- `docs/DSA_VISUALS.md` for diagram/GIF formatting rules on DSA weeks

Recommended pattern:

1. Open the primary source URL from the day's `Sources:` line in `study_plan/<track>.md`.
2. Mirror the topic progression in your own words.
3. Add one small anti-pattern -> corrected pattern snippet.
4. Add one input-validation or explicit-error snippet.
5. End with Further reading that mixes official docs + one practical article from this registry.

### For `code.py`

Use:

- Official docs for exact behavior
- Real Python materials for code shape
- Repo conventions from `.agent.md` and `docs/RUBRIC.md`

Required bar:

- Type hints on public functions
- Clear validation and explicit exceptions
- Small reusable functions
- Docstrings where useful
- Examples that feel like backend, CLI, ETL, or service code rather than toy-only snippets

### For `EXERCISE.md`

Use:

- Exercise banks for idea harvesting
- Day tutorial sources for topic-appropriate difficulty
- DSA archives for complexity-aware practice links
- LeetCode/NeetCode URLs from the DSA per-week table above for Suggested Practice

Required transformation:

- Convert generic challenge text into repo-specific learning objectives
- Add must-pass, stretch, and failure modes
- Map each exercise to Skill IDs from `docs/RUBRIC.md`
- Add scoring and self-check sections
- Keep learner tasks distinct from `src/.../code.py`
- Include 1-2 Suggested Practice links from this registry

### For `ex01_basic.py` to `ex03_advanced.py`

Use source material only to shape the task. Do not lift solutions.

Required repo style:

- Starter stubs only unless explicitly solving
- Typed signatures
- Clear docstring with prompt, signature, examples, constraints
- `TODO` comments with sample input/output
- Inline `assert` checks in `if __name__ == "__main__":`

---

## Recommended source strategy by topic

| Topic type | Primary source | Secondary source | Exercise source |
|-----------|----------------|------------------|-----------------|
| Python basics | Official docs tutorial or Real Python | Asabeneh / CodeWithHarry | zhiwehu exercises |
| Python intermediate | Real Python article + Official docs | Exercism Python track | Exercism / zhiwehu |
| Concurrency / advanced Python | Official docs first | Real Python practical examples | Custom repo-tailored exercises |
| FastAPI / DevOps | Official docs first | Project repos and framework docs | Custom scenario-driven exercises |
| DSA | NeetCode roadmap + Official docs | MTrajK or similar archives | LeetCode (specific URLs above), NeetCode |

---

## Generation efficiency tips

These tips make each generation session faster and higher quality.

1. **Open the primary source first.** The day's `Sources:` line in `study_plan/<track>.md` tells you exactly which URL to open. Read its section headings and concept order before writing CODE.md.
2. **Mirror then elevate.** Follow the source's concept progression (the "what order to teach" part), but write your own examples in production style with type hints, validation, and docstrings.
3. **Use Further reading links from this registry.** Don't hunt for reference URLs — they are already listed here with one-line descriptions. Copy them into CODE.md.
4. **For EXERCISE.md Suggested Practice, use the LeetCode/NeetCode URLs from the DSA table.** They are pre-mapped to each week.
5. **One source per artifact type.** Use the teaching-flow source for CODE.md ordering, the production source for code.py style, and the exercise bank for EXERCISE.md ideas. Don't try to use one source for everything.
6. **Validate gates as you generate.** Before writing code.py, check: type hints? explicit errors? docstrings? This is faster than fixing after generation.
7. **Batch self-checks.** After generating all 5 files, run `ruff check` and all 3 exercise scripts in one go. Fix everything before moving to the next day.

---

## Reuse checklist for future generation

Before generating a new day or week, confirm:

- The source is recorded here or intentionally chosen.
- The source role is clear: progression, production style, or exercise bank.
- You opened the primary source URL from the day's `Sources:` line in `study_plan/<track>.md` before writing.
- `CODE.md` follows the source order without copying.
- `code.py` meets gates G1–G8 in `.agent.md §2`.
- `EXERCISE.md` and `ex01` to `ex03` are original repo-shaped tasks, not copied challenge text.
- `EXERCISE.md` Suggested Practice links come from this registry's LeetCode/NeetCode table.

If a source is helpful but missing, add it here first.

