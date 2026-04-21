# Phase 1 — Python Basics (Days 01–14)

> Track: `python_basic` · Outcome: syntax, built-ins, data structures, I/O, tooling

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

### Day 01 — Syntax, Types, Variables (20)

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
| 18 | Explicit validation | `if not x: raise ValueError(...)` |
| 19 | Anti-pattern: bare except | Catches everything — use specific |
| 20 | Anti-pattern: print vs return | Return for testability |

### Day 02 — Control Flow (22)

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
| 16 | Walrus `:=` | `if (n := len(x)) > 10:` |
| 17 | Bounded while | Max iterations to prevent infinite |
| 18 | `enumerate` in loops | `for i, v in enumerate(items):` |
| 19 | `zip` in loops | `for a, b in zip(xs, ys):` |
| 20 | Anti-pattern: deep nesting | Flatten with guard clauses |
| 21 | Anti-pattern: infinite loop | Always have exit condition |
| 22 | Industrial: state machine | `match` for workflow states |

### Day 03 — Functions (22)

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
| 17 | Closures (basic) | Inner captures outer variable |
| 18 | Recursion basics | Base case + recursive case |
| 19 | Anti-pattern: print vs return | Return for testability |
| 20 | Anti-pattern: too many params | Refactor to smaller functions |
| 21 | Industrial: pluggable validators | Function as strategy |
| 22 | Industrial: flexible formatting | `*args`/`**kwargs` patterns |

### Day 04 — Lists and Sorting (22)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | List creation | `[]`, `list()`, `[0]*n` |
| 2 | Indexing | `lst[0]`, `lst[-1]` |
| 3 | Slicing | `lst[1:3]`, `lst[::-1]` |
| 4 | `len()` | `len(lst)` |
| 5 | `append()` / `extend()` | Add single / multiple |
| 6 | `insert()` | `lst.insert(i, val)` |
| 7 | `remove()` / `pop()` / `del` | Delete by value / index |
| 8 | `index()` / `count()` | Search and count |
| 9 | `in` membership | `val in lst` — O(n) |
| 10 | `sort()` vs `sorted()` | In-place vs new list |
| 11 | `key=` parameter | `sorted(lst, key=lambda x: x[1])` |
| 12 | `reverse=True` | Descending sort |
| 13 | Stable sort | Equal elements keep order |
| 14 | Multi-key sorting | Tuple keys or multiple passes |
| 15 | Top-k pattern | `sorted(lst)[:k]` |
| 16 | `reverse()` / `reversed()` | In-place / lazy iterator |
| 17 | `copy()` / shallow vs deep | `.copy()`, `deepcopy()` |
| 18 | `enumerate()` with lists | `for i, v in enumerate(lst):` |
| 19 | Nested lists | `matrix = [[1,2],[3,4]]` |
| 20 | List comprehension preview | `[x*2 for x in lst]` |
| 21 | Anti-pattern: mutate during iteration | Build new list instead |
| 22 | Anti-pattern: alias `lst2 = lst` | Use `.copy()` |

### Day 05 — Tuples and NamedTuple (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Tuple creation | `(1, 2, 3)`, `tuple(iterable)` |
| 2 | Single-element tuple | `(1,)` not `(1)` |
| 3 | Immutability | Cannot assign `t[0] = x` |
| 4 | Indexing / slicing | Same as lists |
| 5 | Packing / unpacking | `a, b = (1, 2)` |
| 6 | Extended unpacking | `first, *rest = (1,2,3,4)` |
| 7 | Multiple return values | `return x, y` |
| 8 | Tuple as dict key | Hashable → usable as key |
| 9 | Tuple comparison | Lexicographic: `(1,2) < (1,3)` |
| 10 | `len()`, `count()`, `index()` | Tuple methods |
| 11 | `in` membership | `x in t` |
| 12 | Iteration | `for item in t:` |
| 13 | `typing.NamedTuple` | `class Point(NamedTuple): x: int` |
| 14 | `collections.namedtuple` | `Point = namedtuple('Point', ['x','y'])` |
| 15 | `_make()` / `_asdict()` | NamedTuple helpers |
| 16 | NamedTuple as DTO | Typed records for data rows |
| 17 | Mutable inside tuple | `([1,2],)` — list is mutable |
| 18 | Tuple vs list choice | Immutable → tuple |
| 19 | Anti-pattern: plain tuple for records | Use NamedTuple |
| 20 | Industrial: CSV/report DTOs | NamedTuple for structured rows |

