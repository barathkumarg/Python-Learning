"""Exercise 01: Full name formatter.

Problem:
    Implement `format_full_name(first_name: str, last_name: str, *, title: str | None = None) -> str`.
    Trim whitespace, convert names to title case, and optionally prepend a title.

Constraints:
    - `first_name` and `last_name` are required and must be non-empty after trimming.
    - `title` is optional and keyword-only.
    - Return the final string; do not print inside the function.

Examples:
    format_full_name(" ada ", " lovelace ") -> "Ada Lovelace"
    format_full_name("grace", "hopper", title="rear admiral") -> "Rear Admiral Grace Hopper"
    format_full_name("   ", "hopper") -> ValueError
"""

from __future__ import annotations


def format_full_name(
    first_name: str,
    last_name: str,
    *,
    title: str | None = None,
) -> str:
    """Return a clean, formatted full name.

    Args:
        first_name: Required first name.
        last_name: Required last name.
        title: Optional title such as "Dr" or "Rear Admiral".

    Returns:
        Formatted full name in title case.

    Raises:
        ValueError: If either required name is empty after trimming.
    """
    # Trim whitespace
    first = first_name.strip()
    last = last_name.strip()
    # Validate non-empty after trimming
    if not first or not last:
        raise ValueError("Name is blank")
    # Convert to title case
    first = first.title()
    last = last.title()
    if title is not None:
        return f"{title.title()} {first} {last}"
    return f"{first} {last}"


if __name__ == "__main__":
    try:
        # Expected output: "Ada Lovelace"
        assert format_full_name(" ada ", " lovelace ") == "Ada Lovelace"
        # Expected output: "Rear Admiral Grace Hopper"
        assert (
            format_full_name("grace", "hopper", title="rear admiral")
            == "Rear Admiral Grace Hopper"
        )
        try:
            format_full_name("   ", "hopper")
            raise AssertionError("should have raised for blank first_name")
        except ValueError:
            pass
        print("ex01_basic: all asserts passed")
    except NotImplementedError:
        print("ex01_basic: implement format_full_name to run self-checks.")

    # print(format_full_name(" ada ", " lovelace "))  # Expected output: Ada Lovelace
