# Phase 1 — Python Basics (Days 01–14)

> Track: `python_basic` · Outcome: syntax, built-ins, data structures, I/O, tooling
>
> **How to read this file:** each day has a knowledge-base block
> (Prerequisites · Real-world use · Production example · Sources) followed by its
> A-Z **Concept Checklist**. The checklist is the Gate G8 contract — every concept
> must appear in `CODE.md` + at least one of snippet / `code.py` function /
> exercise stub. The **Production example** is what `code.py` must implement.

## Day Plan

| Day | Topic | Slug | Exercise direction |
|-----|-------|------|--------------------|
| 01 | Syntax, types, variables | `day_01_syntax_variables` | CLI parsing, formatting, retry count |
| 02 | Control flow | `day_02_control_flow` | State machine, shipping rules, pattern printing |
| 03 | Functions | `day_03_functions` | Validators, signatures, event formatting |
| 04 | Lists and sorting | `day_04_lists` | Leaderboard ranking, tie-breakers |
| 05 | Tuples and NamedTuple | `day_05_tuples` | CSV row DTOs, coordinate parsing |
| 06 | Dictionaries | `day_06_dictionary` | Inverted index, config merge, word-count |
| 07 | Sets and frozenset | `day_07_sets` | Dedupe logs, allowlist/denylist |
| 08 | Strings and encoding | `day_08_strings` | Slugify, sanitizer, normalizer |
| 09 | File I/O | `day_09_file_io` | CSV→JSONL ETL, file summary |
| 10 | Exceptions | `day_10_exceptions` | Retry wrapper, domain errors |
| 11 | Modules and packages | `day_11_modules` | Package split, runnable module |
| 12 | Built-ins in pipelines | `day_12_builtins` | Parse→map→filter→aggregate |
| 13 | Comprehensions | `day_13_comprehensions` | Filtered projections, generators |
| 14 | Tooling | `day_14_tooling` | Environment bootstrap, task runner |

---

## Concept Checklists

> Gate G8: every concept must appear in CODE.md table + at least one of: snippet, code.py function, or exercise stub.

### Day 01 — Syntax, Types, Variables (26)

