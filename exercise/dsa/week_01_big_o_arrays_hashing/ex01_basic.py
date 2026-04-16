"""Exercise 01: Contains duplicate.

Problem:
    Implement `contains_duplicate(nums: list[int]) -> bool`.

Constraints:
    - Return True when any value appears more than once, else False.
    - Target complexity: O(n) time, O(n) space.
    - Do not mutate the input list.

Examples:
    contains_duplicate([1, 2, 3, 1]) -> True
    contains_duplicate([1, 2, 3, 4]) -> False
"""

from __future__ import annotations


def contains_duplicate(nums: list[int]) -> bool:
    """Return whether the input has any repeated value.

    Expected complexity:
        Time O(n), Space O(n)
    """

    # Use a set to track seen values — O(1) average membership check.
    # Sample: contains_duplicate([1, 2, 3, 1]) -> True
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    try:
        # Expected output: True
        assert contains_duplicate([1, 2, 3, 1]) is True
        # Expected output: False
        assert contains_duplicate([1, 2, 3, 4]) is False
        print("ex01_basic: all asserts passed")
    except NotImplementedError:
        print("ex01_basic: implement contains_duplicate to run self-checks.")
