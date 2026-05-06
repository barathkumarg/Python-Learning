# Day 10 — Exceptions

> **TL;DR:** Exceptions are how Python signals and recovers from errors without
> riddling code with status checks. Day 10 covers `try/except/else/finally`,
> raising and chaining errors, custom exception hierarchies, the
> `BaseException` tree, `ExceptionGroup`, `assert`, EAFP vs LBYL, the
> `traceback` and `warnings` modules, and production patterns like retry
> wrappers and typed domain errors. `code.py` shows production-style helpers
> that fail loudly and predictably.

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|-------------|----------------|---------------|---------------|
| 1 | `try` / `except` | `try: ... except ValueError: ...` | Catch a specific error and recover | Foundation of error handling | Every API call, parse, file open | `safe_divide` |
| 2 | Multiple except | `except (TypeError, ValueError):` | Catch several types in one clause | DRY error handling | Validating mixed inputs | `parse_int_safe` |
| 3 | `as` alias | `except ValueError as exc:` | Bind exception to a name to inspect | Need details for logging / wrapping | Logging + error responses | `parse_int_safe` |
| 4 | `else` clause | `try: ... except ...: ... else: ...` | Runs only when no exception was raised | Separates success path from error path | Distinguishes "no error" from "handled error" | `safe_divide` |
| 5 | `finally` | `try: ... finally: ...` | Always runs — cleanup guaranteed | Resource cleanup even on error/return | Closing handles, releasing locks | `safe_divide` |
| 6 | `raise` | `raise ValueError("msg")` | Signal an error condition | Communicate violated invariants | Input validation, business rules | `validate_age` |
| 7 | Re-raise | bare `raise` inside `except` | Propagate after partial handling | Log then bubble up | Audit logging in middleware | `log_and_reraise` |
| 8 | Chaining `from` | `raise NewErr("…") from exc` | Preserve original cause | Full diagnostic context | Wrapping low-level errors as domain errors | `load_user_config` |
| 9 | Exception hierarchy | `BaseException → Exception → ValueError` | Categorize errors via inheritance | Catch by family, not by name | Catching `OSError` covers many subclasses | `validate_age` |
| 10 | Custom exception class | `class DomainError(Exception): ...` | Define project-specific error types | Distinguishes app errors from stdlib | Public API errors, billing errors | `DomainError`, `ValidationError` |
| 11 | Custom with fields | `__init__(self, value, field)` | Carry structured context on the error | Machine-readable error details | JSON error responses, retry decisions | `ValidationError` |
| 12 | `ExceptionGroup` (3.11+) | `except* ValueError:` | Handle several errors raised together | Concurrent / batch operations | `asyncio.TaskGroup`, batch validators | `validate_batch` |
| 13 | `assert` | `assert x > 0, "must be positive"` | Internal invariant — strippable in `-O` | Self-documenting checks for **devs**, not users | Test helpers, debug builds | `safe_divide` (dev-only) |
| 14 | LBYL vs EAFP | "look before you leap" vs "easier to ask forgiveness" | Two validation styles | EAFP is idiomatic Python | EAFP for race-prone I/O | `parse_int_safe` |
| 15 | `traceback` module | `traceback.format_exc()` | Capture stack trace as a string | Structured logs, error reporting | Sentry-style error capture | `log_and_reraise` |
| 16 | `warnings` module | `warnings.warn("deprecated", DeprecationWarning)` | Non-fatal advisory messages | Soft signals (deprecation, perf) | Library API deprecation | `legacy_api` |
| 17 | OS errors | `FileNotFoundError`, `PermissionError` | Concrete subclasses of `OSError` | Catch specific failures, not all I/O | File handlers, network code | `load_user_config` |
| 18 | Context manager exc handling | `__exit__(exc_type, exc, tb)` | CM observes/suppresses exceptions | Centralizes cleanup + suppression | DB transactions, locks | `Transaction` |
| 19 | `contextlib.suppress` | `with suppress(FileNotFoundError):` | Ignore a specific exception type | Replaces empty except blocks | Best-effort cleanup, idempotent ops | snippet |
| 20 | Anti-pattern: bare `except:` | `except:` | Catches `KeyboardInterrupt`, `SystemExit` | Hides bugs and prevents Ctrl-C exit | Always specify exception type | snippet |
| 21 | Anti-pattern: silent `pass` | `except Exception: pass` | Swallows the error, no log | Bugs become invisible | Always log or re-raise | snippet |
| 22 | Industrial: retry wrapper | exponential backoff on transient errors | Retries flaky operations with delay | Handles network jitter, rate limits | HTTP clients, DB connections | `retry` |
| 23 | Industrial: domain errors | typed hierarchy: `BillingError → CardDeclined` | Stable public error contract | Lets callers catch the right family | REST/RPC error codes, SDKs | `DomainError` tree |

