"""Day 06 reference code: dictionaries — creation, CRUD, merging, and industrial patterns.

Design choices:
- Start with a simple word-count builder that demonstrates literal creation,
  `get()` with default, and `.items()` iteration.
- Progress to config merging with `|`, `update()`, and `**` unpacking.
- Include an inverted-index builder using `setdefault()` and dict comprehension.
- Add a safe nested-get helper for deeply nested dicts.
- Finish with a `defaultdict`-based grouping function as a preview of
  `collections` helpers.

All functions validate inputs, use type hints, and raise descriptive errors.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from copy import deepcopy


def build_word_count(text: str) -> dict[str, int]:
    """Return a case-insensitive word frequency dict.

    Args:
        text: Input string to count words from.

    Returns:
        Dict mapping lowercased words to their occurrence count.

    Raises:
        TypeError: If *text* is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"expected str, got {type(text).__name__}")

    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def merge_configs(
    defaults: Mapping[str, object],
    *overrides: Mapping[str, object],
) -> dict[str, object]:
    """Merge one or more override dicts onto a defaults dict.

    Later overrides take precedence over earlier ones on key collisions.
    The original *defaults* mapping is never mutated.

    Args:
        defaults: Base configuration mapping.
        *overrides: One or more mappings whose values override *defaults*.

    Returns:
        A new merged dict.

    Raises:
        TypeError: If *defaults* is not a mapping.
    """
    if not isinstance(defaults, Mapping):
        raise TypeError(f"defaults must be a Mapping, got {type(defaults).__name__}")

    merged: dict[str, object] = {**defaults}
    for override in overrides:
        merged.update(override)
    return merged


def build_inverted_index(
    documents: Mapping[str, str],
) -> dict[str, list[str]]:
    """Build an inverted index mapping each word to the doc IDs that contain it.

    Args:
        documents: Mapping of document ID to document text.

    Returns:
        Dict mapping lowercased words to sorted lists of doc IDs.

    Raises:
        TypeError: If *documents* is not a mapping.
    """
    if not isinstance(documents, Mapping):
        raise TypeError(f"expected Mapping, got {type(documents).__name__}")

    index: dict[str, list[str]] = {}
    for doc_id, text in documents.items():
        seen_words: set[str] = set()
        for word in text.lower().split():
            if word not in seen_words:
                index.setdefault(word, []).append(doc_id)
                seen_words.add(word)

    return {k: sorted(v) for k, v in sorted(index.items())}


def safe_nested_get(
    data: Mapping[str, object],
    *keys: str,
    default: object = None,
) -> object:
    """Traverse nested dicts by a sequence of keys, returning *default* on miss.

    Args:
        data: The top-level mapping to traverse.
        *keys: One or more string keys representing the access path.
        default: Value returned when any key in the chain is missing.

    Returns:
        The value at the deepest key, or *default*.

    Raises:
        ValueError: If no keys are provided.
    """
    if not keys:
        raise ValueError("provide at least one key")

    current: object = data
    for key in keys:
        if isinstance(current, Mapping):
            current = current.get(key, default)
            if current is default:
                return default
        else:
            return default
    return current


def group_by_key(
    pairs: Sequence[tuple[str, str]],
) -> dict[str, list[str]]:
    """Group values by key using `defaultdict(list)`.

    Args:
        pairs: Sequence of `(key, value)` tuples.

    Returns:
        Dict mapping each key to a list of its values, in encounter order.

    Raises:
        TypeError: If *pairs* is not a sequence.
    """
    if not isinstance(pairs, Sequence):
        raise TypeError(f"expected Sequence, got {type(pairs).__name__}")

    groups: defaultdict[str, list[str]] = defaultdict(list)
    for key, value in pairs:
        groups[key].append(value)
    return dict(groups)


if __name__ == "__main__":
    # --- build_word_count ---
    text = "the cat sat on the mat the cat"
    wc = build_word_count(text)
    print(wc)
    # Expected output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
    assert wc["the"] == 3
    assert wc["cat"] == 2

    # --- merge_configs ---
    defaults = {"color": "green", "width": 80, "debug": False}
    user = {"color": "red", "height": 24}
    env = {"debug": True}
    merged = merge_configs(defaults, user, env)
    print(merged)
    # Expected output: {'color': 'red', 'width': 80, 'debug': True, 'height': 24}
    assert merged["color"] == "red"
    assert merged["debug"] is True
    assert defaults["color"] == "green"  # original unchanged

    # --- build_inverted_index ---
    docs = {
        "d1": "the cat sat",
        "d2": "the dog sat",
        "d3": "the cat and the dog",
    }
    idx = build_inverted_index(docs)
    print(idx)
    # Expected output: {'and': ['d3'], 'cat': ['d1', 'd3'], 'dog': ['d2', 'd3'], 'sat': ['d1', 'd2'], 'the': ['d1', 'd2', 'd3']}
    assert idx["cat"] == ["d1", "d3"]
    assert idx["the"] == ["d1", "d2", "d3"]

    # --- safe_nested_get ---
    nested = {"server": {"host": "localhost", "ports": {"http": 80}}}
    print(safe_nested_get(nested, "server", "host"))
    # Expected output: localhost
    print(safe_nested_get(nested, "server", "ports", "http"))
    # Expected output: 80
    print(safe_nested_get(nested, "server", "missing", default="N/A"))
    # Expected output: N/A
    assert safe_nested_get(nested, "server", "host") == "localhost"
    assert safe_nested_get(nested, "x", "y", default=-1) == -1

    # --- group_by_key (defaultdict preview) ---
    employees = [
        ("sales", "Alice"),
        ("engineering", "Bob"),
        ("sales", "Charlie"),
        ("engineering", "Diana"),
    ]
    grouped = group_by_key(employees)
    print(grouped)
    # Expected output: {'sales': ['Alice', 'Charlie'], 'engineering': ['Bob', 'Diana']}
    assert grouped["sales"] == ["Alice", "Charlie"]

    # --- copy vs deepcopy demo ---
    original: dict[str, list[str]] = {"tags": ["python"]}
    shallow = original.copy()
    deep = deepcopy(original)
    shallow["tags"].append("shallow")
    assert original["tags"] == ["python", "shallow"]  # shared!
    assert deep["tags"] == ["python"]                  # independent

    print("\nAll day-06 self-checks passed.")
