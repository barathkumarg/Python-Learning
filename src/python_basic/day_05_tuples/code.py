"""
Day 05 — Tuples and NamedTuple

This module demonstrates tuple usage, immutability, packing/unpacking, multiple returns, and the use of NamedTuple for DTO-style records. Design choices favor clarity, type safety, and idiomatic Python patterns for grouping related data.
"""
from typing import NamedTuple, Any, Sequence

def min_max(nums: Sequence[int]) -> tuple[int, int]:
    """Return the minimum and maximum values in a sequence.

    Args:
        nums: Sequence of integers.
    Returns:
        Tuple of (min, max).
    Raises:
        ValueError: If nums is empty.
    """
    if not nums:
        raise ValueError("Input sequence is empty.")
    return min(nums), max(nums)

class Point(NamedTuple):
    """2D point with x and y coordinates."""
    x: int
    y: int

def parse_csv_row(row: str) -> tuple[str, int]:
    """Parse a CSV row into a name and age tuple.

    Args:
        row: CSV string in the format 'name,age'.
    Returns:
        Tuple of (name, age).
    Raises:
        ValueError: If the row is not valid.
    """
    try:
        name, age_str = row.strip().split(",")
        age = int(age_str)
        return name, age
    except Exception as e:
        raise ValueError(f"Invalid row '{row}': {e}")

def make_user(name: str, age: int) -> 'User':
    """Create a User NamedTuple from name and age."""
    return User(name, age)

class User(NamedTuple):
    name: str
    age: int

def swap(a: Any, b: Any) -> tuple[Any, Any]:
    """Return a tuple with the values swapped."""
    return b, a

if __name__ == "__main__":
    # Demo: min_max
    # ...assert removed...
    print(min_max([2, 8, 5]))  # Expected output: (2, 8)

    # Demo: Point NamedTuple
    p = Point(3, 4)
    # ...assert removed...
    print(p)  # Expected output: Point(x=3, y=4)

    # Demo: parse_csv_row
    # ...assert removed...
    print(parse_csv_row("alice,30"))  # Expected output: ('alice', 30)

    # Demo: User NamedTuple
    user = make_user("bob", 25)
    # ...assert removed...
    print(user)  # Expected output: User(name='bob', age=25)

    # Demo: swap
    # ...assert removed...
    print(swap(1, 2))  # Expected output: (2, 1)
