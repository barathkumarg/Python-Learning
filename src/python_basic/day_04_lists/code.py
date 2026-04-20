"""Day 04 reference code: list access, mutation, and predictable sorting.

Design choices:
- Validate inputs at boundaries so list operations fail with clear messages.
- Keep read-only operations (`slice_page`) separate from update operations (`bump_score`).
- Use stable multi-pass sorting for leaderboard tie-breakers.
"""

from __future__ import annotations

from collections.abc import Sequence

LeaderboardEntry = tuple[str, int, int]


def validate_scores(raw_scores: Sequence[int]) -> list[int]:
    """Validate score values and return a list copy.

    Args:
        raw_scores: Sequence of numeric scores expected in range 0..100.

    Returns:
        A new list containing the validated scores.

    Raises:
        ValueError: If any score is outside 0..100.
    """
    validated = list(raw_scores)
    for index, score in enumerate(validated):
        if score < 0 or score > 100:
            raise ValueError(f"score must be in 0..100, got score={score} at index={index}")
    return validated


def slice_page(items: Sequence[str], *, start: int, size: int) -> list[str]:
    """Return a fixed-size slice for paginated views.

    Args:
        items: Source sequence of labels.
        start: Zero-based start position.
        size: Number of items requested.

    Returns:
        A new list containing at most `size` items from `start` onward.

    Raises:
        ValueError: If `start` is negative or `size` is less than 1.
    """
    if start < 0:
        raise ValueError(f"start must be >= 0, got start={start}")
    if size < 1:
        raise ValueError(f"size must be >= 1, got size={size}")
    return list(items[start : start + size])


def bump_score(scores: list[int], *, player_index: int, delta: int) -> list[int]:
    """Return a new score list after applying a delta at one index.

    Args:
        scores: Current score list.
        player_index: Index of the player to update.
        delta: Amount to add (or subtract) from the current score.

    Returns:
        A new list with one updated score.

    Raises:
        ValueError: If index is out of range or updated score is outside 0..100.
    """
    if player_index < 0 or player_index >= len(scores):
        raise ValueError(
            f"player_index must be in 0..{len(scores) - 1}, got player_index={player_index}"
        )

    updated = scores.copy()
    candidate = updated[player_index] + delta
    if candidate < 0 or candidate > 100:
        raise ValueError(
            f"updated score must be in 0..100, got updated_score={candidate}"
        )
    updated[player_index] = candidate
    return updated


def sort_leaderboard(entries: Sequence[LeaderboardEntry]) -> list[LeaderboardEntry]:
    """Sort leaderboard entries by score, then penalty, then name.

    Sorting rules:
    1. Higher score first.
    2. Lower penalty minutes first.
    3. Name ascending (case-insensitive) for deterministic display.

    Args:
        entries: Sequence of `(name, score, penalty_minutes)` tuples.

    Returns:
        Sorted leaderboard entries as a new list.

    Raises:
        ValueError: If name is blank, score is outside 0..100, or penalty is negative.
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


def top_k_players(entries: Sequence[LeaderboardEntry], *, k: int) -> list[LeaderboardEntry]:
    """Return the top `k` players using the same leaderboard ordering.

    Args:
        entries: Sequence of `(name, score, penalty_minutes)` tuples.
        k: Number of highest-ranked rows requested.

    Returns:
        A list containing up to `k` ranked entries.

    Raises:
        ValueError: If `k` is less than 1.
    """
    if k < 1:
        raise ValueError(f"k must be >= 1, got k={k}")
    return sort_leaderboard(entries)[:k]


if __name__ == "__main__":
    scores = validate_scores([91, 88, 77, 95])
    # ...assert removed...

    page = slice_page(["Maya", "Arun", "Lina", "Ira"], start=1, size=2)
    # ...assert removed...

    bumped = bump_score([91, 88, 77], player_index=1, delta=5)
    # ...assert removed...

    leaderboard = [
        ("Maya", 91, 4),
        ("Arun", 91, 2),
        ("Lina", 88, 1),
        ("Ira", 95, 5),
    ]
    ordered = sort_leaderboard(leaderboard)
    # ...assert removed...
    # ...assert removed...

    top_two = top_k_players(leaderboard, k=2)
    # ...assert removed...

    print("validated scores:", scores)  # Expected output: validated scores: [91, 88, 77, 95]
    print("page:", page)  # Expected output: page: ['Arun', 'Lina']
    print("bumped:", bumped)  # Expected output: bumped: [91, 93, 77]
    print("ordered:", ordered)  # Expected output: ordered: [('Ira', 95, 5), ('Arun', 91, 2), ('Maya', 91, 4), ('Lina', 88, 1)]
    print("top two:", top_two)  # Expected output: top two: [('Ira', 95, 5), ('Arun', 91, 2)]
