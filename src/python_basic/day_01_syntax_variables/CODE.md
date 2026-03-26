# Day 01 — Syntax, Types & Variables

> **TL;DR:** Variables, type hints, f-strings, and input validation are where production reliability starts. `code.py` shows small typed utility functions that validate inputs and return predictable outputs — the same style used in APIs, CLIs, and data pipelines.

## Concepts

| Concept | What it does | Why it matters | `code.py` ref |
|---------|-------------|----------------|---------------|
| `strip()` | Removes leading/trailing whitespace from strings | Prevents blank-input bugs in user-facing flows | `build_welcome_message` |
| `ValueError` | Exception for values that exist but violate rules | Explicit errors > silent fallbacks; easier debugging | all validation functions |
| `int()` | Converts a value to integer | Parsing CLI/env input safely | `parse_retry_count` |
| `round()` | Rounds float to N decimal places | Clean currency/metric output | `calculate_invoice_total` |
| `Final` | Typing hint marking a constant | Signals "don't reassign" to readers and static tools | module-level constants |
| f-string | Inline variable interpolation in strings | Readable log/output formatting without concatenation | all functions |
| Type hints | Annotate parameter and return types | Self-documenting signatures; enables mypy checks | all function signatures |

## Pitfalls

- Mixing string and number operations without conversion — causes `TypeError` at runtime.
- Using unclear names (`x`, `temp`) in business logic — kills code review speed.
- Catching all exceptions silently (`except: pass`) — hides bugs in production.
- Printing instead of returning from reusable functions — makes code untestable.

## Why this design

Pure functions with explicit return values and typed signatures. Easy to test, reuse across API handlers, CLI tools, and pipelines. Validation raises immediately rather than returning sentinel values.

## Further reading

- [Python Type Hints Cheat Sheet (mypy)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) — quick reference for annotations
- [PEP 498 — f-strings](https://peps.python.org/pep-0498/) — the spec behind formatted string literals
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) — naming, docstrings, error handling conventions
