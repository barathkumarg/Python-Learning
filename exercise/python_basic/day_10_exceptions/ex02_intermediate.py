# ex02_intermediate.py — Day 10: Exceptions — Intermediate

"""
Intermediate exercises for Exceptions.
Covers checklist items: #6–#12, #23.

Instructions:
- Implement each function/class where you see TODO.
- Run this file to verify: python ex02_intermediate.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations


def validate_age(age: object) -> int:
    """Validate and return *age* as an integer in 0–150.

    Demonstrates `raise` (concept #6).

    Args:
        age: Value to validate.

    Returns:
        The validated age.

    Raises:
        TypeError: If age is not an int (include the actual type in message).
        ValueError: If age is outside 0–150 (include the value in message).

    Examples:
        >>> validate_age(25)
        25
        >>> validate_age("old")
        Traceback (most recent call last):
        ...
        TypeError: age must be int, got str
        >>> validate_age(200)
        Traceback (most recent call last):
        ...
        ValueError: age must be 0..150, got 200
    """
    # TODO: Implement this function
    # 1. if not isinstance(age, int) or isinstance(age, bool): raise TypeError
    # 2. if age < 0 or age > 150: raise ValueError with the value
    # 3. return age
    raise NotImplementedError()


def log_and_reraise(func: object, *args: object) -> object:
    """Call *func(*args)*; on exception, print it, then re-raise.

    Demonstrates bare `raise` for re-raising (concept #7).

    Args:
        func: Callable to invoke.
        *args: Arguments forwarded to func.

    Returns:
        Return value of func if no exception.

    Raises:
        Any exception from func, after printing ``"Error: <message>"``.

    Examples:
        >>> log_and_reraise(int, "5")
        5
        >>> log_and_reraise(int, "x")  # prints "Error: ..." then raises ValueError
    """
    # TODO: Implement this function
    # 1. try: return func(*args)
    # 2. except Exception as exc: print(f"Error: {exc}"), then bare `raise`
    raise NotImplementedError()


def convert_config_value(raw: str) -> int:
    """Convert a config string to int, chaining on failure.

    Demonstrates `raise ... from ...` (concept #8).

    Args:
        raw: Raw config string to parse as int.

    Returns:
        Parsed integer.

    Raises:
        RuntimeError: Chained from the original ValueError.

    Examples:
        >>> convert_config_value("42")
        42
        >>> convert_config_value("abc")
        Traceback (most recent call last):
        ...
        RuntimeError: invalid config value: 'abc'
    """
    # TODO: Implement this function
    # 1. try: return int(raw)
    # 2. except ValueError as exc:
    #        raise RuntimeError(f"invalid config value: {raw!r}") from exc
    raise NotImplementedError()


def classify_exception(exc: BaseException) -> str:
    """Classify an exception into a hierarchy category (concept #9).

    Order matters: check subclasses before parents.

    Args:
        exc: An exception instance.

    Returns:
        ``"value"`` for ValueError or subclass,
        ``"os"`` for OSError or subclass (FileNotFoundError, PermissionError),
        ``"other"`` for other Exception subclasses,
        ``"base"`` for BaseException-only (KeyboardInterrupt, SystemExit).

    Examples:
        >>> classify_exception(ValueError("x"))
        'value'
        >>> classify_exception(FileNotFoundError("f"))
        'os'
        >>> classify_exception(KeyboardInterrupt())
        'base'
        >>> classify_exception(RuntimeError("r"))
        'other'
    """
    # TODO: Implement this function
    # 1. isinstance checks: ValueError → "value", OSError → "os",
    #    Exception → "other", BaseException → "base"
    # IMPORTANT: check more specific types FIRST
    raise NotImplementedError()


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds available balance.

    Custom exception with fields (concepts #10, #11, #23).

    Attributes:
        balance: Current account balance.
        amount: Requested withdrawal amount.
        deficit: How much is short (computed property).

    Examples:
        >>> e = InsufficientFundsError(100.0, 250.0)
        >>> e.balance
        100.0
        >>> e.amount
        250.0
        >>> e.deficit
        150.0
        >>> str(e)
        'cannot withdraw 250.0: balance is 100.0 (short 150.0)'
    """

    # TODO: Implement this class
    # 1. __init__(self, balance: float, amount: float) → store fields, call super().__init__(msg)
    # 2. @property deficit → self.amount - self.balance
    # 3. __str__ → descriptive message with balance, amount, deficit
    ...


def withdraw(balance: float, amount: float) -> float:
    """Withdraw *amount* from *balance*; raise on insufficient funds.

    Uses the custom domain error (concept #23).

    Args:
        balance: Current balance.
        amount: Amount to withdraw (must be > 0).

    Returns:
        New balance after withdrawal.

    Raises:
        ValueError: If amount <= 0.
        InsufficientFundsError: If amount > balance.

    Examples:
        >>> withdraw(500.0, 200.0)
        300.0
        >>> withdraw(100.0, 250.0)
        Traceback (most recent call last):
        ...
        InsufficientFundsError: cannot withdraw 250.0: balance is 100.0 (short 150.0)
    """
    # TODO: Implement this function
    # 1. Validate amount > 0, else raise ValueError
    # 2. If amount > balance: raise InsufficientFundsError(balance, amount)
    # 3. return balance - amount
    raise NotImplementedError()


if __name__ == "__main__":
    # --- validate_age ---
    assert validate_age(25) == 25
    assert validate_age(0) == 0
    try:
        validate_age("old")
        assert False, "should have raised TypeError"
    except TypeError as exc:
        assert "str" in str(exc)
    try:
        validate_age(200)
        assert False, "should have raised ValueError"
    except ValueError as exc:
        assert "200" in str(exc)
    print("validate_age           ✓")
    # Expected output: validate_age           ✓

    # --- log_and_reraise ---
    assert log_and_reraise(int, "5") == 5
    try:
        log_and_reraise(int, "x")
        assert False, "should have raised"
    except ValueError:
        pass  # re-raised after print
    print("log_and_reraise        ✓")
    # Expected output:
    # Error: invalid literal for int() with base 10: 'x'
    # log_and_reraise        ✓

    # --- convert_config_value ---
    assert convert_config_value("42") == 42
    try:
        convert_config_value("abc")
        assert False, "should have raised"
    except RuntimeError as exc:
        assert exc.__cause__ is not None  # chained from ValueError
        assert isinstance(exc.__cause__, ValueError)
    print("convert_config_value   ✓")
    # Expected output: convert_config_value   ✓

    # --- classify_exception ---
    assert classify_exception(ValueError("x")) == "value"
    assert classify_exception(FileNotFoundError("f")) == "os"
    assert classify_exception(KeyboardInterrupt()) == "base"
    assert classify_exception(RuntimeError("r")) == "other"
    print("classify_exception     ✓")
    # Expected output: classify_exception     ✓

    # --- InsufficientFundsError ---
    err = InsufficientFundsError(100.0, 250.0)
    assert err.balance == 100.0
    assert err.amount == 250.0
    assert err.deficit == 150.0
    assert "100.0" in str(err) and "250.0" in str(err)
    print("InsufficientFundsError ✓")
    # Expected output: InsufficientFundsError ✓

    # --- withdraw ---
    assert withdraw(500.0, 200.0) == 300.0
    try:
        withdraw(100.0, 250.0)
        assert False, "should have raised"
    except InsufficientFundsError as exc:
        assert exc.deficit == 150.0
    try:
        withdraw(100.0, -10.0)
        assert False, "should have raised ValueError"
    except ValueError:
        pass
    print("withdraw               ✓")
    # Expected output: withdraw               ✓

    print("\n✅ All ex02_intermediate assertions passed!")
