"""Exercise 01: Complete the function logic.

Problem:
    Implement `format_username` for a user onboarding flow.

Function signature:
    format_username(raw_name: str) -> str

Input/Output:
    - Input: raw user name string
    - Output: normalized username string

Constraints:
    - Trim leading/trailing spaces
    - Convert to lowercase
    - Replace internal spaces with underscores
    - Raise ValueError if empty after trim

Examples:
    format_username("  Alice Doe  ") -> "alice_doe"
    format_username("BOB") -> "bob"
"""


def format_username(raw_name: str) -> str:
    """Return normalized username from raw input."""
    # TODO:
    # 1) Strip whitespace
    raw_name = raw_name.strip()
    # 2) Validate non-empty value after strip
    if not raw_name:
        raise ValueError("raw_name must not be empty")
    # 3) Convert to lowercase
    raw_name=raw_name.lower()
    # 4) Replace spaces with underscores
    raw_name=raw_name.replace(' ','_')
    return raw_name
    # Sample: format_username("  Alice Doe  ") -> "alice_doe"


if __name__ == "__main__":
    # Self-check: all asserts must pass before AI evaluation
    assert format_username("  Alice Doe  ") == "alice_doe", "should trim, lowercase, and underscore"
    assert format_username("BOB") == "bob", "single word should just lowercase"
    try:
        format_username("   ")
        raise AssertionError("should raise ValueError on blank input")
    except ValueError:
        pass  # expected
    print("ex01: all asserts passed ✓")
