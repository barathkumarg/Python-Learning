# code.py — Day 07: Sets and frozenset

"""
Sets and frozenset — production-style reference implementations.

Covers: literal/constructor creation, add/remove/discard/update mutation,
union/intersection/difference/symmetric-difference algebra, subset/superset/
disjoint checks, membership, iteration, set comprehension, frozenset,
frozenset-as-dict-key, hashability rules, built-in aggregation, and two
industrial patterns (log dedup, RBAC permission comparison).

Style: typed signatures, Google docstrings, explicit validation, inline asserts.
"""

from __future__ import annotations


# ─── Section 1: Creation ───

def demo_creation() -> dict[str, object]:
    """Demonstrate set creation via literal, constructor, and empty set.

    Returns:
        Dict with keys 'literal', 'from_list', 'empty' holding example sets.

    Examples:
        >>> result = demo_creation()
        >>> result["from_list"] == {1, 2, 3}
        True
    """
    literal: set[str] = {"python", "backend", "api"}
    from_list: set[int] = set([1, 2, 2, 3, 3, 3])
    empty: set[object] = set()  # NOT {} — that's a dict
    return {"literal": literal, "from_list": from_list, "empty": empty}


# ─── Section 2: Mutation ───

def demo_mutation(initial: set[int] | None = None) -> set[int]:
    """Demonstrate add, remove, discard, update, and |= on a set.

    Args:
        initial: Starting set. Defaults to {1, 2, 3} if None.

    Returns:
        The mutated set after all operations.

    Raises:
        TypeError: If *initial* is provided but is not a set.

    Examples:
        >>> demo_mutation({1, 2, 3})
        {1, 3, 4, 5, 6, 7}
    """
    if initial is not None and not isinstance(initial, set):
        raise TypeError(f"expected set or None, got {type(initial).__name__}")

    s = set(initial) if initial is not None else {1, 2, 3}
    s.add(4)           # {1, 2, 3, 4}
    s.discard(99)      # no-op — silent
    s.remove(2)        # removes 2
    s.update([5, 6])   # bulk add
    s |= {7}           # operator form of update
    return s


# ─── Section 3: Set Algebra ───

def compare_permissions(
    required: set[str],
    granted: set[str],
) -> dict[str, object]:
    """Compare required vs granted permission sets using set algebra.

    Args:
        required: Permissions the action needs.
        granted: Permissions the user has.

    Returns:
        Dict with keys: 'is_authorized' (bool), 'missing' (set),
        'extra' (set), 'shared' (set), 'all_perms' (set),
        'symmetric_diff' (set), 'is_disjoint' (bool).

    Raises:
        TypeError: If either argument is not a set.
        ValueError: If *required* is empty.

    Examples:
        >>> result = compare_permissions({"read", "write"}, {"read", "write", "admin"})
        >>> result["is_authorized"]
        True
        >>> result["missing"]
        set()
    """
    if not isinstance(required, set) or not isinstance(granted, set):
        raise TypeError(
            f"expected set arguments, got {type(required).__name__} "
            f"and {type(granted).__name__}"
        )
    if not required:
        raise ValueError("required permissions must not be empty")

    return {
        "is_authorized": required <= granted,       # subset check
        "missing": required - granted,              # difference
        "extra": granted - required,                # reverse difference
        "shared": required & granted,               # intersection
        "all_perms": required | granted,            # union
        "symmetric_diff": required ^ granted,       # symmetric difference
        "is_disjoint": required.isdisjoint(granted),  # no overlap?
    }


# ─── Section 4: Iteration and Comprehension ───

def demo_iteration(s: set[int]) -> list[int]:
    """Return sorted list from a set to demonstrate deterministic iteration.

    Args:
        s: Input set of integers.

    Returns:
        Sorted list of the set's elements.

    Raises:
        TypeError: If *s* is not a set.

    Examples:
        >>> demo_iteration({3, 1, 2})
        [1, 2, 3]
    """
    if not isinstance(s, set):
        raise TypeError(f"expected set, got {type(s).__name__}")
    return sorted(s)


def demo_comprehension(words: list[str]) -> set[str]:
    """Return a set of unique lowercased words via set comprehension.

    Args:
        words: List of strings to normalize and deduplicate.

    Returns:
        Set of lowercased unique words.

    Raises:
        TypeError: If *words* is not a list.

    Examples:
        >>> demo_comprehension(["Hello", "hello", "WORLD"])
        {'hello', 'world'}
    """
    if not isinstance(words, list):
        raise TypeError(f"expected list, got {type(words).__name__}")
    return {w.lower() for w in words}


# ─── Section 5: Aggregation ───

def demo_aggregation(s: set[int | float]) -> dict[str, int | float]:
    """Demonstrate built-in aggregation functions on a set.

    Args:
        s: Non-empty set of numbers.

    Returns:
        Dict with keys 'count', 'min', 'max', 'sum'.

    Raises:
        TypeError: If *s* is not a set.
        ValueError: If *s* is empty.

    Examples:
        >>> demo_aggregation({75, 88, 92, 100})
        {'count': 4, 'min': 75, 'max': 100, 'sum': 355}
    """
    if not isinstance(s, set):
        raise TypeError(f"expected set, got {type(s).__name__}")
    if not s:
        raise ValueError("set must not be empty for aggregation")
    return {"count": len(s), "min": min(s), "max": max(s), "sum": sum(s)}


# ─── Section 6: frozenset ───

