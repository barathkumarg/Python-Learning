"""Week 01 reference code: Big-O, arrays, and hashing basics.

Design choices:
- Use small, typed helpers that match common interview and production patterns.
- Prefer hash-map lookups for O(1) average-time membership and index retrieval.
- Keep outputs deterministic where useful (for easier tests and learning feedback).
"""

from __future__ import annotations


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any number appears more than once.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    seen: set[int] = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False


def two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of two numbers whose sum equals target.

    Uses a hash map from value -> index while scanning once.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    seen_index: dict[int, int] = {}
    for idx, value in enumerate(nums):
        needed = target - value
        if needed in seen_index:
            return (seen_index[needed], idx)
        seen_index[value] = idx
    return None


def frequency_map(items: list[str]) -> dict[str, int]:
    """Return frequency counts for each string item.

    Time complexity: O(n)
    Space complexity: O(k), where k is number of distinct items.
    """

    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def anagram_signature(word: str) -> tuple[int, ...]:
    """Return a 26-letter frequency signature for lowercase English letters.

    Time complexity: O(m)
    Space complexity: O(1) fixed-size array
    """

    counts = [0] * 26
    for ch in word:
        counts[ord(ch) - ord("a")] += 1
    return tuple(counts)


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words by anagram equivalence.

    Returns sorted inner groups to keep output stable for tests and docs.

    Time complexity: O(n * m)
    Space complexity: O(n)
    """

    groups: dict[tuple[int, ...], list[str]] = {}
    for word in words:
        signature = anagram_signature(word)
        groups.setdefault(signature, []).append(word)

    result = [sorted(group) for group in groups.values()]
    return sorted(result, key=lambda group: (len(group), group[0]))


if __name__ == "__main__":
    # print(contains_duplicate([1, 2, 3, 1]))  # Expected output: True
    # print(contains_duplicate([1, 2, 3, 4]))  # Expected output: False

    # print(two_sum_indices([2, 7, 11, 15], 9))  # Expected output: (0, 1)
    # print(two_sum_indices([1, 2, 3], 99))  # Expected output: None

    # print(frequency_map(["api", "db", "api", "cache"]))  # Expected output: {'api': 2, 'db': 1, 'cache': 1}

    print(anagram_signature("tea") == anagram_signature("eat"))  # Expected output: True

    print(
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    )  # Expected output: [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
