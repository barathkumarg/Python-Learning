"""Exercise 01: Word frequency counter.

Problem:
    Implement `word_frequency(text: str) -> dict[str, int]`.
    Split on whitespace, count case-insensitively (lowercase).

    Stretch: Implement `top_n_words(freq: dict[str, int], n: int = 3) -> list[tuple[str, int]]`.
    Return the n most frequent words sorted by count descending, then alphabetically.

Constraints:
    - Raise `TypeError` if `text` is not a string.
    - Do NOT use `collections.Counter` — practice `get()` with default.
    - Do NOT mutate any input.

Examples:
    word_frequency("the cat sat on the mat the cat")
        -> {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
    top_n_words({"the": 3, "cat": 2, "sat": 1}, n=2)
        -> [("the", 3), ("cat", 2)]
"""

from __future__ import annotations


def word_frequency(text: str) -> dict[str, int]:
    """Return a case-insensitive word frequency dict.

    Args:
        text: Input string to count words from.

    Returns:
        Dict mapping lowercased words to their occurrence count.

    Raises:
        TypeError: If *text* is not a string.
    """
    # TODO: validate that text is a str, raise TypeError if not
    # TODO: split text on whitespace
    # TODO: lowercase each word
    # TODO: count occurrences using dict.get(word, 0) + 1
    # TODO: return the counts dict
    raise NotImplementedError()


def top_n_words(freq: dict[str, int], n: int = 3) -> list[tuple[str, int]]:
    """Return the n most frequent words sorted by count desc, then alphabetically.

    Args:
        freq: Word frequency dict (word -> count).
        n: Number of top words to return.

    Returns:
        List of (word, count) tuples.

    Raises:
        ValueError: If *n* is not positive.
    """
    # TODO: validate n > 0
    # TODO: sort freq.items() by (-count, word) using sorted() + lambda
    # TODO: return first n items
    raise NotImplementedError()


if __name__ == "__main__":
    try:
        # --- word_frequency ---
        result = word_frequency("the cat sat on the mat the cat")
        # Expected output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
        assert result["the"] == 3, f"expected 3, got {result.get('the')}"
        assert result["cat"] == 2, f"expected 2, got {result.get('cat')}"
        assert result["sat"] == 1

        # empty string
        assert word_frequency("") == {}

        # TypeError on non-string
        try:
            word_frequency(123)  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # --- top_n_words (stretch) ---
        freq = {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
        top2 = top_n_words(freq, n=2)
        # Expected output: [('the', 3), ('cat', 2)]
        assert top2 == [("the", 3), ("cat", 2)], f"got {top2}"

        print("ex01_basic: all asserts passed")
    except NotImplementedError:
        print("ex01_basic: implement word_frequency to run self-checks.")
