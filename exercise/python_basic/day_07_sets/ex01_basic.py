"""Exercise 01: Set creation, mutation, and basics.

Covers checklist items: #1–#5, #13–#14, #19.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex01_basic.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations


def create_set_from_values(*values: object) -> set[object]:
    """Create a set from variable positional arguments.

    Args:
        *values: Zero or more values to include in the set.

    Returns:
        A set containing the unique values.

    Examples:
        >>> create_set_from_values(1, 2, 2, 3)
        {1, 2, 3}
        >>> create_set_from_values()
        set()
    """
    # TODO: Build and return a set from *values
    # Sample input: create_set_from_values(1, 2, 2, 3)
    # Expected output: {1, 2, 3}
    # if not values:
    #     return set()
    # else:
    #     result = set(list(*values))
    #     print(result)
    return set(values)


def unique_from_list(items: list[object]) -> list[object]:
    """Deduplicate a list and return sorted unique values.

    Args:
        items: List of comparable items (may contain duplicates).

    Returns:
        Sorted list of unique items.

    Raises:
        TypeError: If *items* is not a list.

    Examples:
        >>> unique_from_list([3, 1, 2, 1, 3])
        [1, 2, 3]
    """
    # TODO: Validate items is a list
    # TODO: Convert to set to deduplicate
    # TODO: Return sorted list
    # Sample input: [3, 1, 2, 1, 3]
    # Expected output: [1, 2, 3]
    if not isinstance(items,list):
        raise TypeError("Not a list")
    
    return sorted(set(items))


def build_seen_tracker(items: list[int]) -> set[int]:
    """Return the set of values that appear more than once.

    Uses `in` membership check on a seen-set to detect duplicates.

    Args:
        items: List of integers (may have duplicates).

    Returns:
        Set of duplicate values.

    Raises:
        TypeError: If *items* is not a list.

    Examples:
        >>> build_seen_tracker([1, 2, 3, 2, 4, 3])
        {2, 3}
        >>> build_seen_tracker([1, 2, 3])
        set()
    """
    # TODO: Validate items is a list
    # TODO: Iterate items, track seen values in a set
    # TODO: If item already in seen, add to duplicates set
    # TODO: Return duplicates
    if not isinstance(items, list):
        raise TypeError("No a list")
    seen : set[int] = set()
    duplicate : set[int] = set()
    for item in items:
        if item in seen:
            duplicate.add(item)
        else:
            seen.add(item)
    return duplicate


def safe_remove(
    s: set[object], elem: object, *, strict: bool = False,
) -> set[object]:
    """Remove an element from a copy of the set.

    Args:
        s: Input set (not mutated).
        elem: Element to remove.
        strict: If True, use remove() (raises KeyError if missing).
                If False, use discard() (silent if missing).

    Returns:
        New set with the element removed (if present).

    Raises:
        TypeError: If *s* is not a set.
        KeyError: If *strict* is True and *elem* is not in the set.

    Examples:
        >>> safe_remove({1, 2, 3}, 2)
        {1, 3}
        >>> safe_remove({1, 2, 3}, 99)
        {1, 2, 3}
    """
    if not isinstance(s, set):
        raise TypeError(f"expected set, got {type(s).__name__}")
    copy = set(s)
    if strict:
        copy.remove(elem)
    else:
        copy.discard(elem)
    return copy


def drain_set(s: set[int]) -> list[int]:
    """Pop all elements from a copy of the set, return them sorted.

    Args:
        s: Input set of integers (not mutated).

    Returns:
        Sorted list of all elements.

    Raises:
        TypeError: If *s* is not a set.

    Examples:
        >>> drain_set({3, 1, 2})
        [1, 2, 3]
    """
    if not isinstance(s, set):
        raise TypeError(f"expected set, got {type(s).__name__}")
    copy = set(s)
    result: list[int] = []
    while copy:
        result.append(copy.pop())
    return sorted(result)


def set_stats(s: set[int | float]) -> dict[str, int | float]:
    """Return count, min, max, sum for a numeric set.

    Args:
        s: Non-empty set of numbers.

    Returns:
        Dict with keys 'count', 'min', 'max', 'sum'.

    Raises:
        TypeError: If *s* is not a set.
        ValueError: If *s* is empty.

    Examples:
        >>> set_stats({10, 20, 30})
        {'count': 3, 'min': 10, 'max': 30, 'sum': 60}
    """
    if not isinstance(s, set):
        raise TypeError(f"expected set, got {type(s).__name__}")
    if not s:
        raise ValueError("set must not be empty")
    return {"count": len(s), "min": min(s), "max": max(s), "sum": sum(s)}


if __name__ == "__main__":
    try:
        # ─── create_set_from_values ───
        assert create_set_from_values(1, 2, 2, 3) == {1, 2, 3}
        assert create_set_from_values() == set()
        assert create_set_from_values("a", "a") == {"a"}

        # ─── unique_from_list ───
        assert unique_from_list([3, 1, 2, 1, 3]) == [1, 2, 3]
        assert unique_from_list([]) == []
        assert unique_from_list([5]) == [5]
        try:
            unique_from_list("not a list")  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # ─── build_seen_tracker ───
        assert build_seen_tracker([1, 2, 3, 2, 4, 3]) == {2, 3}
        assert build_seen_tracker([1, 2, 3]) == set()
        assert build_seen_tracker([]) == set()
        try:
            build_seen_tracker("bad")  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # ─── safe_remove ───
        assert safe_remove({1, 2, 3}, 2) == {1, 3}
        assert safe_remove({1, 2, 3}, 99) == {1, 2, 3}  # discard — silent
        try:
            safe_remove({1, 2, 3}, 99, strict=True)
            raise AssertionError("should have raised KeyError")
        except KeyError:
            pass
        original = {1, 2, 3}
        safe_remove(original, 2)
        assert original == {1, 2, 3}, "original must not be mutated"

        # ─── drain_set ───
        assert drain_set({3, 1, 2}) == [1, 2, 3]
        assert drain_set(set()) == []
        original_drain = {10, 20}
        drain_set(original_drain)
        assert original_drain == {10, 20}, "original must not be mutated"

        # ─── set_stats ───
        assert set_stats({10, 20, 30}) == {"count": 3, "min": 10, "max": 30, "sum": 60}
        assert set_stats({42}) == {"count": 1, "min": 42, "max": 42, "sum": 42}
        try:
            set_stats(set())
            raise AssertionError("should have raised ValueError")
        except ValueError:
            pass
        try:
            set_stats([1, 2])  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        print("ex01_basic: all asserts passed ✓")
    except NotImplementedError:
        print("ex01_basic: implement all functions to run self-checks.")
