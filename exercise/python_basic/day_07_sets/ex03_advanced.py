"""Exercise 03: Comprehensions, frozenset, and industrial patterns.

Covers checklist items: #15–#22.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex03_advanced.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations


def normalize_tags(tags: list[str]) -> set[str]:
    """Normalize tags to lowercase, stripped, unique values via set comprehension.

    Args:
        tags: List of tag strings (may have duplicates, mixed case, whitespace).

    Returns:
        Set of cleaned, lowercased, unique tags.

    Raises:
        TypeError: If *tags* is not a list.

    Examples:
        >>> normalize_tags(["Python", " python ", "API", "api"])
        {'python', 'api'}
    """
    if not isinstance(tags, list):
        raise TypeError(f"expected list, got {type(tags).__name__}")
    return {t.lower().strip() for t in tags}


def make_hashable(items: list[object]) -> tuple[object, ...]:
    """Convert a list to a tuple so it can be used in a set or as a dict key.

    Args:
        items: List to convert.

    Returns:
        Tuple containing the same elements.

    Raises:
        TypeError: If *items* is not a list.

    Examples:
        >>> make_hashable([1, 2, 3])
        (1, 2, 3)
    """
    if not isinstance(items, list):
        raise TypeError(f"expected list, got {type(items).__name__}")
    return tuple(items)


def group_by_letter_set(words: list[str]) -> list[list[str]]:
    """Group words that share the same set of unique characters.

    Uses frozenset of characters as a dict key to group words.
    Each group is sorted alphabetically. The outer list is sorted
    by (group length, first word).

    Args:
        words: List of lowercase words.

    Returns:
        Sorted list of sorted groups.

    Raises:
        TypeError: If *words* is not a list.

    Examples:
        >>> group_by_letter_set(["ab", "ba", "abc", "bca", "xy"])
        [['xy'], ['ab', 'ba'], ['abc', 'bca']]
    """
    if not isinstance(words, list):
        raise TypeError(f"expected list, got {type(words).__name__}")
    groups: dict[frozenset[str], list[str]] = {}
    for word in words:
        key = frozenset(word)
        groups.setdefault(key, []).append(word)
    sorted_groups = [sorted(g) for g in groups.values()]
    return sorted(sorted_groups, key=lambda g: (len(g), g[0]))


def dedupe_preserve_order(items: list[str]) -> list[str]:
    """Deduplicate a list while preserving first-occurrence order.

    Uses a seen-set for O(1) membership checks.

    Args:
        items: List of strings (may have duplicates).

    Returns:
        List of unique strings in first-seen order.

    Raises:
        TypeError: If *items* is not a list.

    Examples:
        >>> dedupe_preserve_order(["a", "b", "a", "c", "b"])
        ['a', 'b', 'c']
    """
    if not isinstance(items, list):
        raise TypeError(f"expected list, got {type(items).__name__}")
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def permission_report(
    required: set[str], granted: set[str],
) -> dict[str, object]:
    """Compare required vs granted permissions (RBAC pattern).

    Args:
        required: Permissions the action needs.
        granted: Permissions the user has.

    Returns:
        Dict with keys:
        - 'authorized' (bool): True if required is a subset of granted.
        - 'missing' (set[str]): Permissions in required but not granted.
        - 'extra' (set[str]): Permissions in granted but not required.
        - 'shared' (set[str]): Permissions in both (stretch).
        - 'all_perms' (set[str]): Union of both (stretch).

    Raises:
        TypeError: If either argument is not a set.
        ValueError: If *required* is empty.

    Examples:
        >>> r = permission_report({"read", "write"}, {"read", "write", "admin"})
        >>> r["authorized"]
        True
        >>> r["missing"]
        set()
    """
    if not isinstance(required, set) or not isinstance(granted, set):
        raise TypeError("both arguments must be sets")
    if not required:
        raise ValueError("required permissions must not be empty")
    return {
        "authorized": required <= granted,
        "missing": required - granted,
        "extra": granted - required,
        "shared": required & granted,
        "all_perms": required | granted,
    }


if __name__ == "__main__":
    try:
        # ─── normalize_tags ───
        assert normalize_tags(["Python", " python ", "API", "api"]) == {
            "python", "api",
        }
        assert normalize_tags([]) == set()
        assert normalize_tags(["  HELLO  "]) == {"hello"}
        try:
            normalize_tags("bad")  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # ─── make_hashable ───
        assert make_hashable([1, 2, 3]) == (1, 2, 3)
        assert make_hashable([]) == ()
        # Verify the result is actually hashable
        h = make_hashable([1, 2])
        test_set: set[tuple[object, ...]] = {h}
        assert h in test_set
        try:
            make_hashable("bad")  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # ─── group_by_letter_set ───
        groups = group_by_letter_set(["ab", "ba", "abc", "bca", "xy"])
        assert groups == [["xy"], ["ab", "ba"], ["abc", "bca"]], f"got {groups}"
        assert group_by_letter_set([]) == []
        assert group_by_letter_set(["hello"]) == [["hello"]]
        try:
            group_by_letter_set("bad")  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # ─── dedupe_preserve_order ───
        assert dedupe_preserve_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
        assert dedupe_preserve_order([]) == []
        assert dedupe_preserve_order(["x"]) == ["x"]
        assert dedupe_preserve_order(["a", "a", "a"]) == ["a"]
        try:
            dedupe_preserve_order("bad")  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # ─── permission_report ───
        r = permission_report({"read", "write"}, {"read", "write", "admin"})
        assert r["authorized"] is True
        assert r["missing"] == set()
        assert r["extra"] == {"admin"}
        assert r["shared"] == {"read", "write"}
        assert r["all_perms"] == {"read", "write", "admin"}

        denied = permission_report({"read", "write", "delete"}, {"read"})
        assert denied["authorized"] is False
        assert denied["missing"] == {"write", "delete"}

        try:
            permission_report(set(), {"read"})
            raise AssertionError("should have raised ValueError")
        except ValueError:
            pass
        try:
            permission_report("bad", {"ok"})  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        print("ex03_advanced: all asserts passed ✓")
    except NotImplementedError:
        print("ex03_advanced: implement all functions to run self-checks.")
