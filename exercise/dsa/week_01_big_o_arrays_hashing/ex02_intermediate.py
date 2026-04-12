"""Exercise 02: Two-sum indices.

Problem:
    Implement `two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None`.

Constraints:
    - Return index pair `(i, j)` where `i < j` and `nums[i] + nums[j] == target`.
    - Return None if no valid pair exists.
    - Target complexity: O(n) average time using a hash map.

Examples:
    two_sum_indices([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_indices([1, 2, 3], 99) -> None
"""

from __future__ import annotations


def two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of two numbers that sum to target.

    Expected complexity:
        Time O(n), Space O(n)
    """

    # TODO: Scan once and store value -> index in a dict.
    # TODO: For each value, check if `target - value` is already seen.
    # Sample: two_sum_indices([2, 7, 11, 15], 9) -> (0, 1)
    seek : dict[int, int] = {} # num : index
    for index, num in enumerate(nums):
        value = target - num
        if value in seek:
            return (seek.get(value), index)
        seek[num] = index
    return None
    #raise NotImplementedError("implement two_sum_indices")


if __name__ == "__main__":
    try:
        # Expected output: (0, 1)
        assert two_sum_indices([2, 7, 11, 15], 9) == (0, 1)
        # Expected output: None
        assert two_sum_indices([1, 2, 3], 99) is None
        print("ex02_intermediate: all asserts passed")
    except NotImplementedError:
        print("ex02_intermediate: implement two_sum_indices to run self-checks.")
