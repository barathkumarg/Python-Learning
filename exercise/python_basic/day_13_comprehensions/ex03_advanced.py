# ex03_advanced.py — Day 13: Comprehensions — Advanced

"""
Advanced exercises for Comprehensions.
Covers checklist items: #16–#21 (readability limits, performance, itertools
bridge, over-nested anti-pattern, industrial filtered projection, industrial
index structure).

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex03_advanced.py
- All asserts must pass.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator  # noqa: F401  # Iterator used by learners after implementation
from itertools import count, islice  # noqa: F401  # used by learners inside first_n_squares
from typing import Any


def refactor_nested(workbook: list[list[list[Any]]]) -> list[str]:
    """Uppercase every non-empty string cell across a 3-D ``workbook`` (concepts #16, #19).

    A naive solution would write a 3-`for` nested comprehension — that is the
    over-nested anti-pattern documented in `CODE.md`. Your task is to keep
    the public comprehension to **at most one** `for` clause by extracting a
    private helper generator that does the deep iteration.

    Args:
        workbook: A list of sheets; each sheet is a list of rows; each row
            is a list of cells (mixed types).

    Returns:
        List of uppercased non-empty string cells in row-major order.

    Examples:
        >>> refactor_nested([[["a", " "], [None, "b"]], [["c", ""]]])
        ['A', 'B', 'C']
    """
    # TODO:
    # 1. Define a nested helper function `iter_string_cells(workbook)` that
    #    walks sheets -> rows -> cells with three `for` loops and `yield`s
    #    each cell that is a non-empty stripped string.
    # 2. The public return is a single-level list comprehension calling
    #    `.upper()` on every cell from that helper.
    # 3. The whole function body should contain at MOST one comprehension
    #    with one `for` clause.
    raise NotImplementedError("Implement refactor_nested")


def count_long_words(text: str, min_len: int) -> int:
    """Count words of length ``>= min_len`` lazily (concept #17).

    Must NOT build an intermediate list — pass a generator expression
    straight into ``sum``.

    Args:
        text: Free-form text. Words are whitespace-separated tokens.
        min_len: Non-negative length threshold.

    Returns:
        Number of qualifying words.

    Raises:
        ValueError: If ``min_len`` is negative.

    Examples:
        >>> count_long_words("the quick brown fox", min_len=4)
        2
    """
    # TODO:
    # 1. Reject negative `min_len` with a descriptive ValueError.
    # 2. Split `text` into words with .split().
    # 3. Use sum() over a generator expression that yields 1 for every word
    #    whose length is >= min_len. Do NOT call list(...) anywhere.
    # Sample: count_long_words("the quick brown fox", 4) -> 2.
    raise NotImplementedError("Implement count_long_words")


def first_n_squares(n: int) -> list[int]:
    """Return the squares of ``1..n`` using :func:`itertools.islice` (concept #18).

    Use ``itertools.count(1)`` as a (conceptually infinite) source and pull
    the first ``n`` values with ``islice``. Combine with a list comprehension
    that squares each value.

    Args:
        n: Non-negative count.

    Returns:
        ``[1, 4, 9, ..., n*n]`` (empty when ``n == 0``).

    Raises:
        ValueError: If ``n < 0``.

    Examples:
        >>> first_n_squares(4)
        [1, 4, 9, 16]
        >>> first_n_squares(0)
        []
    """
    # TODO:
    # 1. Reject negative `n` with a ValueError.
    # 2. Bridge: feed `count(1)` into `islice(..., n)` to get the first n
    #    naturals; then write a list comprehension squaring each value.
    # 3. Do NOT use `range` — the point is the itertools bridge.
    raise NotImplementedError("Implement first_n_squares")


def select_active_users(
    users: list[dict[str, Any]], fields: list[str]
) -> list[dict[str, Any]]:
    """Industrial filtered projection (concept #20).

    Keep only users whose ``active`` value is truthy, and project each kept
    user down to the requested ``fields`` (in the order given).

    Args:
        users: List of user dicts. Each must contain an ``active`` key.
        fields: Non-empty list of field names. Every name must exist on at
            least one user; otherwise raise ``ValueError`` listing the bad
            field names.

    Returns:
        New list of dicts, one per active user, containing only ``fields``.

    Raises:
        ValueError: If ``fields`` is empty or contains unknown keys.

    Examples:
        >>> select_active_users(
        ...     [{"id": 1, "name": "Ada", "active": True},
        ...      {"id": 2, "name": "Bob", "active": False}],
        ...     fields=["id", "name"],
        ... )
        [{'id': 1, 'name': 'Ada'}]
    """
    # TODO:
    # 1. Reject empty `fields` with a descriptive ValueError.
    # 2. Compute the union of all keys appearing across users; reject any
    #    `fields` entry not present in that union (mention the unknown names).
    # 3. Build the result with ONE list comprehension:
    #    - filter: `if u.get("active")`.
    #    - projection: a NESTED dict comprehension `{f: u.get(f) for f in fields}`.
    # 4. This is exactly two comprehension layers — that is the limit.
    raise NotImplementedError("Implement select_active_users")


def index_orders_by_id(orders: list[dict[str, Any]]) -> dict[Any, dict[str, Any]]:
    """Build an O(1) lookup dict keyed by ``order_id`` (concept #21).

    Args:
        orders: List of order dicts. Each must contain an ``order_id`` key.

    Returns:
        ``{order["order_id"]: order}``.

    Raises:
        ValueError: If any order lacks ``order_id`` OR if duplicate ids are
            found — mention the duplicated id in the message.

    Examples:
        >>> index_orders_by_id(
        ...     [{"order_id": "A1", "total": 10}, {"order_id": "B2", "total": 20}]
        ... ) == {"A1": {"order_id": "A1", "total": 10},
        ...      "B2": {"order_id": "B2", "total": 20}}
        True
    """
    # TODO:
    # 1. Validate every order has an `order_id` key; raise ValueError
    #    naming the missing key if absent.
    # 2. Collect the order_id values; if `len(set(ids)) != len(ids)` there
    #    is a duplicate — raise ValueError mentioning the duplicate id.
    # 3. Return a dict comprehension `{o["order_id"]: o for o in orders}`.
    raise NotImplementedError("Implement index_orders_by_id")


if __name__ == "__main__":
    # ─── refactor_nested checks ───
    assert refactor_nested(
        [[["a", " "], [None, "b"]], [["c", ""]]]
    ) == ["A", "B", "C"]
    assert refactor_nested([]) == []
    assert refactor_nested([[[]]]) == []
    assert refactor_nested([[[1, 2.0, None]]]) == [], "non-strings ignored"

    # ─── count_long_words checks ───
    assert count_long_words("the quick brown fox", min_len=4) == 2
    assert count_long_words("", min_len=1) == 0
    assert count_long_words("a bb ccc", min_len=0) == 3
    try:
        count_long_words("x", min_len=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("count_long_words must reject negative min_len")

    # ─── first_n_squares checks ───
    assert first_n_squares(4) == [1, 4, 9, 16]
    assert first_n_squares(0) == []
    assert first_n_squares(1) == [1]
    try:
        first_n_squares(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("first_n_squares must reject negative n")

    # ─── select_active_users checks ───
    users = [
        {"id": 1, "name": "Ada", "active": True},
        {"id": 2, "name": "Bob", "active": False},
        {"id": 3, "name": "Grace", "active": True},
    ]
    assert select_active_users(users, ["id", "name"]) == [
        {"id": 1, "name": "Ada"},
        {"id": 3, "name": "Grace"},
    ]
    assert select_active_users([], ["id"]) == []
    try:
        select_active_users(users, [])
    except ValueError:
        pass
    else:
        raise AssertionError("select_active_users must reject empty fields")
    try:
        select_active_users(users, ["id", "ghost"])
    except ValueError:
        pass
    else:
        raise AssertionError("select_active_users must reject unknown fields")

    # ─── index_orders_by_id checks ───
    indexed = index_orders_by_id(
        [{"order_id": "A1", "total": 10}, {"order_id": "B2", "total": 20}]
    )
    assert indexed["A1"]["total"] == 10
    assert indexed["B2"]["total"] == 20
    try:
        index_orders_by_id([{"order_id": "X"}, {"order_id": "X"}])
    except ValueError:
        pass
    else:
        raise AssertionError("index_orders_by_id must reject duplicate ids")
    try:
        index_orders_by_id([{"total": 1}])
    except ValueError:
        pass
    else:
        raise AssertionError("index_orders_by_id must reject missing order_id")

    print("ex03_advanced.py: all asserts passed ✓")
