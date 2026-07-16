# ex01_basic.py — Day 13: Comprehensions — Basic

"""
Basic exercises for Comprehensions.
Covers checklist items: #1–#7 (list / if-filter / if-else / nested /
dict / dict-filter / set comprehensions).

Instructions:
- Implement each function where you see TODO.
- Replace `raise NotImplementedError(...)` with your implementation.
- Run this file to verify: python ex01_basic.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def square_evens(nums: Iterable[int]) -> list[int]:
    """Square only the even numbers, in input order (concepts #1, #2).

    Args:
        nums: Iterable of ints.

    Returns:
        New list of squared evens.

    Examples:
        >>> square_evens([1, 2, 3, 4])
        [4, 16]
        >>> square_evens([])
        []
    """
    # TODO:
    # 1. Use a single list comprehension over `nums`.
    # 2. Add a trailing `if` clause that keeps only even values.
    # 3. The projected expression is the square of the kept value.
    # Sample: square_evens([1, 2, 3, 4]) -> [4, 16].
    raise NotImplementedError("Implement square_evens")


def signs_to_words(nums: Iterable[float]) -> list[str]:
    """Map each number to "pos" / "zero" / "neg" using ``if/else`` (concept #3).

    Args:
        nums: Iterable of numbers.

    Returns:
        List of sign labels, same length as input.

    Examples:
        >>> signs_to_words([-2, 0, 5])
        ['neg', 'zero', 'pos']
    """
    # TODO:
    # 1. Write a list comprehension where the projection itself is a
    #    conditional expression with three branches: positive, zero, negative.
    # 2. Remember: branching `if/else` goes at the FRONT of the expression
    #    (before `for`), not at the end.
    # Sample: signs_to_words([-2, 0, 5]) -> ['neg', 'zero', 'pos'].
    raise NotImplementedError("Implement signs_to_words")


def flatten_grid(matrix: list[list[Any]]) -> list[Any]:
    """Flatten a 2-D matrix in row-major order with a nested comprehension (concept #4).

    Args:
        matrix: List of equal-length rows (may be empty).

    Returns:
        Single list of cells, outer rows then inner cells.

    Raises:
        ValueError: If rows have different lengths.

    Examples:
        >>> flatten_grid([[1, 2], [3, 4]])
        [1, 2, 3, 4]
        >>> flatten_grid([])
        []
    """
    # TODO:
    # 1. If `matrix` is non-empty, check every row has the same length as
    #    the first; otherwise raise ValueError mentioning the offending lengths.
    # 2. Write a nested comprehension: outer loop over rows, inner loop over
    #    cells. Source order is left-to-right exactly like a real nested `for`.
    # Sample: flatten_grid([[1, 2], [3, 4]]) -> [1, 2, 3, 4].
    raise NotImplementedError("Implement flatten_grid")


def swap_keys_values(d: dict[str, int]) -> dict[int, str]:
    """Return a new dict with keys and values swapped (concept #5).

    Args:
        d: Mapping from str to int.

    Returns:
        New mapping from int to str.

    Raises:
        ValueError: If two original values collide after swapping.

    Examples:
        >>> swap_keys_values({"a": 1, "b": 2}) == {1: "a", 2: "b"}
        True
    """
    # TODO:
    # 1. Check that the number of distinct values equals len(d); if not,
    #    raise ValueError mentioning the duplicated value.
    # 2. Build a dict comprehension iterating over `d.items()` and swap.
    # Sample: swap_keys_values({"a": 1, "b": 2}) -> {1: "a", 2: "b"}.
    raise NotImplementedError("Implement swap_keys_values")


def keep_truthy(d: dict[str, Any]) -> dict[str, Any]:
    """Keep only entries whose value is truthy (concept #6).

    Args:
        d: Any string-keyed dict.

    Returns:
        New dict without falsy values (``0``, ``""``, ``None``, ``[]``, ``False``).

    Examples:
        >>> keep_truthy({"a": 1, "b": 0, "c": "", "d": "ok"})
        {'a': 1, 'd': 'ok'}
    """
    # TODO:
    # 1. Use a dict comprehension over `d.items()`.
    # 2. Add a trailing `if v` clause to filter out falsy values.
    # Sample: keep_truthy({"a": 1, "b": 0}) -> {"a": 1}.
    raise NotImplementedError("Implement keep_truthy")


def unique_word_lengths(words: Iterable[str]) -> set[int]:
    """Return the set of distinct word lengths (concept #7).

    Empty strings must be ignored — length 0 should NOT appear in the result.

    Args:
        words: Iterable of strings.

    Returns:
        Set of unique positive lengths.

    Examples:
        >>> sorted(unique_word_lengths(["a", "bb", "cc", "ddd", ""]))
        [1, 2, 3]
    """
    # TODO:
    # 1. Use a set comprehension (curly braces, no key/value separator).
    # 2. Add a trailing `if` clause to skip empty strings.
    # 3. Project `len(word)` for each remaining word.
    # Sample: unique_word_lengths(["a", "bb", "cc"]) -> {1, 2}.
    raise NotImplementedError("Implement unique_word_lengths")


if __name__ == "__main__":
    # ─── square_evens checks ───
    assert square_evens([1, 2, 3, 4]) == [4, 16], "filter + project"
    assert square_evens([]) == [], "empty"
    assert square_evens([1, 3, 5]) == [], "no evens"

    # ─── signs_to_words checks ───
    assert signs_to_words([-2, 0, 5]) == ["neg", "zero", "pos"]
    assert signs_to_words([0]) == ["zero"]
    assert signs_to_words([]) == []

    # ─── flatten_grid checks ───
    assert flatten_grid([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_grid([]) == []
    try:
        flatten_grid([[1, 2], [3]])
    except ValueError:
        pass
    else:
        raise AssertionError("flatten_grid must reject jagged rows")

    # ─── swap_keys_values checks ───
    assert swap_keys_values({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert swap_keys_values({}) == {}
    try:
        swap_keys_values({"a": 1, "b": 1})
    except ValueError:
        pass
    else:
        raise AssertionError("swap_keys_values must reject duplicate values")

    # ─── keep_truthy checks ───
    assert keep_truthy({"a": 1, "b": 0, "c": "", "d": "ok"}) == {"a": 1, "d": "ok"}
    assert keep_truthy({}) == {}
    assert keep_truthy({"x": None, "y": [], "z": "v"}) == {"z": "v"}

    # ─── unique_word_lengths checks ───
    assert unique_word_lengths(["a", "bb", "cc", "ddd", ""]) == {1, 2, 3}
    assert unique_word_lengths([]) == set()
    assert unique_word_lengths(["", ""]) == set(), "empty strings ignored"

    print("ex01_basic.py: all asserts passed ✓")
