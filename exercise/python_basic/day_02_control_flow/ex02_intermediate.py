"""ex02_intermediate — Summarize orders using `continue` / `break`.

Problem: Iterate order records, skip those below a revenue threshold, stop when a
maximum number of qualifying orders is reached, and produce a small summary.
Signature: summarize_orders(orders, threshold, max_count) -> dict
Constraints:
- `threshold` must be >= 0; `max_count` must be >= 1.
- Each order is a dict with keys `id` (str) and `total` (numeric).
- Skip orders with missing/invalid totals; do not mutate the input list.

Examples:
>>> summarize_orders([{"id": "A1", "total": 120.0}, {"id": "B2", "total": 30.0}], 50, 2)
{'count': 1, 'total_revenue': 120.0, 'first_rejected': 'B2'}
>>> summarize_orders([], 10, 1)
{'count': 0, 'total_revenue': 0.0, 'first_rejected': None}
"""

from __future__ import annotations

from typing import Any, Dict, List


def summarize_orders(orders: List[Dict[str, Any]], threshold: float, max_count: int) -> Dict[str, float | int | str | None]:
    """Return summary of qualifying orders with loop control."""
    # validate threshold >= 0 and max_count >= 1, else raise ValueError
    if threshold < 0 or max_count < 1:
        raise ValueError("Threshold or max_count was not in range")

    total_revenue: float = 0.0
    count: int = 0
    first_rejected: str | None = None

    for order in orders:
        total = order.get("total")
        if not isinstance(total, (int, float)) or total < threshold:
            if first_rejected is None:
                first_rejected = order.get("id")
            continue

        count += 1
        total_revenue += float(total)

        # stop once max_count qualifying orders are collected (use break)
        if count >= max_count:
            break

    # build summary with keys: count (int), total_revenue (float), first_rejected (str | None)
    # return totals without mutating the input `orders`
    return {"count": count, "total_revenue": total_revenue, "first_rejected": first_rejected}


if __name__ == "__main__":
    sample = [
        {"id": "A1", "total": 120.0},
        {"id": "B2", "total": 30.0},
        {"id": "C3", "total": 220.0},
    ]
    result = summarize_orders(sample, threshold=50.0, max_count=2)
    assert result["count"] == 2
    assert abs(float(result["total_revenue"]) - 340.0) < 1e-6
    empty_result = summarize_orders([], threshold=10.0, max_count=1)
    assert empty_result["count"] == 0
    print("ex02: all asserts passed ✓")
