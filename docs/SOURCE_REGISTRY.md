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
- **Always consult the per-day source table below** before generating. It maps each day to its best primary + secondary source URL so you can open the right reference immediately.

---

## Source buckets

| Bucket | Best use | Avoid using it for |
|--------|----------|--------------------|
| Tutorial progression | `CODE.md` learning order and beginner examples | Copy-pasting long prose |
| Production examples | `code.py` reference implementations and style cues | Full exercise specs without adaptation |
| Exercise bank | `EXERCISE.md` must-pass/stretch ideas | Direct solution copying |
| DSA problem archive | DSA practice links, stretch prompts, complexity framing | Production Python API design |

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

---

## Per-day source mapping (quick lookup for generation)

Use this table to immediately find the right source URL for each day. Open the primary source before generating.

### Phase 1 — Python Basics

| Day | Topic | Primary source URL | Secondary source URL | Exercise bank URL |
|-----|-------|--------------------|----------------------|-------------------|
| 01 | Syntax, types, variables | <https://docs.python.org/3/tutorial/introduction.html> | <https://realpython.com/python-variables/> | <https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt> |
| 02 | Control flow | <https://docs.python.org/3/tutorial/controlflow.html> | <https://peps.python.org/pep-0636/> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 03 | Functions | <https://realpython.com/defining-your-own-python-function/> | <https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 04 | Lists and sorting | <https://realpython.com/python-lists-tuples/> | <https://docs.python.org/3/tutorial/datastructures.html> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 05 | Tuples and NamedTuple | <https://realpython.com/python-lists-tuples/> | <https://docs.python.org/3/library/collections.html#collections.namedtuple> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 06 | Dictionaries | <https://realpython.com/python-dicts/> | <https://docs.python.org/3/tutorial/datastructures.html#dictionaries> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 07 | Sets and frozenset | <https://realpython.com/python-sets/> | <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset> | <https://github.com/Asabeneh/30-Days-Of-Python/blob/master/07_Day_Sets/07_sets.md> |
| 08 | Strings and encoding | <https://realpython.com/python-strings/> | <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 09 | File I/O and structured files | <https://realpython.com/read-write-files-python/> | <https://docs.python.org/3/library/pathlib.html> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 10 | Exceptions and custom errors | <https://realpython.com/python-exceptions/> | <https://docs.python.org/3/tutorial/errors.html> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 11 | Modules and packages | <https://realpython.com/python-modules-packages/> | <https://docs.python.org/3/tutorial/modules.html> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 12 | Built-ins in data pipelines | <https://docs.python.org/3/library/functions.html> | <https://realpython.com/python-map-filter-reduce/> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 13 | Comprehensions and generator preview | <https://realpython.com/list-comprehension-python/> | <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions> | <https://github.com/zhiwehu/Python-programming-exercises> |
| 14 | Tooling and environments | <https://docs.astral.sh/uv/> | <https://packaging.python.org/en/latest/specifications/pyproject-toml/> | — |

### Phase 2 — Python Intermediate

