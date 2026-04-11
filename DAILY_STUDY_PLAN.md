# Daily Python + DSA Study Plan

> **Role:** Professional backend Python + DSA tutor track with code-first teaching, industrial-style reference code, and graded exercises.  
> **Companions:** [README.md](./README.md) · [.agent.md](./.agent.md) · [docs/CODE_TEMPLATE.md](./docs/CODE_TEMPLATE.md) · [docs/EVALUATION_RUBRIC.md](./docs/EVALUATION_RUBRIC.md) · [docs/AI_EVAL_FRAMEWORK.md](./docs/AI_EVAL_FRAMEWORK.md) · [docs/SOURCE_REGISTRY.md](./docs/SOURCE_REGISTRY.md)

---

## Purpose

This file is the curriculum map for the repo.

- Every Python day produces:
  - `src/<track>/day_NN_topic/CODE.md`
  - `src/<track>/day_NN_topic/code.py`
  - `exercise/<track>/day_NN_topic/EXERCISE.md`
  - `exercise/<track>/day_NN_topic/ex01_basic.py`
  - `exercise/<track>/day_NN_topic/ex02_intermediate.py`
  - `exercise/<track>/day_NN_topic/ex03_advanced.py`
- Every DSA week produces the matching `src/dsa/...` and `exercise/dsa/...` module pair.
- `CODE.md` teaches the topic, `code.py` shows production-style examples, and `exercise/` holds learner tasks and evaluation.

---

## Canonical Repository Layout

```text
src/
  python_basic/
  python_intermediate/
  python_concurrency/
  python_advanced/
  fastapi_track/
  devops_track/
  dsa/

exercise/
  python_basic/
  python_intermediate/
  python_concurrency/
  python_advanced/
  fastapi_track/
  devops_track/
  dsa/
```

| Area | Pattern | Example |
|------|---------|---------|
| Python study module | `src/<track>/day_NN_topic/` | `src/python_basic/day_07_sets/` |
| Python exercise module | `exercise/<track>/day_NN_topic/` | `exercise/python_basic/day_07_sets/` |
| DSA study module | `src/dsa/week_WW_topic/` | `src/dsa/week_03_two_pointers/` |
| DSA exercise module | `exercise/dsa/week_WW_topic/` | `exercise/dsa/week_03_two_pointers/` |

---

## Delivery Standard Per Day

| Artifact | Purpose |
|----------|---------|
| `CODE.md` | Concise concept map with source-aligned learning flow and short snippets |
| `code.py` | Production-style reference implementations with type hints and docstrings |
| `EXERCISE.md` | Learning objectives, skills, must-pass, stretch, failure modes, scoring |
| `ex01_basic.py` | Foundational exercise |
| `ex02_intermediate.py` | Applied exercise |
| `ex03_advanced.py` | Harder design or edge-case exercise |

---

## Daily Generation Workflow

1. Use this file to choose the day, topic, slug, subtopics, and exercise direction.
2. Use [docs/SOURCE_REGISTRY.md](./docs/SOURCE_REGISTRY.md) to choose teaching-flow sources, production references, and exercise banks.
3. Generate the 5-file day module using [docs/PROMPT_TEMPLATES.md](./docs/PROMPT_TEMPLATES.md).
4. Keep output aligned with [docs/CODE_TEMPLATE.md](./docs/CODE_TEMPLATE.md) and [docs/EVALUATION_RUBRIC.md](./docs/EVALUATION_RUBRIC.md).

---

## Time Budget

| Block | Time | Notes |
|------|------|-------|
| Python study day | 60–90 min | Generate, read, code, and self-check one day |
| DSA parallel | 45–90 min | Study one DSA week topic in parallel with Python |
| Sunday lab | 90–120 min | Integrative build using the latest 5 study days |
| Quality pass | 15 min | Run inline asserts and `ruff check` |

---

## Phase Overview

| Phase | Days | Track | Outcome |
|------|------|-------|---------|
| Phase 1 | 01–14 | `python_basic` | Syntax, built-ins, data structures, I/O, and tooling foundation |
| Phase 2 | 15–34 | `python_intermediate` | OOP, iterators, decorators, context managers, typing |
| Phase 3 | 35–50 | `python_concurrency` | Threads, processes, async I/O, testing concurrent code |
| Phase 4 | 51–70 | `python_advanced` | Internals, profiling, testing depth, patterns, packaging |
| Phase 5 | 71–86 | `fastapi_track` | API design, auth, DB integration, testing, deployment basics |
| Phase 6 | 87–100 | `devops_track` | Observability, automation, CI/CD, capstone, review |
| Parallel track | Weeks 01–20 | `dsa` | Interview-grade DSA progression with repo-native implementations |

---

## High-Value References

