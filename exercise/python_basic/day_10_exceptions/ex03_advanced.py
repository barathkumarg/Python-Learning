# ex03_advanced.py — Day 10: Exceptions — Advanced

"""
Advanced exercises for Exceptions.
Covers checklist items: #12, #15–#16, #18–#19, #22.

Instructions:
- Implement each function/class where you see TODO.
- Run this file to verify: python ex03_advanced.py
- All asserts must pass.
- Requires Python 3.11+ for ExceptionGroup / except*.
"""

from __future__ import annotations

import contextlib  # noqa: F401 (used in implementation)
import time  # noqa: F401 (used in implementation)
import traceback  # noqa: F401 (used in implementation)
import warnings
from collections.abc import Callable
from typing import Any
import functools


def format_traceback(exc: BaseException) -> str:
    """Format an exception's traceback as a string (concept #15).

    Uses ``traceback.format_exception`` to produce the full traceback text.

    Args:
        exc: An exception instance (should have been raised/caught so it
             carries a traceback, or may have None traceback).

    Returns:
        Multi-line traceback string, or the exception repr if no traceback.

    Examples:
        >>> try:
        ...     1 / 0
        ... except ZeroDivisionError as e:
        ...     tb = format_traceback(e)
        >>> "ZeroDivisionError" in tb
        True
    """
    # TODO: Implement this function
    # 1. Use traceback.format_exception(type(exc), exc, exc.__traceback__)
    # 2. Join the list into a single string and return it
    return "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))




def deprecated_add(a: float, b: float) -> float:
    """Add two numbers, but warn that this function is deprecated (concept #16).

    Emits a ``DeprecationWarning`` with the message
    ``"deprecated_add is deprecated, use operator.add"``.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.

    Examples:
        >>> import warnings
        >>> with warnings.catch_warnings(record=True) as w:
        ...     warnings.simplefilter("always")
        ...     result = deprecated_add(2, 3)
        ...     assert len(w) == 1
        ...     assert issubclass(w[0].category, DeprecationWarning)
        >>> result
        5
    """
    # TODO: Implement this function
    # 1. warnings.warn("deprecated_add is deprecated, use operator.add",
    #                   DeprecationWarning, stacklevel=2)
    # 2. return a + b
    warnings.warn(
        "deprecated_add is deprecated, use operator.add",
        DeprecationWarning,
        stacklevel=2,
    )
    return a + b


def safe_delete_key(d: dict[str, Any], key: str) -> dict[str, Any]:
    """Delete *key* from dict *d* using ``contextlib.suppress`` (concept #19).

    Does nothing if key is absent — no exception propagates.

    Args:
        d: Dictionary to modify in place.
        key: Key to remove.

    Returns:
        The same dict (modified in place).

    Examples:
        >>> safe_delete_key({"a": 1, "b": 2}, "a")
        {'b': 2}
        >>> safe_delete_key({"a": 1}, "z")
        {'a': 1}
    """
    # TODO: Implement this function
    # 1. with contextlib.suppress(KeyError): del d[key]
    # 2. return d
    with contextlib.suppress(KeyError): del d[key]
    return d


