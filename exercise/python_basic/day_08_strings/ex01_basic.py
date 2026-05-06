# ex01_basic.py — Day 08: Strings and Encoding — Basic

"""
Basic exercises for Strings and Encoding.
Covers checklist items: #1–#6, #9, #15.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex01_basic.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations


def create_greeting(name: str, times: int = 1) -> str:
    """Create a greeting string using concatenation and repetition.

    Build the pattern: "Hello, {name}! " repeated `times` times, stripped.

    Args:
        name: Person's name.
        times: How many times to repeat the greeting (≥ 1).

    Returns:
        The repeated greeting with trailing whitespace stripped.

    Raises:
        ValueError: If name is empty or times < 1.

    Examples:
        >>> create_greeting("Alice", 2)
        'Hello, Alice! Hello, Alice!'
        >>> create_greeting("Bob")
        'Hello, Bob!'
    """
    # TODO: Implement this function
    # Hint: use + for concatenation and * for repetition, then .strip()
    greetings = f"Hello, {name}! "
    final_greetings = greetings * times
    final_greetings = final_greetings.rstrip()
    return final_greetings


def first_last(s: str) -> tuple[str, str, int]:
    """Return the first character, last character, and length of a string.

    Args:
        s: Input string.

    Returns:
        Tuple of (first_char, last_char, length).

    Raises:
        ValueError: If s is empty.

    Examples:
        >>> first_last("Python")
        ('P', 'n', 6)
        >>> first_last("A")
        ('A', 'A', 1)
    """
    # TODO: Implement this function
    return s[0], s[-1], len(s)


def slice_extract(s: str, start: int, stop: int) -> str:
    """Extract a substring using slicing with validation.

    Args:
        s: Input string.
        start: Start index (inclusive, 0-based).
        stop: Stop index (exclusive).

    Returns:
        The substring s[start:stop].

    Raises:
        ValueError: If s is empty or start/stop out of range.

    Examples:
        >>> slice_extract("abcdef", 1, 4)
        'bcd'
        >>> slice_extract("hello", 0, 5)
        'hello'
    """
    # TODO: Implement this function
    # Validate: s non-empty, 0 <= start < stop <= len(s)
    return s[start:stop]


def safe_replace_char(s: str, index: int, new_char: str) -> str:
    """Return a new string with the character at `index` replaced.

    Strings are immutable — build a new one via slicing.

    Args:
        s: Input string.
        index: Position to replace (0-based, supports negative).
        new_char: Single character replacement.

    Returns:
        New string with the replacement applied.

    Raises:
        ValueError: If s is empty, new_char is not length 1, or index out of range.

    Examples:
        >>> safe_replace_char("hello", 0, "H")
        'Hello'
        >>> safe_replace_char("world", -1, "!")
        'worl!'
    """
    # TODO: Implement this function
    # Hint: s[:idx] + new_char + s[idx+1:]  (handle negative index first)
    return s.replace(s[index], new_char)


def raw_path_parts(raw_path: str) -> list[str]:
    r"""Split a raw Windows-style path on backslashes and return non-empty parts.

    Args:
        raw_path: A path string (e.g. r"C:\\Users\\alice\\docs").

    Returns:
        List of path segments.

    Raises:
        ValueError: If raw_path is empty.

    Examples:
        >>> raw_path_parts(r"C:\\Users\\alice")
        ['C:', 'Users', 'alice']
    """
    # TODO: Implement this function
    # Hint: split on "\\" and filter out empty strings
    return raw_path.split('\\')


def classify_token(token: str) -> str:
    """Classify a token as "digit", "alpha", "alnum", or "other".

    Uses .isdigit(), .isalpha(), .isalnum() in priority order.

    Args:
        token: Non-empty string to classify.

    Returns:
        One of "digit", "alpha", "alnum", "other".

    Raises:
        ValueError: If token is empty.

    Examples:
        >>> classify_token("42")
        'digit'
        >>> classify_token("hello")
        'alpha'
        >>> classify_token("h3llo")
        'alnum'
        >>> classify_token("h3!lo")
        'other'
    """
    # TODO: Implement this function
    # Check isdigit first, then isalpha, then isalnum, else "other"
    if token.isdigit():
        return 'digit'
    if token.isalpha():
        return 'alpha'
    if token.isalnum():
        return 'alnum'
    else:
        return 'other'
    


if __name__ == "__main__":
    # ─── create_greeting checks ───
    assert create_greeting("Alice", 2) == "Hello, Alice! Hello, Alice!", "repeat 2"
    assert create_greeting("Bob") == "Hello, Bob!", "default times=1"
    assert create_greeting("X", 3) == "Hello, X! Hello, X! Hello, X!", "repeat 3"

    # ─── first_last checks ───
    assert first_last("Python") == ("P", "n", 6), "normal"
    assert first_last("A") == ("A", "A", 1), "single char"
    assert first_last("ab") == ("a", "b", 2), "two chars"

    # ─── slice_extract checks ───
    assert slice_extract("abcdef", 1, 4) == "bcd", "middle slice"
    assert slice_extract("hello", 0, 5) == "hello", "full slice"
    assert slice_extract("test", 2, 3) == "s", "single char slice"

    # ─── safe_replace_char checks ───
    assert safe_replace_char("hello", 0, "H") == "Hello", "replace first"
    assert safe_replace_char("world", -1, "!") == "worl!", "negative index"
    assert safe_replace_char("abc", 1, "X") == "aXc", "replace middle"

    # ─── raw_path_parts checks ───
    assert raw_path_parts(r"C:\Users\alice") == ["C:", "Users", "alice"], "windows path"
    assert raw_path_parts("single") == ["single"], "no separator"

    # ─── classify_token checks ───
    assert classify_token("42") == "digit", "pure digits"
    assert classify_token("hello") == "alpha", "pure alpha"
    assert classify_token("h3llo") == "alnum", "mixed alnum"
    assert classify_token("h3!lo") == "other", "has punctuation"

    print("ex01_basic.py: all asserts passed ✓")