| Phase | Main references |
|------|------------------|
| Python basics | [Python Tutorial](https://docs.python.org/3/tutorial/) · [Real Python](https://realpython.com/) |
| Python intermediate | [typing docs](https://docs.python.org/3/library/typing.html) · [functools docs](https://docs.python.org/3/library/functools.html) |
| Concurrency | [asyncio docs](https://docs.python.org/3/library/asyncio.html) · [concurrent.futures docs](https://docs.python.org/3/library/concurrent.futures.html) |
| Advanced Python | [Python data model](https://docs.python.org/3/reference/datamodel.html) · [dis docs](https://docs.python.org/3/library/dis.html) |
| FastAPI | [FastAPI docs](https://fastapi.tiangolo.com/) · [Pydantic docs](https://docs.pydantic.dev/) |
| DevOps | [GitHub Actions docs](https://docs.github.com/actions) · [Docker docs](https://docs.docker.com/) |
| DSA | [NeetCode roadmap](https://neetcode.io/roadmap) · [LeetCode](https://leetcode.com/) |

---

## Phase 1 — Python Basics

**Track folders:** `src/python_basic/` and `exercise/python_basic/`

| Day | Topic | Slug | `CODE.md` and `code.py` subtopics | Exercise direction | Primary source |
|-----|-------|------|-----------------------------------|--------------------|----------------|
| 01 | Syntax, types, variables | `day_01_syntax_variables` | naming, literals, type hints, constants, f-strings, input cleanup, explicit validation | CLI-style parsing, username formatting, retry count parsing, runtime banner building | [Python Tutorial — Introduction](https://docs.python.org/3/tutorial/introduction.html) |
| 02 | Control flow | `day_02_control_flow` | `if`/`elif`/`else`, truthiness, loops, `break`, `continue`, `match`, guard clauses, loop-based pattern printing basics | order-status state machine, shipping rules, menu routing, beginner pattern-printing loops | [Python Tutorial — Control Flow](https://docs.python.org/3/tutorial/controlflow.html) |
| 03 | Functions | `day_03_functions` | `def`, return values, defaults, keyword args, `*args`, `**kwargs`, unpacking, short `lambda` usage | pluggable validators, function signatures, flexible event formatting | [Real Python — Defining Functions](https://realpython.com/defining-your-own-python-function/) |
| 04 | Lists and sorting | `day_04_lists` | indexing, slicing, mutation, list methods, sorting keys, stable sort, top-k patterns | leaderboard ranking, tie-breakers, filtered result views | [Real Python — Lists and Tuples](https://realpython.com/python-lists-tuples/) |
| 05 | Tuples and `NamedTuple` | `day_05_tuples` | tuple immutability, packing/unpacking, multiple returns, `NamedTuple`, DTO-style records | CSV row DTOs, coordinate parsing, report rows | [Real Python — Lists and Tuples](https://realpython.com/python-lists-tuples/) |
| 06 | Dictionaries | `day_06_dictionaries` | CRUD, `get`, `setdefault`, iteration, dict comprehension, nested dict safety | inverted index, config merge, word-count registry | [Real Python — Dictionaries](https://realpython.com/python-dicts/) |
| 07 | Sets and `frozenset` | `day_07_sets` | uniqueness, membership, add/remove/update, union, intersection, difference, subset/superset, `frozenset` | dedupe logs, allowlist/denylist, tag matching, permission comparison | [Real Python — Sets](https://realpython.com/python-sets/) |
| 08 | Strings and encoding | `day_08_strings` | slicing, methods, normalization, raw strings, bytes vs str, encoding basics, formatting, substring checks, subsequence checks, character-frequency ops, consecutive-string/run-length ops | slugify, sanitizer, text normalizer, URL-safe labels, substring/subsequence utilities, consecutive-string helpers | [Real Python — Strings](https://realpython.com/python-strings/) |
| 09 | File I/O and structured files | `day_09_file_io` | `open`, context managers, `pathlib`, CSV, JSON, newline handling, safe file paths | CSV validate to JSONL ETL, file summary, import/export stubs | [Real Python — File I/O](https://realpython.com/read-write-files-python/) |
| 10 | Exceptions and custom errors | `day_10_exceptions` | `try`/`except`/`else`/`finally`, raise, custom exception classes, chaining, failure contracts | retry wrapper, domain validation errors, transaction-like flows | [Real Python — Exceptions](https://realpython.com/python-exceptions/) |
| 11 | Modules and packages | `day_11_modules` | imports, package layout, `__name__`, `__main__`, relative imports, module boundaries | package split, runnable module, helper module reuse | [Real Python — Modules and Packages](https://realpython.com/python-modules-packages/) |
| 12 | Built-ins in data pipelines | `day_12_builtins` | `enumerate`, `zip`, `sorted`, `map`, `filter`, `any`, `all`, readability tradeoffs | parse-map-filter-aggregate mini pipeline | [Python Docs — Built-in Functions](https://docs.python.org/3/library/functions.html) |
| 13 | Comprehensions and generator preview | `day_13_comprehensions` | list, dict, set comprehensions, nested filters, generator expressions, readability limits | last-N lines generator, filtered projections, index structures | [Real Python — Comprehensions](https://realpython.com/list-comprehension-python/) |
| 14 | Tooling and environments | `day_14_tooling` | `venv`, `uv`, `requirements`, `pyproject`, script entrypoints, reproducible setup | environment bootstrap, install README, local task runner | [uv Docs](https://docs.astral.sh/uv/) |

---

## Phase 2 — Python Intermediate

**Track folders:** `src/python_intermediate/` and `exercise/python_intermediate/`

| Day | Topic | Slug | `CODE.md` and `code.py` subtopics | Exercise direction | Primary source |
|-----|-------|------|-----------------------------------|--------------------|----------------|
| 15 | Classes and object state | `day_15_classes` | `__init__`, instance state, class attributes, methods, validation in constructors | inventory item model, user account state, config object | [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) |
| 16 | Value-object dunders | `day_16_dunder_value_objects` | `__repr__`, `__str__`, `__eq__`, `__lt__`, `__hash__`, identity vs equality | value-object comparisons, dedupe in sets, sorted domain entities | [Python Data Model](https://docs.python.org/3/reference/datamodel.html) |
| 17 | Properties and invariants | `day_17_properties` | `@property`, setters, computed fields, validation gates, encapsulation | bounded score object, email/user profile validator, money amount guard | [Real Python — Properties](https://realpython.com/python-property/) |
| 18 | Inheritance and MRO | `day_18_inheritance` | `super()`, shared behavior, override patterns, MRO basics, composition vs inheritance | payment providers, transport hierarchy, notification channels | [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) |
| 19 | Abstract base classes | `day_19_abstract_base` | `ABC`, `@abstractmethod`, interface contracts, plugin-style design | storage backend interface, parser strategy family | [Python abc docs](https://docs.python.org/3/library/abc.html) |
| 20 | Dataclasses | `day_20_dataclasses` | `@dataclass`, `field`, defaults, `frozen`, `slots`, `__post_init__` | event records, immutable DTOs, config containers | [Real Python — Dataclasses](https://realpython.com/python-data-classes/) |
| 21 | Class and static methods | `day_21_class_static` | alternative constructors, utility methods, factory patterns, parsing helpers | parse-from-string constructors, registry helpers, formatter utilities | [Real Python — Class/Static Methods](https://realpython.com/instance-class-and-static-methods-demystified/) |
| 22 | Iterators | `day_22_iterators` | iterable protocol, `iter`, `next`, `StopIteration`, custom iterator classes | paginated iterator, row streamer, bounded sequence walker | [Real Python — Iterators](https://realpython.com/python-iterators-iterables-iteration/) |
| 23 | Generators and lazy pipelines | `day_23_generators` | `yield`, generator functions, lazy pipelines, backpressure mindset, `yield from` | ETL stream, lazy log parser, record batching | [Real Python — Generators](https://realpython.com/introduction-to-python-generators/) |
| 24 | Generator expressions | `day_24_generator_expressions` | streaming transforms, memory savings, `sum`/`any`/`all`, readable one-pass code | rolling metrics, filtered scan, lazy report statistics | [Real Python — Generators](https://realpython.com/introduction-to-python-generators/) |
| 25 | Decorators | `day_25_decorators` | wrappers, `functools.wraps`, logging/timing decorators, pure-function decoration | call logger, latency tracker, validation decorator | [Real Python — Decorators](https://realpython.com/primer-on-python-decorators/) |
| 26 | Parametric decorators | `day_26_decorators_advanced` | decorator factories, retries, rate limits, feature flags, configurable wrappers | retry decorator, permission gate, audit tags | [Real Python — Decorators](https://realpython.com/primer-on-python-decorators/) |
| 27 | Context managers | `day_27_context_managers` | `__enter__`, `__exit__`, resource cleanup, transactional thinking | temp file guard, lock wrapper, reversible state change | [Real Python — Context Managers](https://realpython.com/python-with-statement/) |
| 28 | `@contextmanager` | `day_28_contextmanager` | generator-based context managers, setup/teardown flow, exception handling | temporary config override, fake connection scope | [Python contextlib docs](https://docs.python.org/3/library/contextlib.html) |
| 29 | `functools` | `day_29_functools` | `partial`, `lru_cache`, `cache`, `reduce`, `singledispatch`, practical tradeoffs | cached parser, specialized callbacks, command dispatch | [Real Python — functools](https://realpython.com/python-functools/) |
| 30 | `itertools` | `day_30_itertools` | `chain`, `islice`, `groupby`, `product`, `combinations`, lazy composition | cartesian test data, chunking, grouped report builder | [Real Python — itertools](https://realpython.com/python-itertools/) |
| 31 | Typing basics | `day_31_typing_basics` | `Optional`, `Union`, aliases, honest signatures, collection types | typed config parsing, API response modeling | [Real Python — Type Checking](https://realpython.com/python-type-checking/) |
| 32 | Advanced typing helpers | `day_32_typing_advanced` | `TypedDict`, `Literal`, `Final`, `ClassVar`, narrow domain modeling | feature-flag settings, payload schemas, fixed status values | [Python typing docs](https://docs.python.org/3/library/typing.html) |
| 33 | Generics and `TypeVar` | `day_33_generics` | generic containers, reusable helpers, typed repositories, variance intuition | generic stack, typed cache, reusable loader interface | [Python typing docs — Generics](https://docs.python.org/3/library/typing.html#generics) |
| 34 | `mypy` and strictness | `day_34_mypy` | strict mode mindset, `Any` control, typed refactors, narrowing patterns | clean a loosely typed module, enforce safer APIs | [mypy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) |

---

## Phase 3 — Python Concurrency

**Track folders:** `src/python_concurrency/` and `exercise/python_concurrency/`

| Day | Topic | Slug | `CODE.md` and `code.py` subtopics | Exercise direction | Primary source |
|-----|-------|------|-----------------------------------|--------------------|----------------|
| 35 | Threading and locks | `day_35_threading` | threads, locks, race conditions, critical sections, thread-safe state | shared counter, worker pool, safe cache mutation | [Real Python — Threading](https://realpython.com/intro-to-python-threading/) |
| 36 | GIL and workload selection | `day_36_gil` | CPU-bound vs I/O-bound, GIL tradeoffs, choosing thread/process/async | classify workloads, refactor wrong concurrency choices | [Python Glossary — GIL](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) |
| 37 | Multiprocessing | `day_37_multiprocessing` | process pool, serialization cost, `Pool.map`, fan-out workloads | batch CPU job runner, checksum or transform workers | [Real Python — Multiprocessing](https://realpython.com/python-multiprocessing/) |
| 38 | `concurrent.futures` | `day_38_futures` | thread pool, process pool, `submit`, `map`, `as_completed`, timeout handling | parallel fetcher, task aggregation, timeout-aware executor | [Python concurrent.futures docs](https://docs.python.org/3/library/concurrent.futures.html) |
| 39 | `asyncio` basics | `day_39_asyncio` | event loop, coroutines, tasks, `await`, `gather`, cancellation basics | async scheduler, timed tasks, cooperative job runner | [Real Python — Asyncio](https://realpython.com/async-io-python/) |
| 40 | `aiohttp` | `day_40_aiohttp` | async HTTP clients, session reuse, fan-out requests, response handling | async API fetcher, retry sketch, response summarizer | [aiohttp docs](https://docs.aiohttp.org/en/stable/) |
| 41 | Async error handling | `day_41_async_errors` | `gather` strategies, cancellation, partial failures, timeout handling | resilient batch fetch, partial-success report builder | [Real Python — Asyncio](https://realpython.com/async-io-python/) |
| 42 | Sync/async bridge | `day_42_sync_async_bridge` | executors from async, blocking boundaries, adapters, handoff patterns | wrap legacy sync code in async service | [Python asyncio event loop docs](https://docs.python.org/3/library/asyncio-eventloop.html) |
| 43 | Concurrency design boundaries | `day_43_concurrency_design` | service boundaries, resource ownership, idempotency, queueing choices | redesign a multi-worker ingest service | [Real Python — Asyncio](https://realpython.com/async-io-python/) |
| 44 | Refactor day | `day_44_refactor` | simplify async/sync split, centralize error handling, improve API boundaries | cleanup pass over earlier concurrent modules | (own earlier modules) |
| 45 | Concurrency milestone | `day_45_milestone` | mini-project assembly, structured boundaries, observability hooks | concurrent fetch/process/write service skeleton | (own earlier modules) |
| 46 | Packaging concurrent code | `day_46_packaging` | `pyproject`, package layout, CLI entrypoints, reusable service modules | convert milestone into installable package | [pyproject.toml spec](https://packaging.python.org/en/latest/specifications/pyproject-toml/) |
| 47 | Testing concurrent code | `day_47_pytest_async` | async tests, timeout assertions, deterministic test shape, fixtures | test concurrent workers and async entrypoints | [Real Python — pytest](https://realpython.com/pytest-python-testing/) |
| 48 | Mocking I/O | `day_48_mocking` | fake network calls, temp files, patching boundaries, deterministic tests | mocked HTTP pipeline, fake queue or file system | [pytest monkeypatch docs](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) |
| 49 | Logging in concurrent systems | `day_49_logging` | structured logs, request/task context, correlation IDs, failure summaries | add logs to concurrent service flows | [Real Python — Logging](https://realpython.com/python-logging/) |
| 50 | Phase review | `day_50_review` | concurrency decision matrix, tradeoff recap, cleanup and retrospective | review exercises, compare thread/process/async versions | (own earlier modules) |

---

## Phase 4 — Python Advanced

**Track folders:** `src/python_advanced/` and `exercise/python_advanced/`

| Day | Topic | Slug | `CODE.md` and `code.py` subtopics | Exercise direction | Primary source |
|-----|-------|------|-----------------------------------|--------------------|----------------|
| 51 | Descriptors | `day_51_descriptors` | `__get__`, `__set__`, validation descriptors, reusable field rules | validated model fields, descriptor-backed settings | [Real Python — Descriptors](https://realpython.com/python-descriptors/) |
| 52 | `__slots__` | `day_52_slots` | memory layout, attribute restrictions, inheritance caveats, fit-for-purpose usage | lightweight DTO comparisons, memory-minded objects | [Python Data Model — __slots__](https://docs.python.org/3/reference/datamodel.html#slots) |
| 53 | Metaclasses | `day_53_metaclasses` | what metaclasses do, `type`, controlled class creation, limited real-world use | registry metaclass or schema registration sketch | [Real Python — Metaclasses](https://realpython.com/python-metaclasses/) |
| 54 | `__init_subclass__` | `day_54_init_subclass` | subclass hooks, automatic registration, policy enforcement | plugin registry, subclass naming rules | [PEP 487](https://peps.python.org/pep-0487/) |
| 55 | Bytecode and `dis` | `day_55_bytecode` | disassembly, compare implementations, stack machine intuition | inspect slow vs clean functions, explain generated ops | [Python dis docs](https://docs.python.org/3/library/dis.html) |
| 56 | Import system | `day_56_importlib` | import flow, module caching, `importlib`, plugin discovery, lazy import tradeoffs | dynamic loader, plugin discovery helper | [Python importlib docs](https://docs.python.org/3/library/importlib.html) |
| 57 | `cProfile` | `day_57_cprofile` | whole-program profiling, reading stats, hotspot hunting | profile a data-processing script and summarize hotspots | [Python profiler docs](https://docs.python.org/3/library/profile.html) |
| 58 | `timeit` and measurement | `day_58_timeit` | micro-benchmarks, warm-up thinking, fair comparisons, bad benchmark habits | compare parser variants, set/list lookup timings | [Python timeit docs](https://docs.python.org/3/library/timeit.html) |
| 59 | `pytest` fixtures | `day_59_pytest_fixtures` | reusable setup, fixture scopes, temp resources, clean test arrangement | refactor repetitive tests into fixtures | [Real Python — pytest](https://realpython.com/pytest-python-testing/) |
| 60 | Coverage | `day_60_coverage` | line vs branch coverage, missing paths, test gap analysis | raise coverage on an earlier module intentionally | [coverage docs](https://coverage.readthedocs.io/) |
| 61 | Ruff and pre-commit | `day_61_ruff_precommit` | linting, formatting, automation, quality gates, rule tuning | add repo quality config, fix lint issues | [ruff docs](https://docs.astral.sh/ruff/) |
| 62 | Security scanning with Bandit | `day_62_bandit` | unsafe patterns, subprocess risks, path handling, audit basics | harden a risky script and document fixes | [bandit docs](https://bandit.readthedocs.io/) |
| 63 | Strategy and Factory | `day_63_patterns_creational` | pluggable behavior, object creation control, runtime selection | payment/pricing strategy engine, parser factory | [Real Python — Factory Method](https://realpython.com/factory-method-python/) |
| 64 | Repository and DI | `day_64_patterns_architecture` | ports and adapters, dependency injection, test seams | repository-backed service with fake and real adapters | [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| 65 | Packaging a library | `day_65_packaging_library` | `pyproject`, version metadata, package exports, editable install | turn a utility module into a small library | [Python Packaging Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/) |
| 66 | `uv` workflow | `day_66_uv` | dependency management, scripts, reproducible workflows, local tooling | migrate scripts to `uv` commands | [uv docs](https://docs.astral.sh/uv/) |
| 67 | Library CI milestone | `day_67_milestone` | lint, test, package checks, release readiness | CI-ready library slice with docs and tests | [GitHub Actions docs](https://docs.github.com/actions) |
| 68 | Metaprogramming review | `day_68_review_meta` | descriptors vs metaclasses vs subclass hooks, when not to use them | compare patterns in one small system | (own Day 51-54 modules) |
| 69 | Testing strategy review | `day_69_review_testing` | unit vs integration, fixtures, coverage goals, safety checks | test plan for a small service or library | (own Day 47, 59-60 modules) |
| 70 | Retrospective and polish | `day_70_retrospective` | cleanup, naming consistency, docs refresh, architecture notes | tighten previous modules before FastAPI phase | (own all modules) |

---

## Phase 5 — FastAPI Track

**Track folders:** `src/fastapi_track/` and `exercise/fastapi_track/`

| Day | Topic | Slug | `CODE.md` and `code.py` subtopics | Exercise direction | Primary source |
|-----|-------|------|-----------------------------------|--------------------|----------------|
| 71 | FastAPI app basics | `day_71_fastapi_intro` | app instance, routers, OpenAPI, response models, path/query params | build a small task or inventory API | [FastAPI — First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) |
| 72 | Pydantic v2 models | `day_72_pydantic` | body parsing, field validation, model config, serialization, aliases | request/response schemas for CRUD endpoints | [Pydantic — Models](https://docs.pydantic.dev/latest/concepts/models/) |
| 73 | Dependencies | `day_73_dependencies` | dependency injection, reusable auth/db helpers, request-scoped resources | auth stub, repository dependency, config injection | [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| 74 | Error handling | `day_74_errors` | HTTP exceptions, custom handlers, validation responses, consistent error shape | domain-to-HTTP error mapping | [FastAPI — Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) |
| 75 | OAuth2 and JWT | `day_75_security_jwt` | password flow basics, token issue/verify, claims, secure config | protected routes, login flow, token validation | [FastAPI — OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) |
| 76 | Middleware and CORS | `day_76_middleware` | request logging, timing middleware, CORS config, request IDs | add middleware stack to an API service | [FastAPI — CORS](https://fastapi.tiangolo.com/tutorial/cors/) |
| 77 | Background tasks | `day_77_background` | delayed work, email/job stubs, async boundaries, task safety | receipt sender or audit log writer | [FastAPI — Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) |
| 78 | SQLAlchemy async and Alembic | `day_78_db_alembic` | async sessions, models, migrations, transactional endpoints | database-backed CRUD slice | [SQLAlchemy Async](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) |
| 79 | Repository in API services | `day_79_repository` | service layer, repository abstraction, unit-testable route logic | route -> service -> repository design | [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| 80 | API testing | `day_80_testing` | `TestClient`, `AsyncClient`, dependency overrides, fake DB patterns | test a CRUD API with auth and errors | [FastAPI — Testing](https://fastapi.tiangolo.com/tutorial/testing/) |
| 81 | WebSockets | `day_81_websockets` | socket endpoints, push updates, connection lifecycle, simple broadcast | chat or event-feed prototype | [FastAPI — WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) |
| 82 | Docker for FastAPI | `day_82_docker` | Dockerfile, image layers, runtime config, compose basics | containerize the API and run locally | [FastAPI — Docker](https://fastapi.tiangolo.com/deployment/docker/) |
| 83 | Settings management | `day_83_settings` | `pydantic-settings`, env vars, secrets hygiene, deployment config | settings object and env-driven app boot | [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| 84 | FastAPI milestone | `day_84_milestone` | assemble auth, DB, tests, docker, docs into one service slice | mini production-style API project | (own Day 71-83 modules) |
| 85 | Health and readiness | `day_85_probes` | health endpoints, dependency checks, graceful startup, readiness semantics | add `/health` and `/ready` checks | [Docker Compose docs](https://docs.docker.com/compose/) |
| 86 | API review checklist | `day_86_review` | contract review, error consistency, security pass, test and docs audit | full review and hardening of FastAPI module | (own Day 71-85 modules) |

---

## Phase 6 — DevOps and Capstone

**Track folders:** `src/devops_track/` and `exercise/devops_track/`

| Day | Topic | Slug | `CODE.md` and `code.py` subtopics | Exercise direction | Primary source |
|-----|-------|------|-----------------------------------|--------------------|----------------|
| 87 | Debugging with `pdb` | `day_87_pdb` | breakpoints, stepping, inspecting state, debugging workflows | debug a failing script and write findings | [Python pdb docs](https://docs.python.org/3/library/pdb.html) |
| 88 | Structured logging | `day_88_structlog` | event logs, context binding, error fields, readable production logs | migrate prints to structured logs | [structlog docs](https://www.structlog.org/) |
| 89 | OpenTelemetry | `day_89_otel` | traces, spans, instrumentation concepts, service visibility basics | instrument a small API or worker flow | [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/) |
| 90 | Safe `subprocess` | `day_90_subprocess` | argument lists, capture output, timeouts, exit codes, injection safety | CLI wrapper, command runner, safe automation task | [Real Python — subprocess](https://realpython.com/python-subprocess/) |
| 91 | Cloud or container SDK | `day_91_cloud_sdk` | Boto3 or Docker SDK, auth patterns, client reuse, automation scripting | bucket/image automation or deployment helper | [Boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) |
| 92 | GitHub Actions | `day_92_actions` | workflows, jobs, matrix basics, lint/test/package CI | CI pipeline for one module or service | [GitHub Actions docs](https://docs.github.com/actions) |
| 93 | Prometheus metrics | `day_93_prometheus` | counters, histograms, request metrics, alert-friendly labels | expose app metrics and verify key signals | [Prometheus Python guide](https://prometheus.io/docs/guides/python/) |
| 94 | Capstone deploy slice | `day_94_capstone` | deployment path, config, logs, metrics, smoke checks | deployable mini-service or toolchain slice | (own Day 87-93 modules) |
| 95 | Runbooks | `day_95_runbook` | incident notes, startup/shutdown, common failure responses, rollback steps | write an operator guide for capstone | (own capstone module) |
| 96 | Timed DSA practice | `day_96_dsa_timed` | speed strategy, template reuse, error-checking under pressure | timed mixed problem set with notes | [NeetCode Practice](https://neetcode.io/practice) |
| 97 | Explain-aloud DSA | `day_97_dsa_verbal` | communicating approach, complexity, edge cases, interviewer clarity | record or script spoken solutions | [NeetCode Roadmap](https://neetcode.io/roadmap) |
| 98 | Portfolio README | `day_98_portfolio` | project framing, outcomes, architecture summaries, proof of skill | polish repo-facing portfolio narrative | (own repo) |
| 99 | Repo review and sync | `day_99_full_review` | cross-check README, study plan, folder status, consistency audit | final cleanup and documentation sync | (own repo) |
| 100 | Next 30 days roadmap | `day_100_graduation` | identify gaps, choose specialization path, next project plan | write the follow-up study and build roadmap | [NeetCode Roadmap](https://neetcode.io/roadmap) |

---

## Sunday Labs

Use Sundays as integrative build days after every 5 Python study days.

| Lab | After days | Focus | Build direction |
|-----|------------|-------|-----------------|
| 01 | 01–05 | Basics integration | CLI config + CSV leaderboard + typed parsing |
| 02 | 06–10 | Data structures + errors | log pipeline with sets, strings, JSONL, explicit failures |
| 03 | 11–14 | Tooling handoff | package skeleton with `pyproject`, `uv`, docs |
| 04 | 15–19 | OOP integration | plugin system with ABCs, inheritance, dataclass events |
| 05 | 20–24 | Lazy processing | iterator/generator ETL with bounded memory |
| 06 | 25–29 | Cross-cutting concerns | decorators, caching, context-managed file safety |
| 07 | 30–34 | Typed library slice | strict typing, tests, one reusable interface |
| 08 | 35–39 | Concurrency intro | thread pool or asyncio fetcher with timeouts |
| 09 | 40–44 | Concurrency design | sync/async boundary cleanup with logging |
| 10 | 45–50 | Concurrency review | design doc plus code cleanup and measurement |
| 11 | 51–55 | Internals to evidence | profile then optimize a real module |
| 12 | 56–60 | Quality gate | fixtures, coverage, linting, quality automation |
| 13 | 61–65 | Architecture patterns | Strategy + Repository billing or catalog module |
| 14 | 66–70 | Release dry-run | package build, versioning, install, tag workflow |
| 15 | 71–75 | Auth slice | token issue/verify with protected endpoints and tests |
| 16 | 76–80 | Integration tests | FastAPI app with overrides and fake DB |
| 17 | 81–86 | Containerized API | Dockerized service with health checks |
| 18 | 87–91 | Automation and ops | subprocess-safe automation with logs |
| 19 | 92–96 | Delivery plus problem solving | CI plus timed DSA and service maintenance |
| 20 | 97–100 | Capstone review | demo flow, architecture note, next-steps backlog |

Suggested optional lab path pattern:

| Lab folder | Pattern |
|-----------|---------|
| Sunday lab | `exercise/sunday_labs/week_XX_integrated/` |

---

## Parallel DSA Plan

**Track folders:** `src/dsa/` and `exercise/dsa/`

| Week | Topic | Slug | `CODE.md` and `code.py` subtopics | Repo exercise direction | Platform direction | Primary source |
|------|-------|------|-----------------------------------|-------------------------|-------------------|----------------|
| 01 | Big-O, arrays, hashing basics | `week_01_big_o_arrays_hashing` | complexity, amortized cost, **what Big-O is used for**, arrays, hash maps, lookup tradeoffs | two-sum variant, duplicate detection, anagram grouping | Two Sum, Contains Duplicate | [NeetCode — Arrays & Hashing](https://neetcode.io/roadmap) |
| 02 | Arrays, hashing, Kadane basics | `week_02_arrays_hashing_ii` | prefix sums, frequency maps, grouping, Kadane's algorithm, string ops warm-up, subsequence-sum intro | prefix-array builder, max-subarray (Kadane), group-by task, subsequence-sum checks | Maximum Subarray, Top K Frequent | [NeetCode — Arrays & Hashing](https://neetcode.io/roadmap) |
| 03 | Two pointers and 3Sum dedupe | `week_03_two_pointers` | opposite-end scans, sorted pair/triplet logic, 3Sum deduplication rules, palindrome two-pointer scans | pair sum, 3Sum template with dedupe, palindrome pointer checks | 3Sum, Container With Most Water, Valid Palindrome | [NeetCode — Two Pointers](https://neetcode.io/roadmap) |
| 04 | Sliding window and monotonic deque | `week_04_sliding_window` | fixed vs variable windows, invariant tracking, substring frequency windows, monotonic deque for window max | max fixed window, variable-window substring tasks, sliding-window maximum | Longest Repeating Character Replacement, Minimum Window Substring, Sliding Window Maximum | [NeetCode — Sliding Window](https://neetcode.io/roadmap) |
| 05 | Stack and monotonic structures | `week_05_stack` | stack ADT, monotonic stack, bracket matching, next greater pattern, stack-vs-deque choice | valid brackets, daily temperature style stack tasks, histogram-area pattern | Valid Parentheses, Daily Temperatures, Largest Rectangle in Histogram | [NeetCode — Stack](https://neetcode.io/roadmap) |
| 06 | Binary search | `week_06_binary_search` | lower/upper bounds, mid logic, rotated arrays, answer-space search, matrix binary search | custom binary search helpers, boundary finders, matrix search helpers | Binary Search, Search in Rotated Sorted Array, Search a 2D Matrix | [NeetCode — Binary Search](https://neetcode.io/roadmap) |
| 07 | Linked list | `week_07_linked_list` | node structure, dummy nodes, reversal, fast/slow pointers | linked-list utilities, reversal, merge, cycle detection | Reverse Linked List, Merge Two Sorted Lists | [NeetCode — Linked List](https://neetcode.io/roadmap) |
| 08 | Binary trees I | `week_08_binary_tree` | tree construction from list/array, DFS traversals, BFS level order, path-sum style problems, LCA, diameter, vertical/zigzag traversal patterns | tree-from-list helpers, path and LCA helpers, diameter and traversal exercises | Maximum Depth, Binary Tree Level Order Traversal, Lowest Common Ancestor of a Binary Tree, Diameter of Binary Tree | [NeetCode — Trees](https://neetcode.io/roadmap) |
| 09 | Binary search trees | `week_09_bst` | BST validation, insert/search, kth smallest, successor/predecessor, BST LCA | validate BST, ordered traversal, nearest value tasks, BST LCA | Validate BST, Kth Smallest in BST, Lowest Common Ancestor of a BST | [NeetCode — Trees](https://neetcode.io/roadmap) |
| 10 | Heap and priority queue | `week_10_heap` | `heapq`, min/max heap patterns, top-k, merge streams | kth largest, running median sketch, prioritized tasks | Kth Largest, Merge K Sorted Lists | [NeetCode — Heap](https://neetcode.io/roadmap) |
| 11 | Recursion and backtracking foundations | `week_11_backtracking` | base/recursive case design, processed/unprocessed pattern, include/exclude recursion tree, subsequence by character, subsequence-sum and subset-sum patterns, pruning, recursion-based pattern printing | recursion warm-ups, pattern printing via recursion, subsequence generators, subset/combination sum templates | Subsets, Subsets II, Combination Sum | [NeetCode — Backtracking](https://neetcode.io/roadmap) |
| 12 | Graphs I | `week_12_graphs_i` | adjacency list, BFS, DFS, visited sets, island/count patterns, grid/matrix traversal (4-direction BFS/DFS) | graph class, connected components, BFS shortest path, matrix flood-fill tasks | Number of Islands, Clone Graph, Rotting Oranges | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 13 | Graphs II and topo sort | `week_13_graphs_ii_topo` | directed graphs, indegree, Kahn's algorithm, cycle detection | course scheduling, dependency ordering | Course Schedule | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 14 | Union-Find | `week_14_union_find` | DSU structure, path compression, union by rank, connectivity | DSU class, component tracking, merge events | Redundant Connection, Number of Provinces | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 15 | Intervals and greedy | `week_15_greedy` | interval sorting/merging, overlap detection, local choices, proof intuition, schedule selection | interval merge/select, jump decisions, resource scheduling | Non-overlapping Intervals, Merge Intervals, Jump Game | [NeetCode — Greedy](https://neetcode.io/roadmap) |
| 16 | 1D dynamic programming | `week_16_dp_1d` | recurrence design, memoization, tabulation, state compression, max-subarray as DP intuition | climbing stairs, robber, coin-change style tasks, Kadane reinforcement | Coin Change, House Robber, Maximum Subarray | [NeetCode — DP](https://neetcode.io/roadmap) |
| 17 | 2D dynamic programming | `week_17_dp_2d` | grids, table fill order, matrix traversal patterns (row/col/spiral mindset), LCS patterns, path counting | unique paths, edit-distance scaffold, sequence matching, matrix traversal drills | Unique Paths, Longest Common Subsequence, Set Matrix Zeroes | [NeetCode — DP](https://neetcode.io/roadmap) |
| 18 | Shortest paths | `week_18_shortest_path` | Dijkstra, weighted graphs, priority queues, relaxations | shortest-path helper, weighted route planner | Network Delay Time | [NeetCode — Graphs](https://neetcode.io/roadmap) |
| 19 | Tries, string algorithms, and bit tricks | `week_19_tries_bits` | trie insert/search, core string operations, substring search, consecutive-string patterns, palindrome expansion, Rabin-Karp rolling hash idea, KMP prefix map (`k-map`/LPS) intuition, bit masks, XOR-style reasoning | trie class, prefix matcher, substring/rabin-karp helper, kmp-prefix-map helper, bit utility drills | Implement Trie, Longest Palindromic Substring, Find the Index of the First Occurrence in a String, Repeated DNA Sequences | [NeetCode — Roadmap](https://neetcode.io/roadmap) |
| 20 | Mixed review, sorting, and math basics | `week_20_mixed_review` | timed review, weak-area diagnosis, sorting algorithms (merge/quick/heap/counting tradeoffs), math/number theory basics (gcd, primes, fast power, modular arithmetic), template consolidation | mixed set of 3 problems, verbal explanation prompts, sorting warm-up drills, math warm-up drills | NeetCode weak-area revisit, Sort an Array, Pow(x, n), Count Primes | [NeetCode Practice](https://neetcode.io/practice) |

---

## DSA Folder Slugs

| Week | Folder |
|------|--------|
| 01 | `week_01_big_o_arrays_hashing/` |
| 02 | `week_02_arrays_hashing_ii/` |
| 03 | `week_03_two_pointers/` |
| 04 | `week_04_sliding_window/` |
| 05 | `week_05_stack/` |
| 06 | `week_06_binary_search/` |
| 07 | `week_07_linked_list/` |
| 08 | `week_08_binary_tree/` |
| 09 | `week_09_bst/` |
| 10 | `week_10_heap/` |
| 11 | `week_11_backtracking/` |
| 12 | `week_12_graphs_i/` |
| 13 | `week_13_graphs_ii_topo/` |
| 14 | `week_14_union_find/` |
| 15 | `week_15_greedy/` |
| 16 | `week_16_dp_1d/` |
| 17 | `week_17_dp_2d/` |
| 18 | `week_18_shortest_path/` |
| 19 | `week_19_tries_bits/` |
| 20 | `week_20_mixed_review/` |

---

## MAANG Depth Coverage Checklist (DSA)

These concepts must be explicitly covered by generated week artifacts (`CODE.md`, `code.py`, `EXERCISE.md`, `exNN_*.py`) in the mapped weeks:

| Concept | Week mapping |
|---------|--------------|
| Kadane's algorithm | Week 02, reinforced in Week 16 |
| 3Sum triplet dedupe logic | Week 03 |
| Recursion as a standalone foundation | Week 11 |
| Processed vs unprocessed recursion state | Week 11 |
| Subsequence character generation | Week 11 |
| Subsequence sum / subset-sum (`subsum`) | Week 11 and Week 16 |
| Pattern printing (loop + recursion styles) | Day 02 and Week 11 |
| Binary tree construction, path problems, LCA, diameter, zigzag/vertical traversals | Week 08 |
| Monotonic deque patterns | Week 04 (and Week 05 comparisons) |
| Intervals as dedicated study area | Week 15 |
| String algorithms (palindromes, KMP idea, substring handling) | Week 03, Week 04, Week 19 |
| String operations (normalization/search/compare) | Day 08 and Week 19 |
| Substring and consecutive-string patterns | Week 04 and Week 19 |
| Rabin-Karp rolling hash pattern matching | Week 19 |
| KMP prefix map (`k-map` / LPS table) | Week 19 |
| Sorting algorithms (merge, quick, heap, counting) | Week 20 |
| Matrix traversal patterns | Week 12 and Week 17 |
| Math/number theory basics | Week 20 |

---

## Industrial Bar

- Public APIs use type hints.
- `CODE.md` follows [docs/CODE_TEMPLATE.md](./docs/CODE_TEMPLATE.md).
- Exercises use the scoring and gate system from [docs/EVALUATION_RUBRIC.md](./docs/EVALUATION_RUBRIC.md).
- Every exercise file contains inline assert self-checks.
- DSA `CODE.md` files include visual/diagram coverage for the core algorithm flow.
- Every DSA snippet/example in `CODE.md` includes a traversal visual block (ASCII/Mermaid step flow).
- DSA visuals may optionally include GIFs (with caption + source attribution), but must still include ASCII/Mermaid fallback for portability.
- DSA Week 01 explicitly explains what Big-O notation is used for in choosing solution approaches.
- DSA `.md` and `.py` files include time and space complexity for each discussed problem.
- Avoid copying proprietary lesson text or challenge text verbatim. Use [docs/SOURCE_REGISTRY.md](./docs/SOURCE_REGISTRY.md) and rewrite material into this repo's style.

---

## Scheduling Guidance

- A strict lockstep plan can map DSA Week `n` to Python days `5n-4` through `5n`.
- A flexible plan can finish DSA Week `n` within the same broad Python phase.
- Sunday labs are catch-up friendly, but finish each lab before the next major milestone day in that phase.

This file is the planning source of truth for what to generate next.
