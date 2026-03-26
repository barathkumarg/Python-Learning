"""Day 01 reference code: Python syntax and variables in production style.

This module demonstrates how to:
- Define typed variables and constants
- Use clear naming and f-strings
- Validate input with explicit exceptions
- Keep functions small and reusable
"""

from __future__ import annotations

from typing import Final

APP_NAME: Final[str] = "Python Learning"
MAX_RETRY_COUNT: Final[int] = 3


def build_welcome_message(user_name: str) -> str:
    """Return a formatted welcome message.

    Args:
        user_name: End-user display name.

    Returns:
        Readable welcome text.

    Raises:
        ValueError: If `user_name` is blank.
    """
    cleaned_name = user_name.strip()
    if not cleaned_name:
        raise ValueError("user_name must not be empty")
    return f"Welcome {cleaned_name}! Ready to master Python?"


def parse_retry_count(raw_value: str) -> int:
    """Parse retry count from string input with validation."""
    try:
        count = int(raw_value)
    except ValueError as exc:
        raise ValueError("retry count must be an integer") from exc

    if count < 0:
        raise ValueError("retry count must be >= 0")
    if count > MAX_RETRY_COUNT:
        raise ValueError(f"retry count must be <= {MAX_RETRY_COUNT}")
    return count


def calculate_invoice_total(unit_price: float, quantity: int, tax_rate: float = 0.18) -> float:
    """Calculate total invoice amount with tax."""
    if unit_price < 0:
        raise ValueError("unit_price must be >= 0")
    if quantity < 0:
        raise ValueError("quantity must be >= 0")
    if not 0 <= tax_rate <= 1:
        raise ValueError("tax_rate must be between 0 and 1")

    subtotal = unit_price * quantity
    total = subtotal * (1 + tax_rate)
    return round(total, 2)


def summarize_runtime_config(env: str, debug: bool, workers: int) -> str:
    """Return a one-line runtime config summary for logs."""
    if workers <= 0:
        raise ValueError("workers must be > 0")
    return f"app={APP_NAME} env={env} debug={debug} workers={workers}"


if __name__ == "__main__":
    print(build_welcome_message("Barath"))
    print(f"Accepted retry count: {parse_retry_count('2')}")
    print(f"Invoice total: {calculate_invoice_total(199.99, 2)}")
    print(summarize_runtime_config(env="dev", debug=True, workers=2))
