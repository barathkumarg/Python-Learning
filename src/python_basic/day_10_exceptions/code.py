# code.py — Day 10: Exceptions

"""Exceptions — production-style reference implementations.

Covers concepts #1–#23: try/except/else/finally, raise, re-raise, chaining,
custom exception hierarchies, ExceptionGroup, assert, EAFP, traceback, warnings,
OS errors, context-manager exception handling, suppress, retry wrapper, and
domain-error hierarchy.

Style: typed signatures, Google docstrings, explicit ValueError validation,
errors fail loudly with the offending value in the message, and low-level
errors are wrapped via `raise ... from ...` to preserve cause.
"""

from __future__ import annotations

import logging
import time
import traceback
import warnings
from contextlib import suppress
from pathlib import Path
from types import TracebackType
from typing import Callable, TypeVar

T = TypeVar("T")

log = logging.getLogger(__name__)


# ─── Section 1: Domain error hierarchy (concepts #9, #10, #11, #23) ───


class DomainError(Exception):
    """Base class for all application-domain errors."""


class ValidationError(DomainError):
    """Raised when user input fails validation.

    Carries structured fields so callers (e.g. an HTTP handler) can render
    machine-readable error responses without parsing the message.
    """

    def __init__(self, field: str, value: object, reason: str) -> None:
        super().__init__(f"{field}={value!r}: {reason}")
        self.field = field
        self.value = value
        self.reason = reason


class ConfigError(DomainError):
    """Raised when application configuration cannot be loaded."""


class TransientError(DomainError):
    """Recoverable error — safe to retry with backoff."""


# ─── Section 2: try/except/else/finally + assert (concepts #1, #4, #5, #13) ───


def safe_divide(numerator: float, denominator: float) -> float:
    """Divide two numbers with explicit error handling.

    Demonstrates the full try/except/else/finally structure plus an `assert`
    used as an internal invariant (never for user-input validation).

    Args:
        numerator: The dividend.
        denominator: The divisor; must be non-zero and finite.

    Returns:
        The quotient.

    Raises:
        ValueError: If denominator is zero.
        TypeError: If either argument is not a number.

    Examples:
        >>> safe_divide(10, 4)
        2.5
    """
    if not isinstance(numerator, (int, float)) or not isinstance(
        denominator, (int, float)
    ):
        raise TypeError(
            f"both args must be numbers, got "
            f"{type(numerator).__name__} and {type(denominator).__name__}"
        )
    try:
        result = numerator / denominator
    except ZeroDivisionError as exc:
        raise ValueError(
            f"denominator must be non-zero, got {denominator!r}"
        ) from exc
    else:
        # internal invariant — disabled with `python -O`
        assert isinstance(result, float), "division must yield float"
        return result
    finally:
        log.debug("safe_divide(%r, %r) finished", numerator, denominator)


# ─── Section 3: Multiple except + as alias + EAFP (concepts #2, #3, #14) ───


def parse_int_safe(value: object) -> int:
    """Parse a value as int, wrapping low-level errors.

    EAFP style — try the conversion and catch failures rather than checking
    types up front (concept #14). Catches multiple exception types and binds
    them with `as` for the wrapped message (concepts #2, #3).

    Args:
        value: Anything `int()` accepts (str, bytes, number).

    Returns:
        The parsed integer.

    Raises:
        ValueError: If the value cannot be converted; original error chained.

    Examples:
        >>> parse_int_safe("42")
        42
    """
    try:
        return int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError) as exc:
        raise ValueError(f"cannot parse {value!r} as int") from exc


# ─── Section 4: raise + re-raise + traceback (concepts #6, #7, #15) ───


def validate_age(age: int) -> int:
    """Validate that an age is a plausible integer.

    Demonstrates explicit `raise` (concept #6) and the exception hierarchy
    (concept #9) — `Exception` catches both `TypeError` and `ValueError`.

    Args:
        age: Candidate age.

    Returns:
        The same age, unchanged.

    Raises:
        TypeError: If `age` is not an int.
        ValueError: If `age` is outside [0, 150].

    Examples:
        >>> validate_age(30)
        30
    """
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be 0..150, got {age}")
    return age


