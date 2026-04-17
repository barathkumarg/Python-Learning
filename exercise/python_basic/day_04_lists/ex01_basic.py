"""Exercise 01: Slice a result window.

Problem:
    Implement
    `slice_result_window(items: list[str], *, start: int, size: int) -> list[str]`.
    Return a new list containing at most `size` items starting from `start`.

Constraints:
    - `start` must be >= 0.
    - `size` must be >= 1.
    - Must return a new list created by slicing.
    - Raise `ValueError` with the invalid value when input is invalid.

Examples:
    slice_result_window(["a", "b", "c", "d"], start=1, size=2) -> ["b", "c"]
    slice_result_window(["a", "b"], start=5, size=2) -> []
    slice_result_window(["a", "b"], start=-1, size=2) -> ValueError
"""

from __future__ import annotations


def slice_result_window(items: list[str], *, start: int, size: int) -> list[str]:
    """Return a paginated slice from `items`.

    Args:
        items: Source values to slice.
        start: Zero-based start index.
        size: Number of values requested.

    Returns:
        A new list view based on slicing.

    Raises:
        ValueError: If `start` is negative or `size` is less than 1.
    """
    if start < 0:
        raise ValueError(f"start must be >= 0, got start={start}")
    if size < 1:
        raise ValueError(f"size must be >= 1, got size={size}")
    return items[start : start + size]


if __name__ == "__main__":
    # Expected output: ['b', 'c']
    assert slice_result_window(["a", "b", "c", "d"], start=1, size=2) == ["b", "c"]
    # Expected output: []
    assert slice_result_window(["a", "b"], start=5, size=2) == []
    try:
        slice_result_window(["a", "b"], start=-1, size=2)
        raise AssertionError("should have raised ValueError for negative start")
    except ValueError:
        pass
    print("ex01_basic: all asserts passed")