def retry(
    max_attempts: int = 3,
    delay: float = 0.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable:
    """Decorator: retry a function on specified exceptions (concept #22).

    Re-raises the last exception after *max_attempts* failures.

    Args:
        max_attempts: Total attempts before giving up (must be >= 1).
        delay: Seconds to sleep between retries.
        exceptions: Tuple of exception types to catch.

    Returns:
        Decorator wrapping the target function.

    Examples:
        >>> call_count = 0
        >>> @retry(max_attempts=3, delay=0, exceptions=(ValueError,))
        ... def flaky():
        ...     global call_count
        ...     call_count += 1
        ...     if call_count < 3:
        ...         raise ValueError("not yet")
        ...     return "ok"
        >>> flaky()
        'ok'
        >>> call_count
        3
    """
    # TODO: Implement this function
    # 1. Define outer decorator that takes func
    # 2. Inside wrapper: loop max_attempts times
    #    a. try: return func(*args, **kwargs)
    #    b. except exceptions as exc: if last attempt, raise; else time.sleep(delay)
    # 3. Use functools.wraps for proper decoration

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


class ManagedResource:
    """Context manager that suppresses ``ValueError`` (concept #18).

    Demonstrates ``__exit__`` receiving exception info.

    Attributes:
        entered: Set to True after __enter__.
        exited: Set to True after __exit__.
        suppressed: Type name of suppressed exception, or None.

    Examples:
        >>> with ManagedResource() as r:
        ...     raise ValueError("test")
        >>> r.suppressed
        'ValueError'
        >>> r.exited
        True
    """

    # TODO: Implement this class
    # 1. __init__: set entered=False, exited=False, suppressed=None
    # 2. __enter__: set entered=True, return self
    # 3. __exit__(self, exc_type, exc_val, exc_tb):
    #    a. set exited=True
    #    b. if exc_type is ValueError: set suppressed=exc_type.__name__, return True
    #    c. else: return False (propagate)
    ...
    def __init__(self):
        self.entered = False
        self.exited = False
        self.suppressed = None

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exited = True
        if exc_type is ValueError:
            self.suppressed = exc_type.__name__
            return True
        return False


def validate_batch(
    items: list[Any],
    validator: Callable[[Any], Any],
) -> list[Any]:
    """Validate each item, collecting errors into an ``ExceptionGroup`` (concept #12).

    Calls *validator(item)* for each item. Collects all failures.
    If any failures, raises ``ExceptionGroup("validation errors", [...])``.

    Args:
        items: Values to validate.
        validator: Callable that raises on invalid input.

    Returns:
        List of validated (returned) values if all pass.

    Raises:
        ExceptionGroup: Containing all individual exceptions.

    Examples:
        >>> def must_be_positive(x):
        ...     if x <= 0: raise ValueError(f"non-positive: {x}")
        ...     return x
        >>> validate_batch([1, 2, 3], must_be_positive)
        [1, 2, 3]
        >>> validate_batch([1, -2, 3, -4], must_be_positive)
        Traceback (most recent call last):
        ...
        ExceptionGroup: validation errors (2 sub-exceptions)
    """
    # TODO: Implement this function
    # 1. Loop through items, try validator(item)
    # 2. Collect successes in results list, failures in errors list
    # 3. If errors: raise ExceptionGroup("validation errors", errors)
    # 4. Else: return results
    results = []
    errors = []

    for item in items:
        try:
            results.append(validator(item))
        except Exception as exc:
            errors.append(exc)

    if errors:
        raise ExceptionGroup("validation errors", errors)
    return results


if __name__ == "__main__":
    # --- format_traceback ---
    try:
        1 / 0  # noqa: B018
    except ZeroDivisionError as exc:
        tb_str = format_traceback(exc)
    assert "ZeroDivisionError" in tb_str
    print("format_traceback       ✓")
    # Expected output: format_traceback       ✓

    # --- deprecated_add ---
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = deprecated_add(2, 3)
        assert result == 5
        assert len(caught) == 1
        assert issubclass(caught[0].category, DeprecationWarning)
    print("deprecated_add         ✓")
    # Expected output: deprecated_add         ✓

    # --- safe_delete_key ---
    assert safe_delete_key({"a": 1, "b": 2}, "a") == {"b": 2}
    assert safe_delete_key({"a": 1}, "z") == {"a": 1}
    print("safe_delete_key        ✓")
    # Expected output: safe_delete_key        ✓

    # --- retry ---
    attempt_count = 0

    @retry(max_attempts=3, delay=0, exceptions=(ValueError,))
    def flaky_function() -> str:
        global attempt_count  # noqa: PLW0603
        attempt_count += 1
        if attempt_count < 3:
            raise ValueError("not yet")
        return "ok"

    assert flaky_function() == "ok"
    assert attempt_count == 3

    # Verify it re-raises after exhausting attempts
    @retry(max_attempts=2, delay=0, exceptions=(RuntimeError,))
    def always_fails() -> None:
        raise RuntimeError("permanent")

    try:
        always_fails()
        assert False, "should have raised"
    except RuntimeError as exc:
        assert "permanent" in str(exc)
    print("retry                  ✓")
    # Expected output: retry                  ✓

    # --- ManagedResource ---
    with ManagedResource() as res:
        raise ValueError("ignored")
    assert res.entered is True
    assert res.exited is True
    assert res.suppressed == "ValueError"

    try:
        with ManagedResource() as res2:
            raise TypeError("propagated")
        assert False, "should have raised"
    except TypeError:
        pass
    assert res2.exited is True
    assert res2.suppressed is None
    print("ManagedResource        ✓")
    # Expected output: ManagedResource        ✓

    # --- validate_batch ---
    def must_be_positive(x: int) -> int:
        if x <= 0:
            raise ValueError(f"non-positive: {x}")
        return x

    assert validate_batch([1, 2, 3], must_be_positive) == [1, 2, 3]
    try:
        validate_batch([1, -2, 3, -4], must_be_positive)
        assert False, "should have raised"
    except ExceptionGroup as eg:  # noqa: F821
        assert len(eg.exceptions) == 2
    print("validate_batch         ✓")
    # Expected output: validate_batch         ✓

    print("\n✅ All ex03_advanced assertions passed!")
