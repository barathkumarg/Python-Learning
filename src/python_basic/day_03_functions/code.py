"""Day 03 reference code: clear function signatures and small reusable helpers.

Design choices:
- Start with functions that validate input and return values instead of printing.
- Progress from simple parameters to defaults, keyword-only options, `*args`,
  `**kwargs`, and argument unpacking.
- Keep examples practical: greeting text, order formatting, form validation,
  event metadata, and small sort helpers.

Signature symbols used in this file:
- `/` means parameters before it are positional-only.
- `*` (bare separator) means parameters after it are keyword-only.
- `*name` (for example `*tags`) collects extra positional arguments into a tuple.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping


def build_greeting(name: str, greeting: str = "Hello") -> str:
    """Return a greeting for a non-empty name.

    Args:
        name: Name to greet.
        greeting: Optional greeting word or phrase.

    Returns:
        A formatted greeting string.

    Raises:
        ValueError: If `name` is empty after trimming.
    """

    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"{greeting}, {cleaned}!"


def describe_order(
    item: str,
    /,
    quantity: int,
    *,
    price: float,
    currency: str = "USD",
) -> str:
    """Return a readable order summary.

    Args:
        item: Product name. Positional-only because it appears before `/`.
        quantity: Number of units ordered.
        price: Price per unit.
        currency: Currency label for the total. Keyword-only because it appears after `*`.

    Returns:
        A one-line order description.

    Raises:
        ValueError: If quantity or price is negative.
    """

    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    if price < 0:
        raise ValueError("price must be non-negative")

    total = round(quantity * price, 2)
    return f"{quantity} x {item} -> {currency} {total:.2f}"


def build_student_profile(
    name: str,
    *,
    track: str,
    level: str = "beginner",
) -> str:
    """Return a simple student label using keyword-only options.

    `*` in the signature is a separator. Parameters after it cannot be passed
    positionally, so callers must write `track=...` and `level=...`.

    Args:
        name: Student name.
        track: Learning track or topic name. Keyword-only because it is after `*`.
        level: Optional learning level. Also keyword-only.

    Returns:
        A formatted profile string.

    Raises:
        ValueError: If `name` or `track` is empty after trimming.
    """

    cleaned_name = name.strip()
    cleaned_track = track.strip()
    if not cleaned_name:
        raise ValueError("name must not be empty")
    if not cleaned_track:
        raise ValueError("track must not be empty")

    return f"{cleaned_name} -> {cleaned_track} ({level.strip()})"


def collect_missing_fields(
    form_data: Mapping[str, str],
    *required_fields: str,
    trim_values: bool = True,
) -> list[str]:
    """Return required field names that are missing or blank.

    Args:
        form_data: Input dictionary, such as a submitted form payload.
        *required_fields: Names that must exist and contain non-blank values.
        trim_values: Whether to strip surrounding whitespace before checking.

    Returns:
        Missing field names in the same order they were requested.

    Raises:
        ValueError: If no required fields are provided.
    """

    if not required_fields:
        raise ValueError("provide at least one required field")

    missing: list[str] = []
    for field_name in required_fields:
        raw_value = form_data.get(field_name, "")
        value = raw_value.strip() if trim_values else raw_value
        if not value:
            missing.append(field_name)
    return missing


def build_event_message(
    name: str,
    /,
    *tags: str,
    uppercase: bool = False,
    **details: str,
) -> str:
    """Return a formatted event message with optional tags and details.

    Signature meaning:
    - `name` is before `/`, so it is positional-only.
    - `*tags` collects any extra positional arguments.
    - Parameters after `*tags` (like `uppercase`) are keyword-only.
    - `**details` collects extra keyword arguments.

    Args:
        name: Required event name, passed positionally.
        *tags: Optional short labels such as topic names or environments.
        uppercase: Whether to uppercase the event name.
        **details: Optional named metadata to append as key=value pairs.

    Returns:
        A formatted event string.

    Raises:
        ValueError: If the event name is blank after trimming.
    """

    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must not be empty")

    event_name = cleaned_name.upper() if uppercase else cleaned_name
    parts = [event_name]

    cleaned_tags = [tag.strip() for tag in tags if tag.strip()]
    if cleaned_tags:
        parts.append(f"tags={','.join(cleaned_tags)}")

    sorted_details = sorted(details.items(), key=lambda item: item[0])
    for key, value in sorted_details:
        parts.append(f"{key}={str(value).strip()}")

    return " | ".join(parts)


def sort_records(
    records: list[tuple[str, int]],
    *,
    key_func: Callable[[tuple[str, int]], object] | None = None,
    reverse: bool = False,
) -> list[tuple[str, int]]:
    """Return a sorted copy of `(name, score)` records.

    Args:
        records: List of `(name, score)` pairs.
        key_func: Optional sort key; defaults to lowercased name.
        reverse: Whether to reverse the final ordering.

    Returns:
        A new sorted list, leaving the original input unchanged.
    """

    key_func = key_func or (lambda record: record[0].lower())
    return sorted(records, key=key_func, reverse=reverse)


if __name__ == "__main__":
    print(build_greeting("barath"))  # Expected output: Hello, barath!
    print(build_greeting("Ada", greeting="Welcome"))  # Expected output: Welcome, Ada!

    order_options = {"price": 49.99, "currency": "USD"}
    print(describe_order("Notebook", 3, **order_options))  # Expected output: 3 x Notebook -> USD 149.97
    print(build_student_profile("Barath", track="python"))  # Expected output: Barath -> python (beginner)
    print(
        build_student_profile("Ada", track="automation", level="intermediate")
    )  # Expected output: Ada -> automation (intermediate)

    form_payload = {"email": " ada@example.com ", "role": " ", "team": "platform"}
    required = ["email", "role", "team"]
    print(collect_missing_fields(form_payload, *required))  # Expected output: ['role']

    print(
        build_event_message("signup", "python", "day3", level="basic", owner="barath")
    )  # Expected output: signup | tags=python,day3 | level=basic | owner=barath

    records = [("Maya", 88), ("Arun", 91), ("Lina", 84)]
    print(sort_records(records))  # Expected output: [('Arun', 91), ('Lina', 84), ('Maya', 88)]
    print(
        sort_records(records, key_func=lambda record: record[1], reverse=True)
    )  # Expected output: [('Arun', 91), ('Maya', 88), ('Lina', 84)]
