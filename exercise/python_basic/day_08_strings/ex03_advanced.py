# ex03_advanced.py — Day 08: Strings and Encoding — Advanced

"""
Advanced exercises for Strings and Encoding.
Covers checklist items: #17–#25.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex03_advanced.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations


def char_frequency(text: str) -> dict[str, int]:
    """Count character frequency, ignoring spaces.

    Uses collections.Counter internally.

    Args:
        text: Input string.

    Returns:
        Dict mapping each non-space character to its count.

    Raises:
        ValueError: If text is empty.

    Examples:
        >>> char_frequency("aab cc")
        {'a': 2, 'b': 1, 'c': 2}
    """
    # TODO: Implement this function
    # Hint: from collections import Counter; exclude spaces
    ...
    from collections import Counter
    return dict(Counter(text.replace(" ","")))


def safe_decode(data: bytes, encoding: str = "utf-8") -> str:
    """Decode bytes to str safely — return "" on failure instead of raising.

    This demonstrates the str/bytes boundary (concept #24): never concatenate
    str + bytes; always decode explicitly.

    Args:
        data: Raw bytes to decode.
        encoding: Target encoding.

    Returns:
        Decoded string, or "" if decoding fails.

    Examples:
        >>> safe_decode(b"hello")
        'hello'
        >>> safe_decode(b"\\xff\\xfe", "ascii")
        ''
    """
    # TODO: Implement this function
    # Hint: try/except UnicodeDecodeError
    ...
    try:
        return data.decode(encoding)
    except UnicodeDecodeError:
        return ""




def mask_bytes(data: bytes, mask_byte: int) -> bytes:
    """XOR each byte in `data` with `mask_byte` using bytearray.

    Args:
        data: Input bytes.
        mask_byte: Integer 0–255 to XOR with each byte.

    Returns:
        New bytes object with each byte XORed.

    Raises:
        ValueError: If data is empty or mask_byte not in 0–255.

    Examples:
        >>> mask_bytes(b"hi", 0xFF)
        b'\\x97\\x96'
        >>> mask_bytes(mask_bytes(b"hi", 0xFF), 0xFF)
        b'hi'
    """
    # TODO: Implement this function
    # Hint: ba = bytearray(data); loop and XOR each element; return bytes(ba)
    ...
    byte_text = bytearray(data)
    for byte_index in range (0, len(byte_text)):
        byte_text[byte_index] = byte_text[byte_index] ^ mask_byte
    return bytes(byte_text)





def normalize_and_compare(a: str, b: str) -> bool:
    """NFC-normalize both strings and compare for equality.

    Handles cases where visually identical strings have different
    Unicode representations (composed vs decomposed).

    Args:
        a: First string.
        b: Second string.

    Returns:
        True if NFC-normalized forms are equal.

    Examples:
        >>> normalize_and_compare("café", "cafe\\u0301")
        True
        >>> normalize_and_compare("hello", "world")
        False
    """
    # TODO: Implement this function
    # Hint: import unicodedata; unicodedata.normalize("NFC", s)
    ...
    import unicodedata
    return unicodedata.normalize("NFC", b) == a
 


def strip_punctuation(text: str) -> str:
    """Remove all ASCII punctuation from text using str.maketrans + translate.

    Args:
        text: Input string.

    Returns:
        String with all ASCII punctuation characters removed.

    Raises:
        ValueError: If text is empty.

    Examples:
        >>> strip_punctuation("Hello, World!")
        'Hello World'
        >>> strip_punctuation("no-punct-here")
        'nopuncthere'
    """
    # TODO: Implement this function
    # Hint: import string; table = str.maketrans("", "", string.punctuation)
    ...
    import string
    table = str.maketrans("","",string.punctuation)
    return text.strip().translate(table)


def extract_emails(text: str) -> list[str]:
    """Extract all email addresses from text using re.findall.

    Uses a simple pattern: [\\w.+-]+@[\\w-]+\\.[\\w.-]+

    Args:
        text: Input text that may contain email addresses.

    Returns:
        List of extracted email address strings.

    Examples:
        >>> extract_emails("Contact alice@example.com or bob@test.org")
        ['alice@example.com', 'bob@test.org']
        >>> extract_emails("no emails here")
        []
    """
    # TODO: Implement this function
    # Hint: import re; re.findall(pattern, text)
    ...
    import re 
    pattern = "[\\w.+-]+@[\\w-]+\\.[\\w.-]+"
    emails = re.findall(pattern, text)
    print("Extartct emails: ", emails)
    return emails


def slugify(title: str, max_length: int = 80) -> str:
    """Convert a title into a URL-safe slug (industrial pattern).

    Steps: NFKD normalize → encode ASCII (ignore errors) → decode →
    lowercase → replace non-alphanumeric with hyphens → collapse
    multiple hyphens → strip hyphens → truncate to max_length.

    Args:
        title: Human-readable title.
        max_length: Maximum slug length (default 80).

    Returns:
        URL-safe slug string.

    Raises:
        ValueError: If title is empty or produces empty slug.

    Examples:
        >>> slugify("Hello, World! — Part 2")
        'hello-world-part-2'
        >>> slugify("Ärger mit Übung")
        'arger-mit-ubung'
    """
    # TODO: Implement this function
    # Hint: unicodedata.normalize("NFKD", ...).encode("ascii", "ignore").decode()
    # Then re.sub(r"[^a-z0-9]+", "-", ...).strip("-")
    ...
    import unicodedata
    import re
    if not title:
        raise ValueError("Title cannot be empty")

    # 1. NFKD normalize & encode to ASCII (removes accents)
    # Example: "Ä" becomes "A" + "combining diaeresis", then "A"
    slug = unicodedata.normalize("NFKD", title)
    slug = slug.encode("ascii", "ignore").decode("ascii")

    # 2. Lowercase
    slug = slug.lower()

    # 3. Replace non-alphanumeric characters with hyphens
    slug = re.sub(r"[^a-z0-9]+", "-", slug)

    # 4. Collapse multiple hyphens and strip from ends
    slug = re.sub(r"-+", "-", slug).strip("-")

    # 5. Truncate to max_length (ensuring we don't end on a trailing hyphen)
    slug = slug[:max_length].rstrip("-")

    if not slug:
        raise ValueError(f"Title '{title}' produced an empty slug")

    return slug



if __name__ == "__main__":
    # ─── char_frequency checks ───
    assert char_frequency("aab cc") == {"a": 2, "b": 1, "c": 2}, "basic frequency"
    assert char_frequency("x") == {"x": 1}, "single char"
    assert char_frequency("a a a") == {"a": 3}, "spaces ignored"

    # ─── safe_decode checks ───
    assert safe_decode(b"hello") == "hello", "valid utf-8"
    assert safe_decode(b"\xff\xfe", "ascii") == "", "invalid returns empty"
    assert safe_decode("café".encode("utf-8")) == "café", "round-trip"

    # ─── mask_bytes checks ───
    assert mask_bytes(mask_bytes(b"hello", 0xAA), 0xAA) == b"hello", "double XOR = identity"
    assert mask_bytes(b"\x00", 0xFF) == b"\xff", "zero XOR 0xFF"

    # ─── normalize_and_compare checks ───
    assert normalize_and_compare("café", "cafe\u0301") is True, "NFC normalization"
    assert normalize_and_compare("hello", "world") is False, "different strings"
    assert normalize_and_compare("abc", "abc") is True, "identical"

    # ─── strip_punctuation checks ───
    assert strip_punctuation("Hello, World!") == "Hello World", "comma and bang"
    assert strip_punctuation("no-punct-here") == "nopuncthere", "hyphens removed"
    assert strip_punctuation("clean") == "clean", "no punctuation"

    # ─── extract_emails checks ───
    assert extract_emails("Contact alice@example.com or bob@test.org") == [
        "alice@example.com",
        "bob@test.org",
    ], "two emails"
    assert extract_emails("no emails") == [], "empty list"

    # ─── slugify checks ───
    assert slugify("Hello, World! — Part 2") == "hello-world-part-2", "basic slug"
    assert slugify("Ärger mit Übung") == "arger-mit-ubung", "unicode fold"
    assert slugify("  Spaces  Everywhere  ") == "spaces-everywhere", "stripped"

    print("ex03_advanced.py: all asserts passed ✓")
