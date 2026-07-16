# ex02_intermediate.py — Day 13: Comprehensions — Intermediate

"""
Intermediate exercises for Comprehensions.
Covers checklist items: #8–#15 (generator expressions, generator-in-calls,
memory comparison, `yield`, `next`/`StopIteration`, comprehension scoping,
walrus operator).

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex02_intermediate.py
- All asserts must pass.
"""

from __future__ import annotations

import sys  # noqa: F401  # used by learners inside memory_delta
from collections.abc import Iterable, Iterator
from typing import Any


def lazy_doubles(nums: Iterable[int]) -> Iterator[int]:
    """Return a **generator** producing ``2 * n`` for each element (concept #8).

    The result must be a generator/iterator, NOT a list. The asserts check
    this by calling ``iter(result) is result``.

    Args:
        nums: Iterable of ints.

    Returns:
        Iterator yielding doubled values.

    Examples:
        >>> list(lazy_doubles([1, 2, 3]))
        [2, 4, 6]
    """
    # TODO:
    # 1. Build a generator expression with PARENTHESES, not square brackets.
    # 2. Return that expression directly — do NOT wrap it in list().
    # Sample: list(lazy_doubles([1, 2])) -> [2, 4].
    raise NotImplementedError("Implement lazy_doubles")


def total_lengths(strings: Iterable[str]) -> int:
    """Sum the lengths of every string using a bare genexp (concept #9).

    Args:
        strings: Iterable of strings.

    Returns:
        Total combined length (``0`` on empty input).

    Examples:
        >>> total_lengths(["ab", "cde"])
        5
        >>> total_lengths([])
        0
    """
    # TODO:
    # 1. Call the built-in `sum` with a generator expression as its single
    #    argument — that lets you drop the outer parentheses around the genexp.
    # 2. The genexp projects `len(s)` for each string `s`.
    # Sample: total_lengths(["ab", "cde"]) -> 5.
    raise NotImplementedError("Implement total_lengths")


def memory_delta(n: int) -> tuple[int, int]:
    """Compare list vs generator memory footprint via :func:`sys.getsizeof` (concept #10).

    Args:
        n: Non-negative stream length.

    Returns:
        ``(list_bytes, gen_bytes)``. For ``n >= 1`` the list size MUST be
        strictly greater than the generator size.

    Raises:
        ValueError: If ``n < 0``.

    Examples:
        >>> lb, gb = memory_delta(500)
        >>> lb > gb
        True
    """
    # TODO:
    # 1. Reject negative `n` with a descriptive ValueError.
    # 2. Use sys.getsizeof on a list comprehension `[i for i in range(n)]`.
    # 3. Use sys.getsizeof on a generator expression `(i for i in range(n))`.
    # 4. Return them as a tuple (list_bytes, gen_bytes).
    raise NotImplementedError("Implement memory_delta")


def even_stream(limit: int) -> Iterator[int]:
    """Generator function yielding even numbers ``0, 2, 4, ...`` strictly below ``limit`` (concept #11).

    Args:
        limit: Non-negative upper bound (exclusive).

    Yields:
        Successive even ints.

    Raises:
        ValueError: If ``limit < 0``.

    Examples:
        >>> list(even_stream(8))
        [0, 2, 4, 6]
        >>> list(even_stream(0))
        []
    """
    # TODO:
    # 1. Reject negative `limit` with a ValueError mentioning the bad value.
    # 2. Use a `while` or `for` loop with `yield` to emit even numbers
    #    starting at 0, stopping strictly before `limit`.
    # 3. This must be a generator function — therefore it contains `yield`.
    raise NotImplementedError("Implement even_stream")


