# ex01_basic.py — Day 12: Built-ins in Pipelines — Basic

"""
Basic exercises for Built-ins in Pipelines.
Covers checklist items: #1–#5 (enumerate, zip, zip strict, sorted, reversed).

Instructions:
- Implement each function where you see TODO.
- Replace `raise NotImplementedError(...)` with your implementation.
- Run this file to verify: python ex01_basic.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations

from typing import Any


def number_lines(lines: list[str], start: int = 1) -> list[str]:
    """Number each line using :func:`enumerate` (concept #1).

    Args:
        lines: Lines to number.
        start: First index (must be >= 0).

    Returns:
        ``["{i}. {line}", ...]``.

    Raises:
        ValueError: If ``start`` is negative.

    Examples:
        >>> number_lines(["a", "b"])
        ['1. a', '2. b']
        >>> number_lines(["x"], start=10)
        ['10. x']
    """
    # TODO:
    # 1. If start < 0: raise ValueError(f"start must be >= 0, got {start!r}").
    # 2. Use enumerate(lines, start=start) and an f-string "{i}. {line}".
    # Sample input: ["a", "b"]; Expected output: ['1. a', '2. b']
    result = [f'{index}. {line}' for index, line in enumerate(lines, start=start)]
    return result
    


def pair_columns(header: list[str], row: list[Any]) -> dict[str, Any]:
    """Pair ``header`` with ``row`` using :func:`zip` (concept #2).

    Plain ``zip`` silently truncates to the shorter side — accepted here.

    Args:
        header: Column names (non-empty).
        row: Row values.

    Returns:
        ``{column: value}`` dict.

    Raises:
        ValueError: If ``header`` is empty.

    Examples:
        >>> pair_columns(["id", "name"], [7, "Ada"])
        {'id': 7, 'name': 'Ada'}
        >>> pair_columns(["a", "b", "c"], [1, 2])  # truncated, no error
        {'a': 1, 'b': 2}
    """
    # TODO:
    # 1. If not header: raise ValueError("header must not be empty").
    # 2. Return dict(zip(header, row)).
    if not header:
        raise ValueError("header must not be empty")
    return dict(zip(header, row))


def pair_columns_strict(header: list[str], row: list[Any]) -> dict[str, Any]:
    """Strict variant — raises on mismatched lengths (concept #3, PEP 618).

    Args:
        header: Column names (non-empty).
        row: Row values; must equal ``len(header)``.

    Returns:
        ``{column: value}`` dict.

    Raises:
        ValueError: If ``header`` is empty, or lengths differ.

    Examples:
        >>> pair_columns_strict(["a", "b"], [1, 2])
        {'a': 1, 'b': 2}
    """
    # TODO:
    # 1. If not header: raise ValueError("header must not be empty").
    # 2. Return dict(zip(header, row, strict=True)).
    # 3. Mismatched lengths will raise ValueError automatically.
    return dict(zip(header, row, strict=True))


def rank_scores(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sort records by score desc, then name asc (concept #4).

    Args:
        records: Dicts with ``name`` (str) and ``score`` (int) keys.

    Returns:
        New sorted list — input is not mutated.

    Raises:
        ValueError: If any record is missing ``name`` or ``score``.

    Examples:
        >>> rank_scores([{"name": "Ada", "score": 30}, {"name": "Linus", "score": 50}])
        [{'name': 'Linus', 'score': 50}, {'name': 'Ada', 'score': 30}]
        >>> rank_scores([{"name": "Bob", "score": 30}, {"name": "Ada", "score": 30}])
        [{'name': 'Ada', 'score': 30}, {'name': 'Bob', 'score': 30}]
    """
    # TODO:
    # 1. Validate every record has both "name" and "score" keys.
    return sorted(records, key=lambda record: (-record['score'], record['name']))

def recent_first(events: list[str]) -> list[str]:
    """Return ``events`` newest-first using :func:`reversed` (concept #5).

    Args:
        events: Chronological event list.

    Returns:
        New list in reverse order (original unchanged).

    Examples:
        >>> recent_first(["login", "purchase", "logout"])
        ['logout', 'purchase', 'login']
        >>> recent_first([])
        []
    """
    # TODO: return list(reversed(events))
    return list(reversed(events))
    


if __name__ == "__main__":
    # ─── number_lines checks ───
    assert number_lines(["a", "b"]) == ["1. a", "2. b"], "default start=1"
    assert number_lines(["x"], start=10) == ["10. x"], "custom start"
    assert number_lines([]) == [], "empty input"

    # ─── pair_columns checks ───
    assert pair_columns(["id", "name"], [7, "Ada"]) == {"id": 7, "name": "Ada"}, "basic"
    assert pair_columns(["a", "b", "c"], [1, 2]) == {"a": 1, "b": 2}, "silent truncation"
    try:
        pair_columns([], [1])
    except ValueError:
        pass
    else:
        raise AssertionError("pair_columns must reject empty header")

    # ─── pair_columns_strict checks ───
    assert pair_columns_strict(["a", "b"], [1, 2]) == {"a": 1, "b": 2}, "equal lengths"
    try:
        pair_columns_strict(["id", "name", "email"], [7, "Ada"])
    except ValueError:
        pass
    else:
        raise AssertionError("strict variant must raise on mismatch")

    # ─── rank_scores checks ───
    ranked = rank_scores(
        [{"name": "Ada", "score": 30}, {"name": "Linus", "score": 50}, {"name": "Bob", "score": 30}]
    )
    assert ranked[0]["name"] == "Linus", "highest score first"
    assert [r["name"] for r in ranked[1:]] == ["Ada", "Bob"], "tie-break alphabetical"

    # ─── recent_first checks ───
    src = ["login", "purchase", "logout"]
    assert recent_first(src) == ["logout", "purchase", "login"], "reversed"
    assert src == ["login", "purchase", "logout"], "original not mutated"
    assert recent_first([]) == [], "empty"

    print("ex01_basic.py: all asserts passed ✓")