def log_and_reraise(fn: Callable[[], T]) -> T:
    """Run `fn`, log a structured traceback on failure, then re-raise.

    Demonstrates re-raise (concept #7) and the `traceback` module (concept #15).
    The bare `raise` preserves the original traceback — `raise exc` would not.

    Args:
        fn: Zero-arg callable to execute.

    Returns:
        Whatever `fn` returns.

    Raises:
        Exception: Re-raises any exception from `fn` after logging.

    Examples:
        >>> log_and_reraise(lambda: 1 + 1)
        2
    """
    try:
        return fn()
    except Exception:
        log.error("operation failed:\n%s", traceback.format_exc())
        raise  # bare re-raise — keeps original traceback


# ─── Section 5: Chaining + OS errors (concepts #8, #17) ───


def load_user_config(path: str | Path) -> str:
    """Read a config file, wrapping `FileNotFoundError` as `ConfigError`.

    Demonstrates chaining with `from` (concept #8) and concrete `OSError`
    subclasses (concept #17). The original `FileNotFoundError` remains
    accessible via `__cause__` for diagnostics.

    Args:
        path: Path to the config file.

    Returns:
        File contents as text.

    Raises:
        ConfigError: If the file is missing or unreadable. Original error
            preserved as the `__cause__`.

    Examples:
        >>> load_user_config("/definitely/missing.txt")  # doctest: +SKIP
    """
    if not path:
        raise ValueError(f"path must be non-empty, got {path!r}")
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ConfigError(f"config file missing: {path}") from exc
    except PermissionError as exc:
        raise ConfigError(f"config file unreadable: {path}") from exc


# ─── Section 6: ExceptionGroup (concept #12) ───


def validate_batch(values: list[object]) -> list[int]:
    """Validate every value in a batch; raise an `ExceptionGroup` if any fail.

    Demonstrates `ExceptionGroup` (concept #12, Python 3.11+). Callers can use
    `except* ValueError:` to handle just the validation errors.

    Args:
        values: Items to parse as ints.

    Returns:
        Successfully parsed ints (only when all succeed).

    Raises:
        ExceptionGroup: One ValueError per failing item, batched together.
        ValueError: If `values` is empty.

    Examples:
        >>> validate_batch(["1", "2", "3"])
        [1, 2, 3]
    """
    if not values:
        raise ValueError("values must be non-empty")
    parsed: list[int] = []
    errors: list[Exception] = []
    for i, v in enumerate(values):
        try:
            parsed.append(parse_int_safe(v))
        except ValueError as exc:
            errors.append(ValueError(f"index {i}: {exc}"))
    if errors:
        raise ExceptionGroup("batch validation failed", errors)  # noqa: F821 — Py3.11+
    return parsed


# ─── Section 7: warnings module (concept #16) ───


