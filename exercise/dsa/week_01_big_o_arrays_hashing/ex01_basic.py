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

    # TODO: Use a set to track seen values.
    # Sample: contains_duplicate([1, 2, 3, 1]) -> True
    seek : list[int] = []
    for num in nums:
        if num in seek:
            return True
        seek.append(num)
    return False 
    raise NotImplementedError("implement contains_duplicate")


if __name__ == "__main__":
    try:
        # Expected output: True
        assert contains_duplicate([1, 2, 3, 1]) is True
        # Expected output: False
        assert contains_duplicate([1, 2, 3, 4]) is False
        print("ex01_basic: all asserts passed")
    except NotImplementedError:
        print("ex01_basic: implement contains_duplicate to run self-checks.")
