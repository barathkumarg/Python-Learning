# code.py — Day 11: Modules and Packages

"""Modules and Packages — production-style reference implementations.

Covers concepts #1–#20: import forms, __name__ guard, __main__.py, package
layout, __init__.py, relative imports, __all__, sys.path, sys.modules caching,
importlib.reload, stdlib highlights, third-party workflow, namespace packages,
dir()/help(), anti-patterns (circular imports, import *), and industrial
patterns (package split, runnable module).

Style: typed signatures, Google docstrings, explicit validation, inline demos.
Since module/package concepts are largely structural, several functions
*describe* the pattern and print illustrative output rather than returning
computed values.
"""

from __future__ import annotations

import importlib
import json
import sys


# ─── Section 1: Import basics (concepts #1, #2, #3) ───


def show_import_basics() -> dict[str, str]:
    """Demonstrate the three core import forms.

    Returns:
        Dict mapping form name to a one-line description.

    Examples:
        >>> result = show_import_basics()
        >>> "import" in result
        True
    """
    forms: dict[str, str] = {
        "import": "import math          → math.sqrt(4)",
        "from":   "from math import sqrt → sqrt(4)",
        "as":     "import numpy as np   → np.array([1])",
    }
    for form, example in forms.items():
        print(f"  {form:>8}: {example}")
    return forms


# ─── Section 2: __name__ guard (concept #4) ───


def show_name_guard(module_name: str = __name__) -> str:
    """Explain the __name__ guard for a given module name.

    Args:
        module_name: The value of ``__name__`` to inspect.

    Returns:
        ``"script"`` if the module is the entry point, ``"library"`` otherwise.

    Raises:
        ValueError: If *module_name* is empty.

    Examples:
        >>> show_name_guard("__main__")
        'script'
        >>> show_name_guard("mypackage.utils")
        'library'
    """
    if not module_name:
        raise ValueError("module_name must not be empty")
    is_main = module_name == "__main__"
    role = "script" if is_main else "library"
    print(f"  __name__ = {module_name!r} → role = {role}")
    return role


# ─── Section 3: Package layout & __init__.py (concepts #5, #6, #7, #20) ───


def describe_package_layout() -> list[str]:
    """Print and return a canonical package directory tree.

    Covers concepts #5 (``__main__.py``), #6 (package structure),
    #7 (``__init__.py`` role), and #20 (runnable module).

    Returns:
        List of file paths in the example package.

    Examples:
        >>> paths = describe_package_layout()
        >>> "__init__.py" in paths[0]
        True
    """
    tree = [
        "mypackage/__init__.py      # re-exports, __all__",
        "mypackage/core.py          # Engine class",
        "mypackage/helpers.py       # utility functions",
        "mypackage/cli.py           # argparse logic",
        "mypackage/__main__.py      # python -m mypackage",
    ]
    print("  Canonical package layout:")
    for line in tree:
        print(f"    {line}")
    return tree


def describe_runnable_package() -> str:
    """Describe how ``__main__.py`` enables ``python -m pkg``.

    Returns:
        A one-line summary of the mechanism.

    Examples:
        >>> "python -m" in describe_runnable_package()
        True
    """
    summary = (
        "__main__.py is executed when you run 'python -m mypackage'; "
        "it typically parses CLI args and calls into the package."
    )
    print(f"  {summary}")
    return summary


# ─── Section 4: Relative imports & __all__ (concepts #8, #9) ───


def show_relative_import_forms() -> list[str]:
    """List the three relative-import syntaxes with explanations.

    Returns:
        List of syntax examples.

    Examples:
        >>> forms = show_relative_import_forms()
        >>> len(forms) >= 3
        True
    """
    forms = [
        "from . import sibling       # import sibling module",
        "from .sibling import func   # import name from sibling",
        "from ..parent import util   # go up one package level",
    ]
    print("  Relative import forms:")
    for f in forms:
        print(f"    {f}")
    return forms


def demonstrate_all() -> list[str]:
    """Show how ``__all__`` controls ``from module import *``.

    Returns:
        A sample ``__all__`` list.

    Examples:
        >>> exports = demonstrate_all()
        >>> "public_func" in exports
        True
    """
    sample_all: list[str] = ["public_func", "PublicClass"]
    print(f"  __all__ = {sample_all!r}")
    print("  → 'from module import *' only imports these names.")
    print("  → _private_helper is hidden from wildcard import.")
    return sample_all


