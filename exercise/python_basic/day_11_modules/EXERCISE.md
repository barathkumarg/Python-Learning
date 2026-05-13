# Day 11 — Modules and Packages: Exercises

> **Single-file format:** Because Day 11 concepts are largely declarative
> (import syntax, package layout, guards), all 20 checklist items are combined
> into one exercise file — `ex01_basic.py`.

## Learning objectives

After completing these exercises you will be able to:
1. Use all three import forms and explain when each is appropriate (#1–#3).
2. Write a correct `__name__` guard and describe `__main__.py` usage (#4–#5).
3. Describe package structure, `__init__.py`, relative imports, and `__all__` (#6–#9).
4. Inspect and manipulate the module search path and cache (#10–#12).
5. Navigate the standard library, install third-party packages, and use introspection tools (#13–#16).
6. Recognise anti-patterns (circular imports, `import *`) and apply industrial patterns (#17–#20).

## Skills assessed

| Skill ID | Skill | Exercise | Proficiency target |
|----------|-------|----------|-------------------|
| PY-08 | Modules & packages | ex01 | proficient |
| PY-03 | Input validation & error handling | ex01 | developing |
| PY-23 | Packaging & tooling | ex01 | developing |

## Concept coverage map

| # | Concept | Covered in |
|---|---------|------------|
| 1 | `import` | ex01 — `describe_import_forms` |
| 2 | `from ... import` | ex01 — `describe_import_forms` |
| 3 | `import ... as` | ex01 — `describe_import_forms` |
| 4 | `__name__` guard | ex01 — `check_name_guard` |
| 5 | `__main__.py` | ex01 — `check_name_guard` |
| 6 | Package structure | ex01 — `describe_package_tree` |
| 7 | `__init__.py` role | ex01 — `describe_package_tree` |
| 8 | Relative imports | ex01 — `classify_import_statement` |
| 9 | `__all__` | ex01 — `build_all_list` |
| 10 | `sys.path` | ex01 — `search_sys_path` |
| 11 | Module caching | ex01 — `is_module_cached` |
| 12 | `importlib.reload()` | ex01 — `is_module_cached` |
| 13 | Standard library tour | ex01 — `classify_module_origin` |
| 14 | Third-party packages | ex01 — `classify_module_origin` |
| 15 | Namespace packages | ex01 — `classify_import_statement` |
| 16 | `dir()` / `help()` | ex01 — `list_public_names` |
| 17 | Anti-pattern: circular imports | ex01 — `detect_circular_risk` |
| 18 | Anti-pattern: `import *` | ex01 — `classify_import_statement` |
| 19 | Industrial: package split | ex01 — `plan_package_split` |
| 20 | Industrial: runnable module | ex01 — `check_name_guard` |

---

## ex01_basic.py — Modules All-in-One (Checklist items #1–#20)

**Must-pass behaviors:**
- Correctly classify the three import forms and relative/star imports.
- Determine script vs library mode from a `__name__` value.
- Build an `__all__` list filtering out private names.
- Search `sys.path` entries for a substring.
- Detect circular import risk from a dependency mapping.

**Stretch behaviors:**
- Generate a package directory tree string from a flat list of modules.
- Propose a package split plan for a growing flat module list.

### Functions to implement:
1. `describe_import_forms()` — return a dict mapping the three import form names to example strings (#1–#3).
2. `classify_import_statement(stmt)` — given a string like `"from . import utils"`, return its kind: `"absolute"`, `"relative"`, `"star"`, or `"alias"` (#2, #3, #8, #15, #18).
3. `check_name_guard(module_name)` — return `"script"` or `"library"` (#4, #5, #20).
4. `describe_package_tree(modules)` — given a flat list of dotted module paths, return a sorted directory-style tree string (#6, #7).
5. `build_all_list(names)` — filter a list of names to only public ones (no leading `_`) (#9).
6. `search_sys_path(paths, substring)` — return paths containing the substring (#10).
7. `is_module_cached(module_name)` — check if a module name exists in `sys.modules` (#11, #12).
8. `classify_module_origin(module_name)` — return `"stdlib"`, `"third_party"`, or `"unknown"` (#13, #14).
9. `list_public_names(module)` — return sorted public attribute names of a module object (#16).
10. `detect_circular_risk(deps)` — given `{A: [B], B: [A]}` return pairs at risk (#17).
11. `plan_package_split(modules)` — group flat module names by common prefix (#19).

---

## Failure modes to watch for
- Confusing relative (`from .`) with absolute imports.
- Forgetting that `__all__` only affects `import *`, not direct imports.
- Returning unsorted results where sorted is expected.
- Not handling empty inputs (empty list, empty string).
@.agent.md @docs/RUBRIC.md @study_plan/python_basic.md @docs/SOURCE_REGISTRY.md

Generate ONLY exercise/python_basic/day_11_<slug>/ (EXERCISE.md + ex01–ex03).
Day 11 — Modules. Do NOT create CODE.md or code.py.

CRITICAL: Cover ALL items from the A-Z Concept Checklist for this day.
Follow the Exercise Structure Template. Map exercises to checklist concept ranges.
## Scoring

| Criterion | Max | ex01 |
|-----------|-----|------|
| Must-pass behaviors | 40 | |
| Stretch behaviors | 15 | |
| Inline asserts + AI-verified | 25 | |
| Style (types, ruff, docstrings) | 20 | |
| **Total** | **100** | |

## Suggested practice
- [Python docs — Modules tutorial](https://docs.python.org/3/tutorial/modules.html) — official walkthrough
- [Real Python — Python Modules and Packages](https://realpython.com/python-modules-packages/) — deeper dive

## Self-check commands
```bash
ruff check exercise/python_basic/day_11_modules/
python exercise/python_basic/day_11_modules/ex01_basic.py
```