| Day | Topic | Primary source URL | Secondary source URL | Exercise bank URL |
|-----|-------|--------------------|----------------------|-------------------|
| 15 | Classes and object state | <https://realpython.com/python3-object-oriented-programming/> | <https://docs.python.org/3/tutorial/classes.html> | <https://exercism.org/tracks/python> |
| 16 | Value-object dunders | <https://docs.python.org/3/reference/datamodel.html> | <https://realpython.com/python3-object-oriented-programming/> | <https://exercism.org/tracks/python> |
| 17 | Properties and invariants | <https://realpython.com/python-property/> | <https://docs.python.org/3/library/functions.html#property> | <https://exercism.org/tracks/python> |
| 18 | Inheritance and MRO | <https://realpython.com/python3-object-oriented-programming/> | <https://docs.python.org/3/tutorial/classes.html#inheritance> | <https://exercism.org/tracks/python> |
| 19 | Abstract base classes | <https://docs.python.org/3/library/abc.html> | <https://realpython.com/python3-object-oriented-programming/> | <https://exercism.org/tracks/python> |
| 20 | Dataclasses | <https://realpython.com/python-data-classes/> | <https://docs.python.org/3/library/dataclasses.html> | <https://exercism.org/tracks/python> |
| 21 | Class and static methods | <https://realpython.com/instance-class-and-static-methods-demystified/> | <https://docs.python.org/3/library/functions.html#classmethod> | <https://exercism.org/tracks/python> |
| 22 | Iterators | <https://realpython.com/python-iterators-iterables-iteration/> | <https://docs.python.org/3/library/stdtypes.html#iterator-types> | <https://exercism.org/tracks/python> |
| 23 | Generators and lazy pipelines | <https://realpython.com/introduction-to-python-generators/> | <https://docs.python.org/3/tutorial/classes.html#generators> | <https://exercism.org/tracks/python> |
| 24 | Generator expressions | <https://realpython.com/introduction-to-python-generators/> | <https://docs.python.org/3/howto/functional.html> | <https://exercism.org/tracks/python> |
| 25 | Decorators | <https://realpython.com/primer-on-python-decorators/> | <https://peps.python.org/pep-0318/> | <https://exercism.org/tracks/python> |
| 26 | Parametric decorators | <https://realpython.com/primer-on-python-decorators/> | <https://docs.python.org/3/library/functools.html> | <https://exercism.org/tracks/python> |
| 27 | Context managers | <https://realpython.com/python-with-statement/> | <https://docs.python.org/3/library/contextlib.html> | <https://exercism.org/tracks/python> |
| 28 | @contextmanager | <https://realpython.com/python-with-statement/> | <https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager> | <https://exercism.org/tracks/python> |
| 29 | functools | <https://realpython.com/python-functools/> | <https://docs.python.org/3/library/functools.html> | <https://exercism.org/tracks/python> |
| 30 | itertools | <https://realpython.com/python-itertools/> | <https://docs.python.org/3/library/itertools.html> | <https://exercism.org/tracks/python> |
| 31 | Typing basics | <https://realpython.com/python-type-checking/> | <https://docs.python.org/3/library/typing.html> | <https://exercism.org/tracks/python> |
| 32 | Advanced typing helpers | <https://realpython.com/python-type-checking/> | <https://docs.python.org/3/library/typing.html> | <https://exercism.org/tracks/python> |
| 33 | Generics and TypeVar | <https://realpython.com/python-type-checking/> | <https://docs.python.org/3/library/typing.html#generics> | <https://exercism.org/tracks/python> |
| 34 | mypy and strictness | <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html> | <https://docs.python.org/3/library/typing.html> | <https://exercism.org/tracks/python> |

### Phase 3 — Python Concurrency

| Day | Topic | Primary source URL | Secondary source URL | Exercise bank URL |
|-----|-------|--------------------|----------------------|-------------------|
| 35 | Threading and locks | <https://realpython.com/intro-to-python-threading/> | <https://docs.python.org/3/library/threading.html> | — |
| 36 | GIL and workload selection | <https://realpython.com/intro-to-python-threading/> | <https://docs.python.org/3/glossary.html#term-global-interpreter-lock> | — |
| 37 | Multiprocessing | <https://realpython.com/python-multiprocessing/> | <https://docs.python.org/3/library/multiprocessing.html> | — |
| 38 | concurrent.futures | <https://docs.python.org/3/library/concurrent.futures.html> | <https://realpython.com/intro-to-python-threading/> | — |
| 39 | asyncio basics | <https://realpython.com/async-io-python/> | <https://docs.python.org/3/library/asyncio.html> | — |
| 40 | aiohttp | <https://docs.aiohttp.org/en/stable/> | <https://realpython.com/async-io-python/> | — |
| 41 | Async error handling | <https://realpython.com/async-io-python/> | <https://docs.python.org/3/library/asyncio-task.html> | — |
| 42 | Sync/async bridge | <https://docs.python.org/3/library/asyncio-eventloop.html> | <https://realpython.com/async-io-python/> | — |
| 43 | Concurrency design boundaries | <https://realpython.com/async-io-python/> | <https://docs.python.org/3/library/asyncio.html> | — |
| 44 | Refactor day | (own earlier modules) | — | — |
| 45 | Concurrency milestone | (own earlier modules) | — | — |
| 46 | Packaging concurrent code | <https://packaging.python.org/en/latest/specifications/pyproject-toml/> | <https://docs.astral.sh/uv/> | — |
| 47 | Testing concurrent code | <https://realpython.com/pytest-python-testing/> | <https://docs.pytest.org/> | — |
| 48 | Mocking I/O | <https://docs.pytest.org/en/stable/how-to/monkeypatch.html> | <https://realpython.com/pytest-python-testing/> | — |
| 49 | Logging in concurrent systems | <https://realpython.com/python-logging/> | <https://docs.python.org/3/library/logging.html> | — |
| 50 | Phase review | (own earlier modules) | — | — |

