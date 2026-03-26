"""Exercise 02: Complete the function logic.

Problem:
    Implement `parse_retry_count` for validating CLI retry input.

Function signature:
    parse_retry_count(raw: str) -> int

Input/Output:
    - Input: string that should represent an integer
    - Output: integer retry count

Constraints:
    - Parse int from string input
    - Allow only values in range 0..5 (inclusive)
    - Raise ValueError with a clear message for invalid input

Examples:
    parse_retry_count("3") -> 3
    parse_retry_count("0") -> 0
"""


def parse_retry_count(raw: str) -> int:
    """Parse and validate retry count in the range 0..5."""
    # TODO:
    # 1) Convert input string to int
    try:
        raw_int = int(raw)
    except:
        raise ValueError("Conversion error ")
    # 2) If conversion fails, raise ValueError with message
    # 3) Enforce range 0..5 inclusive
    if raw_int < 0:
        raise ValueError("Less than 0 not included")
    if raw_int > 5:
        raise ValueError("More than 5 ")
    return raw_int
    # Sample: parse_retry_count("3") -> 3
    #raise NotImplementedError("Implement parse_retry_count")


if __name__ == "__main__":
    # Self-check: all asserts must pass before AI evaluation
    assert parse_retry_count("3") == 3, "valid mid-range value"
    assert parse_retry_count("0") == 0, "lower bound inclusive"
    assert parse_retry_count("5") == 5, "upper bound inclusive"
    for bad in ["-1", "6", "abc"]:
        try:
            parse_retry_count(bad)
            raise AssertionError(f"should raise ValueError for {bad!r}")
        except ValueError:
            pass  # expected
    print("ex02: all asserts passed ✓")
