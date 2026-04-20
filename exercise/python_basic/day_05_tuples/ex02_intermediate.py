"""Exercise 02: Tuple Unpacking & Multiple Returns.

Problem:
    Implement `min_and_max(nums: tuple[int, ...]) -> tuple[int, int]`.
    Return a tuple (min, max) from nums.

Constraints:
    - nums must not be empty; raise ValueError if so.
    - Do not mutate the input.
    - Return the result; do not print inside the function.

Examples:
    min_and_max((5, 2, 9, 1)) -> (1, 9)
    min_and_max((7,)) -> (7, 7)
    min_and_max(()) -> ValueError
"""

from __future__ import annotations

def min_and_max(nums: tuple[int, ...]) -> tuple[int, int]:
    """Return a tuple (min, max) from nums.

    Args:
        nums: A tuple of integers (must not be empty).

    Returns:
        Tuple of (min, max) values.

    Raises:
        ValueError: If nums is empty.
    """
    # Your code here
      # Your code here
    if not nums:
        raise ValueError("Nums was empty")
    return min(nums), max(nums)

if __name__ == "__main__":
    # Basic cases
    assert min_and_max((5, 2, 9, 1)) == (1, 9)
    assert min_and_max((7,)) == (7, 7)
    # Unpacking
    lo, hi = min_and_max((3, 8, 2))
    assert lo == 2 and hi == 8
    # Error case
    try:
        min_and_max(())
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty tuple")

    print("ex02_intermediate: all asserts passed")
