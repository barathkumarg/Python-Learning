# code.py — Day 08: Strings and Encoding

"""
Strings and Encoding — production-style reference implementations.

Covers: creation, indexing, slicing, immutability, case methods, search,
boolean checks, strip, split/join, replace, f-strings, concatenation,
membership, character frequency, bytes/str encoding, bytearray,
Unicode normalization, regex preview, multi-line, translate/maketrans,
and industrial patterns (slugify, sanitize).

Style: typed signatures, Google docstrings, explicit validation, inline asserts.
"""

from __future__ import annotations

import re
import unicodedata
from collections import Counter


# ─── Section 1: Validation and Search ───


def validate_and_search(text: str, substring: str) -> dict[str, object]:
    """Demonstrate len, find, index, startswith, isdigit, isalpha, and `in`.

    Args:
        text: The string to inspect.
        substring: The substring to search for.

    Returns:
        Dict with length, find position, membership, and boolean checks.

    Raises:
        ValueError: If text is empty.

    Examples:
        >>> validate_and_search("Hello-42", "42")
        {'length': 8, 'find_pos': 6, 'contains': True, 'starts_hello': True, 'is_digit': False, 'is_alpha': False}
    """
    if not text:
        raise ValueError("text must be non-empty")
    return {
        "length": len(text),
        "find_pos": text.find(substring),
        "contains": substring in text,
        "starts_hello": text.startswith("Hello"),
        "is_digit": text.isdigit(),
        "is_alpha": text.isalpha(),
    }


# ─── Section 2: Case Transforms ───


def transform_case(text: str) -> dict[str, str]:
    """Apply upper, lower, and casefold transforms.

    Args:
        text: Input string.

    Returns:
        Dict with upper, lower, and casefold results.

    Raises:
        ValueError: If text is empty.

    Examples:
        >>> transform_case("Straße")
        {'upper': 'STRASSE', 'lower': 'straße', 'casefold': 'strasse'}
    """
    if not text:
        raise ValueError("text must be non-empty")
    return {
        "upper": text.upper(),
        "lower": text.lower(),
        "casefold": text.casefold(),
    }


# ─── Section 3: Character Frequency ───


def char_frequency(text: str, *, ignore_spaces: bool = False) -> dict[str, int]:
    """Count character occurrences using collections.Counter.

    Args:
        text: Input string.
        ignore_spaces: If True, spaces are excluded from the count.

    Returns:
        Dict mapping each character to its count.

    Raises:
        ValueError: If text is empty.

    Examples:
        >>> char_frequency("aab")
        {'a': 2, 'b': 1}
    """
    if not text:
        raise ValueError("text must be non-empty")
    data = text.replace(" ", "") if ignore_spaces else text
    return dict(Counter(data))


# ─── Section 4: Encoding and Decoding ───


def encode_decode_demo(text: str, encoding: str = "utf-8") -> dict[str, object]:
    """Encode text to bytes and decode back, showing byte length vs char length.

    Args:
        text: Input string.
        encoding: Target encoding (default utf-8).

    Returns:
        Dict with encoded bytes, byte_length, char_length, and round-trip result.

    Raises:
        ValueError: If text is empty.

    Examples:
        >>> encode_decode_demo("café")
        {'encoded': b'caf\\xc3\\xa9', 'byte_length': 5, 'char_length': 4, 'round_trip': 'café'}
    """
    if not text:
        raise ValueError("text must be non-empty")
    encoded = text.encode(encoding)
    return {
        "encoded": encoded,
        "byte_length": len(encoded),
        "char_length": len(text),
        "round_trip": encoded.decode(encoding),
    }


# ─── Section 5: Sanitize and Transform ───


def sanitize_text(text: str) -> str:
    """Strip whitespace, remove control characters via translate/maketrans.

    Args:
        text: Raw input that may contain leading/trailing whitespace and
              ASCII control characters (0x00–0x1F except newline).

    Returns:
        Cleaned string with control chars removed and whitespace stripped.

    Raises:
        ValueError: If text is empty after stripping.

    Examples:
        >>> sanitize_text("  hello\\x00world  ")
        'helloworld'
    """
    # Build translation table that maps control chars (except \\n) to None
    control_chars = {c: None for c in range(0x00, 0x20) if c != ord("\n")}
    print(control_chars)
    table = str.maketrans(control_chars)
    print(table)
    cleaned = text.strip().translate(table)
    if not cleaned:
        raise ValueError("text is empty after sanitization")
    return cleaned


# ─── Section 6: Industrial — Slugify ───


def slugify(title: str, *, max_length: int = 80) -> str:
    """Convert a title into a URL-safe slug.

    Steps: NFKD normalize → ASCII fold → lowercase → replace non-alnum with
    hyphens → collapse multiple hyphens → strip leading/trailing hyphens → truncate.

    Args:
        title: Human-readable title.
        max_length: Maximum slug length (default 80).

    Returns:
        URL-safe slug string.

    Raises:
        ValueError: If title is empty or produces an empty slug.

    Examples:
        >>> slugify("  Hello, World! — Part 2  ")
        'hello-world-part-2'
    """
    if not title or not title.strip():
        raise ValueError("title must be non-empty")
    # Normalize Unicode, encode to ASCII (drop non-ASCII), decode back
    normalized = unicodedata.normalize("NFKD", title)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    # Lowercase, replace non-alphanumeric with hyphens, collapse, strip
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
    if not slug:
        raise ValueError(f"title produced empty slug, got {title!r}")
    return slug[:max_length].rstrip("-")


# ─── Self-checks ───

if __name__ == "__main__":
    # Expected output: {'length': 8, 'find_pos': 6, 'contains': True, ...}
    print(f"validate_and_search: {validate_and_search('Hello-42', '42')}")

    # Expected output: {'upper': 'STRASSE', 'lower': 'straße', 'casefold': 'strasse'}
    print(f"transform_case: {transform_case('Straße')}")

    # Expected output: {'b': 1, 'a': 3, 'n': 2}
    print(f"char_frequency: {char_frequency('banana')}")

    # Expected output: {'encoded': b'caf\xc3\xa9', 'byte_length': 5, ...}
    print(f"encode_decode_demo: {encode_decode_demo('café')}")

    # Expected output: 'helloworld'
    print(f"sanitize_text: {sanitize_text('  hello\x00world  ')!r}")

    # Expected output: 'hello-world-part-2'
    print(f"slugify: {slugify('  Hello, World! — Part 2  ')!r}")

    print("\ncode.py: all demos ran ✓")
