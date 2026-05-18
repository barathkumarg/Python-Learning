# ex02_intermediate.py — Day 12: Built-ins in Pipelines — Intermediate

"""
Intermediate exercises for Built-ins in Pipelines.
Covers checklist items: #6–#13 (map, filter, any, all, sum, min/max,
abs/round/divmod, len/range).

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex02_intermediate.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any


def apply_discount(prices: Iterable[float], rate: float) -> Iterator[float]:
    """Apply a discount ``rate`` lazily using :func:`map` (concept #6).

    Args:
        prices: Iterable of non-negative prices.
        rate: Discount rate in ``[0.0, 1.0]``.

    Returns:
        Iterator of ``price * (1 - rate)`` (lazy — NOT a list).

    Raises:
        ValueError: If ``rate`` is outside ``[0, 1]``.

    Examples:
        >>> list(apply_discount([100.0, 50.0], 0.10))
        [90.0, 45.0]
    """
    # TODO:
    # 1. If not (0.0 <= rate <= 1.0): raise ValueError(f"rate must be in [0,1], got {rate!r}").
    # 2. Return map(lambda p: p * (1 - rate), prices)  — do NOT wrap in list().
    if rate < 0.0 or rate > 1.0:
        raise ValueError("Values not in range")
    return map(lambda p: p * (1 - rate), prices)


def drop_disabled(users: Iterable[dict[str, Any]]) -> Iterator[dict[str, Any]]:
    """Filter out users whose ``enabled`` is falsy using :func:`filter` (concept #7).

    Args:
        users: Iterable of user dicts.

    Returns:
        Lazy iterator of enabled users.

    Examples:
        >>> list(drop_disabled([{"id": 1, "enabled": True}, {"id": 2, "enabled": False}]))
        [{'id': 1, 'enabled': True}]
    """
    # TODO: return filter(lambda u: bool(u.get("enabled")), users)
    return  filter(lambda u: bool(u.get('enabled')), users )


def any_overdue(invoices: Iterable[dict[str, Any]]) -> bool:
    """Return True if **any** invoice has ``overdue=True`` (concept #8).

    Must short-circuit on the first match.

    Args:
        invoices: Iterable of invoice dicts.

    Returns:
        ``True`` as soon as an overdue invoice is seen, else ``False``.

    Examples:
        >>> any_overdue([{"id": 1, "overdue": False}, {"id": 2, "overdue": True}])
        True
        >>> any_overdue([])
        False
    """
    # TODO: return any(bool(inv.get("overdue")) for inv in invoices)
    return any(bool(inv.get("overdue")) for inv in invoices)

def all_paid(invoices: Iterable[dict[str, Any]]) -> bool:
    """Return True iff **every** invoice has ``paid=True`` (concept #9).

    Note: ``all([])`` is ``True`` (vacuous truth) — that is the expected behavior.

    Args:
        invoices: Iterable of invoice dicts.

    Returns:
        ``True`` only if every invoice is paid (or list is empty).

    Examples:
        >>> all_paid([{"paid": True}, {"paid": True}])
        True
        >>> all_paid([{"paid": True}, {"paid": False}])
        False
        >>> all_paid([])
        True
    """
    # TODO: return all(bool(inv.get("paid")) for inv in invoices)
    return all(bool(inv.get("paid")) for inv in invoices)


def safe_total(amounts: Iterable[float]) -> float:
    """Sum ``amounts`` returning ``0.0`` on empty input (concept #10).

    Args:
        amounts: Iterable of numeric amounts.

    Returns:
        Total as float.

    Examples:
        >>> safe_total([1.5, 2.5])
        4.0
        >>> safe_total([])
        0.0
    """
    # TODO: return float(sum(amounts, start=0.0))
    return float(sum(amounts, start=0.0))


def cheapest_item(items: list[dict[str, Any]], default: dict[str, Any] | None = None) -> dict[str, Any] | None:
    """Return the item with the lowest ``price`` using :func:`min` (concept #11).

    Use ``default=`` so empty input does not raise.

    Args:
        items: Items with a ``price`` numeric key.
        default: Returned when ``items`` is empty.

    Returns:
        Cheapest item or ``default``.

    Raises:
        ValueError: If any item is missing ``price``.

    Examples:
        >>> cheapest_item([{"sku": "A", "price": 10}, {"sku": "B", "price": 5}])
        {'sku': 'B', 'price': 5}
        >>> cheapest_item([], default=None) is None
        True
    """
    # TODO:
    # 1. Validate every item has "price".
    # 2. Return min(items, key=lambda it: it["price"], default=default).
    for item in items:
        if item.get('price') is None:
            return ValueError("price key not found")
    return min(items, key=lambda price: price["price"], default=default)

def format_hms(seconds: int) -> str:
    """Format ``seconds`` as ``HH:MM:SS`` using :func:`divmod` (concept #12).

    Args:
        seconds: Non-negative duration.

    Returns:
        Zero-padded ``HH:MM:SS``.

    Raises:
        ValueError: If ``seconds`` is negative.

    Examples:
        >>> format_hms(3725)
        '01:02:05'
        >>> format_hms(0)
        '00:00:00'
    """
    # TODO:
    # 1. If seconds < 0: raise ValueError(f"seconds must be >= 0, got {seconds!r}").
    # 2. h, rest = divmod(seconds, 3600); m, s = divmod(rest, 60).
    # 3. Return f"{h:02d}:{m:02d}:{s:02d}".
    if seconds < 0:
        raise ValueError(f"Seconds must be greater than 0")
    h, rest = divmod(seconds, 3600)
    m, s = divmod(rest, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def paginate(total: int, size: int) -> list[tuple[int, int]]:
    """Generate ``(start, end)`` slice indices using :func:`range` and :func:`len` (concept #13).

    Args:
        total: Total item count (>= 0).
        size: Batch size (> 0).

    Returns:
        List of half-open ``(start, end)`` index pairs.

    Raises:
        ValueError: If ``total < 0`` or ``size <= 0``.

    Examples:
        >>> paginate(7, 3)
        [(0, 3), (3, 6), (6, 7)]
        >>> paginate(0, 3)
        []
    """
    # TODO:
    # 1. Validate total >= 0 and size > 0.
    # 2. pairs = [(i, min(i + size, total)) for i in range(0, total, size)].
    # 3. Use len(pairs) to sanity-check expected page count if you like.
    if total < 0 or size <= 0:
        raise ValueError("Insufficient Total or size value")
    return  [(i, min(i+size, total)) for i in range(0, total, size)]


if __name__ == "__main__":
    # ─── apply_discount checks ───
    out = apply_discount([100.0, 50.0], 0.10)
    assert iter(out) is out, "apply_discount must return a lazy iterator"
    assert list(out) == [90.0, 45.0], "10% discount"
    try:
        list(apply_discount([10.0], 1.5))
    except ValueError:
        pass
    else:
        raise AssertionError("rate > 1 must raise")

    # ─── drop_disabled checks ───
    users = [{"id": 1, "enabled": True}, {"id": 2, "enabled": False}, {"id": 3, "enabled": True}]
    assert [u["id"] for u in drop_disabled(users)] == [1, 3], "keep enabled only"

    # ─── any_overdue / all_paid checks ───
    assert any_overdue([{"overdue": False}, {"overdue": True}]) is True
    assert any_overdue([]) is False, "any([]) is False"
    assert all_paid([{"paid": True}, {"paid": True}]) is True
    assert all_paid([{"paid": True}, {"paid": False}]) is False
    assert all_paid([]) is True, "all([]) is True (vacuous)"

    # ─── safe_total checks ───
    assert safe_total([1.5, 2.5, 3.0]) == 7.0
    assert safe_total([]) == 0.0, "empty -> 0.0, not error"

    # ─── cheapest_item checks ───
    assert cheapest_item([{"sku": "A", "price": 10}, {"sku": "B", "price": 5}])["sku"] == "B"
    assert cheapest_item([], default=None) is None, "default on empty"

    # ─── format_hms checks ───
    assert format_hms(3725) == "01:02:05"
    assert format_hms(0) == "00:00:00"
    try:
        format_hms(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative seconds must raise")

    # ─── paginate checks ───
    assert paginate(7, 3) == [(0, 3), (3, 6), (6, 7)]
    assert paginate(0, 3) == []
    try:
        paginate(10, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("size <= 0 must raise")

    print("ex02_intermediate.py: all asserts passed ✓")