# ─── Section 5: sys.path & module caching (concepts #10, #11) ───


def inspect_sys_path(max_entries: int = 5) -> list[str]:
    """Print the first *max_entries* of ``sys.path``.

    Args:
        max_entries: How many path entries to show (default 5).

    Returns:
        The first *max_entries* path strings.

    Raises:
        ValueError: If *max_entries* < 1.

    Examples:
        >>> paths = inspect_sys_path(3)
        >>> isinstance(paths, list)
        True
    """
    if max_entries < 1:
        raise ValueError(f"max_entries must be >= 1, got {max_entries}")
    entries = sys.path[:max_entries]
    print(f"  sys.path (first {max_entries}):")
    for i, p in enumerate(entries):
        print(f"    {i}: {p or '(empty = cwd)'}")
    return entries


def show_module_caching() -> dict[str, bool]:
    """Demonstrate that imported modules are cached in ``sys.modules``.

    Returns:
        Dict showing whether ``json`` and ``os`` are in the cache.

    Examples:
        >>> cache = show_module_caching()
        >>> cache["json"]
        True
    """
    import os  # noqa: F401 — intentional for demo

    report = {
        "json": "json" in sys.modules,
        "os": "os" in sys.modules,
        "nonexistent_xyz": "nonexistent_xyz" in sys.modules,
    }
    print("  sys.modules cache check:")
    for name, cached in report.items():
        print(f"    {name!r}: {'cached' if cached else 'not loaded'}")
    return report


# ─── Section 6: importlib.reload (concept #12) ───


def demonstrate_reload() -> str:
    """Show how ``importlib.reload()`` works.

    Reloads the ``json`` module as a safe, side-effect-free example.

    Returns:
        The ``json`` module's file path after reload.

    Examples:
        >>> path = demonstrate_reload()
        >>> "json" in path
        True
    """
    reloaded = importlib.reload(json)
    file_path = getattr(reloaded, "__file__", "built-in")
    print(f"  importlib.reload(json) → file: {file_path}")
    return file_path or "built-in"


# ─── Section 7: Standard library tour (concept #13) ───


def stdlib_highlights() -> dict[str, str]:
    """Return a curated map of must-know stdlib modules.

    Returns:
        Dict of module name → one-line purpose.

    Examples:
        >>> highlights = stdlib_highlights()
        >>> "pathlib" in highlights
        True
    """
    modules: dict[str, str] = {
        "os": "OS interface — env vars, process control",
        "sys": "Interpreter config — argv, path, modules",
        "pathlib": "OOP file paths — Path.read_text(), glob()",
        "json": "JSON encode/decode — load, dump, loads, dumps",
        "csv": "CSV reading/writing — DictReader, writer",
        "collections": "Specialised containers — Counter, defaultdict, deque",
        "itertools": "Iterator building blocks — chain, islice, groupby",
        "functools": "Higher-order helpers — lru_cache, partial, wraps",
        "logging": "Structured logging — handlers, formatters, levels",
        "typing": "Type hint support — Optional, Union, TypeVar",
    }
    print("  Standard library highlights:")
    for name, desc in modules.items():
        print(f"    {name:>12}: {desc}")
    return modules


# ─── Section 8: Third-party packages (concept #14) ───


def show_third_party_workflow() -> list[str]:
    """Describe the typical workflow for adding a third-party package.

    Returns:
        List of CLI commands in the recommended workflow.

    Examples:
        >>> steps = show_third_party_workflow()
        >>> any("install" in s for s in steps)
        True
    """
    steps = [
        "pip install requests           # classic",
        "uv add httpx                   # modern (uv)",
        "pip install -e .               # editable install",
        "pip freeze > requirements.txt  # pin versions",
    ]
    print("  Third-party package workflow:")
    for s in steps:
        print(f"    $ {s}")
    return steps


# ─── Section 9: Namespace packages (concept #15) ───