### Day 06 — Dictionaries (24)

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
| 14 | Dict comprehension | `{k: f(v) for k, v in items}` |
| 15 | `in` membership | `"key" in d` |
| 16 | Nested dict access | `d["a"]["b"]`, chained `.get()` |
| 17 | `copy()` vs `deepcopy` | Shallow copy pitfall |
| 18 | Dict unpacking `**` | `{**d1, **d2}` |
| 19 | Insertion-order guarantee | Python 3.7+ |
| 20 | Hashability rules | Keys must be immutable |
| 21 | `KeyError` handling | `try/except` vs `get()` |
| 22 | `defaultdict` preview | `defaultdict(list)` |
| 23 | Anti-pattern: bare `[]` access | Use `get()` or `in` |
| 24 | Industrial: config merge, inverted index | `setdefault` / `|` patterns |

### Day 07 — Sets and frozenset (22)

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
| 11 | Subset `<=` / superset `>=` | `s1.issubset(s2)` |
| 12 | `isdisjoint()` | No common elements |
| 13 | `in` membership | O(1) average |
| 14 | Iteration | Unordered |
| 15 | Set comprehension | `{expr for x in iterable}` |
| 16 | `frozenset` | `frozenset(iterable)` |
| 17 | `frozenset` as dict key | Hashable, immutable |
| 18 | Hashability requirement | No lists/dicts in sets |
| 19 | Built-in aggregation | `len()`, `min()`, `max()`, `sum()` |
| 20 | Anti-pattern: unhashable in set | `{[1,2]}` → TypeError |
| 21 | Industrial: dedupe, allowlist | `set()` for O(1) checks |
| 22 | Industrial: permission comparison | Intersection/difference for RBAC |

### Day 08 — Strings and Encoding (25)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | String creation | `'...'`, `"..."`, `'''...'''` |
| 2 | Raw strings | `r"no\nescape"` |
| 3 | Indexing / negative | `s[0]`, `s[-1]` |
| 4 | Slicing | `s[1:5]`, `s[::-1]` |
| 5 | Immutability | Cannot assign `s[0] = 'x'` |
| 6 | `len()` | Character count |
| 7 | Case methods | `.upper()`, `.lower()`, `.casefold()` |
| 8 | Search methods | `.find()`, `.index()`, `.rfind()` |
| 9 | Boolean checks | `.startswith()`, `.isdigit()`, `.isalpha()` |
| 10 | Strip | `.strip()`, `.lstrip()`, `.rstrip()` |
| 11 | Split / join | `.split(sep)`, `sep.join(iter)` |
| 12 | Replace | `.replace(old, new)` |
| 13 | f-strings advanced | `f"{val:.2f}"`, `f"{x = }"` |
| 14 | Legacy formatting | `.format()`, `%` |
| 15 | Concatenation / repetition | `+`, `*` |
| 16 | `in` substring check | `"sub" in s` |
| 17 | Character frequency | `Counter(s)` |
| 18 | `bytes` vs `str` | `.encode()`, `.decode()` |
| 19 | `bytearray` | Mutable bytes |
| 20 | Unicode normalization | `unicodedata.normalize()` |
| 21 | Regex preview | `re.search()`, `re.sub()` |
| 22 | Multi-line / textwrap | Triple quotes, `dedent()` |
| 23 | `translate()` / `maketrans()` | Character mapping |
| 24 | Anti-pattern: str + bytes | Always encode/decode |
| 25 | Industrial: slugify, sanitizer | Strip, lower, replace |

### Day 09 — File I/O (22)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `open()` | `open(path, mode, encoding="utf-8")` |
| 2 | `with` context manager | Guaranteed close |
| 3 | Read methods | `.read()`, `.readline()`, `.readlines()` |
| 4 | Write methods | `.write()`, `.writelines()` |
| 5 | File modes | `r`, `w`, `a`, `x`, `r+`, `b` |
| 6 | Newline handling | `newline=""` for CSV |
| 7 | Encoding parameter | Always specify |
| 8 | `pathlib.Path` basics | `.exists()`, `.is_file()` |
| 9 | `pathlib` read/write | `.read_text()`, `.write_text()` |
| 10 | `pathlib` navigation | `.parent`, `.name`, `.suffix`, `.glob()` |
| 11 | `pathlib` construction | `/` operator, `.resolve()` |
| 12 | CSV reading | `csv.reader()`, `DictReader()` |
| 13 | CSV writing | `csv.writer()`, `DictWriter()` |
| 14 | JSON reading | `json.load()`, `json.loads()` |
| 15 | JSON writing | `json.dump()`, `indent=` |
| 16 | JSONL | One JSON per line |
| 17 | `tempfile` | `NamedTemporaryFile()`, `mkdtemp()` |
| 18 | Safe paths | Validate extensions, no traversal |
| 19 | Binary I/O | `"rb"`, `"wb"` |
| 20 | Anti-pattern: no `with` | File handle leak |
| 21 | Anti-pattern: no encoding | Platform-dependent default |
| 22 | Industrial: CSV→JSONL ETL | File pipeline pattern |

