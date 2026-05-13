# Day 11 — Modules and Packages

> **TL;DR:** Modules are Python's unit of code reuse — every `.py` file is a
> module. Packages organise modules into directory hierarchies with
> `__init__.py`. Day 11 covers all import forms, `__name__` guards,
> `__main__.py`, package layout, relative imports, `__all__`, `sys.path`,
> module caching, `importlib.reload`, standard-library highlights,
> third-party tooling, namespace packages, `dir()`/`help()`, and industrial
> patterns like package splits and runnable modules. `code.py` demonstrates
> production helpers that inspect and manipulate the import system.

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|-------------|----------------|---------------|---------------|
| 1 | `import` | `import os` | Binds the entire module to a name | Access any public attribute via `module.attr` | Standard approach for stdlib | `show_import_basics` |
| 2 | `from ... import` | `from os.path import join` | Imports a specific name into the local namespace | Shorter references, explicit dependencies | Cherry-picking utilities | `show_import_basics` |
| 3 | `import ... as` | `import numpy as np` | Creates an alias for the imported name | Saves typing, avoids collisions | Convention for `np`, `pd`, `plt` | `show_import_basics` |
| 4 | `__name__` guard | `if __name__ == "__main__":` | Detects whether the file is run directly or imported | Prevents side effects on import | Every script and CLI entry point | `show_name_guard` |
| 5 | `__main__.py` | `python -m pkg` | Entry point for runnable packages | Enables `python -m mypackage` | CLI tools, test runners | `describe_runnable_package` |
| 6 | Package structure | `pkg/__init__.py`, `pkg/sub/` | Directory with `__init__.py` = regular package | Organises large codebases into namespaces | Every non-trivial project | `describe_package_layout` |
| 7 | `__init__.py` role | `from .core import Engine` | Marks directory as a package; can re-export | Controls the public API surface | Library facades, barrel files | `describe_package_layout` |
| 8 | Relative imports | `from . import sibling` | Dot-prefixed imports within a package | Avoids hardcoding the top-level name | Internal package wiring | `show_relative_import_forms` |
| 9 | `__all__` | `__all__ = ["func_a", "ClassB"]` | Controls what `from pkg import *` exports | Explicit public API, hides internals | Library packages | `demonstrate_all` |
| 10 | `sys.path` | `sys.path.insert(0, "/extra")` | List of directories Python searches for modules | Diagnose "ModuleNotFoundError" | Debugging, editable installs | `inspect_sys_path` |
| 11 | Module caching | `sys.modules["json"]` | Python caches every imported module in `sys.modules` | Import executes module code only once | Singleton-by-import pattern | `show_module_caching` |
| 12 | `importlib.reload()` | `importlib.reload(mod)` | Re-execute a module's code in place | Dev-only hot-reload during REPL work | REPL hacking, plugin reload | `demonstrate_reload` |
| 13 | Standard library tour | `os`, `sys`, `pathlib`, `json` | Batteries included — 300+ modules ship with Python | Saves external deps for common tasks | Config, I/O, networking, data | `stdlib_highlights` |
| 14 | Third-party packages | `pip install requests`, `uv add httpx` | Installing community packages from PyPI | Extend Python for any domain | Web, ML, DevOps, DB | `show_third_party_workflow` |
| 15 | Namespace packages | PEP 420 / implicit namespace | Package without `__init__.py` spanning multiple dirs | Split a single logical package across distributions | Plugin ecosystems, monorepos | `describe_namespace_packages` |
| 16 | `dir()` / `help()` | `dir(json)`, `help(json.dumps)` | Inspect a module's public names / docstrings | Interactive exploration and debugging | REPL discovery | `introspect_module` |
| 17 | Anti-pattern: circular imports | A imports B, B imports A | Causes `ImportError` or `None` attributes at import time | Breaks startup; hard to debug | Refactor into a third module or lazy import | snippet |
| 18 | Anti-pattern: `import *` | `from os import *` | Dumps all names into the caller's namespace | Name collisions, unreadable code | Never use outside REPL/`__init__` re-exports | snippet |
| 19 | Industrial: package split | Single file → package with sub-modules | Refactor a growing `utils.py` into a `utils/` package | Keeps modules < 300 lines | Any codebase that outgrows a single file | `describe_package_split` |
| 20 | Industrial: runnable module | `python -m mypackage` via `__main__.py` | CLI entry via package invocation | No need for console-script entry-points during dev | Dev CLIs, test harnesses | `describe_runnable_package` |

## Snippets

### 1. Three import forms

The fundamental ways to bring code into scope.

```python
import math                        # full module
from math import sqrt, pi          # specific names
from collections import OrderedDict as OD  # aliased

print(math.ceil(2.3))   # 3
print(sqrt(16))          # 4.0
print(OD(a=1, b=2))     # OrderedDict([('a', 1), ('b', 2)])
```

Expected output:
```text
3
4.0
OrderedDict([('a', 1), ('b', 2)])
```

> 💡 Prefer `from module import name` when you use a name often; use `import module` when you need many attributes.

### 2. The `__name__` guard

Prevents top-level code from running on import.

```python
# greeter.py
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))  # runs only when executed directly
```

Expected output (when run directly):
```text
Hello, World!
```

> 💡 Without the guard, `import greeter` would print to stdout — a side-effect that surprises importers.

### 3. Package layout & `__init__.py`

A minimal package with re-exports.

```text
mypackage/
├── __init__.py      # from .core import Engine
├── core.py          # class Engine: ...
├── helpers.py       # utility functions
└── __main__.py      # python -m mypackage entry
```

```python
# mypackage/__init__.py
from .core import Engine
__all__ = ["Engine"]

# Consumer:
from mypackage import Engine   # clean public API
```

