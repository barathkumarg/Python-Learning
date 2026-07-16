# Phase 4 — Advanced Python (Days 51–70)

> Track: `python_advanced` · Outcome: metaprogramming, descriptors, C extensions, design patterns, security

## Day Plan

| Day | Topic | Slug | Exercise direction |
|-----|-------|------|--------------------|
| 51 | Descriptors | `day_51_descriptors` | Validated attrs, lazy props |
| 52 | Metaclasses | `day_52_metaclasses` | Auto-registry, schema validation |
| 53 | `__init_subclass__` & class hooks | `day_53_class_hooks` | Plugin discovery |
| 54 | Dynamic attributes | `day_54_dynamic_attrs` | `__getattr__`, proxy objects |
| 55 | Abstract syntax trees | `day_55_ast` | Code analysis, linting |
| 56 | `inspect` module | `day_56_inspect` | Signature analysis, frame walking |
| 57 | C extensions / ctypes / cffi | `day_57_c_extensions` | Wrap a C library |
| 58 | Design patterns: Creational | `day_58_creational` | Factory, Builder, Singleton |
| 59 | Design patterns: Structural | `day_59_structural` | Adapter, Decorator, Proxy |
| 60 | Design patterns: Behavioral | `day_60_behavioral` | Strategy, Observer, Command |
| 61 | Dependency injection | `day_61_di` | Constructor injection, container |
| 62 | SOLID principles | `day_62_solid` | Refactoring exercises |
| 63 | Clean code practices | `day_63_clean_code` | Naming, functions, comments |
| 64 | Security: input validation | `day_64_security_input` | Injection, sanitization |
| 65 | Security: crypto & hashing | `day_65_security_crypto` | hashlib, secrets, bcrypt |
| 66 | Security: auth patterns | `day_66_security_auth` | JWT, API keys, RBAC |
| 67 | Database: SQLite + SQLAlchemy | `day_67_database` | ORM basics, queries |
| 68 | Database: migrations & patterns | `day_68_db_patterns` | Alembic, repository pattern |
| 69 | Networking: sockets | `day_69_sockets` | TCP client/server |
| 70 | Advanced project | `day_70_advanced_project` | Plugin system + DB + auth |

---

## Concept Checklists

### Day 51 — Descriptors (23)