## Snippets

### 1. Basic `try` / `except` / `else` / `finally`

The four-clause structure separates the happy path, recovery, and cleanup.

```python
def parse_int(s: str) -> int | None:
    try:
        n = int(s)
    except ValueError:
        return None
    else:
        return n              # only when no exception
    finally:
        print("done")          # always runs

print(parse_int("42"))
print(parse_int("oops"))
```

Expected output:
```text
done
42
done
None
```

> 💡 `else` runs *only* if `try` succeeded — never put success logic inside `try`.

### 2. Catching multiple exceptions and binding with `as`

```python
def parse_int_safe(s: object) -> int:
    try:
        return int(s)               # type: ignore[arg-type]
    except (TypeError, ValueError) as exc:
        raise ValueError(f"cannot parse {s!r} as int") from exc

print(parse_int_safe("7"))
try:
    parse_int_safe(None)
except ValueError as e:
    print(f"caught: {e}")
    print(f"cause:  {e.__cause__!r}")
```

Expected output:
```text
7
caught: cannot parse None as int
cause:  TypeError("int() argument must be a string, a bytes-like object or a real number, not 'NoneType'")
```

> 💡 Always pass `from exc` when re-raising — preserves the full cause chain.

### 3. Raising and the exception hierarchy

```python
def validate_age(age: int) -> int:
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be 0..150, got {age}")
    return age

try:
    validate_age(-3)
except Exception as e:        # Exception covers ValueError + TypeError
    print(f"{type(e).__name__}: {e}")
```

Expected output:
```text
ValueError: age must be 0..150, got -3
```

> 💡 Catch the **most specific** type that still expresses your intent.

### 4. Custom exception with structured fields

Domain errors carry the data needed to render a useful response.

```python
class ValidationError(Exception):
    def __init__(self, field: str, value: object, reason: str) -> None:
        super().__init__(f"{field}={value!r}: {reason}")
        self.field = field
        self.value = value
        self.reason = reason

try:
    raise ValidationError("email", "x@", "missing domain")
except ValidationError as e:
    print(e.field, e.value, e.reason)
```

Expected output:
```text
email 'x@' missing domain
```

> 💡 Subclass `Exception`, never `BaseException` — leave that for `KeyboardInterrupt`/`SystemExit`.

### 5. Chaining (`raise … from …`) — wrapping low-level errors

```python
class ConfigError(Exception): ...

def load_config(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as f:
            return {"raw": f.read()}
    except FileNotFoundError as exc:
        raise ConfigError(f"config file missing: {path}") from exc

try:
    load_config("/nope.json")
except ConfigError as e:
    print(e)
    print("caused by:", type(e.__cause__).__name__)
```

Expected output:
```text
config file missing: /nope.json
caused by: FileNotFoundError
```

> 💡 Use `from None` to *suppress* the cause when it leaks internals.

### 6. EAFP vs LBYL

EAFP ("easier to ask forgiveness than permission") is the Pythonic style.

```python
data = {"name": "Alice"}

# LBYL — race-prone, more code
if "name" in data and isinstance(data["name"], str):
    upper = data["name"].upper()

# EAFP — idiomatic
try:
    upper = data["name"].upper()
except (KeyError, AttributeError):
    upper = ""

print(upper)
```

Expected output:
```text
ALICE
```

> 💡 Prefer EAFP for I/O and dict access — avoids TOCTOU races.

### 7. `contextlib.suppress` and `finally` cleanup

```python
from contextlib import suppress
from pathlib import Path

p = Path("/tmp/maybe-missing.txt")
with suppress(FileNotFoundError):
    p.unlink()                 # idempotent delete
print("cleanup done")
```

