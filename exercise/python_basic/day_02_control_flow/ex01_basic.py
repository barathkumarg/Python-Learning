"""ex01_basic — Order status transition via control flow.

Problem: Implement a small, explicit state machine for order statuses.
Signature: next_status(current: str, action: str) -> str
Constraints:
- Allowed statuses: created, paid, shipped, cancelled (case-insensitive inputs, lowercase outputs).
- Allowed actions: pay, ship, cancel.
- Invalid transitions must raise ValueError.

Examples:
>>> next_status("created", "pay")
'paid'
>>> next_status("paid", "cancel")
'cancelled'
>>> next_status("shipped", "pay")
ValueError
"""

from __future__ import annotations


def next_status(current: str, action: str) -> str:
    """Return the next order status or raise on an illegal transition."""
    # return "paid" when current="created" and action="pay"
    # return "shipped" when current="paid" and action="ship"
    # return "cancelled" when current in {"created", "paid"} and action="cancel"
    current = current.strip().lower()
    action = action.strip().lower()
    match (current, action):
        case ("created", "pay"):
            return "paid"
        case ("paid", "ship"):
            return "shipped"
        case ("created" | "paid", "cancel"):
            return "cancelled"
        case _:
            raise ValueError(
                f"illegal transition: {current!r} + {action!r}"
            )


if __name__ == "__main__":
    # Expected output: paid
    assert next_status("created", "pay") == "paid"
    # Expected output: shipped
    assert next_status("paid", "ship") == "shipped"
    # Expected output: cancelled
    assert next_status("created", "cancel") == "cancelled"
    assert next_status("paid", "cancel") == "cancelled"
    try:
        next_status("shipped", "pay")
    except ValueError:
        pass  # expected
    else:
        raise AssertionError("expected ValueError for illegal transition")
    print("ex01_basic: all asserts passed ✓")