def demo_frozenset() -> dict[str, object]:
    """Demonstrate frozenset creation, equality, hashing, and use as dict key.

    Returns:
        Dict with keys 'equal' (bool), 'same_hash' (bool),
        'lookup_result' (str), 'nested' (set of frozensets).

    Examples:
        >>> result = demo_frozenset()
        >>> result["equal"]
        True
    """
    pair_a = frozenset({"read", "write"})
    pair_b = frozenset({"write", "read"})  # same contents, order irrelevant

    # frozenset as dict key
    combo_map: dict[frozenset[str], str] = {pair_a: "standard"}

    # frozenset nested in a set (set of sets)
    nested: set[frozenset[int]] = {frozenset({1, 2}), frozenset({3, 4})}

    return {
        "equal": pair_a == pair_b,
        "same_hash": hash(pair_a) == hash(pair_b),
        "lookup_result": combo_map[pair_b],
        "nested": nested,
    }


# ─── Industrial Patterns ───

def dedupe_logs(logs: list[str]) -> list[str]:
    """Deduplicate log lines while preserving first-occurrence order.

    Uses a seen-set for O(1) membership checks, giving O(n) total time
    instead of O(n²) with a list-based check.

    Args:
        logs: List of log-line strings (may contain duplicates).

    Returns:
        List of unique log lines in first-seen order.

    Raises:
        TypeError: If *logs* is not a list.

    Examples:
        >>> dedupe_logs(["a", "b", "a", "c", "b"])
        ['a', 'b', 'c']
    """
    if not isinstance(logs, list):
        raise TypeError(f"expected list, got {type(logs).__name__}")

    seen: set[str] = set()
    unique: list[str] = []
    for line in logs:
        if line not in seen:
            seen.add(line)
            unique.append(line)
    return unique


def filter_by_allowlist(
    items: list[str],
    allowed: set[str],
) -> list[str]:
    """Filter items keeping only those in the allow-set.

    Args:
        items: Items to filter.
        allowed: Set of permitted values.

    Returns:
        Filtered list preserving original order.

    Raises:
        TypeError: If *allowed* is not a set.

    Examples:
        >>> filter_by_allowlist(["png", "exe", "jpg", "bat"], {"png", "jpg", "webp"})
        ['png', 'jpg']
    """
    if not isinstance(allowed, set):
        raise TypeError(f"expected set for allowed, got {type(allowed).__name__}")
    return [item for item in items if item in allowed]


# ─── Self-checks ───

if __name__ == "__main__":
    # --- demo_creation ---
    cr = demo_creation()
    assert cr["from_list"] == {1, 2, 3}, f"got {cr['from_list']}"
    assert cr["empty"] == set()
    assert isinstance(cr["literal"], set)
    # Expected output: from_list={1, 2, 3}
    print(f"creation: from_list={cr['from_list']}")

    # --- demo_mutation ---
    mutated = demo_mutation({1, 2, 3})
    assert mutated == {1, 3, 4, 5, 6, 7}, f"got {mutated}"
    # Expected output: mutated={1, 3, 4, 5, 6, 7}
    print(f"mutation: {sorted(mutated)}")

    # --- compare_permissions ---
    perms = compare_permissions({"read", "write"}, {"read", "write", "admin"})
    assert perms["is_authorized"] is True
    assert perms["missing"] == set()
    assert perms["extra"] == {"admin"}
    assert perms["shared"] == {"read", "write"}
    # Expected output: authorized=True, missing=set()
    print(f"permissions: authorized={perms['is_authorized']}, missing={perms['missing']}")

    denied = compare_permissions({"read", "write", "delete"}, {"read"})
    assert denied["is_authorized"] is False
    assert denied["missing"] == {"write", "delete"}

    # --- demo_iteration ---
    assert demo_iteration({3, 1, 2}) == [1, 2, 3]

    # --- demo_comprehension ---
    comp = demo_comprehension(["Hello", "hello", "WORLD", "world"])
    assert comp == {"hello", "world"}, f"got {comp}"
    # Expected output: {'hello', 'world'}
    print(f"comprehension: {sorted(comp)}")

    # --- demo_aggregation ---
    agg = demo_aggregation({75, 88, 92, 100})
    assert agg == {"count": 4, "min": 75, "max": 100, "sum": 355}
    # Expected output: count=4, min=75, max=100, sum=355
    print(f"aggregation: {agg}")

    # --- demo_frozenset ---
    fs = demo_frozenset()
    assert fs["equal"] is True
    assert fs["same_hash"] is True
    assert fs["lookup_result"] == "standard"
    # Expected output: equal=True, lookup=standard
    print(f"frozenset: equal={fs['equal']}, lookup={fs['lookup_result']}")

    # --- dedupe_logs ---
    deduped = dedupe_logs(["a", "b", "a", "c", "b"])
    assert deduped == ["a", "b", "c"], f"got {deduped}"
    assert dedupe_logs([]) == []
    # Expected output: ['a', 'b', 'c']
    print(f"dedupe: {deduped}")

    # --- filter_by_allowlist ---
    filtered = filter_by_allowlist(["png", "exe", "jpg", "bat"], {"png", "jpg", "webp"})
    assert filtered == ["png", "jpg"], f"got {filtered}"
    # Expected output: ['png', 'jpg']
    print(f"allowlist: {filtered}")

    # --- TypeError checks ---
    try:
        demo_mutation("bad")  # type: ignore[arg-type]
        raise AssertionError("should have raised TypeError")
    except TypeError:
        pass

    try:
        demo_iteration([1, 2])  # type: ignore[arg-type]
        raise AssertionError("should have raised TypeError")
    except TypeError:
        pass

    try:
        dedupe_logs("not a list")  # type: ignore[arg-type]
        raise AssertionError("should have raised TypeError")
    except TypeError:
        pass

    print("code.py: all asserts passed ✓")