### Phase 4 — Python Advanced

| Day | Topic | Primary source URL | Secondary source URL | Exercise bank URL |
|-----|-------|--------------------|----------------------|-------------------|
| 51 | Descriptors | <https://realpython.com/python-descriptors/> | <https://docs.python.org/3/reference/datamodel.html#descriptors> | — |
| 52 | __slots__ | <https://docs.python.org/3/reference/datamodel.html#slots> | <https://realpython.com/python-data-classes/> | — |
| 53 | Metaclasses | <https://realpython.com/python-metaclasses/> | <https://docs.python.org/3/reference/datamodel.html#metaclasses> | — |
| 54 | __init_subclass__ | <https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__> | <https://peps.python.org/pep-0487/> | — |
| 55 | Bytecode and dis | <https://docs.python.org/3/library/dis.html> | <https://docs.python.org/3/reference/datamodel.html> | — |
| 56 | Import system | <https://docs.python.org/3/library/importlib.html> | <https://realpython.com/python-modules-packages/> | — |
| 57 | cProfile | <https://docs.python.org/3/library/profile.html> | <https://realpython.com/python-profiling/> | — |
| 58 | timeit and measurement | <https://docs.python.org/3/library/timeit.html> | <https://realpython.com/python-profiling/> | — |
| 59 | pytest fixtures | <https://realpython.com/pytest-python-testing/> | <https://docs.pytest.org/> | — |
| 60 | Coverage | <https://coverage.readthedocs.io/> | <https://docs.pytest.org/> | — |
| 61 | Ruff and pre-commit | <https://docs.astral.sh/ruff/> | <https://pre-commit.com/> | — |
| 62 | Security scanning with Bandit | <https://bandit.readthedocs.io/> | <https://docs.python.org/3/library/subprocess.html> | — |
| 63 | Strategy and Factory | <https://realpython.com/factory-method-python/> | <https://docs.python.org/3/library/abc.html> | — |
| 64 | Repository and DI | <https://realpython.com/python-dependency-injection/> | <https://fastapi.tiangolo.com/tutorial/dependencies/> | — |
| 65 | Packaging a library | <https://packaging.python.org/en/latest/tutorials/packaging-projects/> | <https://docs.astral.sh/uv/> | — |
| 66 | uv workflow | <https://docs.astral.sh/uv/> | <https://packaging.python.org/en/latest/specifications/pyproject-toml/> | — |
| 67 | Library CI milestone | <https://docs.github.com/actions> | <https://docs.astral.sh/ruff/> | — |
| 68 | Metaprogramming review | (own Day 51-54 modules) | — | — |
| 69 | Testing strategy review | (own Day 47, 59-60 modules) | — | — |
| 70 | Retrospective and polish | (own all modules) | — | — |

### Phase 5 — FastAPI Track