### Day 10 — Exceptions (23)

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
| 16 | `warnings` module | `warnings.warn()` |
| 17 | OS errors | `FileNotFoundError`, `PermissionError` |
| 18 | Context manager exc handling | `__exit__` receives exc |
| 19 | `contextlib.suppress` | `with suppress(Error):` |
| 20 | Anti-pattern: bare `except:` | Catches SystemExit |
| 21 | Anti-pattern: silent `pass` | Hides bugs |
| 22 | Industrial: retry wrapper | Backoff on transient errors |
| 23 | Industrial: domain errors | Typed hierarchy for APIs |

### Day 11 — Modules and Packages (20)

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
| 9 | `__all__` | Controls `import *` |
| 10 | `sys.path` | Module search path |
| 11 | Module caching | `sys.modules` |
| 12 | `importlib.reload()` | Dev-only reload |
| 13 | Standard library tour | `os`, `sys`, `pathlib`, `json` |
| 14 | Third-party packages | `pip install`, `uv add` |
| 15 | Namespace packages | PEP 420 |
| 16 | `dir()` / `help()` | Inspect contents |
| 17 | Anti-pattern: circular imports | A ↔ B |
| 18 | Anti-pattern: `import *` | Namespace pollution |
| 19 | Industrial: package split | Organize growing codebase |
| 20 | Industrial: runnable module | `python -m mypackage` |

### Day 12 — Built-ins in Pipelines (22)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `enumerate()` | Index + value |
| 2 | `zip()` | Parallel iteration |
| 3 | `zip()` strict | `strict=True` (3.10+) |
| 4 | `sorted()` | `key=`, `reverse=` |
| 5 | `reversed()` | Lazy reverse |
| 6 | `map()` | Lazy transform |
| 7 | `filter()` | Lazy selection |
| 8 | `any()` | Short-circuit True |
| 9 | `all()` | Short-circuit False |
| 10 | `sum()` | `sum(iter, start=0)` |
| 11 | `min()` / `max()` | `key=`, `default=` |
| 12 | `abs()` / `round()` / `divmod()` | Numeric |
| 13 | `len()` / `range()` | Sizing, sequences |
| 14 | `isinstance()` | Type checking |
| 15 | `type()` / `id()` / `hash()` | Introspection |
| 16 | `input()` / `print()` | `print(sep=, end=)` |
| 17 | `iter()` / `next()` | Manual iteration |
| 18 | `callable()` | Check if callable |
| 19 | `map`+`filter` vs comprehension | Readability tradeoffs |
| 20 | Chaining built-ins | Pipeline pattern |
| 21 | Anti-pattern: `list(map())` | Prefer comprehension |
| 22 | Industrial: data pipeline | Parse→map→filter→aggregate |

### Day 13 — Comprehensions (21)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | List comprehension | `[expr for x in iter]` |
| 2 | With `if` filter | `[x for x in lst if x > 0]` |
| 3 | With `if/else` | `[x if cond else y for ...]` |
| 4 | Nested comprehension | `[x for row in m for x in row]` |
| 5 | Dict comprehension | `{k: v for k, v in items}` |
| 6 | Dict with filter | `{k: v for ... if v > 0}` |
| 7 | Set comprehension | `{expr for x in iter}` |
| 8 | Generator expression | `(expr for x in iter)` |
| 9 | Generator in calls | `sum(x*x for x in range(n))` |
| 10 | Memory: list vs generator | `getsizeof()` comparison |
| 11 | `yield` preview | `def gen(): yield x` |
| 12 | `next()` on generator | Manual stepping |
| 13 | `StopIteration` | End signal |
| 14 | Comprehension scoping | No leaking in 3.x |
| 15 | Walrus `:=` | `[y for x in d if (y := f(x))]` |
| 16 | Readability limits | Max 2 nesting levels |
| 17 | Performance | Faster than for+append |
| 18 | `itertools` connection | When to graduate |
| 19 | Anti-pattern: over-nested | 3+ levels → function |
| 20 | Industrial: filtered projections | Extract fields |
| 21 | Industrial: index structures | Build lookup dicts |

### Day 14 — Tooling (20)

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
| 17 | `.gitignore` | `.venv/`, `__pycache__/` |
| 18 | Editable installs | `pip install -e .` |
| 19 | Anti-pattern: global pip | Always use venv |
| 20 | Industrial: reproducible bootstrap | Clone → sync → run |

---

## Sunday Labs (Phase 1)

| Lab | After | Build |
|-----|-------|-------|
| 01 | Days 01–05 | CLI config + CSV leaderboard + typed parsing |
| 02 | Days 06–10 | Log pipeline with sets, strings, JSONL, errors |
| 03 | Days 11–14 | Package skeleton with pyproject, uv, docs |
