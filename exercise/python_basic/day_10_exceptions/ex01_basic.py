# ex01_basic.py — Day 10: Exceptions — Basic

"""
Basic exercises for Exceptions.
Covers checklist items: #1–#5, #13–#14, #17, #20–#21.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex01_basic.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations

from pathlib import Path


def safe_int_convert(value: str, fallback: int = 0) -> int:
    """Try to convert *value* to int; return *fallback* on failure.

    Demonstrates `try`/`except` (concept #1).
    Anti-pattern #21: do NOT silently `pass` — return the explicit fallback.

    Args:
        value: The string to convert.
        fallback: Value returned when conversion fails.

    Returns:
        Converted int, or *fallback* if conversion fails.

    Examples:
        >>> safe_int_convert("42")
        42
        >>> safe_int_convert("abc", -1)
        -1
        >>> safe_int_convert("", 0)
        0
    """
    # TODO: Implement this function
    # 1. try: return int(value)
    # 2. except (ValueError, TypeError): return fallback
    # 3. Do NOT use bare except or silent pass
    try:
        return int(value)
    except (ValueError, TypeError) as exception:
        return fallback


def parse_pair(text: str) -> tuple[str, int]:
    """Parse a ``"key:value"`` string into ``(key, int(value))``.

    Catches multiple exception types (concept #2) using EAFP style (concept #14).

    Args:
        text: String in ``"key:value"`` format.

    Returns:
        A tuple of (key, numeric_value).

    Raises:
        ValueError: If text cannot be split or value is not numeric.

    Examples:
        >>> parse_pair("port:8080")
        ('port', 8080)
        >>> parse_pair("bad")
        Traceback (most recent call last):
        ...
        ValueError: cannot parse pair from 'bad'
    """
    # TODO: Implement this function
    # 1. try: split text on ":", unpack into key and raw_value
    # 2. Convert raw_value to int
    # 3. except (ValueError, AttributeError): raise ValueError with descriptive msg
    try:
        key, value = text.split(":")
        return key, int(value) 
    except (ValueError, AttributeError) as exception:
        raise ValueError(f"cannot parse pair from {text}")


def describe_error(func: object, *args: object) -> str:
    """Call *func(*args)* and describe any exception raised.

    Uses `as` alias (concept #3). Must catch ``Exception``, NOT bare ``except:``
    (anti-pattern #20).

    Args:
        func: Callable to invoke.
        *args: Arguments forwarded to func.

    Returns:
        ``"ok"`` if no exception, or ``"<ExcType>: <message>"`` on failure.

    Examples:
        >>> describe_error(int, "5")
        'ok'
        >>> describe_error(int, "nope")
        "ValueError: invalid literal for int() with base 10: 'nope'"
    """
    # TODO: Implement this function
    # 1. try: call func(*args)
    # 2. except Exception as exc: return f"{type(exc).__name__}: {exc}"
    # 3. return "ok" if no exception
    # CRITICAL: do NOT use bare `except:` — always `except Exception as exc:`
    try:
        func(*args)
        return "ok"
    except Exception as exception:
        return f"{type(exception).__name__} : {exception}"



def safe_divide(a: float, b: float) -> float | None:
    """Divide *a* by *b*, using ``else`` for the success path.

    Demonstrates `else` clause (concept #4) and EAFP style (concept #14).

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        Result of a / b, or None if b is zero.

    Examples:
        >>> safe_divide(10, 3)
        3.3333333333333335
        >>> safe_divide(10, 0) is None
        True
    """
    # TODO: Implement this function
    # 1. try: result = a / b
    # 2. except ZeroDivisionError: return None
    # 3. else: return result   <-- runs only when no exception
    try:
        result = a / b
    except ZeroDivisionError as exception:
        return None 
    else:
        return result


def read_first_line(path: str | Path) -> str | None:
    """Read the first line of a file, with ``finally`` for cleanup.

    Demonstrates `finally` (concept #5) and OS errors (concept #17).

    Args:
        path: Path to the text file.

    Returns:
        First line stripped, or None if file not found.

    Side effect:
        Prints ``"cleanup done"`` via the finally block, always.

    Examples:
        >>> read_first_line("nonexistent.txt")  # prints "cleanup done"
        # returns None
    """
    # TODO: Implement this function
    # 1. try: open file, read first line
    # 2. except FileNotFoundError: result = None
    # 3. finally: print("cleanup done")
    # 4. return result
    try:
        with open(path, 'r') as f:
            return f.readline()
    except FileNotFoundError as file_exception:
        return None
    


def assert_positive(n: int | float) -> int | float:
    """Assert that *n* is positive (concept #13).

    Uses ``assert`` for dev-time invariant checks. Not for production validation.

    Args:
        n: Number to check.

    Returns:
        The number itself if positive.

    Raises:
        AssertionError: If n <= 0.

    Examples:
        >>> assert_positive(5)
        5
        >>> assert_positive(-1)
        Traceback (most recent call last):
        ...
        AssertionError: n must be positive, got -1
    """
    # TODO: Implement this function
    # 1. assert n > 0, f"n must be positive, got {n}"
    # 2. return n
    if n > 0:
        return n
    else:
        raise AssertionError(f"n must be positive got {n}")



if __name__ == "__main__":
    # --- safe_int_convert ---
    assert safe_int_convert("42") == 42
    assert safe_int_convert("abc", -1) == -1
    assert safe_int_convert("", 0) == 0
    print("safe_int_convert   ✓")
    # Expected output: safe_int_convert   ✓

    # --- parse_pair ---
    assert parse_pair("port:8080") == ("port", 8080)
    try:
        parse_pair("bad")
        assert False, "should have raised"
    except ValueError:
        pass
    print("parse_pair         ✓")
    # Expected output: parse_pair         ✓

    # --- describe_error ---
    assert describe_error(int, "5") == "ok"
    result = describe_error(int, "nope")
    assert "ValueError" in result
    print("describe_error     ✓")
    # Expected output: describe_error     ✓

    # --- safe_divide ---
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
    print("safe_divide        ✓")
    # Expected output: safe_divide        ✓

    # --- read_first_line ---
    result = read_first_line("__nonexistent_test_file__.txt")
    assert result is None
    print("read_first_line    ✓")
    # Expected output:
    # cleanup done
    # read_first_line    ✓

    # --- assert_positive ---
    assert assert_positive(5) == 5
    try:
        assert_positive(-1)
        assert False, "should have raised"
    except AssertionError:
        pass
    print("assert_positive    ✓")
    # Expected output: assert_positive    ✓

    print("\n✅ All ex01_basic assertions passed!")
