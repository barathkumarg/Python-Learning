
"""Exercise 03: NamedTuple for Records.

Problem:
    Define a NamedTuple `Book` with fields `title: str` and `pages: int`.
    Implement `shortest_book(books: tuple[Book, ...]) -> Book`.
    Return the book with the fewest pages.

Constraints:
    - books must not be empty; raise ValueError if so.
    - Do not mutate the input.
    - Return the result; do not print inside the function.

Examples:
    Book = NamedTuple('Book', [('title', str), ('pages', int)])
    books = (
        Book("Python 101", 250),
        Book("Deep Dive", 180),
        Book("Quick Start", 200),
    )
    shortest_book(books) -> Book(title="Deep Dive", pages=180)
    shortest_book(()) -> ValueError
"""

from __future__ import annotations
from typing import NamedTuple

class Book(NamedTuple):
    title: str
    pages: int

def shortest_book(books: tuple[Book, ...]) -> Book:
    """Return the Book with the fewest pages from books (a tuple of Book).

    Args:
        books: Tuple of Book objects (must not be empty).

    Returns:
        The Book with the fewest pages.

    Raises:
        ValueError: If books is empty.
    """
    # Your code here
    if not books:
        raise ValueError("Books not found")
    min_record = books[0]
    actual_name, actual_page = min_record
    for book in books:
        _, pages = book
        if pages <= actual_page:
            min_record = book
            _, actual_page = book # preserve the min pages value  
    return min_record
    pass

if __name__ == "__main__":
    books = (
        Book("Python 101", 250),
        Book("Deep Dive", 180),
        Book("Quick Start", 200),
    )
    assert shortest_book(books) == Book("Deep Dive", 180)
    # Error case
    try:
        shortest_book(())
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty books tuple")

    print("ex03_advanced: all asserts passed")
