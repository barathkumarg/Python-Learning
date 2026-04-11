"""Exercise 02: Collect missing fields with *args.

Problem:
    Implement
    `collect_missing_fields(form_data: dict[str, str], *required_fields: str, trim_values: bool = True) -> list[str]`.
    The function should inspect a form-like dictionary and return the required
    field names that are missing or blank.

Constraints:
    - Raise `ValueError` if no required field names are provided.
    - Preserve the order of the requested field names in the returned list.
    - When `trim_values=True`, whitespace-only strings count as missing.
    - Return the result; do not print inside the function.

Examples:
    collect_missing_fields({"email": " ada@example.com ", "role": " "}, "email", "role")
    -> ["role"]
    collect_missing_fields({"team": "platform"}, *["team", "region"])
    -> ["region"]
    collect_missing_fields({"email": "x@example.com"}) -> ValueError
"""

from __future__ import annotations


def collect_missing_fields(
    form_data: dict[str, str],
    *required_fields: str,
    trim_values: bool = True,
) -> list[str]:
    """Return required field names that are missing or blank.

    Args:
        form_data: Input form payload.
        *required_fields: Field names that must contain values.
        trim_values: Whether to strip surrounding whitespace before checking.

    Returns:
        Missing field names in the same order they were requested.

    Raises:
        ValueError: If no required field names are provided.
    """
    # TODO: Validate that at least one required field name is present.
    if not required_fields:
        raise ValueError("No required fields found")
    # TODO: Check each requested field in order and collect the ones that are
    # missing or blank.
    missing :list[str] = []
    for field in required_fields:
        raw_value = form_data.get(field,"")
        value = raw_value.strip() if trim_values else raw_value
        if not value:
            missing.append(field)
    return missing
    raise NotImplementedError("implement collect_missing_fields")


if __name__ == "__main__":
    try:
        # Expected output: ["role"]
        assert collect_missing_fields(
            {"email": " ada@example.com ", "role": " "},
            "email",
            "role",
        ) == ["role"]
        # Expected output: ["region"]
        assert collect_missing_fields(
            {"team": "platform"},
            *["team", "region"],
        ) == ["region"]
        try:
            # Expected output: ValueError because required_fields is empty
            collect_missing_fields({"email": "x@example.com"})
            raise AssertionError("should have raised for empty required_fields")
        except ValueError:
            pass
        print("ex02_intermediate: all asserts passed")
    except NotImplementedError:
        print("ex02_intermediate: implement collect_missing_fields to run self-checks.")