def legacy_api(x: int) -> int:
    """Doubled value — kept for backward compatibility.

    Demonstrates `warnings.warn` (concept #16) for soft deprecation: callers
    keep working but get a `DeprecationWarning` they can surface in tests.

    Args:
        x: The integer to double.

    Returns:
        `x * 2`.

    Raises:
        ValueError: If `x` is not an int.

    Examples:
        >>> legacy_api(3)
        6
    """
    if not isinstance(x, int):
        raise ValueError(f"x must be int, got {type(x).__name__}")
    warnings.warn(
        "legacy_api is deprecated; use modern_api instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return x * 2


# ─── Section 8: Context manager exception handling (concept #18) ───


class Transaction:
    """A toy transactional context manager.

    Demonstrates how `__exit__` can observe exceptions (concept #18).
    Returns `False` so exceptions propagate; returning `True` would suppress.
    """

    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError(f"name must be non-empty, got {name!r}")
        self.name = name
        self.committed = False
        self.rolled_back = False

    def __enter__(self) -> Transaction:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        if exc_type is None:
            self.committed = True
        else:
            self.rolled_back = True
        return False  # never suppress — propagate


# ─── Industrial Patterns ───


def retry(
    fn: Callable[[], T],
    *,
    attempts: int = 3,
    base_delay: float = 0.0,
    sleep: Callable[[float], None] = time.sleep,
) -> T:
    """Run `fn` with exponential backoff on transient errors.

    Industrial pattern (concept #22). Retries only on `TransientError`,
    `TimeoutError`, and `ConnectionError` — never on `ValueError`.

    Args:
        fn: Zero-arg callable.
        attempts: Maximum total attempts (including the first).
        base_delay: Initial delay in seconds; doubles each retry.
        sleep: Injected sleep — replace with no-op for tests.

    Returns:
        Whatever `fn` returns on the first successful attempt.

    Raises:
        ValueError: If `attempts < 1` or `base_delay < 0`.
        Exception: Last transient exception if all attempts are exhausted.

    Examples:
        >>> retry(lambda: 1, attempts=1)
        1
    """
    if attempts < 1:
        raise ValueError(f"attempts must be >= 1, got {attempts}")
    if base_delay < 0:
        raise ValueError(f"base_delay must be >= 0, got {base_delay}")
    last_exc: Exception | None = None
    for i in range(1, attempts + 1):
        try:
            return fn()
        except (TransientError, TimeoutError, ConnectionError) as exc:
            last_exc = exc
            if i == attempts:
                raise
            sleep(base_delay * (2 ** (i - 1)))
    # Defensive — unreachable because the loop above either returns or raises.
    raise RuntimeError("retry exhausted") from last_exc


def safe_cleanup(path: str | Path) -> bool:
    """Best-effort delete — uses `contextlib.suppress` (concept #19).

    Args:
        path: File to delete.

    Returns:
        True if the file existed and was deleted, False otherwise.

    Raises:
        ValueError: If `path` is empty.

    Examples:
        >>> safe_cleanup("/tmp/this-file-does-not-exist-xyz.txt")
        False
    """
    if not path:
        raise ValueError(f"path must be non-empty, got {path!r}")
    p = Path(path)
    existed = p.exists()
    with suppress(FileNotFoundError):
        p.unlink()
    return existed


# ─── Self-checks ───


if __name__ == "__main__":
    # safe_divide
    print(safe_divide(10, 4))
    # Expected output: 2.5
    try:
        safe_divide(1, 0)
    except ValueError as e:
        print(type(e).__name__, "-", e)
    # Expected output: ValueError - denominator must be non-zero, got 0

    # parse_int_safe
    print(parse_int_safe("42"))
    # Expected output: 42
    try:
        parse_int_safe("abc")
    except ValueError as e:
        print(type(e.__cause__).__name__)
    # Expected output: ValueError

    # validate_age
    print(validate_age(30))
    # Expected output: 30

    # log_and_reraise
    print(log_and_reraise(lambda: 1 + 1))
    # Expected output: 2

    # load_user_config (chained)
    try:
        load_user_config("/definitely/missing.cfg")
    except ConfigError as e:
        print(e, "| cause:", type(e.__cause__).__name__)
    # Expected output: config file missing: /definitely/missing.cfg | cause: FileNotFoundError

    # validate_batch — ExceptionGroup
    try:
        validate_batch(["1", "x", "3", "y"])
    except* ValueError as eg:
        print(f"errors: {len(eg.exceptions)}")
    # Expected output: errors: 2

    # legacy_api — warning
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        legacy_api(3)
        print(caught[0].category.__name__)
    # Expected output: DeprecationWarning

    # Transaction
    with Transaction("payments") as tx:
        pass
    print("committed:", tx.committed)
    # Expected output: committed: True
    tx2 = Transaction("payments")
    try:
        with tx2:
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    print("rolled_back:", tx2.rolled_back)
    # Expected output: rolled_back: True

    # retry — succeeds on second try
    calls = {"n": 0}

    def flaky() -> str:
        calls["n"] += 1
        if calls["n"] < 2:
            raise TransientError("flap")
        return "ok"

    print(retry(flaky, attempts=3, sleep=lambda _: None))
    # Expected output: ok

    # safe_cleanup
    print(safe_cleanup("/tmp/this-file-does-not-exist-xyz-day10.txt"))
    # Expected output: False
