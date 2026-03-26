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
    # 2) Validate non-empty value after strip
    # 3) Convert to lowercase
    # 4) Replace spaces with underscores
    # Sample: format_username("  Alice Doe  ") -> "alice_doe"
    raise NotImplementedError("Implement format_username")


if __name__ == "__main__":
    samples = ["  Alice Doe  ", "BOB", "   "]
    for sample in samples:
        try:
            print(f"input={sample!r} output={format_username(sample)!r}")
        except Exception as exc:  # noqa: BLE001
            print(f"input={sample!r} error={type(exc).__name__}: {exc}")
