# ex01_basic.py — Day 11: Modules and Packages — All-in-One

"""
All-in-one exercises for Modules and Packages.
Covers checklist items: #1–#20.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex01_basic.py
- All asserts must pass.
"""

from __future__ import annotations

import sys
from types import ModuleType


# ─── #1–#3: Import forms ───


def describe_import_forms() -> dict[str, str]:
    """Return a dict with keys 'import', 'from', 'as' mapping to example strings.

    Each value must be a one-line example of that import form.

    Returns:
        Dict with exactly three keys: 'import', 'from', 'as'.

    Examples:
        >>> result = describe_import_forms()
        >>> sorted(result.keys())
        ['as', 'from', 'import']
        >>> 'import' in result['import']
        True
    """
    # TODO: Implement this function
    # Return a dict like:
    return {"import": "import math", "from": "from math import sqrt", "as": "import numpy as np"}


# ─── #2, #3, #8, #15, #18: Classify import statements ───


def classify_import_statement(stmt: str) -> str:
    """Classify a Python import statement string.

    Rules:
    - Contains 'import *'        → 'star'
    - Starts with 'from .'       → 'relative'
    - Contains ' as '            → 'alias'
    - Otherwise                  → 'absolute'

    Apply rules in the order above (first match wins).

    Args:
        stmt: A single import statement string.

    Returns:
        One of 'star', 'relative', 'alias', 'absolute'.

    Raises:
        ValueError: If *stmt* is empty.

    Examples:
        >>> classify_import_statement("from os import *")
        'star'
        >>> classify_import_statement("from . import utils")
        'relative'
        >>> classify_import_statement("import numpy as np")
        'alias'
        >>> classify_import_statement("import os")
        'absolute'
    """
    # TODO: Implement this function
    if stmt == "":
        raise ValueError("Empty statement found")
    if "*" in stmt:
        return 'star'
    if "." in stmt:
        return 'relative'
    if "as" in stmt:
        return 'alias'
    else:
        return 'absolute'


# ─── #4, #5, #20: __name__ guard ───


def check_name_guard(module_name: str) -> str:
    """Return 'script' if module_name is '__main__', else 'library'.

    This mirrors the if __name__ == '__main__' guard and the concept
    of __main__.py for runnable packages.

    Args:
        module_name: The value of __name__ to inspect.

    Returns:
        'script' or 'library'.

    Raises:
        ValueError: If *module_name* is empty.

    Examples:
        >>> check_name_guard("__main__")
        'script'
        >>> check_name_guard("mypackage.utils")
        'library'
    """
    # TODO: Implement this function
    if not module_name:
        raise ValueError("module_name must not be empty")
    is_main = module_name == "__main__"
    role = "script" if is_main else "library"
    print(f"  __name__ = {module_name!r} → role = {role}")
    return role



# ─── #6, #7: Package structure ───


def describe_package_tree(modules: list[str]) -> list[str]:
    """Given dotted module paths, return sorted unique directory components.

    Convert each dotted path into its directory parts (all segments except
    the last are packages). Return a sorted, deduplicated list of all
    package directories implied (using '/' separator).

    For 'mypackage.sub.module' the packages are 'mypackage' and 'mypackage/sub'.

    Args:
        modules: List of dotted module paths, e.g. ['pkg.sub.mod', 'pkg.utils'].

    Returns:
        Sorted list of unique package directory paths.

    Examples:
        >>> describe_package_tree(["pkg.sub.mod", "pkg.utils"])
        ['pkg', 'pkg/sub']
        >>> describe_package_tree([])
        []
    """
    # TODO: Implement this function
    # Hint: split each module by '.', build all parent paths
    packages = set()
    
    for module in modules:
        # Split the module path by dots
        parts = module.split('.')
        
        # Build all parent package paths (all segments except the last)
        for i in range(1, len(parts)):
            # Join the first i segments with '/' to form a package directory
            package_path = '/'.join(parts[:i])
            packages.add(package_path)
    
    return sorted(packages)


# ─── #9: __all__ ───


def build_all_list(names: list[str]) -> list[str]:
    """Filter a list of names to only public ones (no leading underscore).

    Args:
        names: Attribute names, e.g. ['foo', '_bar', '__baz', 'qux'].

    Returns:
        List of names that do NOT start with '_', preserving order.

    Examples:
        >>> build_all_list(["foo", "_bar", "__baz", "qux"])
        ['foo', 'qux']
        >>> build_all_list([])
        []
    """
    # TODO: Implement this function
    result = []
    for name in names:
        if not name.startswith('_'):
            result.append(name)
    return result


