# code.py — Day 13: Comprehensions

"""
Comprehensions — production-style reference implementations.

Covers: list / dict / set comprehensions, generator expressions, generator
functions (yield/next/StopIteration), scoping, walrus, performance, the
itertools bridge, and industrial projection + indexing patterns.
Style: typed signatures, Google docstrings, explicit validation, runnable
demos with `# Expected output:` comments.
"""

from __future__ import annotations

import sys
from collections.abc import Iterable, Iterator
from itertools import islice
from typing import Any, TypeVar

T = TypeVar("T")
K = TypeVar("K")


# ─── Section 1: List comprehensions (#1–#4) ───

def square_all(nums: Iterable[int]) -> list[int]:
    """Return ``[n*n for n in nums]`` (concept #1).

    Args:
        nums: Iterable of ints.

    Returns:
        List of squares in input order.

    Raises:
        TypeError: If any element is not an int.

    Examples:
        >>> square_all([1, 2, 3])
        [1, 4, 9]
    """
    out = [n * n for n in nums]
    if not all(isinstance(n, int) and not isinstance(n, bool) for n in out):
        # Re-validate after materialising — comprehensions raise the natural error too.
        raise TypeError("square_all expects ints only")
    return out


def keep_positive(nums: Iterable[float]) -> list[float]:
    """Filter with a trailing ``if`` clause (concept #2).

    Args:
        nums: Iterable of numbers.

    Returns:
        List of strictly positive values, in input order.

    Examples:
        >>> keep_positive([-1, 0, 2, 5])
        [2, 5]
    """
    return [n for n in nums if n > 0]


def clamp_signs(nums: Iterable[float]) -> list[float]:
    """Take the absolute value using a conditional expression (concept #3).

    Args:
        nums: Iterable of numbers.

    Returns:
        List of ``|n|`` in input order.

    Examples:
        >>> clamp_signs([-3, -1, 0, 2])
        [3, 1, 0, 2]
    """
    return [n if n >= 0 else -n for n in nums]


def flatten_matrix(matrix: list[list[T]]) -> list[T]:
    """Flatten a 2-D matrix with a nested comprehension (concept #4).

    Args:
        matrix: Rectangular list of lists.

    Returns:
        Single list of cells in row-major order.

    Raises:
        ValueError: If ``matrix`` is not rectangular.

    Examples:
        >>> flatten_matrix([[1, 2], [3, 4]])
        [1, 2, 3, 4]
    """
    if matrix and any(len(r) != len(matrix[0]) for r in matrix):
        raise ValueError("flatten_matrix requires a rectangular matrix")
    return [cell for row in matrix for cell in row]


# ─── Section 2: Dict & set comprehensions (#5–#7) ───

def rekey_dict(d: dict[str, T], prefix: str) -> dict[str, T]:
    """Re-key a dict by prefixing each key (concept #5).

    Args:
        d: Source dict.
        prefix: Non-empty prefix string.

    Returns:
        New dict with prefixed keys; values unchanged.

    Raises:
        ValueError: If ``prefix`` is empty.

    Examples:
        >>> rekey_dict({"a": 1, "b": 2}, "x_")
        {'x_a': 1, 'x_b': 2}
    """
    if not prefix:
        raise ValueError(f"prefix must be non-empty, got {prefix!r}")
    return {f"{prefix}{k}": v for k, v in d.items()}


def drop_falsy_values(d: dict[K, Any]) -> dict[K, Any]:
    """Filter dict entries whose value is falsy (concept #6).

    Args:
        d: Source dict.

    Returns:
        New dict with only truthy-valued items.

    Examples:
        >>> drop_falsy_values({"a": 1, "b": 0, "c": "", "d": "ok"})
        {'a': 1, 'd': 'ok'}
    """
    return {k: v for k, v in d.items() if v}


def unique_lowercased(words: Iterable[str]) -> set[str]:
    """Return the distinct lowercased words (concept #7).

    Args:
        words: Iterable of strings.

    Returns:
        Set of unique lowercased non-empty words.

    Examples:
        >>> sorted(unique_lowercased(["Ada", "ADA", "Linus"]))
        ['ada', 'linus']
    """
    return {w.lower() for w in words if w}


# ─── Section 3: Generator expressions & memory (#8–#10) ───

def lazy_squares(nums: Iterable[int]) -> Iterator[int]:
    """Return a generator of squares (concept #8).

    Args:
        nums: Iterable of ints.

    Returns:
        Iterator producing ``n*n`` on demand (constant memory).

    Examples:
        >>> list(lazy_squares([1, 2, 3]))
        [1, 4, 9]
    """
    return (n * n for n in nums)


