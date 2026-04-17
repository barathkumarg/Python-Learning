"""Exercise 03: Filtered top-k leaderboard view.

Problem:
    Implement
    `top_k_by_min_score(entries: list[tuple[str, int, int]], *, min_score: int, k: int)
    -> list[tuple[str, int, int]]`.

Constraints:
    - Keep only rows where score >= min_score.
    - Sort rows by score descending, penalty_minutes ascending, then name ascending.
    - Return at most top `k` rows.
    - Validate `min_score` in 0..100 and `k >= 1`.

Examples:
    top_k_by_min_score(
        [("Maya", 91, 4), ("Arun", 91, 2), ("Lina", 88, 1), ("Ira", 95, 5)],
        min_score=90,
        k=2,
    ) -> [("Ira", 95, 5), ("Arun", 91, 2)]

    top_k_by_min_score([("Maya", 91, 4)], min_score=101, k=1) -> ValueError
"""

from __future__ import annotations


LeaderboardEntry = tuple[str, int, int]


def top_k_by_min_score(
    entries: list[LeaderboardEntry],
    *,
    min_score: int,
    k: int,
) -> list[LeaderboardEntry]:
    """Return a filtered and ranked top-k leaderboard slice.

    Args:
        entries: List of `(name, score, penalty_minutes)` tuples.
        min_score: Minimum allowed score for inclusion.
        k: Maximum number of results to return.

    Returns:
        Top-ranked rows after filtering.

    Raises:
        ValueError: If `min_score` or `k` is out of range.
    """
    if min_score < 0 or min_score > 100:
        raise ValueError(f"min_score must be in 0..100, got min_score={min_score}")
    if k < 1:
        raise ValueError(f"k must be >= 1, got k={k}")

    filtered: list[LeaderboardEntry] = []
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
        if score >= min_score:
            filtered.append((cleaned_name, score, penalty_minutes))

    by_name = sorted(filtered, key=lambda row: row[0].lower())
    by_penalty = sorted(by_name, key=lambda row: row[2])
    ranked = sorted(by_penalty, key=lambda row: row[1], reverse=True)
    return ranked[:k]


if __name__ == "__main__":
    data = [("Maya", 91, 4), ("Arun", 91, 2), ("Lina", 88, 1), ("Ira", 95, 5)]

    # Expected output: [('Ira', 95, 5), ('Arun', 91, 2)]
    assert top_k_by_min_score(data, min_score=90, k=2) == [
        ("Ira", 95, 5),
        ("Arun", 91, 2),
    ]
    # Expected output: []
    assert top_k_by_min_score(data, min_score=99, k=3) == []
    try:
        top_k_by_min_score(data, min_score=50, k=0)
        raise AssertionError("should have raised ValueError for k=0")
    except ValueError:
        pass
    print("ex03_advanced: all asserts passed")