# ─── #10: sys.path ───


def search_sys_path(paths: list[str], substring: str) -> list[str]:
    """Return all entries from *paths* that contain *substring* (case-sensitive).

    Args:
        paths: List of directory path strings (like sys.path).
        substring: The substring to search for.

    Returns:
        List of matching paths, preserving order.

    Raises:
        ValueError: If *substring* is empty.

    Examples:
        >>> search_sys_path(["/usr/lib/python3", "/home/user/venv"], "venv")
        ['/home/user/venv']
    """
    # TODO: Implement this function
    result = []
    if substring == "":
        raise ValueError("Substring was empty")
    for path in paths:
        if substring in path:
            result.append(path)
    return result



# ─── #11, #12: Module caching ───


def is_module_cached(module_name: str) -> bool:
    """Check whether *module_name* is currently in sys.modules.

    Args:
        module_name: Dotted module name, e.g. 'os.path'.

    Returns:
        True if cached, False otherwise.

    Examples:
        >>> is_module_cached("sys")
        True
        >>> is_module_cached("this_does_not_exist_xyz")
        False
    """
    # TODO: Implement this function
    return module_name in sys.modules


# ─── #13, #14: stdlib vs third-party ───


def classify_module_origin(module_name: str) -> str:
    """Classify a module as 'stdlib', 'third_party', or 'unknown'.

    Strategy:
    - Try to import the module.
    - If it fails → 'unknown'.
    - If it succeeds, check the module's __file__ attribute:
      - None or missing → 'stdlib' (built-in like sys).
      - Contains 'site-packages' → 'third_party'.
      - Otherwise → 'stdlib'.

    Args:
        module_name: Name of the module to classify.

    Returns:
        'stdlib', 'third_party', or 'unknown'.

    Examples:
        >>> classify_module_origin("json")
        'stdlib'
        >>> classify_module_origin("nonexistent_pkg_xyz")
        'unknown'
    """
    import importlib
    try:
        # Attempt to import the module
        module = importlib.import_module(module_name)
    except ImportError:
        # Import failed
        return 'unknown'
    except Exception:
        # Catch other exceptions (e.g., SyntaxError during import)
        return 'unknown'
    
    # Check the __file__ attribute
    module_file = getattr(module, '__file__', None)
    
    if module_file is None:
        # Built-in module with no file (e.g., sys)
        return 'stdlib'
    
    # Check if 'site-packages' is in the path
    if 'site-packages' in module_file:
        return 'third_party'
    
    # Otherwise, assume stdlib
    return 'stdlib'
    


# ─── #16: dir() / help() ───


def list_public_names(module: ModuleType) -> list[str]:
    """Return sorted public attribute names of a module (no leading underscore).

    Args:
        module: An already-imported module object.

    Returns:
        Sorted list of public names.

    Examples:
        >>> import json
        >>> 'dumps' in list_public_names(json)
        True
    """
    # TODO: Implement this function
    # Hint: use dir(module) and filter
    return sorted([name for name in dir(module) if not name.startswith("_")])



# ─── #17: Circular import detection ───


def detect_circular_risk(deps: dict[str, list[str]]) -> list[tuple[str, str]]:
    """Find pairs (A, B) where A depends on B AND B depends on A.

    Args:
        deps: Mapping of module name → list of modules it imports.

    Returns:
        Sorted list of (A, B) tuples where A < B alphabetically,
        representing mutual dependency pairs.

    Examples:
        >>> detect_circular_risk({"a": ["b"], "b": ["a"]})
        [('a', 'b')]
        >>> detect_circular_risk({"a": ["b"], "b": ["c"]})
        []
    """
    circular_pairs = set()
    
    for module_a, imports_a in deps.items():
        # Check if any of the modules that A imports also import A
        for module_b in imports_a:
            # Skip self-loops (module importing itself)
            if module_a == module_b:
                continue
            
            # Get the list of imports for module_b (default to empty if not found)
            imports_b = deps.get(module_b, [])
            
            # If module_b also imports module_a, we have a circular dependency
            if module_a in imports_b:
                # Store as a normalized tuple (smaller name first) to avoid duplicates
                pair = tuple(sorted([module_a, module_b]))
                circular_pairs.add(pair)
    
    # Return sorted list of tuples
    return sorted(circular_pairs)


