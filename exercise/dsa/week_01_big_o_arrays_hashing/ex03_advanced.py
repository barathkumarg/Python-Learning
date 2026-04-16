"""Exercise 03: Group anagrams with deterministic output.

Problem:
    Implement `group_anagrams(words: list[str]) -> list[list[str]]`.

Constraints:
    - Words are lowercase English letters.
    - Group anagrams together.
    - Deterministic output is required:
      1) sort each group alphabetically
      2) sort groups by `(len(group), group[0])`
    - Target complexity: O(n * m), where `m` is average word length.

Examples:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    -> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    group_anagrams([]) -> []
"""

from __future__ import annotations


def anagram_signature(word: str) -> tuple[int, ...]:
    """Return a 26-element frequency tuple keyed by character position."""
    sign = [0] * 26
    for char in word:
        sign[ord(char) - ord('a')] += 1
    return tuple(sign)


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Return deterministic anagram groups.

    Expected complexity:
        Time O(n * m), Space O(n)
    """

    # TODO: Build a hash key per word (sorted-word key or frequency signature).
    # TODO: Group words in a dict[key] -> list[str].
    # TODO: Sort each group and then sort the outer list by (len(group), group[0]).
    # Sample expected output:
    # group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # -> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    results: dict[tuple[int, ...], list[str]] = {}
    for word in words:
        signature = anagram_signature(word)
        results.setdefault(signature,[]).append(word)
    final = [sorted(result) for result in results.values()]
    return sorted(final, key=lambda result: (len(result), result[0]))


if __name__ == "__main__":
    try:
        # Expected output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ]
        # Expected output: []
        assert group_anagrams([]) == []
        print("ex03_advanced: all asserts passed")
    except NotImplementedError:
        print("ex03_advanced: implement group_anagrams to run self-checks.")