def describe_namespace_packages() -> str:
    """Explain PEP 420 implicit namespace packages.

    Returns:
        A summary string.

    Examples:
        >>> "no __init__.py" in describe_namespace_packages()
        True
    """
    summary = (
        "Namespace packages have no __init__.py. Python merges "
        "same-named directories across multiple sys.path entries "
        "into a single logical package. Used for plugin ecosystems "
        "and monorepo distribution splits."
    )
    print(f"  {summary}")
    return summary


# ─── Section 10: dir() / help() introspection (concept #16) ───


def introspect_module(module_name: str = "json") -> list[str]:
    """List public names of an already-imported module.

    Args:
        module_name: Name of a module present in ``sys.modules``.

    Returns:
        Sorted list of public (non-underscore) names.

    Raises:
        ValueError: If the module is not in ``sys.modules``.

    Examples:
        >>> names = introspect_module("json")
        >>> "dumps" in names
        True
    """
    mod = sys.modules.get(module_name)
    if mod is None:
        raise ValueError(
            f"module {module_name!r} not in sys.modules — import it first"
        )
    public = sorted(n for n in dir(mod) if not n.startswith("_"))
    print(f"  dir({module_name}) public names ({len(public)}):")
    print(f"    {public[:8]}{'...' if len(public) > 8 else ''}")
    return public


# ─── Section 11: Industrial — package split (concept #19) ───


def describe_package_split() -> dict[str, str]:
    """Show the before/after of splitting a monolithic module into a package.

    Returns:
        Dict with "before" and "after" layout descriptions.

    Examples:
        >>> result = describe_package_split()
        >>> "utils.py" in result["before"]
        True
    """
    result = {
        "before": "utils.py  (800 lines — parsing, validation, formatting)",
        "after": (
            "utils/\n"
            "  __init__.py   (re-exports: from .parsing import parse_config)\n"
            "  parsing.py    (200 lines)\n"
            "  validation.py (250 lines)\n"
            "  formatting.py (200 lines)"
        ),
    }
    print("  Package split — before:")
    print(f"    {result['before']}")
    print("  Package split — after:")
    for line in result["after"].splitlines():
        print(f"    {line}")
    return result


# ─── Self-checks ───

if __name__ == "__main__":
    print("=" * 60)
    print("Day 11 — Modules and Packages: code.py demos")
    print("=" * 60)

    print("\n--- 1. Import basics ---")
    forms = show_import_basics()
    print(f"  forms returned: {list(forms.keys())}")
    # Expected output:
    #     import: import math          → math.sqrt(4)
    #       from: from math import sqrt → sqrt(4)
    #         as: import numpy as np   → np.array([1])

    print("\n--- 2. __name__ guard ---")
    role = show_name_guard(__name__)
    print(f"  role = {role!r}")
    # Expected output:
    #   __name__ = '__main__' → role = script

    print("\n--- 3. Package layout ---")
    describe_package_layout()
    # Expected output: canonical package tree

    print("\n--- 4. Runnable package ---")
    describe_runnable_package()
    # Expected output: __main__.py description

    print("\n--- 5. Relative imports ---")
    show_relative_import_forms()
    # Expected output: three relative import examples

    print("\n--- 6. __all__ ---")
    demonstrate_all()
    # Expected output: __all__ = ['public_func', 'PublicClass']

    print("\n--- 7. sys.path ---")
    inspect_sys_path(4)
    # Expected output: first 4 sys.path entries

    print("\n--- 8. Module caching ---")
    show_module_caching()
    # Expected output: json: cached, os: cached, nonexistent_xyz: not loaded

    print("\n--- 9. importlib.reload ---")
    demonstrate_reload()
    # Expected output: importlib.reload(json) → file: .../json/__init__.py

    print("\n--- 10. Stdlib highlights ---")
    stdlib_highlights()
    # Expected output: 10-row table of module → purpose

    print("\n--- 11. Third-party workflow ---")
    show_third_party_workflow()
    # Expected output: 4 CLI commands

    print("\n--- 12. Namespace packages ---")
    describe_namespace_packages()
    # Expected output: PEP 420 explanation

    print("\n--- 13. Introspect module ---")
    introspect_module("json")
    # Expected output: public names of json module

    print("\n--- 14. Package split ---")
    describe_package_split()
    # Expected output: before/after layout

    print("\n" + "=" * 60)
    print("code.py: all demos completed ✓")
