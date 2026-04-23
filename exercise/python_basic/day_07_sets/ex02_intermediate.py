"""Exercise 02: Set algebra and containment checks.

Covers checklist items: #6–#12.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex02_intermediate.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations


def combine_teams(team_a: set[str], team_b: set[str]) -> set[str]:
    """Return the union of two teams (all members from both).

    Args:
        team_a: First team's member set.
        team_b: Second team's member set.

    Returns:
        Set of all members from both teams.

    Raises:
        TypeError: If either argument is not a set.

    Examples:
        >>> combine_teams({"alice", "bob"}, {"bob", "carol"})
        {'alice', 'bob', 'carol'}
    """
    if not isinstance(team_a, set) or not isinstance(team_b, set):
        raise TypeError("both arguments must be sets")
    return team_a | team_b


def find_common_members(
    group_a: set[str], group_b: set[str],
) -> set[str]:
    """Return members present in both groups (intersection).

    Args:
        group_a: First group.
        group_b: Second group.

    Returns:
        Set of shared members.

    Raises:
        TypeError: If either argument is not a set.

    Examples:
        >>> find_common_members({"alice", "bob", "carol"}, {"bob", "carol", "dave"})
        {'bob', 'carol'}
    """
    if not isinstance(group_a, set) or not isinstance(group_b, set):
        raise TypeError("both arguments must be sets")
    return group_a & group_b


def find_exclusive(
    primary: set[str], secondary: set[str],
) -> set[str]:
    """Return elements in primary but not in secondary (difference).

    Args:
        primary: Set to check from.
        secondary: Set to exclude.

    Returns:
        Elements exclusive to primary.

    Raises:
        TypeError: If either argument is not a set.

    Examples:
        >>> find_exclusive({"alice", "bob", "carol"}, {"bob", "dave"})
        {'alice', 'carol'}
    """
    if not isinstance(primary, set) or not isinstance(secondary, set):
        raise TypeError("both arguments must be sets")
    return primary - secondary


def find_all_differences(
    set_a: set[str], set_b: set[str],
) -> set[str]:
    """Return elements in either set but not both (symmetric difference).

    Args:
        set_a: First set.
        set_b: Second set.

    Returns:
        Symmetric difference of the two sets.

    Raises:
        TypeError: If either argument is not a set.

    Examples:
        >>> find_all_differences({"alice", "bob"}, {"bob", "carol"})
        {'alice', 'carol'}
    """
    if not isinstance(set_a, set) or not isinstance(set_b, set):
        raise TypeError("both arguments must be sets")
    return set_a ^ set_b


def check_containment(
    subset_candidate: set[str],
    superset_candidate: set[str],
) -> dict[str, bool]:
    """Check subset, superset, and disjoint relationships.

    Args:
        subset_candidate: Set to test as potential subset.
        superset_candidate: Set to test as potential superset.

    Returns:
        Dict with keys 'is_subset', 'is_superset', 'is_disjoint'.

    Raises:
        TypeError: If either argument is not a set.

    Examples:
        >>> check_containment({"read"}, {"read", "write"})
        {'is_subset': True, 'is_superset': False, 'is_disjoint': False}
    """
    if not isinstance(subset_candidate, set) or not isinstance(superset_candidate, set):
        raise TypeError("both arguments must be sets")
    return {
        "is_subset": subset_candidate <= superset_candidate,
        "is_superset": subset_candidate >= superset_candidate,
        "is_disjoint": subset_candidate.isdisjoint(superset_candidate),
    }


def merge_tag_sets(*tag_sets: set[str]) -> set[str]:
    """Merge multiple tag sets into one using update.

    Args:
        *tag_sets: Variable number of string sets.

    Returns:
        A single set containing all tags from all inputs.

    Raises:
        TypeError: If any argument is not a set.

    Examples:
        >>> merge_tag_sets({"python", "api"}, {"api", "docker"}, {"ci"})
        {'python', 'api', 'docker', 'ci'}
    """
    for ts in tag_sets:
        if not isinstance(ts, set):
            raise TypeError(f"expected set, got {type(ts).__name__}")
    result: set[str] = set()
    for ts in tag_sets:
        result |= ts
    return result


if __name__ == "__main__":
    try:
        # ─── combine_teams ───
        assert combine_teams({"alice", "bob"}, {"bob", "carol"}) == {
            "alice", "bob", "carol",
        }
        assert combine_teams(set(), {"x"}) == {"x"}
        assert combine_teams(set(), set()) == set()

        # ─── find_common_members ───
        assert find_common_members(
            {"alice", "bob", "carol"}, {"bob", "carol", "dave"},
        ) == {"bob", "carol"}
        assert find_common_members({"a"}, {"b"}) == set()

        # ─── find_exclusive ───
        assert find_exclusive({"alice", "bob", "carol"}, {"bob", "dave"}) == {
            "alice", "carol",
        }
        assert find_exclusive({"a"}, {"a"}) == set()

        # ─── find_all_differences ───
        assert find_all_differences({"alice", "bob"}, {"bob", "carol"}) == {
            "alice", "carol",
        }
        assert find_all_differences({"a"}, {"a"}) == set()

        # ─── check_containment ───
        result = check_containment({"read"}, {"read", "write"})
        assert result == {
            "is_subset": True,
            "is_superset": False,
            "is_disjoint": False,
        }
        disjoint = check_containment({"x"}, {"y"})
        assert disjoint["is_disjoint"] is True
        assert disjoint["is_subset"] is False
        equal = check_containment({"a", "b"}, {"a", "b"})
        assert equal["is_subset"] is True
        assert equal["is_superset"] is True

        # ─── merge_tag_sets ───
        merged = merge_tag_sets({"python", "api"}, {"api", "docker"}, {"ci"})
        assert merged == {"python", "api", "docker", "ci"}
        assert merge_tag_sets() == set()
        assert merge_tag_sets({"solo"}) == {"solo"}

        # TypeError checks
        try:
            combine_teams("bad", {"ok"})  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        try:
            merge_tag_sets({"ok"}, [1, 2])  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        print("ex02_intermediate: all asserts passed ✓")
    except NotImplementedError:
        print("ex02_intermediate: implement all functions to run self-checks.")