# ─── #19: Package split planning ───


def plan_package_split(modules: list[str]) -> dict[str, list[str]]:
    """Group module names by their first underscore-separated prefix.

    Args:
        modules: Flat list of module names like ['auth_login', 'auth_signup', 'db_connect'].

    Returns:
        Dict mapping prefix → list of module names with that prefix.

    Raises:
        ValueError: If any module name is empty.

    Examples:
        >>> plan_package_split(["auth_login", "auth_signup", "db_connect"])
        {'auth': ['auth_login', 'auth_signup'], 'db': ['db_connect']}
        >>> plan_package_split([])
        {}
    """
    # TODO: Implement this function
    # Hint: split on '_' and take the first segment as the group key
    result = {}
    
    for module in modules:
        # Check for empty module names
        if not module:
            raise ValueError("Module name cannot be empty")
        
        # Split on '_' and take the first segment as the prefix
        parts = module.split('_')
        prefix = parts[0]
        
        # Add module to the appropriate prefix group
        if prefix not in result:
            result[prefix] = []
        result[prefix].append(module)
    
    return result



# ─── Self-checks ───

if __name__ == "__main__":
    # ─── describe_import_forms ───
    forms = describe_import_forms()
    assert sorted(forms.keys()) == ["as", "from", "import"], "must have 3 keys"
    assert isinstance(forms["import"], str), "values must be strings"
    assert len(forms) == 3, "exactly three forms"

    # ─── classify_import_statement ───
    assert classify_import_statement("from os import *") == "star", "star import"
    assert classify_import_statement("from . import utils") == "relative", "relative"
    assert classify_import_statement("import numpy as np") == "alias", "alias"
    assert classify_import_statement("import os") == "absolute", "absolute"
    try:
        classify_import_statement("")
        assert False, "should raise ValueError on empty"
    except ValueError:
        pass

    # ─── check_name_guard ───
    assert check_name_guard("__main__") == "script", "__main__ is script"
    assert check_name_guard("mypackage") == "library", "non-main is library"
    try:
        check_name_guard("")
        assert False, "should raise ValueError on empty"
    except ValueError:
        pass

    # ─── describe_package_tree ───
    assert describe_package_tree(["pkg.sub.mod", "pkg.utils"]) == ["pkg", "pkg/sub"]
    assert describe_package_tree([]) == [], "empty input"
    assert describe_package_tree(["single"]) == [], "no packages for top-level module"

    # ─── build_all_list ───
    assert build_all_list(["foo", "_bar", "__baz", "qux"]) == ["foo", "qux"]
    assert build_all_list([]) == [], "empty input"
    assert build_all_list(["_private"]) == [], "all private"

    # ─── search_sys_path ───
    assert search_sys_path(["/usr/lib", "/home/venv"], "venv") == ["/home/venv"]
    assert search_sys_path(["/a", "/b"], "z") == [], "no match"
    try:
        search_sys_path(["/a"], "")
        assert False, "should raise ValueError on empty substring"
    except ValueError:
        pass

    # ─── is_module_cached ───
    assert is_module_cached("sys") is True, "sys is always cached"
    assert is_module_cached("nonexistent_xyz_999") is False, "unknown module"

    # ─── classify_module_origin ───
    assert classify_module_origin("json") == "stdlib", "json is stdlib"
    assert classify_module_origin("sys") == "stdlib", "sys is stdlib"
    assert classify_module_origin("no_such_pkg_xyz") == "unknown", "missing module"

    # ─── list_public_names ───
    import json as _json
    pub = list_public_names(_json)
    assert "dumps" in pub, "json.dumps is public"
    assert all(not n.startswith("_") for n in pub), "no private names"
    assert pub == sorted(pub), "must be sorted"

    # ─── detect_circular_risk ───
    assert detect_circular_risk({"a": ["b"], "b": ["a"]}) == [("a", "b")]
    assert detect_circular_risk({"a": ["b"], "b": ["c"]}) == []
    assert detect_circular_risk({}) == [], "empty graph"

    # ─── plan_package_split ───
    assert plan_package_split(["auth_login", "auth_signup", "db_connect"]) == {
        "auth": ["auth_login", "auth_signup"],
        "db": ["db_connect"],
    }
    assert plan_package_split([]) == {}, "empty input"
    try:
        plan_package_split([""])
        assert False, "should raise ValueError on empty name"
    except ValueError:
        pass

    print("ex01_basic.py: all asserts passed ✓")
