# code.py — Day 06: Dictionaries

"""Examples and reference implementations for dictionary basics, safe access, iteration, and comprehensions."""

def get_value(d: dict, key, default=None):
    """Return the value for key if present, else default."""
    return d.get(key, default)


def add_or_update(d: dict, key, value):
    """Add or update a key-value pair in the dictionary."""
    d[key] = value
    return d


def delete_key(d: dict, key):
    """Delete a key from the dictionary if it exists."""
    if key in d:
        del d[key]
    return d


def dict_comprehension_square(d: dict[str, int]) -> dict[str, int]:
    """Return a new dictionary with values squared."""
    return {k: v*v for k, v in d.items()}


if __name__ == "__main__":
    d = {"a": 1, "b": 2}
    assert get_value(d, "a") == 1
    assert get_value(d, "z", 0) == 0
    add_or_update(d, "c", 3)
    assert d["c"] == 3
    delete_key(d, "b")
    assert "b" not in d
    squares = dict_comprehension_square({"x": 2, "y": 3})
    assert squares == {"x": 4, "y": 9}
    print("code.py: all asserts passed")