**Prerequisites:** Day 15 (classes, `__dict__`), Day 17 (properties), Day 21 (class/static methods).
**Real-world use:** reusable, validated, typed attributes — the machinery behind ORM columns, settings fields, and framework field types.
**Production example (code.py):** a reusable typed-field library — `Positive`, `NonEmpty`, `Typed` data descriptors with `__set_name__` that validate on assignment and back a small config/ORM-style model class.
**Sources:** [Real Python — Descriptors](https://realpython.com/python-descriptors/) · [Data Model — Implementing Descriptors](https://docs.python.org/3/reference/datamodel.html#descriptors)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Descriptor protocol | `__get__`, `__set__`, `__delete__` |
| 2 | Data descriptor | Has `__set__` or `__delete__` |
| 3 | Non-data descriptor | Only `__get__` |
| 4 | Descriptor priority | Data > instance > non-data |
| 5 | `__set_name__` | `def __set_name__(self, owner, name):` |
| 6 | Validated attribute | Type/range check in `__set__` |
| 7 | Lazy property descriptor | Compute once, cache |
| 8 | `property` is a descriptor | Built-in example |
| 9 | Functions as descriptors | Method binding |
| 10 | `classmethod` / `staticmethod` | Descriptor implementations |
| 11 | Instance storage | `obj.__dict__[self.name]` |
| 12 | Owner class access | `__get__(None, owner)` |
| 13 | Reusable validators | `Positive()`, `NonEmpty()` |
| 14 | Descriptor + `__slots__` | Compatible patterns |
| 15 | `__delete__` usage | Attribute removal |
| 16 | Anti-pattern: descriptor on instance | Must be on class |
| 17 | Anti-pattern: no `__set_name__` | Manual name tracking |
| 18 | Industrial: ORM field | SQLAlchemy Column concept |
| 19 | Industrial: validated config | Typed fields with checks |
| 20 | Testing descriptors | Access via class and instance |
| 21 | `functools.cached_property` | Stdlib lazy non-data descriptor |
| 22 | Instance storage strategies | Per-instance dict vs `WeakKeyDictionary` (avoid leaks) |
| 23 | Descriptor invocation | Dispatched by `type.__getattribute__` |

### Day 52 — Metaclasses (23)

**Prerequisites:** Day 51 (descriptors), Day 18 (inheritance/MRO), Day 19 (ABCs).
**Real-world use:** framework-level control of class creation — ORM model registries, plugin auto-registration, API schema enforcement.
**Production example (code.py):** a model-registry metaclass — validate required class attributes at creation, auto-register each subclass into a `name → class` registry, and inject a generated `__repr__`, mirroring an ORM base.
**Sources:** [Real Python — Metaclasses](https://realpython.com/python-metaclasses/) · [Data Model — Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `type` as metaclass | `type(name, bases, dict)` |
| 2 | `class Meta(type):` | Custom metaclass |
| 3 | `__new__` in metaclass | Create class object |
| 4 | `__init__` in metaclass | Initialize class |
| 5 | `__prepare__` | Custom namespace |
| 6 | `metaclass=Meta` | Apply metaclass |
| 7 | Auto-registry pattern | Track all subclasses |
| 8 | Schema validation | Check required attrs |
| 9 | Method injection | Add methods dynamically |
| 10 | Abstract enforcement | Require implementation |
| 11 | Singleton metaclass | Only one instance |
| 12 | `__init_subclass__` alternative | Simpler than metaclass |
| 13 | `__class_getitem__` | Generic syntax |
| 14 | Metaclass conflict | Multiple metaclasses |
| 15 | `abc.ABCMeta` | Built-in metaclass |
| 16 | `__instancecheck__` / `__subclasscheck__` | Custom isinstance |
| 17 | Anti-pattern: metaclass for simple | Use decorator instead |
| 18 | Anti-pattern: complex metaclass | Hard to debug |
| 19 | Industrial: ORM model metaclass | Django Model concept |
| 20 | Industrial: API schema | Auto-validate fields |
| 21 | Metaclass `__call__` | Intercept `Cls(...)` instantiation |
| 22 | Most-derived metaclass rule | Bases' metaclasses must be compatible |
| 23 | Class kwargs to metaclass | `class C(metaclass=M, x=1)` → `__new__(..., **kw)` |

### Day 53 — `__init_subclass__` & Class Hooks (23)

**Prerequisites:** Day 52 (metaclasses), Day 51 (`__set_name__`), Day 19 (ABCs).
**Real-world use:** lightweight class customization without a metaclass — plugin discovery, serializer registries, subclass validation.
**Production example (code.py):** a plugin framework — a base class whose `__init_subclass__` validates required methods and registers each plugin by a `name=` class keyword into a discovery registry.
**Sources:** [Data Model — `__init_subclass__`](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__) · [PEP 487 — Simpler customisation of class creation](https://peps.python.org/pep-0487/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `__init_subclass__` | `def __init_subclass__(cls, **kw):` |
| 2 | Keyword arguments | `class Child(Parent, key="val"):` |
| 3 | Auto-registration | `_registry[cls.name] = cls` |
| 4 | Validation on subclass | Check required attrs |
| 5 | Class decorators vs hooks | Decorator = explicit |
| 6 | `__set_name__` (recap) | Descriptor naming |
| 7 | `__init_subclass__` + `super()` | Chain to parent |
| 8 | Plugin discovery | Auto-collect implementations |
| 9 | Abstract enforcement | Check before registration |
| 10 | Configuration inheritance | Merge parent + child config |
| 11 | `__class_getitem__` | `MyClass[int]` support |
| 12 | `__subclasses__()` | List direct subclasses |
| 13 | Class factory functions | `def make_class(config):` |
| 14 | `types.new_class()` | Programmatic class creation |
| 15 | Anti-pattern: metaclass when hook works | Prefer simpler |
| 16 | Anti-pattern: mutable class state | Thread safety |
| 17 | Industrial: plugin system | Auto-discover plugins |
| 18 | Industrial: serializer registry | Format → handler mapping |
| 19 | Testing class hooks | Subclass in test |
| 20 | Combine with Protocol | Type-safe plugins |
| 21 | Implicit classmethod | No `@classmethod` needed on `__init_subclass__` |
| 22 | Consume kwargs before `super()` | Pop keys or `object.__init_subclass__` errors |
| 23 | PEP 487 mechanism | Hooks replace many metaclass use cases |

### Day 54 — Dynamic Attributes (23)

**Prerequisites:** Day 15 (classes, `__dict__`), Day 51 (descriptors), Day 17 (properties).
**Real-world use:** proxies, lazy loaders, and dot-access wrappers — REST client SDKs, config objects, ORM row proxies.
**Production example (code.py):** a lazy API-client proxy — `__getattr__` builds resource paths on demand (`client.users.list()`), caches resolved attributes in `__dict__`, and raises `AttributeError` correctly.
**Sources:** [Data Model — Customizing Attribute Access](https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access) · [Built-in Functions — getattr / setattr](https://docs.python.org/3/library/functions.html#getattr)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `__getattr__` | Called when attr missing |
| 2 | `__getattribute__` | Called on every access |
| 3 | `__setattr__` | Called on every assignment |
| 4 | `__delattr__` | Called on deletion |
| 5 | `getattr()` / `setattr()` / `delattr()` | Built-in functions |
| 6 | `hasattr()` | Calls `getattr`, catches |
| 7 | `__dict__` manipulation | Direct namespace access |
| 8 | `vars(obj)` | Same as `__dict__` |
| 9 | Proxy pattern | Delegate to wrapped object |
| 10 | Lazy loading proxy | Load on first access |
| 11 | Attribute caching | Store in `__dict__` |
| 12 | `__getattr__` vs `__getattribute__` | Fallback vs always |
| 13 | Infinite recursion pitfall | `__getattribute__` calls self |
| 14 | `super().__getattribute__()` | Safe access in override |
| 15 | `object.__setattr__()` | Safe set in override |
| 16 | Dynamic API wrappers | REST client proxy |
| 17 | Anti-pattern: `__getattribute__` overuse | Performance hit |
| 18 | Anti-pattern: no `AttributeError` | Break `hasattr` |
| 19 | Industrial: API proxy | `client.users.list()` |
| 20 | Industrial: config dot-access | `config.db.host` |
| 21 | `__dir__` override | Customize `dir(obj)` for dynamic attrs |
| 22 | `__slots__` interaction | No `__dict__`, `__getattr__` still fires |
| 23 | Descriptor vs `__getattr__` precedence | Data descriptors resolve first |

### Day 55 — Abstract Syntax Trees (24)

**Prerequisites:** Day 11 (modules/imports), Day 03 (functions), Day 10 (errors).
**Real-world use:** code analysis and generation — custom linters, codemods, safe config evaluation, framework auto-wiring.
**Production example (code.py):** a custom lint rule — an `ast.NodeVisitor` that flags functions exceeding a nesting/branch threshold and non-PEP 8 names, reporting file/line diagnostics.
**Sources:** [ast — Abstract Syntax Trees](https://docs.python.org/3/library/ast.html) · [Green Tree Snakes — the AST guide](https://greentreesnakes.readthedocs.io/en/latest/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `ast.parse()` | `ast.parse(source)` |
| 2 | `ast.dump()` | Pretty-print tree |
| 3 | Node types | `FunctionDef`, `Assign`, `Call` |
| 4 | `ast.walk()` | Flat iteration |
| 5 | `ast.NodeVisitor` | `visit_FunctionDef()` |
| 6 | `ast.NodeTransformer` | Modify tree |
| 7 | `compile()` / `exec()` | Execute modified AST |
| 8 | `ast.literal_eval()` | Safe eval for literals |
| 9 | Source analysis | Count functions, classes |
| 10 | Complexity metrics | Nesting depth, branches |
| 11 | Code generation | Build AST → `compile` |
| 12 | Custom linter | Check naming conventions |
| 13 | Decorator detection | Find decorated functions |
| 14 | Import analysis | Extract imports |
| 15 | `ast.fix_missing_locations()` | Required for transforms |
| 16 | `ast.unparse()` (3.9+) | AST back to source |
| 17 | Anti-pattern: `eval()` | Security risk |
| 18 | Anti-pattern: string manipulation | Use AST for code |
| 19 | Industrial: code linter | Custom rule enforcement |
| 20 | Industrial: code generation | Template → AST → source |
| 21 | `generic_visit()` | Recurse into child nodes in a visitor |
| 22 | `ast.Constant` node | Unified literals (3.8+, replaces `Num`/`Str`) |
| 23 | Node positions | `lineno`, `col_offset`, `end_lineno` for diagnostics |
| 24 | `ast.parse` modes | `mode="exec"`, `"eval"`, `"single"` |

### Day 56 — inspect Module (24)

**Prerequisites:** Day 03 (functions/signatures), Day 25 (decorators), Day 55 (introspection mindset).
**Real-world use:** signature-driven tooling — auto-documentation, DI containers, CLI generators, decorator validation.
**Production example (code.py):** a signature-driven dispatcher — read a callable's `Signature`, `bind()` and validate incoming kwargs, and auto-generate a usage/help string from parameters and the docstring.
**Sources:** [inspect — Inspect live objects](https://docs.python.org/3/library/inspect.html) · [PEP 362 — Function Signature Object](https://peps.python.org/pep-0362/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `inspect.signature()` | `sig = signature(fn)` |
| 2 | `Parameter` objects | `.name`, `.default`, `.kind` |
| 3 | `inspect.getsource()` | Get source code |
| 4 | `inspect.getfile()` | Get file path |
| 5 | `inspect.getmembers()` | List members with filter |
| 6 | `inspect.isfunction()` | Type predicates |
| 7 | `inspect.isclass()` | Class check |
| 8 | `inspect.stack()` | Call stack frames |
| 9 | `inspect.currentframe()` | Current frame |
| 10 | Frame objects | `f_locals`, `f_globals`, `f_code` |
| 11 | `inspect.getcallargs()` | Resolve call arguments |
| 12 | `inspect.getdoc()` | Cleaned docstring |
| 13 | `inspect.getmro()` | Method resolution order |
| 14 | `inspect.iscoroutinefunction()` | Async detection |
| 15 | `inspect.isgeneratorfunction()` | Generator detection |
| 16 | Anti-pattern: frame manipulation | Fragile, slow |
| 17 | Anti-pattern: source at runtime | May not be available |
| 18 | Industrial: auto-documentation | Signature extraction |
| 19 | Industrial: decorator introspection | Validate signatures |
| 20 | Industrial: debug tools | Frame-based logging |
| 21 | `Signature.bind()` | Map args to parameters, validate calls |
| 22 | `inspect.unwrap()` | Peel `functools.wraps` layers |
| 23 | `inspect.get_annotations()` | Safe annotation access (3.10+) |
| 24 | `Parameter.empty` sentinel | Detect missing default/annotation |

### Day 57 — C Extensions / ctypes / cffi (23)

**Prerequisites:** Day 11 (modules), Day 10 (error handling), Day 09 (bytes/binary I/O).
**Real-world use:** bridging Python to native code — wrapping system libraries and accelerating CPU-bound hot paths.
**Production example (code.py):** a `ctypes` wrapper for a shared C library — declare `argtypes`/`restype`, marshal a `Structure`, check return codes, and expose a safe, typed Python API.
**Sources:** [ctypes — Foreign function library](https://docs.python.org/3/library/ctypes.html) · [CFFI — C Foreign Function Interface](https://cffi.readthedocs.io/en/stable/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Why C extensions | Performance, existing libs |
| 2 | `ctypes` module | `ctypes.CDLL("lib.so")` |
| 3 | `ctypes` types | `c_int`, `c_char_p`, `c_double` |
| 4 | Function signatures | `.argtypes`, `.restype` |
| 5 | Passing arrays | `(c_int * n)()` |
| 6 | Structures | `class S(Structure):` |
| 7 | `byref()` | Pass by reference |
| 8 | `cffi` overview | `ffi.cdef()`, `ffi.verify()` |
| 9 | `cffi` inline mode | ABI vs API mode |
| 10 | Shared library loading | Platform differences |
| 11 | Error handling | Check return codes |
| 12 | Memory management | Who owns the memory? |
| 13 | Callback functions | Python → C → Python |
| 14 | `ctypes.util.find_library()` | Locate libraries |
| 15 | `cython` overview | Compiled Python |
| 16 | `pybind11` overview | C++ bindings |
| 17 | Anti-pattern: ctypes for complex | Use cffi/pybind11 |
| 18 | Anti-pattern: no error check | Segfault risk |
| 19 | Industrial: wrap system lib | OpenSSL, zlib |
| 20 | Industrial: performance hot path | C for inner loop |
| 21 | `POINTER()` / `.contents` | Pointer types and dereferencing |
| 22 | Python C API basics | `PyObject`, reference counting |
| 23 | GIL and native code | Release the GIL for CPU-bound C sections |

### Day 58 — Design Patterns: Creational (23)

**Prerequisites:** Day 19 (ABCs), Day 21 (classmethods), Day 03 (first-class functions).
**Real-world use:** decoupling construction from use — connection factories, config builders, and object pools in service code.
**Production example (code.py):** a config-driven object factory — a registry mapping type strings to constructors with a fluent builder, producing configured service clients (e.g., cache/DB backends).
**Sources:** [Real Python — Factory Method](https://realpython.com/factory-method-python/) · [Refactoring Guru — Creational Patterns](https://refactoring.guru/design-patterns/creational-patterns)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Factory Method | `def create(type):` |
| 2 | Abstract Factory | Family of related objects |
| 3 | Builder | Step-by-step construction |
| 4 | Builder fluent API | Method chaining |
| 5 | Singleton | `_instance` class variable |
| 6 | Singleton via module | Module = natural singleton |
| 7 | Prototype | `copy.deepcopy()` |
| 8 | Object Pool | Reuse expensive objects |
| 9 | `__new__` for singleton | Override construction |
| 10 | Metaclass singleton | `type.__call__` |
| 11 | Factory registry | Dict of constructors |
| 12 | Config-driven factory | Type string → class |
| 13 | Lazy initialization | Create on first use |
| 14 | Python-specific: module globals | Simple singleton |
| 15 | Python-specific: `__init_subclass__` | Auto-register |
| 16 | Anti-pattern: complex factory | YAGNI |
| 17 | Anti-pattern: singleton state | Testing difficulty |
| 18 | Industrial: connection factory | DB connection creation |
| 19 | Industrial: config builder | Fluent configuration |
| 20 | When to use which | Decision guide |
| 21 | Monostate / Borg | Shared state alternative to Singleton |
| 22 | `functools.partial` factory | Pre-bind constructor arguments |
| 23 | Abstract product via `abc.ABC` | Enforce a product interface |

### Day 59 — Design Patterns: Structural (22)

**Prerequisites:** Day 58 (creational patterns), Day 18 (inheritance), Day 54 (dynamic attrs for proxy).
**Real-world use:** composing and adapting objects — normalizing third-party APIs, caching proxies, and memory-efficient object graphs.
**Production example (code.py):** a caching adapter/proxy — wrap a third-party client behind a uniform interface, delegate via `__getattr__`, and cache idempotent reads with invalidation.
**Sources:** [Refactoring Guru — Structural Patterns](https://refactoring.guru/design-patterns/structural-patterns) · [Data Model — Special method names](https://docs.python.org/3/reference/datamodel.html#special-method-names)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Adapter | Wrap incompatible interface |
| 2 | Object adapter | Composition-based |
| 3 | Class adapter | Inheritance-based |
| 4 | Decorator pattern | Wrap to add behavior |
| 5 | Python decorator vs pattern | Both are valid |
| 6 | Proxy | Control access |
| 7 | Lazy proxy | Load on first access |
| 8 | Protection proxy | Access control |
| 9 | Facade | Simplified interface |
| 10 | Composite | Tree structure |
| 11 | Bridge | Abstraction + implementation |
| 12 | Flyweight | Share common state |
| 13 | `__slots__` as flyweight | Memory optimization |
| 14 | Mixin pattern | Multiple inheritance add-on |
| 15 | Python-specific: duck typing | No adapter needed sometimes |
| 16 | Python-specific: `__getattr__` | Proxy via dynamic attrs |
| 17 | Anti-pattern: unnecessary wrapper | Direct call is fine |
| 18 | Anti-pattern: deep composition | Hard to debug |
| 19 | Industrial: API adapter | Normalize third-party APIs |
| 20 | Industrial: caching proxy | Cache + delegate |
| 21 | `weakref.proxy` | Lightweight proxy without a strong ref |
| 22 | `functools.wraps` in decorator | Preserve wrapped metadata |

### Day 60 — Design Patterns: Behavioral (24)

**Prerequisites:** Day 03 (first-class functions), Day 22 (iterators), Day 25 (callables/decorators).
**Real-world use:** flexible control flow — event systems, rule engines, request pipelines, and undoable commands.
**Production example (code.py):** an event-driven rule engine — an observer registry dispatches events to pluggable strategy handlers resolved from a registry, with a chain-of-responsibility pipeline.
**Sources:** [Refactoring Guru — Behavioral Patterns](https://refactoring.guru/design-patterns/behavioral-patterns) · [Python Docs — Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Strategy | Pluggable algorithms |
| 2 | Strategy with functions | First-class functions |
| 3 | Observer | Event notification |
| 4 | Observer with callbacks | `callbacks: list[Callable]` |
| 5 | Command | Encapsulate request |
| 6 | Command with undo | `execute()` / `undo()` |
| 7 | Template Method | Override steps |
| 8 | Iterator | Custom `__iter__` / `__next__` |
| 9 | Chain of Responsibility | Handler pipeline |
| 10 | State | State-dependent behavior |
| 11 | Mediator | Centralized communication |
| 12 | Memento | Save/restore state |
| 13 | Visitor | Double dispatch |
| 14 | Python-specific: `match/case` | State + strategy |
| 15 | Python-specific: generators | Iterator pattern |
| 16 | Python-specific: context managers | Template method |
| 17 | Anti-pattern: god class | Split with strategy |
| 18 | Anti-pattern: tight coupling | Use observer |
| 19 | Industrial: event system | Observer + callbacks |
| 20 | Industrial: pipeline handler | Chain of responsibility |
| 21 | Industrial: rule engine | Strategy + registry |
| 22 | Combining patterns | Strategy + factory |
| 23 | `functools.singledispatch` | Pythonic visitor / double dispatch |
| 24 | `enum.Enum` for State | Enumerate states cleanly |

### Day 61 — Dependency Injection (22)

**Prerequisites:** Day 58 (factories), Day 19 (ABCs/Protocol), Day 15 (composition).
**Real-world use:** testable, decoupled services — swap real dependencies for fakes, and wire everything in one composition root.
**Production example (code.py):** a service wired by constructor injection against `Protocol` interfaces, with a small IoC container resolving a repository + logger, and mocks injected in tests.
**Sources:** [Real Python — Dependency Injection](https://realpython.com/python-dependency-injection/) · [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Constructor injection | `def __init__(self, dep):` |
| 2 | Method injection | `def process(self, dep):` |
| 3 | Interface segregation | Small protocols |
| 4 | Dependency inversion | Depend on abstractions |
| 5 | IoC container concept | Resolve dependencies |
| 6 | Manual DI | Wire in composition root |
| 7 | `inject` library | `@inject` decorator |
| 8 | Factory injection | Inject factory function |
| 9 | Scoped dependencies | Request/session scope |
| 10 | Testing with DI | Inject mocks |
| 11 | Configuration injection | Settings as dependency |
| 12 | Service locator (anti-pattern) | Hidden dependencies |
| 13 | Python-specific: module DI | Import-time wiring |
| 14 | Python-specific: Protocol | Type-safe injection |
| 15 | Anti-pattern: `new` in constructor | Hard to test |
| 16 | Anti-pattern: global state | Hidden coupling |
| 17 | Industrial: repository pattern | Inject storage |
| 18 | Industrial: service layer | Inject dependencies |
| 19 | Industrial: FastAPI DI | `Depends()` |
| 20 | Composition root | Single wiring point |
| 21 | Lifetime scopes | Singleton vs transient vs scoped instances |
| 22 | Anti-pattern: over-injection | Too many constructor deps → SRP smell |

### Day 62 — SOLID Principles (22)

**Prerequisites:** Day 61 (DI), Day 19 (ABCs/Protocol), Day 18 (inheritance/MRO).
**Real-world use:** maintainable OO design — the principles behind extensible, testable service layers that survive change.
**Production example (code.py):** refactor a "god" service class into SRP-compliant collaborators wired via DIP (Protocol + injection), extensible by OCP strategy — a before/after in one module.
**Sources:** [Real Python — SOLID Principles](https://realpython.com/solid-principles-python/) · [Architecture Patterns with Python (Percival & Gregory)](https://www.cosmicpython.com/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Single Responsibility (SRP) | One reason to change |
| 2 | SRP example | Separate logger from processor |
| 3 | Open/Closed (OCP) | Open for extension, closed for modification |
| 4 | OCP with Protocol | New implementations, same interface |
| 5 | Liskov Substitution (LSP) | Subtypes must be substitutable |
| 6 | LSP violations | Square vs Rectangle |
| 7 | Interface Segregation (ISP) | Small, focused interfaces |
| 8 | ISP with Protocol | Multiple small protocols |
| 9 | Dependency Inversion (DIP) | Depend on abstractions |
| 10 | DIP with injection | Constructor injection |
| 11 | Refactoring to SRP | Extract class |
| 12 | Refactoring to OCP | Strategy pattern |
| 13 | Refactoring to LSP | Fix hierarchy |
| 14 | Refactoring to ISP | Split interface |
| 15 | Refactoring to DIP | Inject dependencies |
| 16 | Python-specific: duck typing | Natural ISP |
| 17 | Python-specific: protocols | DIP without ABC |
| 18 | Anti-pattern: god class | Violates SRP |
| 19 | Anti-pattern: isinstance chains | Violates OCP |
| 20 | Industrial: service refactoring | Apply all five |
| 21 | Law of Demeter | Talk to immediate collaborators only |
| 22 | Composition over inheritance | Favor for OCP/LSP flexibility |

### Day 63 — Clean Code Practices (22)

**Prerequisites:** Day 03 (functions), Day 62 (SOLID), Day 10 (error handling).
**Real-world use:** readable, reviewable code — the naming, function-size, and comment discipline every code review enforces.
**Production example (code.py):** a refactoring module — take a smelly function (magic numbers, deep nesting, poor names) and produce a clean version with guard clauses, named constants, and docstrings, side by side.
**Sources:** [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/) · [Real Python — Python Code Quality](https://realpython.com/python-code-quality/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Meaningful names | Intention-revealing |
| 2 | Naming conventions | PEP 8 compliance |
| 3 | Small functions | Do one thing |
| 4 | Function arguments | Max 3-4, use objects |
| 5 | No side effects | Pure when possible |
| 6 | DRY principle | Don't repeat yourself |
| 7 | KISS principle | Keep it simple |
| 8 | YAGNI principle | Don't build unused features |
| 9 | Comments: why, not what | Self-documenting code |
| 10 | Docstrings | Google/NumPy style |
| 11 | Error handling | Specific exceptions |
| 12 | Guard clauses | Reduce nesting |
| 13 | Type hints | Document contracts |
| 14 | Immutability | Prefer immutable data |
| 15 | Composition over inheritance | Flexible design |
| 16 | Code smells | Long method, god class |
| 17 | Refactoring techniques | Extract, rename, move |
| 18 | Anti-pattern: magic numbers | Use named constants |
| 19 | Anti-pattern: dead code | Remove unused |
| 20 | Industrial: code review checklist | Systematic quality |
| 21 | Command-Query Separation | Methods either do or return, not both |
| 22 | Cyclomatic complexity | Measure with `ruff`/`radon`, keep it low |

### Day 64 — Security: Input Validation (22)

**Prerequisites:** Day 08 (strings), Day 09 (paths), Day 31 (typing/validation).
**Real-world use:** the first line of defense — every external input is hostile until validated; injection is the top web risk.
**Production example (code.py):** an input-sanitization pipeline — validate type/range/length against an allowlist, escape HTML, quote shell args, and reject path traversal, returning structured validation errors.
**Sources:** [OWASP — Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) · [Bandit — Security linter](https://bandit.readthedocs.io/en/latest/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Never trust input | Validate everything |
| 2 | Type validation | `isinstance()`, type hints |
| 3 | Range validation | Min/max bounds |
| 4 | Length validation | String/collection limits |
| 5 | Allowlist vs denylist | Prefer allowlist |
| 6 | SQL injection | Parameterized queries |
| 7 | Command injection | `subprocess` list args |
| 8 | Path traversal | Validate, resolve paths |
| 9 | XSS prevention | Escape HTML output |
| 10 | SSRF prevention | Validate URLs |
| 11 | Regex DoS (ReDoS) | Avoid catastrophic backtracking |
| 12 | `html.escape()` | HTML entity encoding |
| 13 | `shlex.quote()` | Shell escaping |
| 14 | `urllib.parse` | URL parsing/validation |
| 15 | JSON schema validation | `jsonschema` library |
| 16 | `pydantic` validation | Model-based |
| 17 | Anti-pattern: `eval()` / `exec()` | Code injection |
| 18 | Anti-pattern: format string injection | `f"...{user_input}"` in SQL |
| 19 | Industrial: input sanitizer | Clean + validate pipeline |
| 20 | Industrial: API request validation | Schema-based |
| 21 | Unsafe deserialization | Never `pickle.loads` untrusted data |
| 22 | XML attacks | Billion laughs / XXE — use `defusedxml` |

### Day 65 — Security: Crypto & Hashing (22)

**Prerequisites:** Day 64 (security mindset), Day 08 (bytes/encoding), Day 10 (errors).
**Real-world use:** protecting secrets and data — password storage, token generation, integrity checks, and encryption at rest.
**Production example (code.py):** a credential + token toolkit — hash passwords with `argon2`/`bcrypt` + per-user salt, generate API keys with `secrets`, verify with `compare_digest`, and encrypt a blob with Fernet.
**Sources:** [hashlib — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html) · [secrets — Generate secure tokens](https://docs.python.org/3/library/secrets.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `hashlib` | `hashlib.sha256(data).hexdigest()` |
| 2 | Hash algorithms | SHA-256, SHA-3, BLAKE2 |
| 3 | Password hashing | `bcrypt`, `argon2` |
| 4 | `secrets` module | `secrets.token_hex()` |
| 5 | `secrets.token_urlsafe()` | URL-safe tokens |
| 6 | `secrets.compare_digest()` | Timing-safe comparison |
| 7 | Salt concept | Unique per password |
| 8 | HMAC | `hmac.new(key, msg, "sha256")` |
| 9 | `os.urandom()` | Cryptographic randomness |
| 10 | Symmetric encryption | `cryptography.fernet` |
| 11 | Key derivation | PBKDF2, scrypt |
| 12 | Fernet encrypt/decrypt | `Fernet(key).encrypt(data)` |
| 13 | Never roll your own crypto | Use established libraries |
| 14 | Hash vs encryption | One-way vs reversible |
| 15 | Digital signatures concept | Verify integrity |
| 16 | Anti-pattern: MD5/SHA1 | Broken for security |
| 17 | Anti-pattern: plain text passwords | Always hash |
| 18 | Anti-pattern: `random` for security | Use `secrets` |
| 19 | Industrial: API key generation | `secrets.token_urlsafe` |
| 20 | Industrial: file integrity | SHA-256 checksums |
| 21 | AEAD / authenticated encryption | AES-GCM — don't use raw modes |
| 22 | Nonce/IV uniqueness | Never reuse an IV with the same key |

### Day 66 — Security: Auth Patterns (22)

**Prerequisites:** Day 65 (hashing/tokens), Day 06 (dicts for claims), Day 61 (DI for middleware).
**Real-world use:** controlling who can do what — JWT sessions, API keys, and RBAC across services.
**Production example (code.py):** an auth middleware — issue and verify JWTs with expiry, hash-and-store API keys, and enforce RBAC permissions via a decorator that injects the current user.
**Sources:** [PyJWT — Documentation](https://pyjwt.readthedocs.io/en/stable/) · [OWASP — Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Authentication vs authorization | Who vs what permission |
| 2 | Password storage | Hash + salt |
| 3 | JWT structure | Header.Payload.Signature |
| 4 | JWT creation | `jwt.encode(payload, secret)` |
| 5 | JWT verification | `jwt.decode(token, secret)` |
| 6 | JWT expiration | `exp` claim |
| 7 | Refresh tokens | Short access + long refresh |
| 8 | API keys | `secrets.token_urlsafe()` |
| 9 | API key storage | Hash the key, store hash |
| 10 | RBAC | Role-based access control |
| 11 | Permission checking | Decorator or middleware |
| 12 | Session management | Server-side sessions |
| 13 | OAuth2 flow overview | Authorization code grant |
| 14 | CORS basics | Cross-origin requests |
| 15 | Rate limiting | Token bucket, sliding window |
| 16 | Anti-pattern: JWT in URL | Use headers |
| 17 | Anti-pattern: no expiration | Tokens live forever |
| 18 | Anti-pattern: symmetric JWT in distributed | Use asymmetric |
| 19 | Industrial: auth middleware | Check + decode + inject user |
| 20 | Industrial: RBAC system | Permission hierarchy |
| 21 | Token revocation | `jti` + blocklist for logout |
| 22 | Secure cookie flags | `HttpOnly`, `Secure`, `SameSite` |

### Day 67 — Database: SQLite + SQLAlchemy (24)

**Prerequisites:** Day 09 (files/I/O), Day 05 (row DTOs), Day 10 (errors/transactions).
**Real-world use:** durable state — parameterized SQL and ORM models back nearly every backend service.
**Production example (code.py):** a repository over SQLite — parameterized `sqlite3` CRUD plus an equivalent SQLAlchemy 2.0 typed model (`Mapped`, `mapped_column`) with sessions, filtering, and transaction handling.
**Sources:** [sqlite3 — DB-API 2.0 interface](https://docs.python.org/3/library/sqlite3.html) · [SQLAlchemy — ORM Documentation](https://docs.sqlalchemy.org/en/20/orm/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `sqlite3.connect()` | `conn = sqlite3.connect("db.sqlite")` |
| 2 | Cursor execution | `cur.execute(sql, params)` |
| 3 | Parameterized queries | `?` placeholders |
| 4 | `fetchone()` / `fetchall()` | Read results |
| 5 | `Row` factory | `conn.row_factory = sqlite3.Row` |
| 6 | Transaction commit/rollback | `conn.commit()` |
| 7 | Context manager | `with conn:` auto-commit |
| 8 | SQLAlchemy engine | `create_engine(url)` |
| 9 | SQLAlchemy Session | `Session(bind=engine)` |
| 10 | Declarative models | `class User(Base):` |
| 11 | Column types | `Column(Integer)`, `Column(String)` |
| 12 | Relationships | `relationship()`, `ForeignKey` |
| 13 | CRUD operations | `add()`, `query()`, `delete()` |
| 14 | Filtering | `.filter()`, `.filter_by()` |
| 15 | `session.commit()` | Persist changes |
| 16 | `session.rollback()` | Undo changes |
| 17 | SQLAlchemy 2.0 style | `select()`, `Session.execute()` |
| 18 | Type annotations | `Mapped[int]`, `mapped_column()` |
| 19 | Anti-pattern: string SQL | Always parameterize |
| 20 | Anti-pattern: no index | Slow queries |
| 21 | Industrial: repository pattern | Abstract DB access |
| 22 | Industrial: connection pooling | SQLAlchemy pool |
| 23 | `executemany()` | Batch parameterized inserts |
| 24 | `sessionmaker` | Session factory bound to engine |

### Day 68 — Database: Migrations & Patterns (22)

**Prerequisites:** Day 67 (SQLAlchemy/SQLite), Day 61 (repository via DI), Day 47 (testing).
**Real-world use:** evolving schemas safely and keeping data access clean — migrations, repositories, and N+1 avoidance in production.
**Production example (code.py):** an Alembic migration flow plus a repository layer — autogenerate an upgrade/downgrade, seed data, and expose a repository that avoids N+1 with eager loading; tested on in-memory SQLite.
**Sources:** [Alembic — Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) · [Architecture Patterns with Python — Repository](https://www.cosmicpython.com/book/chapter_02_repository.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Migration concept | Schema versioning |
| 2 | Alembic setup | `alembic init` |
| 3 | Auto-generate migration | `alembic revision --autogenerate` |
| 4 | `upgrade()` / `downgrade()` | Apply/revert |
| 5 | `alembic upgrade head` | Apply all |
| 6 | Migration history | `alembic history` |
| 7 | Repository pattern | Abstract data access |
| 8 | Unit of Work | Transaction boundary |
| 9 | Data mapper vs active record | SQLAlchemy vs Django ORM |
| 10 | DTO pattern | Separate DB model from API |
| 11 | Seeding data | Initial/test data |
| 12 | Database testing | In-memory SQLite |
| 13 | Fixture factories | `factory_boy` |
| 14 | Query optimization | Eager loading, N+1 |
| 15 | N+1 problem | `joinedload()`, `selectinload()` |
| 16 | Soft delete | `is_deleted` flag |
| 17 | Anti-pattern: no migrations | Manual schema changes |
| 18 | Anti-pattern: business in SQL | Keep logic in Python |
| 19 | Industrial: migration pipeline | CI migration checks |
| 20 | Industrial: multi-tenant | Schema per tenant |
| 21 | Data migrations | Move/backfill data, not just schema |
| 22 | Optimistic locking | Version column detects concurrent writes |

### Day 69 — Networking: Sockets (23)

**Prerequisites:** Day 09 (bytes/I/O), Day 10 (errors/timeouts), Day 38 (concurrency for multi-client).
**Real-world use:** the foundation under every network protocol — building servers/clients, framing messages, and handling partial reads.
**Production example (code.py):** a length-prefixed TCP protocol server — `struct`-framed messages, `sendall` writes, buffered `recv` until complete, `SO_REUSEADDR`, timeouts, and a multi-client loop via `selectors`.
**Sources:** [socket — Low-level networking interface](https://docs.python.org/3/library/socket.html) · [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `socket.socket()` | `s = socket(AF_INET, SOCK_STREAM)` |
| 2 | TCP client | `connect()`, `send()`, `recv()` |
| 3 | TCP server | `bind()`, `listen()`, `accept()` |
| 4 | UDP | `SOCK_DGRAM`, `sendto()`, `recvfrom()` |
| 5 | `with` socket | Context manager |
| 6 | Address tuple | `("host", port)` |
| 7 | Buffered reading | Loop `recv()` until done |
| 8 | Message framing | Length prefix, delimiter |
| 9 | `select` / `selectors` | I/O multiplexing |
| 10 | `socketserver` | `TCPServer`, `ThreadingMixIn` |
| 11 | `ssl.wrap_socket()` | TLS encryption |
| 12 | `socket.timeout` | Timeout setting |
| 13 | Non-blocking | `setblocking(False)` |
| 14 | `asyncio` streams | High-level async sockets |
| 15 | `struct` for protocols | Binary message format |
| 16 | Anti-pattern: no framing | Partial reads |
| 17 | Anti-pattern: no timeout | Hanging connection |
| 18 | Industrial: TCP echo server | Multi-client |
| 19 | Industrial: protocol parser | Header + body pattern |
| 20 | Testing sockets | `socket.socketpair()` |
| 21 | `sendall()` vs `send()` | `sendall` writes the full buffer |
| 22 | `SO_REUSEADDR` | `setsockopt` to rebind quickly |
| 23 | `getaddrinfo()` | Resolve host/port, IPv4/IPv6 agnostic |

### Day 70 — Advanced Project (22)

**Prerequisites:** Day 53 (plugin registry), Day 61 (dependency injection), Day 66 (auth), Day 67–68 (database).
**Real-world use:** assembling everything into a production-shaped application — layered, tested, secure, and extensible.
**Production example (code.py):** a plugin-driven CLI service — `__init_subclass__` plugin registry, SQLAlchemy repository, JWT auth, validated inputs, DI wiring, structured logging, and a pytest suite, in a `src/` layout.
**Sources:** Build on your own earlier modules — Day 53 (plugin registry) · Day 61 (DI) · Day 66 (auth) · Days 67–68 (database).

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Project architecture | Clean layers |
| 2 | Plugin system | `__init_subclass__` registry |
| 3 | Database layer | SQLAlchemy + repository |
| 4 | Authentication | JWT + password hash |
| 5 | Input validation | Pydantic or manual |
| 6 | Error handling | Domain exceptions |
| 7 | Logging | Structured JSON |
| 8 | Configuration | Dataclass + env vars |
| 9 | CLI entry point | `argparse` |
| 10 | Type annotations | Full coverage |
| 11 | Testing | pytest + fixtures |
| 12 | Dependency injection | Constructor-based |
| 13 | SOLID compliance | Check all five |
| 14 | Design patterns used | Factory, strategy, observer |
| 15 | Security review | Input validation, auth |
| 16 | Documentation | Docstrings + README |
| 17 | Anti-pattern: monolith | Split modules |
| 18 | Anti-pattern: no tests | Add coverage |
| 19 | Industrial: production structure | src/ layout |
| 20 | Code review checklist | Final quality pass |
| 21 | Plugin entry points | `importlib.metadata.entry_points` discovery |
| 22 | Graceful shutdown | Handle SIGINT/SIGTERM, close resources |

---

## Sunday Labs (Phase 4)

| Lab | After | Build |
|-----|-------|-------|
| 11 | Days 51–55 | Meta-framework: descriptors + metaclass registry + AST linter |
| 12 | Days 56–60 | Design patterns showcase: factory + adapter + observer |
| 13 | Days 61–65 | Secure service: DI + SOLID + crypto + validation |
| 14 | Days 66–70 | Full-stack CLI app: auth + DB + plugins + tests |
