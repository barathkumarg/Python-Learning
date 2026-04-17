"""Exercise 02: Leaderboard sort with tie-breakers.

Problem:
    Implement
    `sort_leaderboard(entries: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]`.
    Tuple format is `(name, score, penalty_minutes)`.

Constraints:
    - Sort by score (descending), penalty_minutes (ascending), then name (ascending, case-insensitive).
    - Validate non-empty names.
    - Validate score range 0..100.
    - Validate penalty_minutes >= 0.
    - Return a new list, do not mutate `entries`.

Examples:
    sort_leaderboard([("Maya", 91, 4), ("Arun", 91, 2), ("Lina", 88, 1)])
    -> [("Arun", 91, 2), ("Maya", 91, 4), ("Lina", 88, 1)]

    sort_leaderboard([("", 70, 1)]) -> ValueError
"""

from __future__ import annotations


LeaderboardEntry = tuple[str, int, int]


def sort_leaderboard(entries: list[LeaderboardEntry]) -> list[LeaderboardEntry]:
    """Return leaderboard rows sorted by score and tie-breakers.

    Args:
        entries: List of `(name, score, penalty_minutes)` tuples.

    Returns:
        A newly sorted leaderboard list.

    Raises:
        ValueError: If entry data is invalid.
    """
    normalized: list[LeaderboardEntry] = []
    for name, score, penalty_minutes in entries:
        cleaned_name = name.strip()
        if not cleaned_name:
            raise ValueError(f"name must not be empty, got name={name!r}")
        if score < 0 or score > 100:
            raise ValueError(f"score must be in 0..100, got score={score}")
        if penalty_minutes < 0:
            raise ValueError(
                f"penalty_minutes must be >= 0, got penalty_minutes={penalty_minutes}"
            )
        normalized.append((cleaned_name, score, penalty_minutes))

    by_name = sorted(normalized, key=lambda row: row[0].lower())
    by_penalty = sorted(by_name, key=lambda row: row[2])
    return sorted(by_penalty, key=lambda row: row[1], reverse=True)


if __name__ == "__main__":
    sample = [("Maya", 91, 4), ("Arun", 91, 2), ("Lina", 88, 1)]

    # Expected output: [('Arun', 91, 2), ('Maya', 91, 4), ('Lina', 88, 1)]
    assert sort_leaderboard(sample) == [
        ("Arun", 91, 2),
        ("Maya", 91, 4),
        ("Lina", 88, 1),
    ]
    # Expected output: original sample list unchanged
    assert sample == [("Maya", 91, 4), ("Arun", 91, 2), ("Lina", 88, 1)]
    try:
        sort_leaderboard([("", 70, 1)])
        raise AssertionError("should have raised ValueError for blank name")
    except ValueError:
        pass
    print("ex02_intermediate: all asserts passed")