def first_or_default(it: Iterable[Any], default: Any = None) -> Any:
    """Return the first item using :func:`next`, catching :class:`StopIteration` (concepts #12, #13).

    Args:
        it: Any iterable.
        default: Returned when ``it`` is empty.

    Returns:
        First item, or ``default``.

    Examples:
        >>> first_or_default([10, 20])
        10
        >>> first_or_default([], default=-1)
        -1
    """
    # TODO:
    # 1. Get an iterator with `iter(it)`.
    # 2. Wrap a single `next(iterator)` call in try/except StopIteration.
    # 3. On StopIteration, return `default`.
    # Sample: first_or_default(iter([]), default=-1) -> -1.
    raise NotImplementedError("Implement first_or_default")


def no_leak() -> tuple[str, list[int]]:
    """Demonstrate that a comprehension's loop variable does NOT leak (concept #14).

    Bind a local variable named ``token`` to the string ``"outer"`` BEFORE
    building a list comprehension that also uses ``token`` as its loop name.
    After the comprehension, ``token`` must still be ``"outer"``.

    Returns:
        ``(token_after, comprehension_result)``.

    Examples:
        >>> outer, squares = no_leak()
        >>> outer, squares
        ('outer', [0, 1, 4])
    """
    # TODO:
    # 1. Assign `token = "outer"`.
    # 2. Build `[token * token for token in range(3)]` — yes, the same name.
    # 3. Return (token, that_list). The first element MUST equal "outer".
    #    If it changes, Python 2-style leaking has happened — but in Py3 it never does.
    raise NotImplementedError("Implement no_leak")


def compact_squares(nums: Iterable[int], threshold: int) -> list[int]:
    """Use the walrus operator to compute each square only once (concept #15).

    For every ``n`` in ``nums``, compute ``y = n * n`` ONCE; keep ``y`` only
    when ``y > threshold``.

    Args:
        nums: Iterable of ints.
        threshold: Lower bound (exclusive).

    Returns:
        List of squares strictly greater than ``threshold``.

    Examples:
        >>> compact_squares(range(5), threshold=3)
        [4, 9, 16]
    """
    # TODO:
    # 1. Inside a list comprehension, use `(y := n * n)` as the filter
    #    condition AND as the value projected out.
    # 2. Wrap the walrus in parentheses so the parser accepts it inside
    #    the trailing `if` clause.
    # 3. Do NOT call `n * n` twice — that defeats the point of `:=`.
    # Sample: compact_squares(range(5), threshold=3) -> [4, 9, 16].
    raise NotImplementedError("Implement compact_squares")


if __name__ == "__main__":
    # ─── lazy_doubles checks ───
    g = lazy_doubles([1, 2, 3])
    assert iter(g) is g, "lazy_doubles must return a generator/iterator"
    assert list(g) == [2, 4, 6]
    assert list(lazy_doubles([])) == []

    # ─── total_lengths checks ───
    assert total_lengths(["ab", "cde"]) == 5
    assert total_lengths([]) == 0

    # ─── memory_delta checks ───
    lb, gb = memory_delta(500)
    assert lb > gb, f"list ({lb}) should be larger than generator ({gb})"
    assert memory_delta(0)[0] >= 0, "n=0 should still return valid sizes"
    try:
        memory_delta(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("memory_delta must reject negative n")

    # ─── even_stream checks ───
    assert list(even_stream(8)) == [0, 2, 4, 6]
    assert list(even_stream(0)) == []
    es = even_stream(4)
    assert hasattr(es, "__next__"), "even_stream must return a generator"
    try:
        list(even_stream(-2))
    except ValueError:
        pass
    else:
        raise AssertionError("even_stream must reject negative limit")

    # ─── first_or_default checks ───
    assert first_or_default([10, 20]) == 10
    assert first_or_default(iter([])) is None
    assert first_or_default([], default=-1) == -1

    # ─── no_leak checks ───
    outer, squares = no_leak()
    assert outer == "outer", "comprehension loop var must not leak"
    assert squares == [0, 1, 4]

    # ─── compact_squares checks ───
    assert compact_squares(range(5), threshold=3) == [4, 9, 16]
    assert compact_squares([], threshold=0) == []
    assert compact_squares([0, 1, 2], threshold=10) == []

    print("ex02_intermediate.py: all asserts passed ✓")
