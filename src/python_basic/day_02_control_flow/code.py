"""Day 02 reference code: control flow patterns for order state handling.

Design choices:
- Guard clauses keep invalid states out of the main logic paths.
- `match` expresses allowed transitions explicitly (no silent fallthrough).
- Bounded loops with `else` communicate timeouts instead of hanging forever.
"""

from __future__ import annotations

from typing import Callable, Iterable, Final

TERMINAL_STATUSES: Final[set[str]] = {"shipped", "cancelled"}


def normalize_status(raw_status: str) -> str:
    """Normalize an order status string and validate it.

    Args:
        raw_status: User- or system-supplied status label.

    Returns:
        Lowercase status constrained to the allowed set.

    Raises:
        ValueError: If the status is empty or not supported.
    """
    normalized = raw_status.strip().lower()
    allowed = {"created", "paid", "shipped", "cancelled"}
    if normalized not in allowed:
        raise ValueError(f"unsupported status: {raw_status!r}")
    return normalized


def transition_order_status(current: str, action: str) -> str:
    """Compute the next status using a small state machine.

    Args:
        current: Current order status.
        action: Event applied to the order (e.g., "pay", "ship", "cancel").

    Returns:
        Next legal status string.

    Raises:
        ValueError: If the transition is not allowed.
    """
    current_norm = normalize_status(current)
    action_norm = action.strip().lower()

    match (current_norm, action_norm):
        case ("created", "pay"):
            return "paid"
        case ("paid", "ship"):
            return "shipped"
        case ("created" | "paid", "cancel"):
            return "cancelled"
        case _:
            raise ValueError(f"illegal transition: {current_norm} + {action_norm}")


def collect_high_value_orders(orders: Iterable[dict[str, object]], threshold: float) -> list[str]:
    """Return IDs of orders whose totals meet or exceed the threshold.

    Demonstrates `continue` to skip low-value orders without nested conditionals.

    Args:
        orders: Iterable of order payloads containing `id` and `total`.
        threshold: Minimum revenue to include.

    Returns:
        List of qualifying order IDs.

    Raises:
        ValueError: If threshold is negative or order payloads are malformed.
    """
    if threshold < 0:
        raise ValueError("threshold must be non-negative")

    selected: list[str] = []
    for order in orders:
        try:
            total = float(order["total"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("order must include numeric 'total'") from exc

        if total < threshold:
            continue

        order_id = str(order.get("id", "")).strip()
        if not order_id:
            raise ValueError("order must include non-empty 'id'")
        selected.append(order_id)

    return selected


def wait_for_terminal_status(poll: Callable[[], str], max_checks: int = 5) -> str:
    """Poll for a terminal status with a bounded while/else loop.

    Args:
        poll: Zero-argument callable returning a status string on each call.
        max_checks: Maximum number of polls before raising `TimeoutError`.

    Returns:
        Terminal status when observed within the allotted checks.

    Raises:
        TimeoutError: If no terminal status is seen before `max_checks` elapse.
        ValueError: If `max_checks` is less than 1.
    """
    if max_checks < 1:
        raise ValueError("max_checks must be >= 1")

    attempts = 0
    while attempts < max_checks:
        status = normalize_status(poll())
        if status in TERMINAL_STATUSES:
            return status
        attempts += 1
    raise TimeoutError("status not reached before timeout")


def first_paid_order(order_feed: Iterable[tuple[str, str]]) -> str | None:
    """Return the first order ID that reached `paid`, or `None` if none did.

    Demonstrates `for` / `else` to separate found vs exhausted outcomes.

    Args:
        order_feed: Iterable of `(order_id, status)` tuples.

    Returns:
        Order ID when a `paid` status is encountered, otherwise `None`.
    """
    for order_id, status in order_feed:
        if normalize_status(status) == "paid":
            return order_id
    else:
        return None


if __name__ == "__main__":
    sample_orders = [
        {"id": "A1", "total": 120.0},
        {"id": "B2", "total": 40.0},
        {"id": "C3", "total": 220.0},
    ]

    # Expected output: next status: paid
    print("next status:", transition_order_status("created", "pay"))
    # Expected output: high value: ['A1', 'C3']
    print("high value:", collect_high_value_orders(sample_orders, threshold=100))

    def mock_poll_factory(statuses: list[str]) -> Callable[[], str]:
        def poll() -> str:
            return statuses.pop(0) if statuses else "created"

        return poll

    poller = mock_poll_factory(["created", "paid", "shipped"])
    # Expected output: terminal status: shipped
    print("terminal status:", wait_for_terminal_status(poller, max_checks=3))
    # Expected output: first paid order: O2
    print("first paid order:", first_paid_order([("O1", "created"), ("O2", "paid")]))
