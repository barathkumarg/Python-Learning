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

## Snippets

**`strip()` + validation** — clean user input before any logic touches it.
```python
cleaned = user_name.strip()
if not cleaned:
    raise ValueError("user_name must not be empty")
```
> Always strip first, then validate. Skipping this lets `"   "` slip through as valid input.

**`int()` with safe conversion** — parse string input without crashing the caller.
```python
try:
    count = int(raw_value)
except ValueError as exc:
    raise ValueError("must be an integer") from exc
```
> Chain with `from exc` so the original traceback isn’t lost during debugging.

**`Final` constant** — mark values that should never be reassigned.
```python
from typing import Final
MAX_RETRY: Final[int] = 3
```
> `Final` is a hint, not enforced at runtime. `mypy` catches accidental reassignment.

**f-string formatting** — embed variables directly, no concatenation needed.
```python
return f"app={APP_NAME} env={env} debug={debug}"
```
> Prefer f-strings over `.format()` or `%` — shorter, faster, easier to read.

**Type hints on functions** — document what goes in and what comes out.
```python
def parse_retry_count(raw_value: str) -> int:
```
> Types make signatures self-documenting. Pair with `mypy` for static checking.

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
