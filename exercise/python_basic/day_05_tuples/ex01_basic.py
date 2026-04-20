from __future__ import annotations

#     Exercise 01: Tuple Basics.

#     Problem:
#         Implement `first_and_last(nums: tuple[int, ...]) -> tuple[int, int]`.
#         Return a tuple with the first and last elements of nums.

#     Constraints:
#         - nums must not be empty; raise ValueError if so.
#         - Do not mutate the input.
#         - Return the result; do not print inside the function.

#     Examples:
#         first_and_last((10, 20, 30, 40)) -> (10, 40)
#         first_and_last((5,)) -> (5, 5)
#         first_and_last(()) -> ValueError



def first_and_last(nums: tuple[int, ...]) -> tuple[int, int]:
    """Return a tuple with the first and last elements of nums.

    Args:
        nums: A tuple of integers (must not be empty).

    Returns:
        Tuple of (first, last) elements.

    Raises:
        ValueError: If nums is empty.
    """
    # Your code here
    if not nums:
        raise ValueError("Nums was empty")
    return min(nums), max(nums)


if __name__ == "__main__":
    # Basic cases
    assert first_and_last((10, 20, 30, 40)) == (10, 40)
    assert first_and_last((5,)) == (5, 5)
    # Error case
    try:
        first_and_last(())
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty tuple")

    print("ex01_basic: all asserts passed")