def sum_of_squares(nums: Iterable[int]) -> int:
    """Bare genexp passed straight into ``sum`` (concept #9).

    Args:
        nums: Iterable of ints.

    Returns:
        Sum of squares (0 on empty input).

    Examples:
        >>> sum_of_squares([1, 2, 3])
        14
    """
    return sum(n * n for n in nums)


def compare_memory(n: int) -> tuple[int, int]:
    """Compare list-vs-generator memory footprints (concept #10).

    Args:
        n: Stream length (>= 0).

    Returns:
        ``(list_bytes, generator_bytes)`` — the list is typically 100x+ larger.

    Raises:
        ValueError: If ``n < 0``.

    Examples:
        >>> lb, gb = compare_memory(1000)
        >>> lb > gb
        True
    """
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n!r}")
    list_bytes = sys.getsizeof([i for i in range(n)])
    gen_bytes = sys.getsizeof((i for i in range(n)))
    return list_bytes, gen_bytes


# ─── Section 4: yield, next, StopIteration, scoping (#11–#14) ───

def countdown(n: int) -> Iterator[int]:
    """Generator function counting down from ``n`` to 1 (concept #11).

    Args:
        n: Non-negative start.

    Yields:
        Successive ints from ``n`` down to 1.

    Raises:
        ValueError: If ``n < 0``.

    Examples:
        >>> list(countdown(3))
        [3, 2, 1]
    """
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n!r}")
    while n > 0:
        yield n
        n -= 1


def peek_first(it: Iterable[T], default: T | None = None) -> T | None:
    """Pull the first item with ``next`` (concepts #12, #13).

    Args:
        it: Any iterable.
        default: Returned when ``it`` is empty (StopIteration handled).

    Returns:
        First item, or ``default``.

    Examples:
        >>> peek_first(iter([10, 20]))
        10
        >>> peek_first(iter([]), default=-1)
        -1
    """
    iterator = iter(it)
    try:
        return next(iterator)
    except StopIteration:
        return default


def show_scoping() -> tuple[str, list[int]]:
    """Demonstrate Py3 comprehension scoping (concept #14).

    Returns:
        ``(outer_value, squares)`` — ``outer_value`` proves the comprehension's
        loop variable did not leak.

    Examples:
        >>> outer, squares = show_scoping()
        >>> outer, squares
        ('outer', [0, 1, 4])
    """
    x = "outer"
    squares = [i * i for i in range(3)]  # `i` is local to the comprehension
    return x, squares


# ─── Section 5: Walrus, itertools bridge (#15, #18) ───

def filter_with_walrus(items: Iterable[int], threshold: int) -> list[int]:
    """Filter using a costly predicate computed once via ``:=`` (concept #15).

    Args:
        items: Iterable of ints.
        threshold: Lower bound (exclusive).

    Returns:
        List of ``y`` values where ``y = item * item - 1 > threshold``.

    Examples:
        >>> filter_with_walrus(range(5), threshold=0)
        [3, 8, 15]
    """
    return [y for x in items if (y := x * x - 1) > threshold]


def take_first_n(it: Iterable[T], n: int) -> list[T]:
    """Bridge a comprehension to ``itertools.islice`` (concept #18).

    Args:
        it: Any iterable (incl. infinite generators).
        n: Non-negative count.

    Returns:
        First ``n`` items as a list.

    Raises:
        ValueError: If ``n < 0``.

    Examples:
        >>> take_first_n(range(100), 3)
        [0, 1, 2]
    """
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n!r}")
    return [x for x in islice(it, n)]


# ─── Section 6: Performance & industrial patterns (#17, #20, #21) ───

def benchmark_comprehension_vs_loop(n: int = 10_000, repeats: int = 200) -> dict[str, float]:
    """Time a comprehension against a manual ``for``/``append`` (concept #17).

    Args:
        n: Range size.
        repeats: Number of timing repetitions.

    Returns:
        Dict with ``loop_seconds``, ``comp_seconds``, ``speedup`` keys.

    Raises:
        ValueError: If ``n < 0`` or ``repeats <= 0``.

    Examples:
        >>> r = benchmark_comprehension_vs_loop(n=1000, repeats=50)
        >>> r["speedup"] > 0
        True
    """
    import timeit
    if n < 0 or repeats <= 0:
        raise ValueError(f"invalid args n={n!r} repeats={repeats!r}")
    setup = f"nums = list(range({n}))"
    loop_s = timeit.timeit(
        "out=[]\nfor x in nums: out.append(x*x)", setup=setup, number=repeats
    )
    comp_s = timeit.timeit("[x*x for x in nums]", setup=setup, number=repeats)
    speedup = loop_s / comp_s if comp_s > 0 else float("inf")
    return {"loop_seconds": loop_s, "comp_seconds": comp_s, "speedup": speedup}


