# ex02_intermediate.py — Day 08: Strings and Encoding — Intermediate

"""
Intermediate exercises for Strings and Encoding.
Covers checklist items: #7–#8, #10–#14, #16, #22.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex02_intermediate.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations
import re

def normalize_compare(a: str, b: str) -> bool:
    """Compare two strings in a case-insensitive, locale-safe way using casefold.

    Args:
        a: First string.
        b: Second string.

    Returns:
        True if the strings are equal after casefold().

    Raises:
        ValueError: If either string is empty.

    Examples:
        >>> normalize_compare("Straße", "STRASSE")
        True
        >>> normalize_compare("hello", "world")
        False
    """
    # TODO: Implement this function
    # Hint: .casefold() is stronger than .lower() for international text
    if a.casefold() == b.casefold():
        return True
    return False


def find_all_positions(text: str, sub: str) -> list[int]:
    """Find all start indices where `sub` appears in `text`.

    Args:
        text: The string to search within.
        sub: The substring to find.

    Returns:
        List of 0-based start positions (empty list if not found).

    Raises:
        ValueError: If text or sub is empty.

    Examples:
        >>> find_all_positions("abcabc", "abc")
        [0, 3]
        >>> find_all_positions("aaa", "aa")
        [0, 1]
    """
    # TODO: Implement this function
    # Hint: use .find(sub, start) in a loop, advancing start by 1 after each hit
    
    seen : set[int] = set()
    for index in range (0,len(text)):
        position  = text.find(sub, index)
        seen.add(position)
    seen.remove(-1)
    print(list(seen))
    return list(seen)



def clean_fields(csv_line: str, sep: str = ",") -> list[str]:
    """Split a line on `sep`, strip each field, and drop empty fields.

    Args:
        csv_line: Raw line of text.
        sep: Delimiter to split on (default comma).

    Returns:
        List of cleaned, non-empty field strings.

    Raises:
        ValueError: If csv_line is empty after stripping.

    Examples:
        >>> clean_fields("  alice , bob ,  , charlie  ")
        ['alice', 'bob', 'charlie']
    """
    # TODO: Implement this function
    # Hint: split → strip each → filter out empty strings

    clean_names = [name.strip() for name in csv_line.strip().split(sep) if name.strip()]
    print(clean_names)
    return clean_names

def censor_word(text: str, word: str) -> str:
    """Replace every occurrence of `word` with '***' (case-insensitive).

    The replacement preserves surrounding text. Uses `in` to check presence
    and builds the result via case-insensitive matching.

    Args:
        text: Original text.
        word: Word to censor.

    Returns:
        Text with all case-insensitive occurrences of word replaced by '***'.

    Raises:
        ValueError: If text or word is empty.

    Examples:
        >>> censor_word("Hello hello HELLO world", "hello")
        '*** *** *** world'
    """
    # TODO: Implement this function
    # Hint: use re.sub with re.IGNORECASE, or iterate via .lower()
    pattern = re.escape(word)

    replacement = '***'
    
    return re.sub(pattern, replacement, text, flags=re.IGNORECASE)


def format_invoice_line(item: str, qty: int, price: float) -> str:
    """Format an invoice line with aligned columns using f-strings.

    Format: "{item:<20s} x{qty:<3d} ${price:>8.2f}"

    Args:
        item: Item description.
        qty: Quantity (≥ 1).
        price: Unit price (≥ 0).

    Returns:
        Formatted invoice line string.

    Raises:
        ValueError: If item is empty, qty < 1, or price < 0.

    Examples:
        >>> format_invoice_line("Widget", 3, 9.99)
        'Widget               x3   $    9.99'
    """
    # TODO: Implement this function
    # Also implement a second version using .format() for practice (concept #14)
    ...
    if qty < 1 or price < 0:
        raise ValueError("Quantity must be ≥ 1 and price must be ≥ 0.")
    return f"{item:<20s} x{qty:<3d} ${price:>8.2f}"


def build_template(name: str, items: list[str]) -> str:
    """Build a multi-line receipt template using textwrap.dedent.

    The receipt should look like:
        Receipt for {name}
        ---
        - item1
        - item2
        ---
        Total: {count} items

    Args:
        name: Customer name.
        items: List of item descriptions.

    Returns:
        Dedented multi-line receipt string (no leading/trailing blank lines).

    Raises:
        ValueError: If name is empty or items is empty.

    Examples:
        >>> print(build_template("Alice", ["Pen", "Book"]))
        Receipt for Alice
        ---
        - Pen
        - Book
        ---
        Total: 2 items
    """
    # TODO: Implement this function
    # Hint: use textwrap.dedent() with a triple-quoted template
    ...
    receipt = f"""Receipt for {name}
---
"""
    for item in items:
        receipt += f"- {item}\n"        
    receipt += f"""---
Total: {len(items)} items"""
    return receipt


if __name__ == "__main__":
    # ─── normalize_compare checks ───
    assert normalize_compare("Straße", "STRASSE") is True, "German casefold"
    assert normalize_compare("hello", "HELLO") is True, "basic case"
    assert normalize_compare("a", "b") is False, "different strings"

    # ─── find_all_positions checks ───
    assert find_all_positions("abcabc", "abc") == [0, 3], "two matches"
    assert find_all_positions("aaa", "aa") == [0, 1], "overlapping"
    assert find_all_positions("hello", "xyz") == [], "no match"

    # ─── clean_fields checks ───
    assert clean_fields("  alice , bob ,  , charlie  ") == ["alice", "bob", "charlie"]
    assert clean_fields("one|two||three", sep="|") == ["one", "two", "three"]
    assert clean_fields("solo") == ["solo"]

    # ─── censor_word checks ───
    assert censor_word("Hello hello HELLO world", "hello") == "*** *** *** world"
    assert censor_word("no match here", "xyz") == "no match here"
    assert censor_word("aAbBaA", "aa") == "***bB***"

    # ─── format_invoice_line checks ───
    line = format_invoice_line("Widget", 3, 9.99)
    assert "Widget" in line and "9.99" in line, "contains item and price"
    assert line == "Widget               x3   $    9.99", "exact format"

    # ─── build_template checks ───
    receipt = build_template("Alice", ["Pen", "Book"])
    assert "Receipt for Alice" in receipt, "header present"
    assert "- Pen" in receipt and "- Book" in receipt, "items present"
    assert "Total: 2 items" in receipt, "total present"

    print("ex02_intermediate.py: all asserts passed ✓")