Expected output:
```text
cleanup done
```

> 💡 `suppress` only catches the exact types listed — never use it as a blanket.

### 8. `ExceptionGroup` and `except*` (Python 3.11+)

```python
def validate_all(items: list[int]) -> None:
    errors = [ValueError(f"bad: {x}") for x in items if x < 0]
    if errors:
        raise ExceptionGroup("validation failed", errors)

try:
    validate_all([1, -2, 3, -4])
except* ValueError as eg:
    print(f"{len(eg.exceptions)} validation errors")
```

Expected output:
```text
2 validation errors
```

> 💡 Use `ExceptionGroup` for batch / concurrent failures — preserves every cause.

### 9. Industrial: retry wrapper with backoff

```python
import time, random

def retry(fn, *, attempts: int = 3, base_delay: float = 0.0):
    for i in range(1, attempts + 1):
        try:
            return fn()
        except (TimeoutError, ConnectionError) as exc:
            if i == attempts:
                raise
            time.sleep(base_delay * (2 ** (i - 1)))
    raise RuntimeError("unreachable")

random.seed(0)
calls = {"n": 0}
def flaky() -> str:
    calls["n"] += 1
    if calls["n"] < 2:
        raise ConnectionError("flap")
    return "ok"

print(retry(flaky, attempts=3))
print("calls:", calls["n"])
```

Expected output:
```text
ok
calls: 2
```

> 💡 Retry **only** transient errors (network, timeouts) — never `ValueError`.

## Anti-patterns

### Anti-pattern: bare `except:`
```python
# ❌ Bad — catches KeyboardInterrupt, SystemExit, MemoryError
try:
    do_work()
except:
    print("oops")

# ✅ Corrected — name the exact errors you can recover from
try:
    do_work()
except (TimeoutError, ConnectionError) as exc:
    log.warning("transient: %s", exc)
    raise
```
> Bare `except` masks real bugs and prevents Ctrl-C from terminating the program.

### Anti-pattern: silent `pass`
```python
# ❌ Bad — error is invisible, no signal, no log
try:
    risky()
except Exception:
    pass

# ✅ Corrected — log, narrow, and decide explicitly
try:
    risky()
except RetryableError as exc:
    log.warning("retrying after %r", exc)
    schedule_retry()
```
> "Silent except" is the #1 source of unreproducible production bugs.

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| Domain error hierarchy | `class BillingError(Exception); class CardDeclined(BillingError)` | Stable public API errors callers can `except` precisely |
| Wrap low-level errors | `raise ConfigError(...) from FileNotFoundError(...)` | Hide stdlib internals while preserving cause |
| Retry with backoff | `retry(fn, attempts=3, base_delay=0.2)` | Network calls, DB connects, rate-limited APIs |
| Structured logging on re-raise | `log.exception("during %s", op); raise` | Audit trails — keep stack trace, propagate error |

## Pitfalls

- **Catching `Exception` too high** — masks bugs. Catch specific types close to where you can recover.
- **`raise exc` vs `raise`** — bare `raise` keeps the original traceback; `raise exc` resets it.
- **`assert` for input validation** — disabled by `python -O`. Always use `if … raise ValueError`.
- **Silently swallowing `KeyboardInterrupt`** — `except BaseException:` and bare `except:` both do this.
- **Forgetting `from exc`** — chained errors lose context: you see the wrapper, not the cause.

## Why this design

`code.py` exposes typed helpers that **fail loudly with descriptive messages**,
**chain low-level errors** into domain errors, and **use `else`/`finally`**
clauses correctly. Every custom exception subclasses `Exception` (never
`BaseException`) and carries structured fields so callers can render JSON
responses or take retry decisions without parsing strings.

## Further reading

- [Python tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — official walk-through of the syntax and hierarchy
- [Real Python — Python Exceptions: An Introduction](https://realpython.com/python-exceptions/) — practical guide to try/except/finally and custom errors
- [PEP 3134 — Exception Chaining](https://peps.python.org/pep-3134/) — rationale for `raise … from …`
- [PEP 654 — Exception Groups and `except*`](https://peps.python.org/pep-0654/) — design behind 3.11+ exception groups
- [Python docs — `contextlib.suppress`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress) — when targeted suppression is OK
