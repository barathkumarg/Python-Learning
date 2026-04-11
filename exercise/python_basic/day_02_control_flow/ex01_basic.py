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
    match (current, action):
        case ("created", "pay"):
            return "paid"
        case ("paid", "ship"):
            return "shipped"
        case ("created", "paid"):
            return "cancelled"
        case _:
            raise ValueError("Value not accepted")


if __name__ == "__main__":
    assert next_status("created", "pay") == "paid"
    assert next_status("paid", "ship") == "shipped"
    try:
        next_status("shipped", "pay")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for illegal transition")
    print("ex01: all asserts passed ✓")
