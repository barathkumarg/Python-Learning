"""Exercise 03: Inverted index builder.

Problem:
    Implement `build_inverted_index(documents: dict[str, str]) -> dict[str, list[str]]`.
    Map each lowercased word to a sorted list of doc IDs that contain it.

    Stretch: Implement `search_index(index: dict[str, list[str]], *terms: str) -> list[str]`.
    Return sorted doc IDs that contain ALL given terms (AND search).

Constraints:
    - Raise `TypeError` if `documents` is not a `dict`.
    - Each doc ID appears at most once per word.
    - Word lists in the index must be sorted.
    - Do NOT mutate the input documents dict.

Examples:
    docs = {"d1": "the cat sat", "d2": "the dog sat", "d3": "the cat and the dog"}
    index = build_inverted_index(docs)
    index["cat"]  -> ["d1", "d3"]
    index["the"]  -> ["d1", "d2", "d3"]

    search_index(index, "cat", "the")  -> ["d1", "d3"]
    search_index(index, "cat", "dog")  -> ["d3"]
"""

from __future__ import annotations


def build_inverted_index(
    documents: dict[str, str],
) -> dict[str, list[str]]:
    """Build an inverted index from document ID → text mapping.

    Args:
        documents: Dict mapping doc IDs to their text content.

    Returns:
        Dict mapping lowercased words to sorted lists of doc IDs.

    Raises:
        TypeError: If *documents* is not a dict.
    """
    # TODO: validate documents is a dict, raise TypeError if not
    # TODO: initialize an empty index dict
    # TODO: for each (doc_id, text) in documents.items():
    #   - split text into words, lowercase each
    #   - for each unique word in this doc, use setdefault(word, []).append(doc_id)
    #   - track seen words per doc to avoid duplicates
    # TODO: sort each word's doc list
    # TODO: return the index (optionally sort by key for deterministic output)
    if not isinstance(documents,dict):
        raise TypeError("Documents was not a dictionary")
    
    result :dict[str,list[str]] = {}
    for index, sentence in documents.items():
        seen_words : set[str] = set()
        for words in sentence.split():
            if words not in seen_words:
                result.setdefault(words, []).append(index)
                seen_words.add(words)
    print(result)
    return result

def search_index(
    index: dict[str, list[str]],
    *terms: str,
) -> list[str]:
    """Return sorted doc IDs containing ALL given terms (AND search).

    Args:
        index: Inverted index mapping words to doc ID lists.
        *terms: One or more search terms.

    Returns:
        Sorted list of doc IDs present in every term's posting list.

    Raises:
        ValueError: If no terms are provided.
    """
    # TODO: validate at least one term is provided
    # TODO: for each term, get the set of doc IDs from the index (empty set if missing)
    # TODO: intersect all sets
    # TODO: return sorted list of the intersection
    if not isinstance(index, dict) and not isinstance(terms, str):
        raise TypeError("Not in the correct type - provided values")
    if len(terms) <=0:
        raise ValueError("No terms passed")
    result : list[str] = index.get(terms[0], [])
    print(result)

    # for topic, sentence in index.items():
    #     print(sentence)
    #     word_list = sentence.split(' ')
    #     for term in terms:
    #         if term not in word_list:
    #             continue
    #         result.append(topic)
    for term in terms:
        list_item = index.get(term,[])
        result = list(set(result) & set(list_item))
    return sorted(result)
     



if __name__ == "__main__":
    try:
        # --- build_inverted_index ---
        docs = {
            "d1": "the cat sat",
            "d2": "the dog sat",
            "d3": "the cat and the dog",
        }
        index = build_inverted_index(docs)
        # Expected output: index["cat"] == ["d1", "d3"]
        assert index["cat"] == ["d1", "d3"], f"got {index.get('cat')}"
        assert index["the"] == ["d1", "d2", "d3"], f"got {index.get('the')}"
        assert index["sat"] == ["d1", "d2"], f"got {index.get('sat')}"
        assert index["dog"] == ["d2", "d3"], f"got {index.get('dog')}"

        # TypeError check
        try:
            build_inverted_index("not a dict")  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # --- search_index (stretch) ---
        results_cat_the = search_index(index, "cat", "the")
        # Expected output: ["d1", "d3"]
        assert results_cat_the == ["d1", "d3"], f"got {results_cat_the}"

        results_cat_dog = search_index(index, "cat", "dog")
        # Expected output: ["d3"]
        assert results_cat_dog == ["d3"], f"got {results_cat_dog}"

        # missing term returns empty
        assert search_index(index, "elephant") == []

        # ValueError on no terms
        try:
            search_index(index)
            raise AssertionError("should have raised ValueError")
        except ValueError:
            pass

        print("ex03_advanced: all asserts passed")
    except NotImplementedError:
        print("ex03_advanced: implement build_inverted_index to run self-checks.")