def project_users(
    users: list[dict[str, Any]], fields: list[str]
) -> list[dict[str, Any]]:
    """Filtered projection — active users, selected fields (concept #20).

    Args:
        users: List of user dicts. Each must have a boolean ``active`` key.
        fields: Non-empty list of field names to keep.

    Returns:
        New list of dicts containing only ``fields`` for active users.

    Raises:
        ValueError: If ``fields`` is empty or any user lacks ``active``.

    Examples:
        >>> project_users(
        ...     [{"id": 1, "name": "Ada", "active": True},
        ...      {"id": 2, "name": "Bob", "active": False}],
        ...     fields=["id", "name"],
        ... )
        [{'id': 1, 'name': 'Ada'}]
    """
    if not fields:
        raise ValueError("fields must be non-empty")
    if any("active" not in u for u in users):
        raise ValueError("every user must have an 'active' key")
    return [{f: u.get(f) for f in fields} for u in users if u["active"]]


def index_by(records: list[dict[str, Any]], key_field: str) -> dict[Any, dict[str, Any]]:
    """Build an O(1) lookup dict from a list of records (concept #21).

    Args:
        records: List of dicts; each must contain ``key_field``.
        key_field: Name of the unique key.

    Returns:
        ``{record[key_field]: record}``. Later records overwrite earlier ones.

    Raises:
        ValueError: If any record is missing ``key_field``.

    Examples:
        >>> index_by([{"id": 1, "v": "a"}, {"id": 2, "v": "b"}], "id")
        {1: {'id': 1, 'v': 'a'}, 2: {'id': 2, 'v': 'b'}}
    """
    if any(key_field not in r for r in records):
        raise ValueError(f"every record must contain {key_field!r}")
    return {r[key_field]: r for r in records}


# ─── Self-checks (runnable demos) ───

if __name__ == "__main__":
    print(square_all([1, 2, 3]))
    # Expected output: [1, 4, 9]

    print(keep_positive([-2, 0, 3, 5]))
    # Expected output: [3, 5]

    print(clamp_signs([-3, -1, 0, 2]))
    # Expected output: [3, 1, 0, 2]

    print(flatten_matrix([[1, 2], [3, 4]]))
    # Expected output: [1, 2, 3, 4]

    print(rekey_dict({"a": 1, "b": 2}, "x_"))
    # Expected output: {'x_a': 1, 'x_b': 2}

    print(drop_falsy_values({"a": 1, "b": 0, "c": "", "d": "ok"}))
    # Expected output: {'a': 1, 'd': 'ok'}

    print(sorted(unique_lowercased(["Ada", "ADA", "Linus"])))
    # Expected output: ['ada', 'linus']

    print(list(lazy_squares([1, 2, 3])))
    # Expected output: [1, 4, 9]

    print(sum_of_squares(range(5)))
    # Expected output: 30

    list_bytes, gen_bytes = compare_memory(1000)
    print(list_bytes > gen_bytes)
    # Expected output: True

    print(list(countdown(3)))
    # Expected output: [3, 2, 1]

    print(peek_first(iter([10, 20])), peek_first(iter([]), default=-1))
    # Expected output: 10 -1

    print(show_scoping())
    # Expected output: ('outer', [0, 1, 4])

    print(filter_with_walrus(range(5), threshold=0))
    # Expected output: [3, 8, 15]

    print(take_first_n(range(100), 3))
    # Expected output: [0, 1, 2]

    bench = benchmark_comprehension_vs_loop(n=1000, repeats=50)
    print("comp faster?", bench["speedup"] >= 1.0)
    # Expected output: comp faster? True

    print(project_users(
        [{"id": 1, "name": "Ada", "active": True},
         {"id": 2, "name": "Bob", "active": False}],
        fields=["id", "name"],
    ))
    # Expected output: [{'id': 1, 'name': 'Ada'}]

    print(index_by([{"id": 1, "v": "a"}, {"id": 2, "v": "b"}], "id"))
    # Expected output: {1: {'id': 1, 'v': 'a'}, 2: {'id': 2, 'v': 'b'}}
