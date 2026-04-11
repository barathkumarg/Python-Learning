"""Exercise 03: Flexible event message builder.

Problem:
    Implement
    `build_event_message(name: str, /, *tags: str, uppercase: bool = False, **details: str) -> str`.
    The function should build a readable event message from a required event
    name, optional positional tags, and optional keyword details.

Constraints:
    - `name` is positional-only and must be non-empty after trimming.
    - `uppercase` is keyword-only because it appears after `*tags`.
    - `**details` captures key-value metadata from keyword args
      (example: `env="prod", level="basic"` -> `{"env": "prod", "level": "basic"}`).
    - Ignore blank tags after trimming.
    - Return a string formatted from the provided pieces.

Examples:
    build_event_message("signup") -> "signup"
    build_event_message("signup", "python", "day3", level="basic")
    -> "signup | tags=python,day3 | level=basic"
    build_event_message("deploy", uppercase=True, env="prod")
    -> "DEPLOY | env=prod"
    build_event_message("   ") -> ValueError
"""

from __future__ import annotations


def build_event_message(
    name: str,
    /,
    *tags: str,
    uppercase: bool = False,
    **details: str,
) -> str:
    """Return a formatted event message.

    Signature note:
        `**details: str` means Python captures extra keyword arguments as
        key-value pairs in a dict-like object named `details`.
        Example call: `build_event_message("signup", level="basic")`
        Inside function: `details == {"level": "basic"}`.

    Args:
        name: Required event name, passed positionally.
        *tags: Optional positional tags such as topic names.
        uppercase: Whether to uppercase the event name.
        **details: Optional key-value metadata to append as `key=value` pairs.

    Returns:
        A formatted event message string.

    Raises:
        ValueError: If `name` is empty after trimming.
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
    raise NotImplementedError("implement build_event_message")


if __name__ == "__main__":
    try:
        # Expected output: "signup"
        assert build_event_message("signup") == "signup"
        # Expected output: "signup | tags=python,day3 | level=basic"
        assert build_event_message("signup", "python", "day3", level="basic") == (
            "signup | tags=python,day3 | level=basic"
        )
        # Expected output: "DEPLOY | env=prod"
        assert build_event_message("deploy", uppercase=True, env="prod") == "DEPLOY | env=prod"
        print("ex03_advanced: all asserts passed")
    except NotImplementedError:
        print("ex03_advanced: implement build_event_message to run self-checks.")
