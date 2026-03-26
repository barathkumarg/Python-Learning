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
    # 2) If conversion fails, raise ValueError with message
    # 3) Enforce range 0..5 inclusive
    # Sample: parse_retry_count("3") -> 3
    raise NotImplementedError("Implement parse_retry_count")


if __name__ == "__main__":
    samples = ["3", "0", "7", "abc"]
    for sample in samples:
        try:
            print(f"input={sample!r} output={parse_retry_count(sample)!r}")
        except Exception as exc:  # noqa: BLE001
            print(f"input={sample!r} error={type(exc).__name__}: {exc}")