Expected output:
```text
(no output — import succeeds silently)
```

> 💡 `__init__.py` acts as the package's facade — only export what callers need.

### 4. Relative imports

Dot-prefixed imports within a package avoid hardcoding the package name.

```python
# Inside mypackage/helpers.py
from . import core              # sibling module
from .core import Engine        # specific name from sibling
from ..utils import sanitize    # parent package (if nested)
```

Expected output:
```text
(no output — demonstration of syntax only)
```

> 💡 Relative imports only work inside packages. A bare script cannot use `from . import x`.

### 5. `sys.path` and module search order

Python searches these locations in order when you `import`.

```python
import sys

for i, p in enumerate(sys.path[:5]):
    print(f"{i}: {p}")

# Typical order:
# 0: "" (current directory or script's dir)
# 1: stdlib zip / site-packages
# ...
```

Expected output:
```text
0: 
1: /usr/lib/python312.zip
2: /usr/lib/python3.12
3: /usr/lib/python3.12/lib-dynload
4: /home/user/.venv/lib/python3.12/site-packages
```

> 💡 Inserting paths into `sys.path` is a last resort — prefer editable installs (`pip install -e .`) or `PYTHONPATH`.

### 6. Module caching with `sys.modules`

Every import is cached; the module code runs only once.

```python
import sys
import json

print("json" in sys.modules)          # True — cached after import
print(json is sys.modules["json"])     # True — same object

# Second `import json` is a dict lookup, not re-execution.
```

Expected output:
```text
True
True
```

> 💡 Module-level singletons exploit this: define an instance at module scope and import it everywhere.

### 7. `dir()` and `help()` for discovery

Explore a module's public API interactively.

```python
import json

public = [n for n in dir(json) if not n.startswith("_")]
print(public[:6])
# help(json.dumps)  # would print full docstring
```

Expected output:
```text
['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', 'dump', 'dumps', 'load']
```

> 💡 `dir()` plus `__all__` filtering shows the intended public surface of a library.

### 8. `__all__` — controlling `import *`

Defines the explicit public API for wildcard imports.

```python
# mymodule.py
__all__ = ["public_func"]

def public_func() -> str:
    return "exported"

def _private_helper() -> str:
    return "hidden"

# from mymodule import *  → only public_func is imported
```

Expected output:
```text
(no output — demonstrates declaration pattern)
```

> 💡 Always define `__all__` in library `__init__.py` files. It documents intent and prevents namespace pollution.

### 9. Anti-pattern: circular imports

```python
# ❌ Bad — a.py and b.py import each other at top level
# a.py
from b import helper_b   # triggers import of b
# b.py
from a import helper_a   # triggers import of a → ImportError or None

# ✅ Fix 1 — move the import inside the function (lazy import)
def do_work():
    from b import helper_b
    return helper_b()

# ✅ Fix 2 — extract shared code into a third module c.py
```

> Circular imports fail silently with `None` attributes or raise `ImportError`. Break cycles by lazy-importing or extracting shared dependencies.

### 10. Anti-pattern: `import *`

```python
# ❌ Bad — pollutes namespace, hides origin
from os import *
from sys import *
print(path)  # os.path? sys.path? Ambiguous!

# ✅ Corrected — explicit imports
from os import getcwd
from sys import path as sys_path
```

> `import *` makes code unreadable and un-greppable. The only acceptable use is re-exporting in `__init__.py` with a defined `__all__`.

## Anti-patterns

### Anti-pattern: Circular imports

```python
# ❌ Bad
# file_a.py: from file_b import B
# file_b.py: from file_a import A   → crash

# ✅ Corrected: lazy import
def get_b():
    from file_b import B
    return B()
```
> Circular top-level imports break startup. Lazy imports or a shared dependency module fix it.

### Anti-pattern: Star imports in application code

```python
# ❌ Bad
from itertools import *
from collections import *   # shadows 'chain'?

# ✅ Corrected
from itertools import chain, islice
from collections import Counter, defaultdict
```
> Star imports create invisible name collisions that only surface at runtime.

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| Barrel `__init__.py` | `from .models import User; __all__ = ["User"]` | Library packages — expose a clean facade |
| Lazy imports | `def heavy(): import pandas as pd; ...` | Reduce startup time when a dep is rarely needed |
| Editable install | `pip install -e .` / `uv pip install -e .` | Development — changes take effect without reinstall |
| `python -m` runner | `__main__.py` with arg parsing | Dev CLI tools, test harnesses |

## Pitfalls

- **Pitfall 1** — Running a package file directly (`python pkg/mod.py`) breaks relative imports. Use `python -m pkg.mod` instead.
- **Pitfall 2** — Shadowing stdlib names: creating `json.py` or `email.py` in your project hides the real stdlib module.
- **Pitfall 3** — Forgetting `__init__.py` turns a directory into a namespace package, which may silently import from the wrong location.
- **Pitfall 4** — Mutating `sys.path` at runtime makes builds non-reproducible. Prefer `pyproject.toml` + editable installs.
- **Pitfall 5** — `importlib.reload()` does not update already-bound names: `from mod import func` keeps the old reference.

## Why this design

`code.py` uses helper functions that *inspect* the import system (paths, caches,
module attributes) rather than building a real multi-file package — because a
single-file demo cannot exercise actual package imports. The functions print
structured output so the reader can see exactly how Python resolves imports.

## Further reading

- [Real Python — Modules and Packages](https://realpython.com/python-modules-packages/) — comprehensive tutorial on import mechanics
- [Python docs — The import system](https://docs.python.org/3/reference/import.html) — authoritative spec for finders, loaders, and caching
- [Python docs — `importlib`](https://docs.python.org/3/library/importlib.html) — programmatic import control and reload
- [Python Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html) — official beginner-friendly walkthrough
