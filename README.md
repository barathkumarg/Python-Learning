# 🐍 Python Mastery Roadmap
> **Basic → Intermediate → Advanced → FastAPI → DevOps → MAANG DSA**
> Industrial-standard curriculum with free resources. All topics, all concepts, zero paywalls.

---

## 📋 Table of Contents

- [How to Use This Repo](#how-to-use-this-repo)
- [Python — Basic](#python--basic)
- [Python — Intermediate](#python--intermediate)
- [Python — Advanced](#python--advanced)
- [FastAPI — Web & API Framework](#fastapi--web--api-framework)
- [DevOps Python](#devops-python)
- [DSA — MAANG Standard](#dsa--maang-standard)
- [Tools & Environment Setup](#tools--environment-setup)
- [Study Schedule](#study-schedule)
- [Progress Tracker](#progress-tracker)

---

## How to Use This Repo

```
Python-Learning/
├── README.md                        ← you are here
├── DAILY_STUDY_PLAN.md              ← curriculum map (what to generate next)
├── requirements.txt                 ← project dependencies (ruff, pytest)
├── .agent.md                        ← AI agent generation instructions
│
├── docs/                            ← framework documentation
│   ├── RUBRIC.md                    ← gates, scoring, skills, evaluation protocol
│   ├── PROMPT_TEMPLATES.md          ← copy-paste generation prompts
│   ├── SOURCE_REGISTRY.md           ← curated sources with per-day URLs
│   ├── DSA_VISUALS.md               ← Mermaid templates per DSA week (reference lookup)
│   └── SCORE_TRACKER.md             ← unified evaluation dashboard
│
├── src/                             ← teaching reference code
│   ├── python_basic/                ← Phase 1: Days 01–14
│   │   ├── day_01_syntax_variables/
│   │   │   ├── CODE.md              ← concept map with snippets
│   │   │   └── code.py              ← production-style reference
│   │   ├── day_02_control_flow/
│   │   ├── day_03_functions/
│   │   └── ...day_04 through day_14
│   ├── python_intermediate/         ← Phase 2: Days 15–34
│   ├── python_concurrency/          ← Phase 3: Days 35–50
│   ├── python_advanced/             ← Phase 4: Days 51–70
│   ├── fastapi_track/               ← Phase 5: Days 71–86
│   ├── devops_track/                ← Phase 6: Days 87–100
│   └── dsa/                         ← DSA Weeks 01–20 (parallel track)
│       ├── week_01_big_o_arrays_hashing/
│       │   ├── CODE.md
│       │   └── code.py
│       └── ...week_02 through week_20
│
├── exercise/                        ← learner exercises and evaluations
│   ├── python_basic/
│   │   ├── day_01_syntax_variables/
│   │   │   ├── EXERCISE.md          ← specs, skills, scoring, eval report
│   │   │   ├── ex01_basic.py        ← foundational exercise
│   │   │   ├── ex02_intermediate.py ← applied exercise
│   │   │   └── ex03_advanced.py     ← harder design exercise
│   │   └── ...
│   ├── python_intermediate/
│   ├── python_concurrency/
│   ├── python_advanced/
│   ├── fastapi_track/
│   ├── devops_track/
│   ├── dsa/
│   │   ├── week_01_big_o_arrays_hashing/
│   │   └── ...
│   └── sunday_labs/                 ← integrative build days
│       └── week_XX_integrated/
```

**Study strategy:**
- Run DSA practice in parallel with Python learning — 2 hrs/day DSA + 1.5 hrs/day Python
- Write code for every topic — reading alone does not build skill
- Commit every practice file; use git log as your progress journal
- See [DAILY_STUDY_PLAN.md](DAILY_STUDY_PLAN.md) for the full curriculum map and generation priority

---

## Python — Basic

> **Duration:** Weeks 1–2 · **Goal:** Solid Python foundation

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Syntax & Variables | int, float, str, bool, None, naming conventions, f-strings | [Python Tutorial](https://docs.python.org/3/tutorial/) · [W3Schools](https://www.w3schools.com/python/) |
| Control Flow | if/elif/else, for, while, break, continue, pass, match (3.10+) | [Real Python — Control Flow](https://realpython.com/python-conditional-statements/) |
| Functions | def, args, kwargs, *args, **kwargs, default params, return, lambda | [Real Python — Functions](https://realpython.com/defining-your-own-python-function/) |
| Lists | indexing, slicing, append, extend, sort, list methods | [Python Docs — Lists](https://docs.python.org/3/tutorial/datastructures.html) |
| Tuples | immutability, packing/unpacking, named tuples | [Real Python — Tuples](https://realpython.com/python-lists-tuples/) |
| Dictionaries | CRUD operations, dict methods, dict comprehension | [Real Python — Dicts](https://realpython.com/python-dicts/) |
| Sets | union, intersection, difference, frozenset | [Real Python — Sets](https://realpython.com/python-sets/) |
| Strings | methods, slicing, f-strings, raw strings, encoding | [Real Python — Strings](https://realpython.com/python-strings/) |
| File I/O | open(), read/write modes, with statement, csv, json | [Real Python — File I/O](https://realpython.com/read-write-files-python/) |
| Error Handling | try/except/else/finally, raise, built-in exceptions | [Real Python — Exceptions](https://realpython.com/python-exceptions/) |
| Modules | import, from…import, __name__, sys.path | [Real Python — Modules](https://realpython.com/python-modules-packages/) |
| Built-ins | len, range, enumerate, zip, map, filter, sorted, reversed | [Python Docs — Built-ins](https://docs.python.org/3/library/functions.html) |
| Comprehensions | list, dict, set, generator comprehensions | [Real Python — Comprehensions](https://realpython.com/list-comprehension-python/) |
| Virtual Environments | venv, pip, requirements.txt, pip freeze | [Python Packaging Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) |

```python
# basics/01_variables.py — example file structure
x: int = 42
name: str = "Python"
pi: float = 3.14
active: bool = True
nothing: None = None

# f-string formatting
print(f"Hello, {name}! Pi is approximately {pi:.2f}")

# walrus operator (Python 3.8+)
if n := len(name):
    print(f"name has {n} characters")
```

---

## Python — Intermediate

> **Duration:** Weeks 3–9 · **Goal:** Write idiomatic, professional Python

### Object-Oriented Programming

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Classes & Objects | `__init__`, `self`, instance vs class variables, methods | [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) |
| Dunder Methods | `__repr__`, `__str__`, `__len__`, `__eq__`, `__lt__`, `__hash__`, `__contains__` | [Real Python — Magic Methods](https://realpython.com/python-magic-methods/) |
| Properties | `@property`, getter/setter/deleter, `property()` | [Real Python — Properties](https://realpython.com/python-property/) |
| Inheritance | single/multiple inheritance, `super()`, method resolution order (MRO) | [Real Python — Inheritance](https://realpython.com/inheritance-composition-python/) |
| Abstract Classes | `abc.ABC`, `@abstractmethod`, interface patterns | [Python Docs — abc](https://docs.python.org/3/library/abc.html) |
| Dataclasses | `@dataclass`, `field()`, `__post_init__`, frozen, slots | [Real Python — Dataclasses](https://realpython.com/python-data-classes/) |
| Class vs Static Methods | `@classmethod`, `@staticmethod`, when to use each | [Real Python — Class Methods](https://realpython.com/instance-class-and-static-methods-easyguide/) |

```python
# intermediate/oop/vehicle.py
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.make!r}, {self.model!r}, {self.year})"

    @abstractmethod
    def fuel_type(self) -> str: ...

    @classmethod
    def from_string(cls, data: str) -> "Vehicle":
        make, model, year = data.split(",")
        return cls(make.strip(), model.strip(), int(year))

@dataclass(frozen=True, slots=True)
class ElectricCar(Vehicle):
    battery_kwh: float = field(default=75.0)

    def fuel_type(self) -> str:
        return "electric"
```

### Iterators, Generators & Functional

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Iterators | `__iter__`, `__next__`, StopIteration, iter() | [Python Docs — Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types) |
| Generators | `yield`, `yield from`, generator expressions, send(), throw() | [Real Python — Generators](https://realpython.com/introduction-to-python-generators/) |
| Decorators | function decorators, `functools.wraps`, class decorators, stacking | [Real Python — Decorators](https://realpython.com/primer-on-python-decorators/) |
| Context Managers | `__enter__`/`__exit__`, `@contextmanager`, suppress | [Real Python — with Statement](https://realpython.com/python-with-statement/) |
| functools | `partial`, `lru_cache`, `cache`, `reduce`, `total_ordering` | [Python Docs — functools](https://docs.python.org/3/library/functools.html) |
| itertools | `chain`, `islice`, `groupby`, `product`, `combinations`, `permutations` | [Python Docs — itertools](https://docs.python.org/3/library/itertools.html) |

```python
# intermediate/generators/pipeline.py
import itertools
from typing import Generator, Iterator

def read_lines(filename: str) -> Generator[str, None, None]:
    with open(filename) as f:
        yield from (line.strip() for line in f if line.strip())

def parse_csv_rows(lines: Iterator[str]) -> Generator[list[str], None, None]:
    yield from (line.split(",") for line in lines)

# Lazy pipeline — processes gigabyte files in constant memory
pipeline = parse_csv_rows(read_lines("data.csv"))
batch = list(itertools.islice(pipeline, 1000))
```

### Type System

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Type Hints | basic annotations, `Optional`, `Union`, `Any` | [Real Python — Type Checking](https://realpython.com/python-type-checking/) |
| Generic Types | `TypeVar`, `Generic`, `list[int]`, `dict[str, Any]` | [Python Docs — typing](https://docs.python.org/3/library/typing.html) |
| Protocols | `Protocol`, structural subtyping, runtime_checkable | [PEP 544](https://peps.python.org/pep-0544/) |
| TypedDict & Literal | typed dicts, literal types, `Final`, `ClassVar` | [mypy Docs](https://mypy.readthedocs.io/en/stable/) |
| mypy Static Analysis | running mypy, strict mode, ignore comments, stubs | [mypy Docs](https://mypy.readthedocs.io/en/stable/) |

### Concurrency

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Threading | `threading.Thread`, daemon threads, `Lock`, `Event`, `Semaphore` | [Real Python — Concurrency](https://realpython.com/python-concurrency/) |
| GIL | what it is, when it matters, CPU-bound vs IO-bound | [Real Python — GIL](https://realpython.com/python-gil/) |
| Multiprocessing | `Process`, `Pool`, `Queue`, `Pipe`, shared memory | [Python Docs — multiprocessing](https://docs.python.org/3/library/multiprocessing.html) |
| concurrent.futures | `ThreadPoolExecutor`, `ProcessPoolExecutor`, `as_completed` | [Python Docs — concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) |
| asyncio | event loop, `async def`, `await`, `create_task`, `gather`, `sleep` | [Real Python — Async IO](https://realpython.com/async-io-python/) |
| aiohttp | async HTTP client/server, sessions, connection pooling | [aiohttp Docs](https://docs.aiohttp.org/) |

```python
# intermediate/async/fetch_many.py
import asyncio
import aiohttp

async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as resp:
        return {"url": url, "status": resp.status, "body": await resp.text()}

async def fetch_all(urls: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    urls = ["https://httpbin.org/get?n=1", "https://httpbin.org/get?n=2"]
    results = asyncio.run(fetch_all(urls))
```

---

## Python — Advanced

> **Duration:** Weeks 10–14 · **Goal:** Deep Python internals and production patterns

### Metaprogramming

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Descriptors | `__get__`, `__set__`, `__delete__`, data vs non-data, `property` internals | [Python Docs — Descriptors](https://docs.python.org/3/howto/descriptor.html) |
| Metaclasses | `type`, `__new__`, `__init_subclass__`, `__prepare__` | [Real Python — Metaclasses](https://realpython.com/python-metaclasses/) |
| `__slots__` | memory optimization, slot inheritance, comparison with `__dict__` | [Real Python — Slots](https://realpython.com/python-slots/) |
| `__init_subclass__` | hook on subclass creation, plugin systems | [Python Docs](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__) |
| `__class_getitem__` | generic alias support, custom `[]` on classes | [Python Docs](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__) |

### CPython Internals

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Bytecode & `dis` | disassemble functions, understand LOAD_FAST, CALL, stack-based VM | [Python Docs — dis](https://docs.python.org/3/library/dis.html) |
| Reference Counting | `sys.getrefcount`, cyclic GC, `weakref` | [Real Python — Memory](https://realpython.com/python-memory-management/) |
| Frame Objects | `inspect.currentframe`, locals/globals, traceback inspection | [Python Docs — inspect](https://docs.python.org/3/library/inspect.html) |
| Import System | finders, loaders, `importlib`, lazy imports, `sys.meta_path` | [Real Python — Import](https://realpython.com/python-import/) |
| Peephole Optimizer | constant folding, dead code elimination, SETUP_FINALLY | [CPython Dev Guide](https://devguide.python.org/internals/) |

### Profiling & Optimization

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| `cProfile` | profile entire programs, `pstats`, `snakeviz` visualization | [Python Docs — cProfile](https://docs.python.org/3/library/profile.html) |
| `line_profiler` | line-by-line profiling with `@profile` decorator | [line_profiler GitHub](https://github.com/pyutils/line_profiler) |
| `memory_profiler` | peak memory, line-by-line memory tracking | [memory_profiler GitHub](https://github.com/pythonprofilers/memory_profiler) |
| `tracemalloc` | memory allocation traces, compare snapshots | [Python Docs — tracemalloc](https://docs.python.org/3/library/tracemalloc.html) |
| `timeit` | microbenchmarks, command-line and API usage | [Python Docs — timeit](https://docs.python.org/3/library/timeit.html) |

### Testing & Quality

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| pytest | fixtures, parametrize, marks, conftest.py, plugins | [pytest Docs](https://docs.pytest.org/) |
| Mocking | `MagicMock`, `patch`, `patch.object`, `side_effect`, `autospec` | [Python Docs — mock](https://docs.python.org/3/library/unittest.mock.html) |
| Coverage | `pytest-cov`, coverage.py, branch coverage, HTML reports | [coverage.py Docs](https://coverage.readthedocs.io/) |
| ruff | linting, formatting, isort, pyflakes replacement — zero-config | [Ruff Docs](https://docs.astral.sh/ruff/) |
| mypy strict | `--strict` flag, `py.typed`, inline `# type: ignore` | [mypy Docs](https://mypy.readthedocs.io/en/stable/) |
| pre-commit | hooks for ruff, mypy, bandit, secret scanning | [pre-commit Docs](https://pre-commit.com/) |
| bandit | security linting, common vulnerability detection | [bandit Docs](https://bandit.readthedocs.io/) |

### Packaging

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| pyproject.toml | `[project]`, `[build-system]`, `[tool.ruff]`, `[tool.mypy]` | [Python Packaging Guide](https://packaging.python.org/en/latest/) |
| setuptools / hatchling | build backends, editable installs, entry_points | [setuptools Docs](https://setuptools.pypa.io/) |
| uv | ultra-fast pip/venv replacement, `uv sync`, `uv add` | [uv Docs](https://docs.astral.sh/uv/) |
| Publishing to PyPI | `twine`, TestPyPI, CI publish workflow | [Real Python — PyPI](https://realpython.com/pypi-publish-python-package/) |

### Design Patterns

| Pattern | Category | Free Resource |
|---------|----------|---------------|
| Singleton | Creational | [python-patterns.guide](https://python-patterns.guide/gang-of-four/singleton/) |
| Factory Method | Creational | [Refactoring Guru](https://refactoring.guru/design-patterns/factory-method/python/example) |
| Abstract Factory | Creational | [Refactoring Guru](https://refactoring.guru/design-patterns/abstract-factory/python/example) |
| Builder | Creational | [Refactoring Guru](https://refactoring.guru/design-patterns/builder/python/example) |
| Adapter | Structural | [Refactoring Guru](https://refactoring.guru/design-patterns/adapter/python/example) |
| Decorator | Structural | [python-patterns.guide](https://python-patterns.guide/gang-of-four/decorator-pattern/) |
| Observer | Behavioral | [Refactoring Guru](https://refactoring.guru/design-patterns/observer/python/example) |
| Strategy | Behavioral | [Refactoring Guru](https://refactoring.guru/design-patterns/strategy/python/example) |
| Repository | Architectural | [Cosmic Python](https://www.cosmicpython.com/) |
| Dependency Injection | Architectural | [python-dependency-injector](https://python-dependency-injector.ets-labs.org/) |

---

## FastAPI — Web & API Framework

> **Duration:** Weeks 15–18 · **Goal:** Build production-grade REST APIs

### Foundation

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Installation & First App | `uvicorn`, `fastapi`, hot-reload, auto-docs at `/docs` | [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) |
| Path Parameters | type hints as validators, `Path()`, `Annotated` | [FastAPI — Path Params](https://fastapi.tiangolo.com/tutorial/path-params/) |
| Query Parameters | optional/required, `Query()`, default values, aliases | [FastAPI — Query Params](https://fastapi.tiangolo.com/tutorial/query-params/) |
| Request Body | Pydantic models, nested models, `Body()`, multiple bodies | [FastAPI — Body](https://fastapi.tiangolo.com/tutorial/body/) |
| Response Models | `response_model`, `response_model_exclude_unset`, status codes | [FastAPI — Response Model](https://fastapi.tiangolo.com/tutorial/response-model/) |
| HTTP Methods | GET, POST, PUT, PATCH, DELETE — when to use each | [FastAPI — Request Methods](https://fastapi.tiangolo.com/tutorial/request-forms/) |
| Headers & Cookies | `Header()`, `Cookie()`, custom headers | [FastAPI — Headers](https://fastapi.tiangolo.com/tutorial/header-params/) |
| Form Data & File Upload | `Form()`, `File()`, `UploadFile`, multipart | [FastAPI — Forms](https://fastapi.tiangolo.com/tutorial/request-forms/) |

### Pydantic v2

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| BaseModel | field definitions, defaults, aliases, `model_validate` | [Pydantic Docs](https://docs.pydantic.dev/) |
| Validators | `@field_validator`, `@model_validator`, mode before/after | [Pydantic — Validators](https://docs.pydantic.dev/latest/concepts/validators/) |
| Field Types | constrained types, `constr`, `conint`, `EmailStr`, `AnyUrl` | [Pydantic — Types](https://docs.pydantic.dev/latest/concepts/types/) |
| Settings Management | `BaseSettings`, env files, secrets, `pydantic-settings` | [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| Serialization | `model_dump()`, `model_dump_json()`, `exclude`, `include` | [Pydantic — Serialization](https://docs.pydantic.dev/latest/concepts/serialization/) |

### Advanced FastAPI

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Dependency Injection | `Depends()`, nested deps, class deps, yield deps | [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| OAuth2 + JWT Auth | `OAuth2PasswordBearer`, `python-jose`, token creation/validation | [FastAPI — Security](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) |
| Middleware | `@app.middleware("http")`, `BaseHTTPMiddleware`, CORS, GZip | [FastAPI — Middleware](https://fastapi.tiangolo.com/tutorial/middleware/) |
| Background Tasks | `BackgroundTasks`, fire-and-forget, Celery integration | [FastAPI — Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) |
| WebSockets | `WebSocket`, `WebSocketDisconnect`, broadcast patterns | [FastAPI — WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) |
| APIRouter | modular routing, `prefix`, `tags`, `dependencies` on router | [FastAPI — Bigger Apps](https://fastapi.tiangolo.com/tutorial/bigger-applications/) |
| Exception Handlers | `HTTPException`, custom `exception_handler`, 422 override | [FastAPI — Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) |
| Async Database | `asyncpg`, `databases`, async SQLAlchemy, connection pooling | [SQLAlchemy Async](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) |
| Alembic Migrations | `alembic init`, `revision --autogenerate`, `upgrade head` | [Alembic Docs](https://alembic.sqlalchemy.org/) |
| Testing with TestClient | `TestClient`, `AsyncClient`, override dependencies, test DB | [FastAPI — Testing](https://fastapi.tiangolo.com/tutorial/testing/) |
| Deployment | Docker multi-stage, `gunicorn + uvicorn workers`, health checks | [FastAPI — Deployment](https://fastapi.tiangolo.com/deployment/) |

```python
# fastapi/app/main.py — production app structure
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.routers import users, items, auth
from app.core.config import settings
from app.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()          # startup
    yield
    # teardown here

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs" if settings.DEBUG else None,
)

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
```

---

## DevOps Python

> **Duration:** Weeks 19–22 · **Goal:** Automate infrastructure, debug production systems

### Debugging

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| pdb / ipdb | `breakpoint()`, `n/s/c/l/p/q`, post-mortem with `pdb.pm()` | [Python Docs — pdb](https://docs.python.org/3/library/pdb.html) · [Real Python](https://realpython.com/python-debugging-pdb/) |
| Structured Logging | `structlog`, JSON output, correlation IDs, log levels | [structlog Docs](https://www.structlog.org/) |
| Remote Debugging | VS Code `debugpy`, `ptsvd`, attach to running process | [debugpy GitHub](https://github.com/microsoft/debugpy) |
| Exception Monitoring | Sentry SDK, `sys.excepthook`, unhandled exceptions | [Sentry Python](https://docs.sentry.io/platforms/python/) |
| OpenTelemetry | traces, spans, context propagation, Jaeger/Tempo integration | [OTel Python](https://opentelemetry.io/docs/instrumentation/python/) |

### Automation & Scripting

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| subprocess | `run()`, `Popen`, `check_output`, `shell=False` security, `shlex` | [Python Docs](https://docs.python.org/3/library/subprocess.html) · [Real Python](https://realpython.com/python-subprocess/) |
| os & shutil | `os.walk`, `shutil.copy`, `shutil.rmtree`, file/dir management | [Python Docs — os](https://docs.python.org/3/library/os.html) |
| Fabric & Invoke | remote SSH via Python, deployment scripts, task runner | [Fabric Docs](https://www.fabfile.org/) · [Invoke Docs](https://www.pyinvoke.org/) |
| Ansible Modules | custom Python modules for Ansible, dynamic inventories | [Ansible Dev Guide](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html) |
| schedule & APScheduler | cron-like scheduling in pure Python | [schedule Docs](https://schedule.readthedocs.io/) |

### Cloud & Infrastructure

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| Boto3 — AWS SDK | EC2, S3, Lambda, IAM, CloudWatch, paginators, waiters | [Boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) |
| Docker SDK | manage containers/images via Python, `docker.from_env()` | [docker-py Docs](https://docker-py.readthedocs.io/) |
| Kubernetes Client | manage pods/deployments, watch events, custom operators | [k8s Python](https://github.com/kubernetes-client/python) |
| Pulumi (IaC) | provision AWS/GCP/Azure in Python, stacks, `pulumi up` | [Pulumi Python](https://www.pulumi.com/docs/languages-sdks/python/) |
| AWS CDK (Python) | CloudFormation via Python constructs, L2/L3 patterns | [AWS CDK Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html) |

### CI/CD

| Topic | What to Learn | Free Resource |
|-------|--------------|---------------|
| GitHub Actions | matrix builds, pip caching with `uv`, coverage upload | [GH Actions Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) |
| Dockerfile (Python) | multi-stage builds, slim images, non-root user, `.dockerignore` | [Docker Python Guide](https://docs.docker.com/language/python/) |
| Prometheus Metrics | `Counter`, `Gauge`, `Histogram`, `Summary`, push gateway | [prometheus_client](https://github.com/prometheus/client_python) |

---

## DSA — MAANG Standard

> Run in parallel with Python. **2 hours/day.** Primary tracker: [NeetCode Roadmap](https://neetcode.io/roadmap)

### Big-O Complexity Reference

| Complexity | Name | Example |
|-----------|------|---------|
| O(1) | Constant | Hash map lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Array traversal |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Subsets recursion |
| O(n!) | Factorial | Permutations brute force |

Big-O Cheat Sheet: https://www.bigocheatsheet.com

### Foundation

| Topic | Key Patterns | Resource |
|-------|-------------|----------|
| Arrays | sliding window, prefix sum, Kadane's | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Arrays](https://leetcode.com/tag/array/) |
| Strings | string operations, substring search, consecutive-string patterns, KMP (`k-map`/LPS), Rabin-Karp idea | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Strings](https://leetcode.com/tag/string/) |
| Sorting Algorithms | merge sort, quick sort, heap sort, counting/radix tradeoffs | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Sorting](https://leetcode.com/tag/sorting/) |
| Hash Maps & Sets | frequency count, two-sum variants, group anagrams | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Hash](https://leetcode.com/tag/hash-table/) |
| Stack (Monotonic) | next greater element, daily temperatures, largest rectangle | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Stack](https://leetcode.com/tag/stack/) |
| Queue & Deque | sliding window maximum, BFS, LRU cache | [Python Docs — collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) |
| Linked Lists | Floyd's cycle, reversal, merge K sorted, LRU cache | [NeetCode](https://neetcode.io/roadmap) · [LeetCode LL](https://leetcode.com/tag/linked-list/) |
| Binary Search | left/right boundary, rotated array, koko bananas | [NeetCode](https://neetcode.io/roadmap) · [LeetCode BS](https://leetcode.com/tag/binary-search/) |

### Intermediate

| Topic | Key Patterns | Resource |
|-------|-------------|----------|
| Two Pointers | 3Sum, container with water, trapping rain | [NeetCode](https://neetcode.io/roadmap) · [LeetCode 2P](https://leetcode.com/tag/two-pointers/) |
| Sliding Window | variable/fixed, min window substring | [NeetCode](https://neetcode.io/roadmap) |
| String Pattern Matching | Rabin-Karp rolling hash, KMP prefix map (`k-map`/LPS), exact substring search | [CP Algorithms — Prefix Function](https://cp-algorithms.com/string/prefix-function.html) · [CP Algorithms — String Hashing](https://cp-algorithms.com/string/string-hashing.html) |
| Binary Trees | DFS pre/in/post, BFS level order, LCA, diameter | [NeetCode](https://neetcode.io/roadmap) · [VisuAlgo BST](https://visualgo.net/en/bst) |
| Binary Search Tree | insert/delete/validate, kth smallest, BST iterator | [LeetCode BST](https://leetcode.com/tag/binary-search-tree/) |
| Heaps | K largest/smallest, merge K sorted, median stream | [Python heapq](https://docs.python.org/3/library/heapq.html) |
| Tries | insert/search/startsWith, word search II | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Trie](https://leetcode.com/tag/trie/) |
| Graphs (BFS/DFS) | islands, connected components, topological sort | [NeetCode](https://neetcode.io/roadmap) · [VisuAlgo](https://visualgo.net/en/graphds) |
| Union-Find | Kruskal's MST, redundant connections, provinces | [CP Algorithms](https://cp-algorithms.com/data_structures/disjoint_set_union.html) |
| Backtracking | subsets, permutations, N-Queens, Sudoku solver | [NeetCode](https://neetcode.io/roadmap) · [LeetCode BT](https://leetcode.com/tag/backtracking/) |
| Greedy | intervals, gas station, jump game, task scheduler | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Greedy](https://leetcode.com/tag/greedy/) |

### Advanced

| Topic | Key Patterns | Resource |
|-------|-------------|----------|
| 1D DP | Fibonacci, house robber, coin change, word break | [NeetCode](https://neetcode.io/roadmap) · [LeetCode DP](https://leetcode.com/tag/dynamic-programming/) |
| 2D DP | edit distance, LCS, unique paths, maximal square | [NeetCode](https://neetcode.io/roadmap) · [CP Algorithms DP](https://cp-algorithms.com/dynamic_programming/) |
| Knapsack DP | 0/1 knapsack, unbounded, partition equal subset | [NeetCode](https://neetcode.io/roadmap) |
| DP on Trees | diameter, max path sum, rob houses III | [LeetCode DP](https://leetcode.com/tag/dynamic-programming/) |
| Dijkstra | network delay, cheapest flights K stops | [CP Algorithms](https://cp-algorithms.com/graph/dijkstra.html) |
| Bellman-Ford / Floyd | negative weights, all-pairs shortest path | [CP Algorithms](https://cp-algorithms.com/graph/bellman_ford.html) |
| Topological Sort | Kahn's algorithm, course schedule I & II | [CP Algorithms](https://cp-algorithms.com/graph/topological-sort.html) |
| Minimum Spanning Tree | Kruskal, Prim, point connections | [CP Algorithms Kruskal](https://cp-algorithms.com/graph/mst_kruskal.html) |
| Segment Trees | range sum/min/max queries, point/range updates | [CP Algorithms](https://cp-algorithms.com/data_structures/segment_tree.html) |
| Binary Indexed Tree | prefix sums, `update` + `query` in O(log n) | [CP Algorithms BIT](https://cp-algorithms.com/data_structures/fenwick.html) |
| Bit Manipulation | XOR tricks, power-of-2, counting bits, bitmask DP | [NeetCode](https://neetcode.io/roadmap) · [LeetCode Bit](https://leetcode.com/tag/bit-manipulation/) |

### MAANG Problem Sets

| Resource | What It Is | Link |
|----------|-----------|------|
| NeetCode 150 | Best curated 150 problems covering all patterns | https://neetcode.io/practice |
| Blind 75 | Original 75 problems shared by a Meta engineer | https://leetcode.com/discuss/general-discussion/460599 |
| LeetCode — Google | Questions tagged & filtered by Google | https://leetcode.com/company/google/ |
| LeetCode — Meta | Questions tagged & filtered by Meta | https://leetcode.com/company/meta/ |
| LeetCode — Amazon | Questions tagged & filtered by Amazon | https://leetcode.com/company/amazon/ |
| System Design Primer | GitHub repo with system design concepts & examples | https://github.com/donnemartin/system-design-primer |
| ByteByteGo | Free newsletter on system design | https://bytebytego.com |

---

## Tools & Environment Setup

```bash
# 1. Install uv (fast pip + venv replacement)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create project with uv
uv init python-mastery
cd python-mastery
uv add fastapi uvicorn sqlalchemy alembic pydantic-settings

# 3. Dev dependencies
uv add --dev pytest pytest-cov pytest-asyncio httpx mypy ruff pre-commit

# 4. Run your app
uv run uvicorn app.main:app --reload

# 5. Run tests
uv run pytest --cov=app --cov-report=html

# 6. Type check
uv run mypy app --strict

# 7. Lint & format
uv run ruff check . && uv run ruff format .
```

### Recommended pyproject.toml

```toml
[project]
name = "python-mastery"
version = "0.1.0"
requires-python = ">=3.12"

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "ANN", "S", "B", "A", "C4", "PT"]
ignore = ["ANN101"]

[tool.mypy]
python_version = "3.12"
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
addopts = "--cov=app --cov-report=term-missing"
```

### VS Code Settings (`.vscode/settings.json`)

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },
  "mypy-type-checker.args": ["--strict"]
}
```

---

## Study Schedule

```
Week 1–2   │ Python Basics + DSA Foundation (Arrays, Strings, HashMap)
Week 3–4   │ OOP, Iterators, Generators + DSA (Stack, Queue, Linked List)
Week 5–6   │ Decorators, Context Managers, Type Hints + DSA (Binary Search)
Week 7–8   │ Concurrency (Threading, Multiprocessing) + DSA (Binary Trees)
Week 9     │ asyncio deep dive + DSA (Heaps, Tries)
Week 10–11 │ Advanced (Metaclasses, Descriptors) + DSA (Graphs, Union-Find)
Week 12    │ CPython Internals + DSA (Backtracking, Greedy)
Week 13–14 │ Testing, Packaging, Design Patterns + DSA (1D & 2D DP)
Week 15–16 │ FastAPI Foundations + DSA (Knapsack, Dijkstra)
Week 17–18 │ FastAPI Advanced (Auth, DB, Deploy) + DSA (Segment Tree, BIT)
Week 19–22 │ DevOps Python + LeetCode company-filtered grind (NeetCode 150)
```

---

## Progress Tracker

Copy into a GitHub Issue and check off as you go:

### Python Basics
- [ ] Variables & Data Types
- [ ] Control Flow
- [ ] Functions & Scope
- [ ] Lists, Tuples, Sets, Dicts
- [ ] Strings
- [ ] File I/O & Pathlib
- [ ] Error Handling
- [ ] Modules & Packages

### Python Intermediate
- [ ] OOP — Classes & Dunder Methods
- [ ] Inheritance, MRO, ABC
- [ ] Dataclasses
- [ ] Iterators & Generators
- [ ] Decorators
- [ ] Context Managers
- [ ] functools & itertools
- [ ] Type Hints & mypy
- [ ] Threading & GIL
- [ ] Multiprocessing
- [ ] asyncio

### Python Advanced
- [ ] Descriptors
- [ ] Metaclasses
- [ ] CPython Bytecode (dis)
- [ ] Memory Management & gc
- [ ] Import System
- [ ] Profiling (cProfile, line_profiler)
- [ ] Design Patterns
- [ ] pytest & Mocking
- [ ] Packaging (pyproject.toml + uv)

### FastAPI
- [ ] First app + auto-docs
- [ ] Pydantic v2 models & validators
- [ ] Dependency Injection
- [ ] OAuth2 + JWT Auth
- [ ] Async routes & BackgroundTasks
- [ ] SQLAlchemy + Alembic
- [ ] Middleware & CORS
- [ ] WebSockets
- [ ] Testing (TestClient + AsyncClient)
- [ ] Docker deployment

### DevOps Python
- [ ] pdb debugging
- [ ] Structured logging (structlog)
- [ ] OpenTelemetry tracing
- [ ] subprocess automation
- [ ] Docker SDK
- [ ] Boto3 (AWS)
- [ ] GitHub Actions CI
- [ ] Prometheus metrics

### DSA
- [ ] Arrays & Sliding Window
- [ ] Two Pointers
- [ ] Hash Maps
- [ ] Stack (Monotonic)
- [ ] Linked Lists
- [ ] Binary Search
- [ ] Binary Trees
- [ ] Heaps
- [ ] Tries
- [ ] Graphs (BFS/DFS)
- [ ] Union-Find
- [ ] Backtracking
- [ ] Greedy
- [ ] 1D Dynamic Programming
- [ ] 2D Dynamic Programming
- [ ] Knapsack Patterns
- [ ] Dijkstra & Shortest Paths
- [ ] Topological Sort
- [ ] Segment Trees
- [ ] Bit Manipulation
- [ ] NeetCode 150 — complete

---

> Built for developers who take learning seriously. Every resource linked is free.
> Star this repo, fork it, and commit your practice files daily.
