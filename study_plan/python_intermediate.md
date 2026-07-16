# Phase 2 — Python Intermediate (Days 15–34)

> Track: `python_intermediate` · Outcome: OOP, decorators, itertools, typing, testing, regex, logging, dates, CLI

## Day Plan

| Day | Topic | Slug | Exercise direction |
|-----|-------|------|--------------------|
| 15 | OOP: classes, `__init__`, attrs | `day_15_oop_basics` | Bank account, inventory item |
| 16 | OOP: inheritance, `super()` | `day_16_inheritance` | Shape hierarchy, permission model |
| 17 | OOP: dunder methods | `day_17_dunders` | Custom container, money arithmetic |
| 18 | OOP: class/static methods | `day_18_class_methods` | Registry, factory, counter |
| 19 | `dataclasses` | `day_19_dataclasses` | Config DTO, order record |
| 20 | Protocols and ABCs | `day_20_protocols` | Plugin interface, storage backend |
| 21 | Decorators | `day_21_decorators` | Timer, retry, auth check |
| 22 | Context managers | `day_22_context_managers` | DB connection, timer, lock |
| 23 | `itertools` | `day_23_itertools` | Batch, sliding window, combos |
| 24 | Advanced typing | `day_24_typing` | `TypeVar`, `Protocol`, `Literal`, `Annotated` |
| 25 | `enum` and constants | `day_25_enums` | Status machines, flag sets |
| 26 | Regex | `day_26_regex` | Log parser, email validator |
| 27 | Dates and times | `day_27_datetime` | Scheduler, timezone converter |
| 28 | `collections` deep-dive | `day_28_collections` | Counters, deque, ordered dict |
| 29 | `functools` | `day_29_functools` | Caching, reduce, partials |
| 30 | Testing: `pytest` basics | `day_30_testing` | AAA pattern, fixtures, markers |
| 31 | Testing: mocking | `day_31_mocking` | `unittest.mock`, patch, side_effect |
| 32 | Logging | `day_32_logging` | Structured logs, handlers |
| 33 | CLI: `argparse` / `click` | `day_33_cli` | Multi-command CLI |
| 34 | Packaging and distribution | `day_34_packaging` | Wheel, publish flow |

---

## Concept Checklists

### Day 15 — OOP: Classes, `__init__`, Attributes (25)