| Day | Topic | Primary source URL | Secondary source URL | Exercise bank URL |
|-----|-------|--------------------|----------------------|-------------------|
| 71 | FastAPI app basics | <https://fastapi.tiangolo.com/tutorial/first-steps/> | <https://fastapi.tiangolo.com/tutorial/path-params/> | — |
| 72 | Pydantic v2 models | <https://docs.pydantic.dev/latest/concepts/models/> | <https://fastapi.tiangolo.com/tutorial/body/> | — |
| 73 | Dependencies | <https://fastapi.tiangolo.com/tutorial/dependencies/> | <https://fastapi.tiangolo.com/tutorial/dependency-injection-in-fastapi/> | — |
| 74 | Error handling | <https://fastapi.tiangolo.com/tutorial/handling-errors/> | <https://docs.pydantic.dev/latest/concepts/models/#model-validation> | — |
| 75 | OAuth2 and JWT | <https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/> | <https://fastapi.tiangolo.com/tutorial/security/> | — |
| 76 | Middleware and CORS | <https://fastapi.tiangolo.com/tutorial/cors/> | <https://fastapi.tiangolo.com/advanced/middleware/> | — |
| 77 | Background tasks | <https://fastapi.tiangolo.com/tutorial/background-tasks/> | <https://docs.python.org/3/library/asyncio-task.html> | — |
| 78 | SQLAlchemy async and Alembic | <https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html> | <https://alembic.sqlalchemy.org/en/latest/tutorial.html> | — |
| 79 | Repository in API services | <https://fastapi.tiangolo.com/tutorial/dependencies/> | <https://docs.sqlalchemy.org/en/20/orm/queryguide/> | — |
| 80 | API testing | <https://fastapi.tiangolo.com/tutorial/testing/> | <https://docs.pytest.org/> | — |
| 81 | WebSockets | <https://fastapi.tiangolo.com/advanced/websockets/> | <https://www.starlette.io/websockets/> | — |
| 82 | Docker for FastAPI | <https://fastapi.tiangolo.com/deployment/docker/> | <https://docs.docker.com/> | — |
| 83 | Settings management | <https://docs.pydantic.dev/latest/concepts/pydantic_settings/> | <https://fastapi.tiangolo.com/advanced/settings/> | — |
| 84 | FastAPI milestone | (own Day 71-83 modules) | — | — |
| 85 | Health and readiness | <https://fastapi.tiangolo.com/advanced/advanced-user-guide/> | <https://docs.docker.com/compose/> | — |
| 86 | API review checklist | (own Day 71-85 modules) | <https://fastapi.tiangolo.com/tutorial/> | — |

### Phase 6 — DevOps and Capstone

| Day | Topic | Primary source URL | Secondary source URL | Exercise bank URL |
|-----|-------|--------------------|----------------------|-------------------|
| 87 | Debugging with pdb | <https://docs.python.org/3/library/pdb.html> | <https://realpython.com/python-debugging-pdb/> | — |
| 88 | Structured logging | <https://www.structlog.org/> | <https://realpython.com/python-logging/> | — |
| 89 | OpenTelemetry | <https://opentelemetry.io/docs/languages/python/> | <https://opentelemetry.io/docs/concepts/signals/traces/> | — |
| 90 | Safe subprocess | <https://realpython.com/python-subprocess/> | <https://docs.python.org/3/library/subprocess.html> | — |
| 91 | Cloud or container SDK | <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html> | <https://docs.docker.com/engine/api/> | — |
| 92 | GitHub Actions | <https://docs.github.com/actions> | <https://docs.github.com/actions/quickstart> | — |
| 93 | Prometheus metrics | <https://prometheus.io/docs/guides/python/> | <https://prometheus.io/docs/concepts/data-model/> | — |
| 94 | Capstone deploy slice | (own Day 87-93 modules) | <https://docs.docker.com/> | — |
| 95 | Runbooks | <https://docs.github.com/actions> | (own capstone module) | — |
| 96 | Timed DSA practice | <https://neetcode.io/practice> | <https://leetcode.com/> | — |
| 97 | Explain-aloud DSA | <https://neetcode.io/roadmap> | (own DSA modules) | — |
| 98 | Portfolio README | (own repo) | — | — |
| 99 | Repo review and sync | (own repo) | — | — |
| 100 | Next 30 days roadmap | <https://neetcode.io/roadmap> | <https://realpython.com/> | — |

### Parallel DSA — LeetCode problem URLs per week

