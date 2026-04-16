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
Expected output:
```text
strip("  Alice  ") -> "Alice"
strip("   ")       -> raises ValueError
```
> Always strip first, then validate. Skipping this lets `"   "` slip through as valid input.

**`int()` with safe conversion** — parse string input without crashing the caller.
```python
try:
    count = int(raw_value)
except ValueError as exc:
    raise ValueError("must be an integer") from exc
```Expected output:
```text
int("3")   -> 3
int("abc") -> raises ValueError
```> Chain with `from exc` so the original traceback isn’t lost during debugging.

**`Final` constant** — mark values that should never be reassigned.
```python
from typing import Final
MAX_RETRY: Final[int] = 3
```
Expected output:
```text
MAX_RETRY -> 3  (reassignment flagged by mypy)
```
> `Final` is a hint, not enforced at runtime. `mypy` catches accidental reassignment.

**f-string formatting** — embed variables directly, no concatenation needed.
```python
return f"app={APP_NAME} env={env} debug={debug}"
```
Expected output:
```text
"app=Python Learning env=dev debug=True"
```
> Prefer f-strings over `.format()` or `%` — shorter, faster, easier to read.

**Type hints on functions** — document what goes in and what comes out.
```python
def parse_retry_count(raw_value: str) -> int:
```
Expected output:
```text
parse_retry_count("2") -> 2  (mypy verifies str in, int out)
```
> Types make signatures self-documenting. Pair with `mypy` for static checking.

**Range validation with descriptive errors** — reject invalid values with context.
```python
def calculate_invoice_total(unit_price: float, quantity: int, tax_rate: float = 0.18) -> float:
    if unit_price < 0:
        raise ValueError(f"unit_price must be >= 0, got {unit_price}")
    if not 0 <= tax_rate <= 1:
        raise ValueError(f"tax_rate must be 0..1, got {tax_rate}")
    return round(unit_price * quantity * (1 + tax_rate), 2)
```
Expected output:
```text
calculate_invoice_total(199.99, 2) -> 471.98
calculate_invoice_total(-1, 2)     -> raises ValueError
```
> Include the actual value in error messages — faster debugging in logs.

**Anti-pattern → corrected pattern** — catch specific exceptions, not everything.
```python
# Anti-pattern: bare except hides bugs
try:
    count = int(raw)
except:
    count = 0  # silently swallows TypeError, KeyboardInterrupt, etc.

# Corrected: catch only what you expect
try:
    count = int(raw)
except ValueError as exc:
    raise ValueError(f"expected integer, got {raw!r}") from exc
```
Expected output:
```text
Anti-pattern: int("abc") -> silently returns 0 (bug hidden)
Corrected:    int("abc") -> raises ValueError with context
```
> Bare `except:` catches `SystemExit` and `KeyboardInterrupt` too — never use it.

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