**Prerequisites:** none — this is the entry point.
**Real-world use:** every script and service reads raw input (CLI args, env vars, config), validates it, coerces types, and formats output.
**Production example (code.py):** a typed input reader that parses raw strings into `int`/`float`/`bool`, validates a retry-count is in range, and returns a formatted summary line (never `print`s from the logic).
**Sources:** [Python Tutorial — Introduction](https://docs.python.org/3/tutorial/introduction.html) · [Real Python — Variables](https://realpython.com/python-variables/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Naming conventions | `snake_case`, `PascalCase`, `UPPER_SNAKE` |
| 2 | Numeric literals | `42`, `3.14`, `0xFF`, `0b101`, `1_000_000` |
| 3 | String literals | `'...'`, `"..."`, `'''...'''`, `r"raw"` |
| 4 | Boolean and None | `True`, `False`, `None` |
| 5 | Type system basics | `int`, `float`, `str`, `bool`, `None` |
| 6 | Type hints | `def f(x: str) -> int:` |
| 7 | `Final` constants | `MAX: Final[int] = 3` |
| 8 | `type()` / `isinstance()` | Runtime type checking |
| 9 | Type conversion | `int("42")`, `float("3.14")`, `str(42)` |
| 10 | `input()` | `raw = input("prompt: ")` |
| 11 | `strip()` for cleanup | Removes whitespace |
| 12 | f-strings | `f"name={name}"` |
| 13 | `.format()` / `%` legacy | `"{} {}".format(a, b)` |
| 14 | Multiple assignment | `a, b = 1, 2` |
| 15 | Augmented assignment | `x += 1`, `x *= 2` |
| 16 | Identity vs equality | `is` vs `==`, `id()` |
| 17 | `round()` | `round(3.14159, 2)` |
| 18 | Arithmetic operators | `+ - * / // % **`, `divmod()` |
| 19 | Comparison operators | `== != < <= > >=` |
| 20 | Logical operators | `and`, `or`, `not` (short-circuit) |
| 21 | Chained comparison | `0 <= x < 10` |
| 22 | Operator precedence | `**` > `*//%` > `+-`; use parens for clarity |
| 23 | Comments & module docstring | `#`, `"""module summary"""` |
| 24 | Explicit validation | `if not x: raise ValueError(...)` |
| 25 | Anti-pattern: bare except | Catches everything — use specific |
| 26 | Anti-pattern: print vs return | Return for testability |

### Day 02 — Control Flow (25)

**Prerequisites:** Day 01 (types, truthy values, comparison/logical operators).
**Real-world use:** routing requests, applying business rules, retry/timeout loops, and workflow state transitions.
**Production example (code.py):** an order-shipping rules engine — `match`/guard-clause dispatch over order state that returns the next action, with a bounded retry loop for transient states.
**Sources:** [Python Tutorial — Control Flow](https://docs.python.org/3/tutorial/controlflow.html) · [PEP 636 — match/case](https://peps.python.org/pep-0636/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `if` / `elif` / `else` | Basic branching |
| 2 | Truthiness | `0`, `""`, `[]`, `None` are falsy |
| 3 | Ternary expression | `x = a if cond else b` |
| 4 | `for` + `range()` | `for i in range(n):` |
| 5 | `for` over iterables | `for item in lst:` |
| 6 | `while` loop | `while cond:` |
| 7 | `break` | Exit loop early |
| 8 | `continue` | Skip to next iteration |
| 9 | `pass` | Empty block placeholder |
| 10 | `for-else` / `while-else` | `else` runs if no `break` |
| 11 | Nested loops | Loop inside loop |
| 12 | Pattern printing | Triangle, pyramid with `*` |
| 13 | Guard clauses | Early return to reduce nesting |
| 14 | `match` / `case` (3.10+) | Structural pattern matching |
| 15 | `match` with sequences | `case (x, y):` |
| 16 | `match` with mapping/class | `case {"k": v}:`, `case Point(x=0):` |
| 17 | `match` guard | `case n if n > 0:` |
| 18 | Walrus `:=` | `if (n := len(x)) > 10:` |
| 19 | Bounded while | Max iterations to prevent infinite |
| 20 | `enumerate` in loops | `for i, v in enumerate(items):` |
| 21 | `zip` in loops | `for a, b in zip(xs, ys):` |
| 22 | Loop over `dict.items()` | `for k, v in d.items():` |
| 23 | Anti-pattern: deep nesting | Flatten with guard clauses |
| 24 | Anti-pattern: infinite loop | Always have exit condition |
| 25 | Industrial: state machine | `match` for workflow states |

### Day 03 — Functions (24)

**Prerequisites:** Day 01 (types, type hints), Day 02 (control flow, guard clauses).
**Real-world use:** every reusable unit — validators, formatters, handlers, strategy callbacks — is a well-typed function with a clear contract.
**Production example (code.py):** a pluggable validation pipeline — small typed validator functions passed as strategies, composed by a runner that applies `*args`/`**kwargs` and returns structured results.
**Sources:** [Real Python — Defining Functions](https://realpython.com/defining-your-own-python-function/) · [Python Tutorial — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `def` + `return` | `def f(x): return x + 1` |
| 2 | Multiple return values | `return a, b` |
| 3 | Implicit `return None` | No return = None |
| 4 | Default arguments | `def f(x, y=10):` |
| 5 | Keyword arguments | `f(y=20, x=10)` |
| 6 | Positional-only `/` | `def f(x, /, y):` |
| 7 | Keyword-only `*` | `def f(*, key):` |
| 8 | `*args` | Variable positional args |
| 9 | `**kwargs` | Variable keyword args |
| 10 | Unpacking in calls | `f(*list)`, `f(**dict)` |
| 11 | `lambda` | `key=lambda x: x[1]` |
| 12 | Docstrings (Google style) | Args / Returns / Raises |
| 13 | Type hints on functions | `def f(x: str) -> int:` |
| 14 | Scope: local/global/nonlocal | `global x`, `nonlocal y` |
| 15 | Mutable default pitfall | `def f(items=None):` fix |
| 16 | First-class functions | Functions as arguments |
| 17 | Returning functions | Factory returning a callable |
| 18 | Closures (basic) | Inner captures outer variable |
| 19 | Recursion basics | Base case + recursive case |
| 20 | Callable typing | `Callable[[int], str]` |
| 21 | Anti-pattern: print vs return | Return for testability |
| 22 | Anti-pattern: too many params | Refactor to smaller functions |
| 23 | Industrial: pluggable validators | Function as strategy |
| 24 | Industrial: flexible formatting | `*args`/`**kwargs` patterns |

### Day 04 — Lists and Sorting (27)

**Prerequisites:** Day 01 (types), Day 02 (loops), Day 03 (lambda for `key=`).
**Real-world use:** ordering API results, leaderboards, batch record processing, and maintaining sorted collections.
**Production example (code.py):** a stable multi-key leaderboard — rank records by score desc then name asc (tie-breakers), select top-k, and insert new entries into an already-sorted list with `bisect.insort`.
**Sources:** [Real Python — Lists and Tuples](https://realpython.com/python-lists-tuples/) · [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | List creation | `[]`, `list()`, `[0]*n` |
| 2 | Indexing | `lst[0]`, `lst[-1]` |
| 3 | Slicing | `lst[1:3]`, `lst[::-1]` |
| 4 | Slice assignment | `lst[1:3] = [x, y]` |
| 5 | `del` on index/slice | `del lst[0]`, `del lst[1:3]` |
| 6 | `len()` | `len(lst)` |
| 7 | `append()` / `extend()` | Add single / multiple |
| 8 | `insert()` | `lst.insert(i, val)` |
| 9 | `remove()` / `pop()` / `del` | Delete by value / index |
| 10 | `index()` / `count()` | Search and count |
| 11 | `in` membership | `val in lst` — O(n) |
| 12 | `sort()` vs `sorted()` | In-place vs new list |
| 13 | `key=` parameter | `sorted(lst, key=lambda x: x[1])` |
| 14 | `reverse=True` | Descending sort |
| 15 | Stable sort | Equal elements keep order |
| 16 | Multi-key sorting | Tuple keys or multiple passes |
| 17 | Top-k pattern | `sorted(lst)[:k]` |
| 18 | `bisect` / `insort` | Keep a list sorted, O(log n) find |
| 19 | `reverse()` / `reversed()` | In-place / lazy iterator |
| 20 | `min` / `max` / `sum` / `any` / `all` | Aggregation over lists |
| 21 | Star-unpacking in literals | `[*a, *b]`, `first, *rest = lst` |
| 22 | `copy()` / shallow vs deep | `.copy()`, `deepcopy()` |
| 23 | `enumerate()` with lists | `for i, v in enumerate(lst):` |
| 24 | Nested lists | `matrix = [[1,2],[3,4]]` |
| 25 | List comprehension preview | `[x*2 for x in lst]` |
| 26 | Anti-pattern: mutate during iteration | Build new list instead |
| 27 | Anti-pattern: alias `lst2 = lst` / shared nested refs | Use `.copy()` / `deepcopy` |

### Day 05 — Tuples and NamedTuple (21)

**Prerequisites:** Day 04 (sequences, indexing/slicing), Day 01 (type hints).
**Real-world use:** immutable records/DTOs — CSV rows, coordinates, DB result rows, dictionary keys.
**Production example (code.py):** parse CSV rows into typed `NamedTuple` DTOs, use `_asdict()` for serialization, and use `(lat, lon)` tuples as hashable cache keys.
**Sources:** [Real Python — Lists and Tuples](https://realpython.com/python-lists-tuples/) · [collections.namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Tuple creation | `(1, 2, 3)`, `tuple(iterable)` |
| 2 | Single-element tuple | `(1,)` not `(1)` |
| 3 | Immutability | Cannot assign `t[0] = x` |
| 4 | Indexing / slicing | Same as lists |
| 5 | Packing / unpacking | `a, b = (1, 2)` |
| 6 | Extended unpacking | `first, *rest = (1,2,3,4)` |
| 7 | Swap via tuples | `a, b = b, a` |
| 8 | Multiple return values | `return x, y` |
| 9 | Tuple as dict key | Hashable → usable as key |
| 10 | Tuple comparison | Lexicographic: `(1,2) < (1,3)` |
| 11 | `len()`, `count()`, `index()` | Tuple methods |
| 12 | `in` membership | `x in t` |
| 13 | Iteration | `for item in t:` |
| 14 | `typing.NamedTuple` | `class Point(NamedTuple): x: int` |
| 15 | `collections.namedtuple` | `Point = namedtuple('Point', ['x','y'])` |
| 16 | `_make()` / `_asdict()` / `_replace()` | NamedTuple helpers |
| 17 | NamedTuple defaults | `defaults=` / field defaults |
| 18 | Mutable inside tuple | `([1,2],)` — list is mutable |
| 19 | Tuple vs list choice | Immutable → tuple |
| 20 | Anti-pattern: plain tuple for records | Use NamedTuple |
| 21 | Industrial: CSV/report DTOs | NamedTuple for structured rows |

### Day 06 — Dictionaries (26)

**Prerequisites:** Day 04 (iteration), Day 05 (hashable keys), Day 03 (functions).
**Real-world use:** configuration, lookups, grouping/counting, in-memory indexes, JSON payloads.
**Production example (code.py):** a config merger + inverted index — deep-merge layered config dicts with `|`, and build a `defaultdict(list)` inverted index (term → doc ids) with a word-count `Counter`.
**Sources:** [Real Python — Dictionaries](https://realpython.com/python-dicts/) · [Python Tutorial — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Literal creation | `{"k": v}` |
| 2 | `dict()` constructor | `dict(a=1)`, `dict(zip(k, v))` |
| 3 | `dict.fromkeys()` | `dict.fromkeys(keys, default)` |
| 4 | Access `[]` / KeyError | `d["key"]` raises if missing |
| 5 | `get()` with default | `d.get("k", 0)` |
| 6 | `setdefault()` | `d.setdefault("k", []).append(v)` |
| 7 | Insert / update `[]` | `d["new"] = val` |
| 8 | `update()` / `|=` | `d.update(other)` (3.9+) |
| 9 | Merge `|` | `merged = d1 | d2` |
| 10 | `del` | `del d["key"]` |
| 11 | `pop()` / `popitem()` | `d.pop("k", default)` |
| 12 | `clear()` | `d.clear()` |
| 13 | `.keys()` / `.values()` / `.items()` | View objects |
| 14 | Iterate keys / values / items | `for k, v in d.items():` |
| 15 | Dict comprehension | `{k: f(v) for k, v in items}` |
| 16 | `in` membership | `"key" in d` |
| 17 | Nested dict access | `d["a"]["b"]`, chained `.get()` |
| 18 | `copy()` vs `deepcopy` | Shallow copy pitfall |
| 19 | Dict unpacking `**` | `{**d1, **d2}` |
| 20 | Insertion-order guarantee | Python 3.7+ |
| 21 | Hashability rules | Keys must be immutable |
| 22 | `KeyError` handling | `try/except` vs `get()` |
| 23 | `Counter` | Frequency counting |
| 24 | `defaultdict` | `defaultdict(list)` grouping |
| 25 | Anti-pattern: bare `[]` access | Use `get()` or `in` |
| 26 | Industrial: config merge, inverted index | `setdefault` / `|` patterns |

### Day 07 — Sets and frozenset (22)

**Prerequisites:** Day 05 (hashability), Day 06 (dicts), Day 04 (iteration).
**Real-world use:** deduplication, membership tests, allow/deny lists, permission (RBAC) comparisons.
**Production example (code.py):** a log deduplicator + RBAC checker — dedupe events with `set()`, and compute granted/denied permissions via `&`, `-`, `<=` with a `frozenset` role key.
**Sources:** [Real Python — Sets](https://realpython.com/python-sets/) · [set / frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Literal creation | `{1, 2, 3}`, empty: `set()` |
| 2 | `set()` constructor | `set(iterable)` |
| 3 | `add()` | `s.add(elem)` |
| 4 | `remove()` vs `discard()` | `remove` raises, `discard` silent |
| 5 | `pop()` / `clear()` | Arbitrary remove / empty |
| 6 | `update()` / `|=` | Add from iterable |
| 7 | Union `|` | All from both sets |
| 8 | Intersection `&` | Common elements |
| 9 | Difference `-` | In first, not second |
| 10 | Symmetric difference `^` | In either, not both |
| 11 | In-place set ops | `&=`, `-=`, `^=` |
| 12 | Subset `<=` / superset `>=` | `s1.issubset(s2)` |
| 13 | `isdisjoint()` | No common elements |
| 14 | `in` membership | O(1) average |
| 15 | Iteration | Unordered |
| 16 | Set comprehension | `{expr for x in iterable}` |
| 17 | `frozenset` | `frozenset(iterable)` |
| 18 | `frozenset` as dict key | Hashable, immutable |
| 19 | Hashability requirement | No lists/dicts in sets |
| 20 | Built-in aggregation | `len()`, `min()`, `max()`, `sum()` |
| 21 | Anti-pattern: unhashable in set | `{[1,2]}` → TypeError |
| 22 | Industrial: dedupe, allowlist, RBAC | `set()` O(1) checks, intersection/difference |

### Day 08 — Strings and Encoding (26)

**Prerequisites:** Day 01 (string literals, f-strings), Day 04 (slicing), Day 06 (Counter preview).
**Real-world use:** input sanitization, slugs/identifiers, parsing, and correct text/bytes handling across encodings.
**Production example (code.py):** a slugify + sanitizer utility — normalize Unicode (`NFKD`), casefold, strip/replace unsafe chars via `translate`, and encode/decode safely to UTF-8 bytes.
**Sources:** [Real Python — Strings](https://realpython.com/python-strings/) · [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | String creation | `'...'`, `"..."`, `'''...'''` |
| 2 | Raw strings | `r"no\nescape"` |
| 3 | Escape sequences | `\n`, `\t`, `\\`, `\uXXXX` |
| 4 | Indexing / negative | `s[0]`, `s[-1]` |
| 5 | Slicing | `s[1:5]`, `s[::-1]` |
| 6 | Immutability | Cannot assign `s[0] = 'x'` |
| 7 | `len()` | Character count |
| 8 | Case methods | `.upper()`, `.lower()`, `.casefold()`, `.title()` |
| 9 | Search methods | `.find()`, `.index()`, `.rfind()`, `.count()` |
| 10 | Boolean checks | `.startswith()`, `.isdigit()`, `.isalpha()`, `.isspace()` |
| 11 | Strip | `.strip()`, `.lstrip()`, `.rstrip()` |
| 12 | Split / rsplit / splitlines | `.split(sep)`, `.splitlines()` |
| 13 | Join | `sep.join(iter)` |
| 14 | Replace | `.replace(old, new)` |
| 15 | Padding / alignment | `.zfill()`, `.ljust()`, `.center()` |
| 16 | f-strings advanced | `f"{val:.2f}"`, `f"{x = }"`, `f"{v:>10}"` |
| 17 | Legacy formatting | `.format()`, `%` |
| 18 | Concatenation / repetition | `+`, `*` |
| 19 | `in` substring check | `"sub" in s` |
| 20 | Character frequency | `Counter(s)` |
| 21 | `bytes` vs `str` | `.encode()`, `.decode()` |
| 22 | `bytearray` | Mutable bytes |
| 23 | Unicode normalization | `unicodedata.normalize()` |
| 24 | `translate()` / `maketrans()` | Character mapping |
| 25 | Anti-pattern: str + bytes / no encoding | Always encode/decode explicitly |
| 26 | Industrial: slugify, sanitizer | Strip, casefold, normalize, translate |

### Day 09 — File I/O (24)

**Prerequisites:** Day 08 (strings/encoding), Day 06 (dicts for JSON), Day 05 (rows), Day 10 preview (errors).
**Real-world use:** reading/writing config and data files, ETL pipelines, logs, and structured exports (CSV/JSON/JSONL).
**Production example (code.py):** a CSV→JSONL ETL — read a CSV with `DictReader`, validate/transform rows, write one JSON object per line, all under `with` + `pathlib`, with a run summary.
**Sources:** [Real Python — Reading & Writing Files](https://realpython.com/read-write-files-python/) · [pathlib](https://docs.python.org/3/library/pathlib.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `open()` | `open(path, mode, encoding="utf-8")` |
| 2 | `with` context manager | Guaranteed close |
| 3 | Read methods | `.read()`, `.readline()`, `.readlines()` |
| 4 | Iterate a file object | `for line in f:` (streaming) |
| 5 | Write methods | `.write()`, `.writelines()` |
| 6 | File modes | `r`, `w`, `a`, `x`, `r+`, `b` |
| 7 | Newline handling | `newline=""` for CSV |
| 8 | Encoding parameter | Always specify |
| 9 | `seek()` / `tell()` | Position within a file |
| 10 | `pathlib.Path` basics | `.exists()`, `.is_file()` |
| 11 | `pathlib` read/write | `.read_text()`, `.write_text()` |
| 12 | `pathlib` navigation | `.parent`, `.name`, `.suffix`, `.stem`, `.glob()` |
| 13 | `pathlib` construction | `/` operator, `.resolve()` |
| 14 | CSV reading | `csv.reader()`, `DictReader()` |
| 15 | CSV writing | `csv.writer()`, `DictWriter()` |
| 16 | JSON reading | `json.load()`, `json.loads()` |
| 17 | JSON writing | `json.dump()`, `indent=` |
| 18 | JSONL | One JSON per line |
| 19 | `tempfile` | `NamedTemporaryFile()`, `mkdtemp()` |
| 20 | Safe paths | Validate extensions, no traversal |
| 21 | Binary I/O | `"rb"`, `"wb"` |
| 22 | Anti-pattern: no `with` | File handle leak |
| 23 | Anti-pattern: no encoding | Platform-dependent default |
| 24 | Industrial: CSV→JSONL ETL | File pipeline pattern |

### Day 10 — Exceptions (24)

**Prerequisites:** Day 03 (functions), Day 09 (file/OS errors), Day 02 (control flow).
**Real-world use:** resilient services — typed domain errors, retry/backoff on transient failures, cleanup, and clear diagnostics.
**Production example (code.py):** a retry wrapper + domain error hierarchy — retry a flaky operation with bounded attempts on `TransientError`, raise a typed `DomainError` with context, chain the original with `from`.
**Sources:** [Real Python — Exceptions](https://realpython.com/python-exceptions/) · [Python Tutorial — Errors](https://docs.python.org/3/tutorial/errors.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `try` / `except` | `except ValueError:` |
| 2 | Multiple except | `except (TypeError, ValueError):` |
| 3 | `as` alias | `except ValueError as exc:` |
| 4 | `else` clause | Runs if no exception |
| 5 | `finally` | Always runs — cleanup |
| 6 | `raise` | `raise ValueError("msg")` |
| 7 | Re-raise | Bare `raise` |
| 8 | Chaining `from` | `raise New from original` |
| 9 | Exception hierarchy | `BaseException → Exception → ...` |
| 10 | Custom exception class | `class DomainError(Exception):` |
| 11 | Custom with fields | `__init__` with context |
| 12 | `ExceptionGroup` (3.11+) | `except*` syntax |
| 13 | `assert` | Dev checks only |
| 14 | LBYL vs EAFP | Two styles |
| 15 | `traceback` module | `traceback.format_exc()` |
| 16 | `logging.exception` | Log with traceback |
| 17 | `warnings` module | `warnings.warn()` |
| 18 | OS errors | `FileNotFoundError`, `PermissionError` |
| 19 | Context manager exc handling | `__exit__` receives exc |
| 20 | `contextlib.suppress` | `with suppress(Error):` |
| 21 | Anti-pattern: bare `except:` | Catches SystemExit |
| 22 | Anti-pattern: silent `pass` | Hides bugs |
| 23 | Industrial: retry wrapper | Backoff on transient errors |
| 24 | Industrial: domain errors | Typed hierarchy for APIs |

### Day 11 — Modules and Packages (21)

**Prerequisites:** Day 03 (functions), Day 10 (imports appear everywhere).
**Real-world use:** organizing a growing codebase into importable, testable, runnable packages.
**Production example (code.py):** a small package split into modules with `__init__.py` re-exports, an `__all__`, and a `__main__.py` so it runs as `python -m pkg`.
**Sources:** [Real Python — Modules & Packages](https://realpython.com/python-modules-packages/) · [Python Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `import` | `import module` |
| 2 | `from ... import` | `from module import func` |
| 3 | `import ... as` | `import numpy as np` |
| 4 | `__name__` guard | `if __name__ == "__main__":` |
| 5 | `__main__.py` | `python -m pkg` |
| 6 | Package structure | `__init__.py`, nested packages |
| 7 | `__init__.py` role | Marker, re-exports |
| 8 | Relative imports | `from . import sibling` |
| 9 | Absolute vs relative | When to use each |
| 10 | `__all__` | Controls `import *` |
| 11 | `sys.path` | Module search path |
| 12 | Module caching | `sys.modules` |
| 13 | Module-level `__doc__` / attributes | Introspecting a module |
| 14 | `importlib.reload()` | Dev-only reload |
| 15 | Standard library tour | `os`, `sys`, `pathlib`, `json` |
| 16 | Third-party packages | `pip install`, `uv add` |
| 17 | Namespace packages | PEP 420 |
| 18 | `dir()` / `help()` | Inspect contents |
| 19 | Anti-pattern: circular imports | A ↔ B |
| 20 | Anti-pattern: `import *` | Namespace pollution |
| 21 | Industrial: runnable package | `python -m mypackage` with `__main__` |

### Day 12 — Built-ins in Pipelines (23)

**Prerequisites:** Day 03 (lambda), Day 04 (iterables), Day 13 preview (comprehensions).
**Real-world use:** data transformation pipelines — parse → transform → filter → aggregate without heavyweight libraries.
**Production example (code.py):** a records pipeline — parse raw rows, `map` a typed transform, `filter` invalid rows, then aggregate with `sum`/`min`/`max`/`sorted(key=)` into a report.
**Sources:** [Built-in Functions](https://docs.python.org/3/library/functions.html) · [Real Python — map/filter/reduce](https://realpython.com/python-map-filter-reduce/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `enumerate()` | Index + value |
| 2 | `zip()` | Parallel iteration |
| 3 | `zip()` strict | `strict=True` (3.10+) |
| 4 | `sorted()` | `key=`, `reverse=` |
| 5 | `reversed()` | Lazy reverse |
| 6 | `map()` | Lazy transform |
| 7 | `filter()` | Lazy selection |
| 8 | `functools.reduce()` | Fold to single value |
| 9 | `any()` | Short-circuit True |
| 10 | `all()` | Short-circuit False |
| 11 | `sum()` | `sum(iter, start=0)` |
| 12 | `min()` / `max()` | `key=`, `default=` |
| 13 | `abs()` / `round()` / `divmod()` | Numeric |
| 14 | `len()` / `range()` | Sizing, sequences |
| 15 | `isinstance()` | Type checking |
| 16 | `type()` / `id()` / `hash()` | Introspection |
| 17 | `input()` / `print()` | `print(sep=, end=)` |
| 18 | `iter()` / `next()` | Manual iteration |
| 19 | `callable()` | Check if callable |
| 20 | `map`+`filter` vs comprehension | Readability tradeoffs |
| 21 | Chaining built-ins | Pipeline pattern |
| 22 | Anti-pattern: `list(map())` for side effects | Prefer comprehension / loop |
| 23 | Industrial: data pipeline | Parse→map→filter→aggregate |

### Day 13 — Comprehensions (22)

**Prerequisites:** Day 04 (lists), Day 06 (dicts), Day 07 (sets), Day 12 (built-ins).
**Real-world use:** concise projections/filters, building lookup structures, and memory-efficient streaming via generators.
**Production example (code.py):** filtered projections + a lookup index — build a `{id: record}` dict comprehension and a lazy generator pipeline that streams and filters large input without materializing it.
**Sources:** [Real Python — List Comprehensions](https://realpython.com/list-comprehension-python/) · [Python Tutorial — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | List comprehension | `[expr for x in iter]` |
| 2 | With `if` filter | `[x for x in lst if x > 0]` |
| 3 | With `if/else` | `[x if cond else y for ...]` |
| 4 | Nested comprehension | `[x for row in m for x in row]` |
| 5 | Nested data build | `[[..] for .. ]` matrices |
| 6 | Dict comprehension | `{k: v for k, v in items}` |
| 7 | Dict with filter | `{k: v for ... if v > 0}` |
| 8 | Set comprehension | `{expr for x in iter}` |
| 9 | Generator expression | `(expr for x in iter)` |
| 10 | Generator in calls | `sum(x*x for x in range(n))` |
| 11 | Memory: list vs generator | `getsizeof()` comparison |
| 12 | `yield` preview | `def gen(): yield x` |
| 13 | `next()` on generator | Manual stepping |
| 14 | `StopIteration` | End signal |
| 15 | Comprehension scoping | No leaking in 3.x |
| 16 | Walrus `:=` in comprehension | `[y for x in d if (y := f(x))]` |
| 17 | Conditional key/value in dict comp | Branching inside |
| 18 | Readability limits | Max 2 nesting levels |
| 19 | Performance | Faster than for+append |
| 20 | `itertools` connection | When to graduate |
| 21 | Anti-pattern: over-nested | 3+ levels → function |
| 22 | Industrial: filtered projections, index structures | Extract fields, build lookups |

### Day 14 — Tooling (22)

**Prerequisites:** Day 11 (packages), Day 09 (files), Day 01 (running scripts).
**Real-world use:** reproducible environments, dependency locking, linting/formatting/type-checking — the baseline every professional repo enforces in CI.
**Production example (code.py):** a project bootstrap/task-runner script — create a venv, sync deps from `pyproject.toml`/lockfile, and run `ruff check` + `mypy` as a single reproducible command.
**Sources:** [uv docs](https://docs.astral.sh/uv/) · [pyproject.toml spec](https://packaging.python.org/en/latest/specifications/pyproject-toml/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `venv` creation | `python -m venv .venv` |
| 2 | `venv` activation | `source .venv/bin/activate` |
| 3 | `pip` basics | `pip install`, `pip freeze` |
| 4 | `requirements.txt` | `pip freeze > requirements.txt` |
| 5 | `uv` install | `pip install uv` |
| 6 | `uv` environments | `uv venv`, `uv pip install` |
| 7 | `uv` deps | `uv add`, `uv lock`, `uv sync` |
| 8 | `uv` scripts | `uv run script.py` |
| 9 | `pyproject.toml` basics | `[project]` table |
| 10 | `pyproject` scripts | `[project.scripts]` |
| 11 | `pyproject` optional deps | `[project.optional-dependencies]` |
| 12 | Build systems | setuptools, hatchling, flit |
| 13 | Lock files | `uv.lock` |
| 14 | `ruff` linter | `ruff check .`, `ruff format .` |
| 15 | `ruff` config | `[tool.ruff]` in pyproject |
| 16 | `mypy` basics | `mypy .` |
| 17 | pre-commit hooks | `.pre-commit-config.yaml` |
| 18 | `.gitignore` | `.venv/`, `__pycache__/` |
| 19 | Editable installs | `pip install -e .` |
| 20 | `python -m` module run | Run tools & packages consistently |
| 21 | Anti-pattern: global pip | Always use venv |
| 22 | Industrial: reproducible bootstrap | Clone → sync → run |

---

## Sunday Labs (Phase 1)

| Lab | After | Build |
|-----|-------|-------|
| 01 | Days 01–05 | CLI config + CSV leaderboard + typed parsing |
| 02 | Days 06–10 | Log pipeline with sets, strings, JSONL, errors |
| 03 | Days 11–14 | Package skeleton with pyproject, uv, docs |