| Week | Topic | LeetCode practice problems | NeetCode section |
|------|-------|---------------------------|-------------------|
| 01 | Big-O, arrays, hashing | [Two Sum](https://leetcode.com/problems/two-sum/) · [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | <https://neetcode.io/roadmap> Arrays & Hashing |
| 02 | Arrays and hashing II | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) · [Top K Frequent](https://leetcode.com/problems/top-k-frequent-elements/) · [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | <https://neetcode.io/roadmap> Arrays & Hashing |
| 03 | Two pointers | [3Sum](https://leetcode.com/problems/3sum/) · [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | <https://neetcode.io/roadmap> Two Pointers |
| 04 | Sliding window | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) · [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | <https://neetcode.io/roadmap> Sliding Window |
| 05 | Stack | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | <https://neetcode.io/roadmap> Stack |
| 06 | Binary search | [Binary Search](https://leetcode.com/problems/binary-search/) · [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | <https://neetcode.io/roadmap> Binary Search |
| 07 | Linked list | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) · [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | <https://neetcode.io/roadmap> Linked List |
| 08 | Binary trees I | [Maximum Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · [Same Tree](https://leetcode.com/problems/same-tree/) | <https://neetcode.io/roadmap> Trees |
| 09 | BST | [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) · [Kth Smallest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | <https://neetcode.io/roadmap> Trees |
| 10 | Heap and priority queue | [Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | <https://neetcode.io/roadmap> Heap / Priority Queue |
| 11 | Backtracking | [Subsets](https://leetcode.com/problems/subsets/) · [Combination Sum](https://leetcode.com/problems/combination-sum/) | <https://neetcode.io/roadmap> Backtracking |
| 12 | Graphs I | [Number of Islands](https://leetcode.com/problems/number-of-islands/) · [Clone Graph](https://leetcode.com/problems/clone-graph/) | <https://neetcode.io/roadmap> Graphs |
| 13 | Graphs II and topo sort | [Course Schedule](https://leetcode.com/problems/course-schedule/) · [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | <https://neetcode.io/roadmap> Graphs |
| 14 | Union-Find | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) · [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | <https://neetcode.io/roadmap> Graphs |
| 15 | Greedy | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) · [Jump Game](https://leetcode.com/problems/jump-game/) | <https://neetcode.io/roadmap> Greedy |
| 16 | 1D DP | [Coin Change](https://leetcode.com/problems/coin-change/) · [House Robber](https://leetcode.com/problems/house-robber/) | <https://neetcode.io/roadmap> Dynamic Programming |
| 17 | 2D DP | [Unique Paths](https://leetcode.com/problems/unique-paths/) · [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | <https://neetcode.io/roadmap> Dynamic Programming |
| 18 | Shortest paths | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) · [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | <https://neetcode.io/roadmap> Graphs |
| 19 | Tries and bit tricks | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) · [Single Number](https://leetcode.com/problems/single-number/) | <https://neetcode.io/roadmap> 1-D DP / Intervals |
| 20 | Mixed review | <https://neetcode.io/practice> (weak-area revisit) | <https://neetcode.io/roadmap> |

---

## Artifact mapping

### For `CODE.md`

Use:

- Official docs for correctness
- Day-scoped tutorials for learning order
- Real Python for concise, practical examples
- PEPs for Further reading links

Recommended pattern:

1. Open the primary source URL from the per-day mapping table above.
2. Mirror the topic progression in your own words.
3. Add one small anti-pattern -> corrected pattern snippet.
4. Add one input-validation or explicit-error snippet.
5. End with Further reading that mixes official docs + one practical article from this registry.

### For `code.py`

Use:

- Official docs for exact behavior
- Real Python materials for code shape
- Repo conventions from `docs/CODE_TEMPLATE.md` and `docs/EVALUATION_RUBRIC.md`

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
- Map each exercise to Skill IDs from `docs/EVALUATION_RUBRIC.md`
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

1. **Open the primary source first.** The per-day table tells you exactly which URL to open. Read its section headings and concept order before writing CODE.md.
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
- You opened the primary source URL from the per-day table before writing.
- `CODE.md` follows the source order without copying.
- `code.py` meets the industrial checklist in `docs/EVALUATION_RUBRIC.md`.
- `EXERCISE.md` and `ex01` to `ex03` are original repo-shaped tasks, not copied challenge text.
- `EXERCISE.md` Suggested Practice links come from this registry's LeetCode/NeetCode table.

If a source is helpful but missing, add it here first.