**Prerequisites:** Day 03 (functions), Day 05 (tuple/NamedTuple records this replaces).
**Real-world use:** domain models — the objects that carry state and enforce their own invariants across a service.
**Production example (code.py):** a `BankAccount` domain model — encapsulated balance behind `@property` guards, `deposit`/`withdraw` methods that validate and raise on overdraft, and a `__repr__` safe for logs.
**Sources:** [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) · [Python Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `class` definition | `class Foo:` |
| 2 | `__init__` | `def __init__(self, x):` |
| 3 | Instance attributes | `self.x = x` |
| 4 | Class attributes | `count = 0` on class body |
| 5 | `self` parameter | First arg in instance methods |
| 6 | Instance methods | `def method(self):` |
| 7 | `__str__` / `__repr__` | String representations |
| 8 | Property `@property` | Computed attributes |
| 9 | Property setter | `@x.setter` |
| 10 | Private convention `_` | `_internal` |
| 11 | Name mangling `__` | `__private` → `_Class__private` |
| 12 | `isinstance()` / `type()` | Type checking |
| 13 | `hasattr()` / `getattr()` | Dynamic attribute access |
| 14 | `__slots__` | Memory optimization |
| 15 | Class docstrings | Document purpose, attrs |
| 16 | Type-annotated attrs | `self.name: str = name` |
| 17 | Equality: default is `is` | Override `__eq__` if needed |
| 18 | `__dict__` | Instance namespace |
| 19 | Anti-pattern: god class | Split responsibilities |
| 20 | Anti-pattern: mutable class attr | Shared state surprise |
| 21 | Industrial: bank account | Encapsulated state + validation |
| 22 | Industrial: inventory item | Property + computed fields |
| 23 | Property deleter | `@x.deleter` releases resources |
| 24 | `setattr()` / `delattr()` | Dynamic set/delete by name |
| 25 | Attribute lookup order | Instance `__dict__` shadows class attrs |

### Day 16 — Inheritance, `super()` (22)

**Prerequisites:** Day 15 (classes, attributes, methods).
**Real-world use:** modeling is-a hierarchies and sharing behavior — framework base classes, permission roles, and plugin bases.
**Production example (code.py):** a shape + permission hierarchy — a base `Shape` with an abstract `area()` and concrete subclasses, plus a role model where `Admin(User)` extends permissions through cooperative `super()`.
**Sources:** [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) · [Python Tutorial — Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Single inheritance | `class Child(Parent):` |
| 2 | `super().__init__()` | Call parent init |
| 3 | Method overriding | Redefine parent method |
| 4 | `super()` in methods | Extend parent behavior |
| 5 | `isinstance()` with hierarchy | True for parent classes |
| 6 | `issubclass()` | `issubclass(Child, Parent)` |
| 7 | Multiple inheritance | `class C(A, B):` |
| 8 | MRO | `C.__mro__`, C3 linearization |
| 9 | Diamond problem | MRO resolves it |
| 10 | Mixin classes | Small behavior add-ons |
| 11 | Abstract methods | `@abstractmethod` |
| 12 | Template method pattern | Parent calls abstract methods |
| 13 | Liskov substitution | Subtypes must be substitutable |
| 14 | Composition over inheritance | Has-a vs is-a |
| 15 | `__init_subclass__` | Hook on subclass creation |
| 16 | `type()` for class creation | Dynamic classes |
| 17 | Anti-pattern: deep hierarchy | Max 2-3 levels |
| 18 | Anti-pattern: override without super | Breaks parent logic |
| 19 | Industrial: shape hierarchy | Area/perimeter polymorphism |
| 20 | Industrial: permission model | Role inheritance |
| 21 | Cooperative multiple inheritance | `super()` walks the full MRO |
| 22 | `object` root class | Implicit base of every class |

### Day 17 — Dunder Methods (25)

**Prerequisites:** Day 15 (classes, `__repr__`), Day 16 (inheritance).
**Real-world use:** making custom types feel native — value objects, containers, and domain types that support `==`, ordering, `+`, `len()`, and iteration.
**Production example (code.py):** a `Money` value object — `__add__`/`__sub__` with currency checks, `__eq__`/`__hash__`, `@total_ordering`, and `__repr__`/`__format__`; plus a custom container implementing `__len__`/`__getitem__`/`__iter__`.
**Sources:** [Python Data Model](https://docs.python.org/3/reference/datamodel.html) · [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `__str__` / `__repr__` | Human / dev string |
| 2 | `__eq__` / `__ne__` | Equality comparison |
| 3 | `__hash__` | Hashability |
| 4 | `__lt__` / `__le__` / `__gt__` / `__ge__` | Ordering |
| 5 | `@total_ordering` | Auto-fill comparisons |
| 6 | `__add__` / `__radd__` | `+` operator |
| 7 | `__sub__` / `__mul__` | `-`, `*` operators |
| 8 | `__len__` | `len(obj)` |
| 9 | `__getitem__` / `__setitem__` | `obj[key]` |
| 10 | `__contains__` | `in` operator |
| 11 | `__iter__` / `__next__` | Iteration protocol |
| 12 | `__bool__` | Truthiness |
| 13 | `__call__` | `obj()` callable |
| 14 | `__enter__` / `__exit__` | Context manager |
| 15 | `__del__` | Destructor (avoid) |
| 16 | `__format__` | `format(obj, spec)` |
| 17 | `__new__` | Pre-init constructor |
| 18 | `__class_getitem__` | `MyClass[int]` syntax |
| 19 | Anti-pattern: mutable + `__hash__` | Hash must match `__eq__` |
| 20 | Anti-pattern: magic without `__repr__` | Always add repr |
| 21 | Industrial: money arithmetic | `__add__`, `__eq__`, `__repr__` |
| 22 | Industrial: custom container | `__len__`, `__getitem__`, `__iter__` |
| 23 | `__delitem__` | `del obj[key]` |
| 24 | In-place operators | `__iadd__`, `__imul__` |
| 25 | `__getattr__` / `__setattr__` | Attribute access interception |

### Day 18 — Class/Static Methods (22)

**Prerequisites:** Day 15 (classes, attributes), Day 16 (inheritance, `cls`).
**Real-world use:** alternative constructors, registries, and grouped pure helpers — the machinery behind factories and plugin registration.
**Production example (code.py):** a `Config` with `from_env()`/`from_file()` alternative constructors, a subclass auto-registry via `__init_subclass__`, and a class-level ID counter shared across instances.
**Sources:** [Real Python — Class & Static Methods](https://realpython.com/instance-class-and-static-methods-demystified/) · [docs — classmethod](https://docs.python.org/3/library/functions.html#classmethod)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `@classmethod` | `def method(cls):` |
| 2 | `@staticmethod` | `def method():` |
| 3 | Factory pattern | `cls(...)` in classmethod |
| 4 | Alternative constructors | `from_json()`, `from_dict()` |
| 5 | Class-level state | Counter, registry |
| 6 | `cls` vs `self` | Class vs instance reference |
| 7 | When static | No access to cls/self |
| 8 | Registry pattern | `cls._registry` in classmethod |
| 9 | Singleton (basic) | `_instance` classmethod |
| 10 | `__init_subclass__` | Auto-register subclasses |
| 11 | Method dispatch table | `classmethod` returning handler |
| 12 | Validation in factory | Raise before construction |
| 13 | Anti-pattern: static that uses state | Should be instance method |
| 14 | Anti-pattern: classmethod modifying instance | Wrong method type |
| 15 | Industrial: config factory | `Config.from_env()`, `.from_file()` |
| 16 | Industrial: ID generator | Classmethod with counter |
| 17 | `__new__` as factory | Pre-init construction |
| 18 | Inheritance + classmethod | `cls` is the subclass |
| 19 | Static utility grouping | Namespace for pure functions |
| 20 | Decorator stacking order | `@classmethod` + `@cache` |
| 21 | Access via instance or class | Both dispatch to the class-level function |
| 22 | `staticmethod` vs module function | Nest in class only for cohesion |

### Day 19 — Dataclasses (25)

**Prerequisites:** Day 15 (classes), Day 17 (dunders it generates), Day 05 (NamedTuple contrast).
**Real-world use:** boilerplate-free typed records — DTOs, config objects, and value objects with generated `__init__`/`__repr__`/`__eq__`.
**Production example (code.py):** an order record + frozen config DTO — `@dataclass(slots=True)` with `field(default_factory=...)`, `__post_init__` validation, a computed total via `@property`, and `asdict()` JSON serialization.
**Sources:** [Real Python — Data Classes](https://realpython.com/python-data-classes/) · [docs — dataclasses](https://docs.python.org/3/library/dataclasses.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `@dataclass` decorator | `@dataclass` |
| 2 | Field declarations | `name: str` |
| 3 | Default values | `count: int = 0` |
| 4 | `field()` | `field(default_factory=list)` |
| 5 | `__post_init__` | Validation after init |
| 6 | `frozen=True` | Immutable dataclass |
| 7 | `order=True` | Auto comparison methods |
| 8 | `kw_only=True` (3.10+) | Keyword-only fields |
| 9 | `slots=True` (3.10+) | Memory efficient |
| 10 | `repr=`, `eq=`, `hash=` | Control auto-generation |
| 11 | `asdict()` / `astuple()` | Serialization helpers |
| 12 | Inheritance in dataclasses | Parent + child fields |
| 13 | Mutable default pitfall | Must use `field()` |
| 14 | Computed fields | `@property` + `init=False` |
| 15 | Validation in `__post_init__` | `if x < 0: raise` |
| 16 | `InitVar` | Init-only variables |
| 17 | Dataclass vs NamedTuple | Mutable vs immutable |
| 18 | Dataclass vs dict | Typed structure |
| 19 | JSON serialization | `asdict()` → `json.dumps()` |
| 20 | Anti-pattern: mutable default | `list` → `field(default_factory=list)` |
| 21 | Industrial: config DTO | `@dataclass(frozen=True)` |
| 22 | Industrial: order record | Computed total, validation |
| 23 | `dataclasses.replace()` | Copy with field overrides |
| 24 | `fields()` introspection | Iterate declared fields + metadata |
| 25 | Per-field control | `field(compare=, repr=, metadata=)` |

### Day 20 — Protocols and ABCs (23)

**Prerequisites:** Day 15 (classes), Day 16 (inheritance, abstract methods).
**Real-world use:** defining interfaces — pluggable backends and dependency boundaries via structural (Protocol) or nominal (ABC) typing.
**Production example (code.py):** a storage backend interface — a `Protocol` with `save()`/`load()` implemented by file and in-memory backends, plus an `ABC` plugin base with `@abstractmethod` that refuses instantiation until fully implemented.
**Sources:** [docs — abc](https://docs.python.org/3/library/abc.html) · [docs — typing.Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `ABC` class | `from abc import ABC` |
| 2 | `@abstractmethod` | Must override |
| 3 | Cannot instantiate ABC | Raises TypeError |
| 4 | `@abstractproperty` (deprecated) | Use `@property` + `@abstractmethod` |
| 5 | `typing.Protocol` | Structural subtyping |
| 6 | `runtime_checkable` | `isinstance()` with Protocol |
| 7 | Protocol vs ABC | Structural vs nominal |
| 8 | Duck typing formalized | Protocol captures it |
| 9 | Interface segregation | Small protocols |
| 10 | `__subclasshook__` | Custom isinstance logic |
| 11 | `register()` virtual subclass | `ABC.register(cls)` |
| 12 | Mixin + ABC | Partial implementation |
| 13 | `Callable` protocol | `def __call__(self):` |
| 14 | `Iterable` / `Iterator` | Protocol examples |
| 15 | `Sized` / `Container` | `__len__`, `__contains__` |
| 16 | Anti-pattern: deep ABC tree | Keep flat |
| 17 | Anti-pattern: ABC for one impl | Premature abstraction |
| 18 | Industrial: storage backend | `Protocol` with `save()`/`load()` |
| 19 | Industrial: plugin interface | Discoverable implementations |
| 20 | Testing with protocols | Mock satisfies protocol |
| 21 | `collections.abc` bases | Inherit `Sequence`, `Mapping`, `Iterator` |
| 22 | Abstract classmethod/staticmethod | Stack with `@abstractmethod` |
| 23 | Protocol with attributes | Declare instance vars / properties |

### Day 21 — Decorators (25)

**Prerequisites:** Day 03 (first-class functions, closures), Day 18 (built-in decorators).
**Real-world use:** cross-cutting concerns without touching business logic — timing, retries, auth, caching, and route registration.
**Production example (code.py):** a decorator toolkit — a `@retry(times=3)` parametric decorator with backoff, a `@timed` logger, a `@requires_role` auth guard (all using `functools.wraps`), plus a route-style registration decorator.
**Sources:** [Real Python — Decorators](https://realpython.com/primer-on-python-decorators/) · [PEP 318 — Decorators](https://peps.python.org/pep-0318/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Function as first-class | Pass/return functions |
| 2 | Closure recap | Inner captures outer |
| 3 | Simple decorator | `def deco(fn): def wrapper(...):` |
| 4 | `@decorator` syntax | Sugar for `fn = deco(fn)` |
| 5 | `functools.wraps` | Preserve `__name__`, `__doc__` |
| 6 | Decorator with arguments | `def deco(arg): def wrapper(fn):` |
| 7 | Class-based decorator | `__init__` + `__call__` |
| 8 | Stacking decorators | Applied bottom-up |
| 9 | `@property` as decorator | Built-in example |
| 10 | `@staticmethod` / `@classmethod` | Built-in decorators |
| 11 | `@functools.cache` | Memoization |
| 12 | `@functools.lru_cache` | Bounded cache |
| 13 | Timer decorator | Measure execution time |
| 14 | Retry decorator | Backoff on exception |
| 15 | Auth check decorator | Permission guard |
| 16 | Logging decorator | Log entry/exit |
| 17 | Type checking decorator | Validate at runtime |
| 18 | Decorator on class | `@dataclass` model |
| 19 | `__wrapped__` attribute | Access original |
| 20 | Anti-pattern: no `wraps` | Lost metadata |
| 21 | Anti-pattern: decorator side effects | Keep pure |
| 22 | Industrial: framework decorators | Flask `@app.route` style |
| 23 | Registration decorator | Populate a handler registry |
| 24 | Optional-argument decorator | Works with or without `()` |
| 25 | Decorating async functions | `async def wrapper` + `await` |

### Day 22 — Context Managers (22)

**Prerequisites:** Day 17 (`__enter__`/`__exit__` dunders), Day 10 (exceptions, cleanup), Day 21 (decorators for `@contextmanager`).
**Real-world use:** guaranteed setup/teardown — connections, transactions, locks, temp resources, and timers that clean up even on error.
**Production example (code.py):** a transaction context manager — commit on success, rollback in `__exit__` on exception; plus a `@contextmanager` timer and an `ExitStack` opening a dynamic number of resources.
**Sources:** [Real Python — with Statement](https://realpython.com/python-with-statement/) · [docs — contextlib](https://docs.python.org/3/library/contextlib.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `with` statement | `with open(f) as fh:` |
| 2 | `__enter__` / `__exit__` | Protocol methods |
| 3 | Exception in `__exit__` | `exc_type, exc_val, tb` |
| 4 | Suppressing exceptions | Return `True` from `__exit__` |
| 5 | `@contextmanager` | `from contextlib import contextmanager` |
| 6 | `yield` in contextmanager | Before = enter, after = exit |
| 7 | Multiple `with` | `with A() as a, B() as b:` |
| 8 | `ExitStack` | Dynamic number of managers |
| 9 | `suppress()` | `with suppress(FileNotFoundError):` |
| 10 | `redirect_stdout` / `redirect_stderr` | Capture output |
| 11 | `closing()` | Wrap objects with `.close()` |
| 12 | `nullcontext()` | Optional context manager |
| 13 | Async context managers | `async with` |
| 14 | Reentrant vs reusable | Can you nest the same CM? |
| 15 | Timer context manager | Measure block duration |
| 16 | DB connection CM | Commit/rollback pattern |
| 17 | Temp directory CM | Auto-cleanup |
| 18 | Anti-pattern: manual close | Use `with` instead |
| 19 | Anti-pattern: no cleanup on error | `finally` or CM |
| 20 | Industrial: transaction manager | Commit on success, rollback on fail |
| 21 | `ContextDecorator` | Use a CM as a `@decorator` |
| 22 | `__enter__` return value | Bound to the `as` target |

### Day 23 — itertools (23)

**Prerequisites:** Day 13 (comprehensions, generators), Day 12 (built-in iterables).
**Real-world use:** memory-efficient stream processing — batching, windowing, grouping, and combinatorics over large or infinite sequences.
**Production example (code.py):** a streaming ETL helper set — `batched()` chunking for bulk inserts, `groupby()` aggregation over sorted records, `islice()` pagination, and `pairwise()` sliding-window deltas.
**Sources:** [Real Python — itertools](https://realpython.com/python-itertools/) · [docs — itertools](https://docs.python.org/3/library/itertools.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `chain()` | Flatten iterables |
| 2 | `chain.from_iterable()` | Flatten nested |
| 3 | `islice()` | Slice any iterator |
| 4 | `count()` / `cycle()` / `repeat()` | Infinite iterators |
| 5 | `takewhile()` / `dropwhile()` | Conditional slicing |
| 6 | `groupby()` | Group sorted data |
| 7 | `accumulate()` | Running totals |
| 8 | `product()` | Cartesian product |
| 9 | `permutations()` | Order matters |
| 10 | `combinations()` | Order doesn't matter |
| 11 | `combinations_with_replacement()` | With repeats |
| 12 | `starmap()` | Unpack args |
| 13 | `compress()` | Selector mask |
| 14 | `filterfalse()` | Inverse filter |
| 15 | `zip_longest()` | Fill missing |
| 16 | `tee()` | Clone iterator |
| 17 | `pairwise()` (3.10+) | Adjacent pairs |
| 18 | `batched()` (3.12+) | Fixed-size chunks |
| 19 | Lazy evaluation | Memory efficient |
| 20 | Anti-pattern: `list()` everything | Stay lazy |
| 21 | Industrial: batch processing | `batched()` / `islice()` |
| 22 | Industrial: sliding window | `pairwise()` / custom |
| 23 | itertools recipes | `grouper`, `flatten`, `unique_everseen` |

### Day 24 — Advanced Typing (26)

**Prerequisites:** Day 01 (type hints), Day 15/19 (classes, dataclasses), Day 20 (Protocol).
**Real-world use:** type-safe generic APIs — reusable containers, decorator typing, and precise contracts mypy can verify in CI.
**Production example (code.py):** a generic `Repository[T]` with a bound `TypeVar`, a `ParamSpec` decorator that preserves signatures, a `TypedDict` config, `Literal` modes, and `@overload`ed accessors.
**Sources:** [Real Python — Type Checking](https://realpython.com/python-type-checking/) · [docs — typing](https://docs.python.org/3/library/typing.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `TypeVar` | `T = TypeVar("T")` |
| 2 | `TypeVar` bound | `TypeVar("T", bound=int)` |
| 3 | `Generic[T]` | `class Box(Generic[T]):` |
| 4 | `TypeAlias` (3.10+) | `type Vector = list[float]` |
| 5 | `Union` / `X | Y` (3.10+) | `int | str` |
| 6 | `Optional[X]` | `X | None` |
| 7 | `Literal` | `Literal["r", "w"]` |
| 8 | `Annotated` | `Annotated[int, Gt(0)]` |
| 9 | `Final` | Cannot reassign |
| 10 | `ClassVar` | Class-level only |
| 11 | `TypedDict` | `class Config(TypedDict):` |
| 12 | `Callable` | `Callable[[int], str]` |
| 13 | `ParamSpec` | Decorator typing |
| 14 | `Concatenate` | Prepend params |
| 15 | `Protocol` (recap) | Structural typing |
| 16 | `@overload` | Multiple signatures |
| 17 | `TYPE_CHECKING` | Import-only for type hints |
| 18 | `cast()` | Override type checker |
| 19 | `reveal_type()` | Debug type inference |
| 20 | Anti-pattern: `Any` everywhere | Defeats purpose |
| 21 | Anti-pattern: no return type | Always annotate |
| 22 | Industrial: generic repository | `Repository[T]` pattern |
| 23 | `NewType` | Distinct type wrapper |
| 24 | `Self` type (3.11+) | Return-`self` annotations |
| 25 | `NoReturn` / `Never` | Functions that never return |
| 26 | `TypeGuard` | Custom type-narrowing helpers |

### Day 25 — Enum and Constants (23)

**Prerequisites:** Day 15 (classes), Day 02 (`match`/`case` over enums).
**Real-world use:** replacing magic strings/ints with a fixed, type-safe, self-documenting set — statuses, roles, and bitwise feature flags.
**Production example (code.py):** an order `Status(StrEnum)` state machine with allowed transitions, an `IntFlag` permission set combined with `|`/`&`, and JSON serialization via `.value`.
**Sources:** [docs — enum](https://docs.python.org/3/library/enum.html) · [Real Python — Enums](https://realpython.com/python-enum/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `Enum` class | `class Color(Enum): RED = 1` |
| 2 | `auto()` | Auto-assign values |
| 3 | Accessing members | `Color.RED`, `Color["RED"]`, `Color(1)` |
| 4 | `.name` / `.value` | String name, assigned value |
| 5 | Iteration | `for c in Color:` |
| 6 | `IntEnum` | Integer comparison |
| 7 | `StrEnum` (3.11+) | String comparison |
| 8 | `Flag` / `IntFlag` | Bitwise combinations |
| 9 | `@unique` | No duplicate values |
| 10 | Methods on Enum | `def describe(self):` |
| 11 | Enum as dict key | Hashable |
| 12 | Enum in match/case | Pattern matching |
| 13 | Enum vs constants | Type safety |
| 14 | Enum serialization | `.value` for JSON |
| 15 | `_missing_()` hook | Custom lookup |
| 16 | `_generate_next_value_()` | Custom auto values |
| 17 | Functional API | `Color = Enum("Color", ["R","G","B"])` |
| 18 | Anti-pattern: plain strings | Use Enum for fixed sets |
| 19 | Industrial: status machine | State transitions with Enum |
| 20 | Industrial: feature flags | Flag combinations |
| 21 | `__members__` mapping | All members incl. aliases |
| 22 | Enum aliases | Duplicate value becomes an alias |
| 23 | Identity comparison | Members compared with `is` |

### Day 26 — Regex (27)

**Prerequisites:** Day 08 (strings, raw strings), Day 09 (file/log lines).
**Real-world use:** extracting and validating structured text — log parsing, input validation, tokenizing, and search/replace at scale.
**Production example (code.py):** a log-line parser + validators — a compiled pattern with named groups extracting timestamp/level/message via `finditer`, plus email/phone validators using anchors and `fullmatch`.
**Sources:** [docs — re](https://docs.python.org/3/library/re.html) · [Real Python — Regex](https://realpython.com/regex-python/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `re.search()` | First match |
| 2 | `re.match()` | Start of string |
| 3 | `re.fullmatch()` | Entire string |
| 4 | `re.findall()` | All matches |
| 5 | `re.finditer()` | Lazy match objects |
| 6 | `re.sub()` | Replace |
| 7 | `re.split()` | Split on pattern |
| 8 | `re.compile()` | Pre-compiled pattern |
| 9 | Groups `()` | `m.group(1)` |
| 10 | Named groups | `(?P<name>...)` |
| 11 | Character classes | `[a-z]`, `\d`, `\w`, `\s` |
| 12 | Quantifiers | `*`, `+`, `?`, `{n,m}` |
| 13 | Greedy vs lazy | `*?`, `+?` |
| 14 | Anchors | `^`, `$`, `\b` |
| 15 | Alternation | `a|b` |
| 16 | Lookahead / lookbehind | `(?=...)`, `(?<=...)` |
| 17 | Flags | `re.IGNORECASE`, `re.MULTILINE` |
| 18 | Raw strings | `r"\d+"` |
| 19 | Backreferences | `\1`, `(?P=name)` |
| 20 | Anti-pattern: regex for HTML | Use parser instead |
| 21 | Industrial: log parser | Extract fields from lines |
| 22 | Industrial: input validation | Email, phone, ID formats |
| 23 | Non-capturing group | `(?:...)` |
| 24 | Match object methods | `.group()`, `.groups()`, `.groupdict()`, `.span()` |
| 25 | `re.escape()` | Escape literal text in patterns |
| 26 | Verbose mode | `re.VERBOSE` for readable patterns |
| 27 | `re.subn()` | Replace and return a count |

### Day 27 — Dates and Times (26)

**Prerequisites:** Day 01 (types), Day 08 (string formatting), Day 26 (parsing patterns).
**Real-world use:** correct time handling — scheduling, timezone conversion, durations, and timestamps that survive DST and regional differences.
**Production example (code.py):** a timezone-aware scheduler + converter — parse ISO strings with `fromisoformat`, convert between zones via `zoneinfo`, compute next-run with `timedelta`, and always store aware UTC.
**Sources:** [docs — datetime](https://docs.python.org/3/library/datetime.html) · [Real Python — datetime](https://realpython.com/python-datetime/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `date` | `date(2024, 1, 15)` |
| 2 | `time` | `time(14, 30, 0)` |
| 3 | `datetime` | `datetime(2024, 1, 15, 14, 30)` |
| 4 | `datetime.now()` / `.utcnow()` | Current time |
| 5 | `timedelta` | `timedelta(days=7)` |
| 6 | Arithmetic | `dt + timedelta(hours=3)` |
| 7 | `strftime()` | Format to string |
| 8 | `strptime()` | Parse from string |
| 9 | `.isoformat()` | ISO 8601 string |
| 10 | `.fromisoformat()` | Parse ISO 8601 |
| 11 | Timezone with `zoneinfo` | `ZoneInfo("UTC")` |
| 12 | Aware vs naive | `.tzinfo` present? |
| 13 | `.astimezone()` | Convert timezone |
| 14 | `date.today()` | Current date |
| 15 | `.weekday()` / `.isoweekday()` | Day of week |
| 16 | `.replace()` | Modify fields |
| 17 | Comparison | `dt1 < dt2` |
| 18 | `calendar` module | Month/year helpers |
| 19 | Timestamps | `.timestamp()`, `.fromtimestamp()` |
| 20 | Anti-pattern: naive UTC | Always use aware |
| 21 | Anti-pattern: custom parsing | Use `fromisoformat()` |
| 22 | Industrial: scheduler, converter | Timezone-aware scheduling |
| 23 | `datetime.combine()` | Merge `date` + `time` |
| 24 | `timedelta.total_seconds()` | Duration as seconds |
| 25 | Aware `now()` | `datetime.now(ZoneInfo(...))` over `utcnow()` |
| 26 | `isocalendar()` | ISO year / week / weekday |

### Day 28 — Collections Deep-dive (24)

**Prerequisites:** Day 06 (dicts), Day 05 (namedtuple), Day 04 (lists).
**Real-world use:** the right specialized container for the job — frequency counts, O(1) queues, layered config, and grouping.
**Production example (code.py):** a log analytics module — `Counter.most_common()` for top endpoints, a `deque(maxlen=)` bounded event buffer, `defaultdict(list)` grouping, and `ChainMap` layered config resolution.
**Sources:** [docs — collections](https://docs.python.org/3/library/collections.html) · [Real Python — collections](https://realpython.com/python-collections-module/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `Counter` | `Counter(iterable)` |
| 2 | `Counter.most_common()` | Top-N elements |
| 3 | Counter arithmetic | `c1 + c2`, `c1 - c2` |
| 4 | `defaultdict` | `defaultdict(list)` |
| 5 | `defaultdict` factory | `int`, `list`, `set`, `lambda` |
| 6 | `OrderedDict` | Ordered (pre-3.7 compat) |
| 7 | `deque` | `deque(maxlen=n)` |
| 8 | `deque.appendleft()` / `popleft()` | O(1) both ends |
| 9 | `deque.rotate()` | Circular rotation |
| 10 | `ChainMap` | `ChainMap(child, parent)` |
| 11 | `ChainMap` for config | Layered settings |
| 12 | `UserDict` / `UserList` / `UserString` | Subclassable wrappers |
| 13 | `namedtuple` (recap) | Lightweight record |
| 14 | `Counter` as multiset | Frequency bag |
| 15 | `deque` as bounded buffer | `maxlen` auto-evicts |
| 16 | `defaultdict` group-by | `dd[key].append(val)` |
| 17 | Anti-pattern: manual counting | Use `Counter` |
| 18 | Anti-pattern: manual grouping | Use `defaultdict(list)` |
| 19 | Industrial: frequency analysis | `Counter` for text |
| 20 | Industrial: LRU with deque | Bounded history |
| 21 | `Counter.elements()` | Expand counts back to an iterator |
| 22 | `Counter.total()` (3.10+) | Sum of all counts |
| 23 | `Counter.update()` / `subtract()` | Combine / remove counts |
| 24 | `deque.extendleft()` | Bulk left-append (reverses order) |

### Day 29 — functools (23)

**Prerequisites:** Day 21 (decorators), Day 03 (functions), Day 17 (`total_ordering`).
**Real-world use:** higher-order utilities — memoization for expensive calls, partial application for callbacks, and type-based dispatch.
**Production example (code.py):** a memoized data-access layer — `@lru_cache` wrapping an expensive lookup with `cache_info()` monitoring, `@cached_property` for lazy fields, `partial` pre-configured callbacks, and `@singledispatch` serialization.
**Sources:** [Real Python — functools](https://realpython.com/python-functools/) · [docs — functools](https://docs.python.org/3/library/functools.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `functools.reduce()` | `reduce(fn, iterable, init)` |
| 2 | `functools.partial()` | Pre-fill arguments |
| 3 | `functools.wraps()` | Decorator metadata |
| 4 | `functools.cache` | Unbounded memoization |
| 5 | `functools.lru_cache` | Bounded cache |
| 6 | `cache_info()` | Cache hit/miss stats |
| 7 | `functools.total_ordering` | Auto comparisons |
| 8 | `functools.singledispatch` | Type-based dispatch |
| 9 | `singledispatch` register | `@f.register(int)` |
| 10 | `functools.cached_property` | One-time computed |
| 11 | `partial` vs `lambda` | `partial` is picklable |
| 12 | `reduce` patterns | Sum, product, flatten |
| 13 | `reduce` vs comprehension | When to use which |
| 14 | `lru_cache` with unhashable | Convert args |
| 15 | `lru_cache(maxsize=None)` | Same as `cache` |
| 16 | `cmp_to_key()` | Legacy comparison adapter |
| 17 | Anti-pattern: cache mutable | Returns same reference |
| 18 | Anti-pattern: reduce for sum | Use `sum()` |
| 19 | Industrial: memoized API calls | `lru_cache` wrapper |
| 20 | Industrial: partial callbacks | Pre-configured handlers |
| 21 | `singledispatchmethod` | Type dispatch on methods |
| 22 | `partialmethod` | `partial` applied to methods |
| 23 | `update_wrapper()` | Manual metadata copy |

### Day 30 — Testing: pytest Basics (26)

**Prerequisites:** Day 03 (functions), Day 10 (exceptions), Day 11 (imports).
**Real-world use:** the professional testing baseline — fast, isolated, table-driven tests that gate every merge in CI.
**Production example (code.py):** a test suite for a domain module — AAA-structured tests, `parametrize` tables, `pytest.raises` for error paths, fixtures with `yield` teardown, `tmp_path`, and `--cov` in CI.
**Sources:** [Real Python — pytest](https://realpython.com/pytest-python-testing/) · [docs — pytest](https://docs.pytest.org/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Test file naming | `test_*.py` / `*_test.py` |
| 2 | Test function naming | `def test_something():` |
| 3 | `assert` | `assert result == expected` |
| 4 | `pytest.raises` | `with pytest.raises(ValueError):` |
| 5 | `pytest.approx` | Float comparison |
| 6 | `@pytest.fixture` | Setup/teardown |
| 7 | Fixture scope | `function`, `module`, `session` |
| 8 | `@pytest.mark.parametrize` | Table-driven tests |
| 9 | `@pytest.mark.skip` / `skipif` | Conditional skip |
| 10 | `@pytest.mark.xfail` | Expected failure |
| 11 | `conftest.py` | Shared fixtures |
| 12 | `tmp_path` fixture | Temp directory |
| 13 | `capsys` | Capture stdout |
| 14 | `monkeypatch` | Patch env, attrs |
| 15 | AAA pattern | Arrange → Act → Assert |
| 16 | Test isolation | Each test independent |
| 17 | `pytest.ini` / `pyproject.toml` | Configuration |
| 18 | Running tests | `pytest -v`, `pytest -k "name"` |
| 19 | Coverage | `pytest --cov` |
| 20 | Anti-pattern: test depends on order | Isolate state |
| 21 | Anti-pattern: too many asserts | One concern per test |
| 22 | Industrial: CI test suite | `pytest` in pipeline |
| 23 | Yield fixtures | Setup/teardown around `yield` |
| 24 | `autouse=True` fixtures | Applied without being requested |
| 25 | Parametrized fixtures | `@fixture(params=[...])` |
| 26 | `caplog` | Capture emitted log records |

### Day 31 — Testing: Mocking (24)

**Prerequisites:** Day 30 (pytest), Day 21 (patching wraps functions), Day 11 (import paths).
**Real-world use:** isolating the unit under test from slow or external dependencies — APIs, clocks, filesystems, and databases.
**Production example (code.py):** tests for an API client — `@patch` the HTTP call where it is imported, configure `return_value`/`side_effect` for retries, assert with `assert_called_once_with`, and `mock_open` the file layer.
**Sources:** [docs — unittest.mock](https://docs.python.org/3/library/unittest.mock.html) · [Real Python — pytest](https://realpython.com/pytest-python-testing/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `unittest.mock.Mock` | `m = Mock()` |
| 2 | `MagicMock` | Auto dunders |
| 3 | `mock.return_value` | Configure return |
| 4 | `mock.side_effect` | Exception or callable |
| 5 | `mock.assert_called_once_with` | Verify calls |
| 6 | `mock.call_args` | Inspect arguments |
| 7 | `@patch` decorator | Replace target |
| 8 | `patch` as context manager | `with patch(...):` |
| 9 | `patch.object()` | Patch attribute |
| 10 | `patch.dict()` | Patch dictionary |
| 11 | Where to patch | Patch where imported |
| 12 | `spec=True` | Restrict mock API |
| 13 | `autospec=True` | Full signature check |
| 14 | `PropertyMock` | Mock `@property` |
| 15 | `AsyncMock` | Async function mock |
| 16 | `call` helper | Build expected call list |
| 17 | Anti-pattern: mock everything | Test nothing |
| 18 | Anti-pattern: implementation test | Test behavior, not internals |
| 19 | Industrial: mock API client | External service isolation |
| 20 | Industrial: mock file system | `tmp_path` + mock |
| 21 | `mock_open()` | Mock the builtin `open()` |
| 22 | `create_autospec()` | Spec'd mock factory |
| 23 | Call assertions | `call_count`, `assert_not_called()` |
| 24 | `reset_mock()` | Clear recorded calls |

### Day 32 — Logging (23)

**Prerequisites:** Day 10 (exceptions), Day 11 (modules, `__name__`), Day 30 (asserting on logs).
**Real-world use:** observability — structured, leveled, routed logs that make production systems debuggable.
**Production example (code.py):** a logging setup module — named loggers per module, `dictConfig` wiring a JSON formatter, a `RotatingFileHandler` plus console handler, `logger.exception()` on failures, and `extra=` context.
**Sources:** [Real Python — Logging](https://realpython.com/python-logging/) · [docs — logging](https://docs.python.org/3/library/logging.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `logging.getLogger()` | `logger = getLogger(__name__)` |
| 2 | Log levels | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| 3 | `logger.info()` etc. | Level methods |
| 4 | `basicConfig()` | Quick setup |
| 5 | Handlers | `StreamHandler`, `FileHandler` |
| 6 | Formatters | `Formatter("%(levelname)s %(message)s")` |
| 7 | Logger hierarchy | Dot-separated names |
| 8 | `logger.exception()` | Log with traceback |
| 9 | `extra=` dict | Additional context |
| 10 | `RotatingFileHandler` | Size-based rotation |
| 11 | `TimedRotatingFileHandler` | Time-based rotation |
| 12 | `logging.config.dictConfig` | Dict-based config |
| 13 | Structured logging | JSON format |
| 14 | `logging.Filter` | Custom filtering |
| 15 | `LoggerAdapter` | Add context |
| 16 | `NullHandler` | Library default |
| 17 | Lazy formatting | `logger.info("x=%s", x)` |
| 18 | Anti-pattern: `print()` in prod | Use logging |
| 19 | Anti-pattern: root logger | Use named loggers |
| 20 | Industrial: structured JSON logs | Machine-parseable |
| 21 | Logger vs handler levels | `setLevel()` on both |
| 22 | Propagation | Records bubble up; `propagate=False` |
| 23 | `QueueHandler` / `QueueListener` | Non-blocking, concurrency-safe logging |

### Day 33 — CLI: argparse / click (24)

**Prerequisites:** Day 03 (functions), Day 11 (packages, `__main__`), Day 19 (config DTOs).
**Real-world use:** operable tools — every service ships CLIs for admin, migration, and batch jobs with clear args and help.
**Production example (code.py):** a multi-command CLI — `argparse` subcommands (or `click.group`) with typed options, `choices`, defaults merged from a config file, a `--verbose` count, and proper exit codes.
**Sources:** [docs — argparse](https://docs.python.org/3/library/argparse.html) · [Click docs](https://click.palletsprojects.com/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `argparse.ArgumentParser` | `parser = ArgumentParser()` |
| 2 | Positional arguments | `parser.add_argument("name")` |
| 3 | Optional arguments | `parser.add_argument("--verbose")` |
| 4 | `type=` | Type conversion |
| 5 | `choices=` | Restricted values |
| 6 | `default=` | Default value |
| 7 | `nargs=` | `"*"`, `"+"`, `"?"` |
| 8 | `action=` | `"store_true"`, `"count"` |
| 9 | Subcommands | `add_subparsers()` |
| 10 | `parse_args()` | Returns namespace |
| 11 | Mutually exclusive | `add_mutually_exclusive_group()` |
| 12 | `click.command()` | Decorator-based CLI |
| 13 | `click.option()` | `@click.option("--name")` |
| 14 | `click.argument()` | Positional |
| 15 | `click.group()` | Multi-command |
| 16 | `click.echo()` | Cross-platform output |
| 17 | `click.prompt()` | Interactive input |
| 18 | Anti-pattern: no help text | Always add help |
| 19 | Industrial: multi-command CLI | `click.group` + subcommands |
| 20 | Industrial: config + CLI merge | Defaults from file, override CLI |
| 21 | Argument metadata | `help=`, `metavar=`, `dest=` |
| 22 | click types & validation | `type=click.Path`, `IntRange` |
| 23 | click context | `@click.pass_context`, `ctx.obj` |
| 24 | Exit codes | `sys.exit()` / `ctx.exit()` |

### Day 34 — Packaging and Distribution (24)

**Prerequisites:** Day 11 (packages), Day 14 (tooling, `pyproject.toml`), Day 33 (console entry points).
**Real-world use:** shipping code others can install — internal libraries and CLIs published to PyPI or a private index with reproducible builds.
**Production example (code.py):** a publishable package — `pyproject.toml` with metadata, `dependencies`, and a `[project.scripts]` entry point; `src/` layout; `python -m build` producing wheel + sdist; and a TestPyPI `twine`/`uv publish` dry run.
**Sources:** [packaging.python.org — Packaging Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) · [pyproject.toml spec](https://packaging.python.org/en/latest/specifications/pyproject-toml/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `pyproject.toml` layout | `[project]`, `[build-system]` |
| 2 | `[project]` metadata | name, version, description |
| 3 | `[project.scripts]` | Console entry points |
| 4 | `[build-system]` | `requires`, `build-backend` |
| 5 | Build backends | setuptools, hatchling, flit |
| 6 | `python -m build` | Create sdist + wheel |
| 7 | Wheel format | `.whl` = zip of installed files |
| 8 | sdist | Source distribution |
| 9 | `MANIFEST.in` | Include non-Python files |
| 10 | `twine upload` | Publish to PyPI |
| 11 | TestPyPI | `--repository testpypi` |
| 12 | Versioning | SemVer, `__version__` |
| 13 | `[project.optional-dependencies]` | `pip install pkg[dev]` |
| 14 | `uv publish` | Modern publish |
| 15 | `README.md` in package | `readme = "README.md"` |
| 16 | License | `license = {text = "MIT"}` |
| 17 | Classifiers | Trove classifiers |
| 18 | Namespace packages | Multiple packages, one namespace |
| 19 | Anti-pattern: setup.py only | Use pyproject.toml |
| 20 | Industrial: publish workflow | Build → test → publish |
| 21 | `dependencies` / `requires-python` | Declare runtime deps + version floor |
| 22 | `src/` layout | Recommended package structure |
| 23 | `importlib.metadata.version()` | Read installed version at runtime |
| 24 | `[project.entry-points]` | Plugin discovery |

---

## Sunday Labs (Phase 2)

| Lab | After | Build |
|-----|-------|-------|
| 04 | Days 15–19 | OOP model: bank system with dataclasses + factory |
| 05 | Days 20–23 | Plugin framework: Protocol + decorators + itertools pipeline |
| 06 | Days 24–27 | Typed CLI tool: enums, regex parser, date formatting |
| 07 | Days 28–34 | Tested package: Counter analytics, logging, pytest suite, publish |
