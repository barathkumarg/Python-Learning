"""Exercise 02: Add, Update, and Delete.

Problem:
    Implement `add_or_update(d: dict, key, value)` to add or update a key-value pair,
    and `delete_key(d: dict, key)` to remove a key if present.

Examples:
    d = {"x": 1}
    add_or_update(d, "y", 2)
    # d == {"x": 1, "y": 2}
    delete_key(d, "x")
    # d == {"y": 2}
"""

def add_or_update(d: dict, key, value):
    """Add or update a key-value pair in the dictionary."""
    # Your code here
    pass

def delete_key(d: dict, key):
    """Delete a key from the dictionary if it exists."""
    # Your code here
    pass

if __name__ == "__main__":
    d = {"x": 1}
    add_or_update(d, "y", 2)
    assert d == {"x": 1, "y": 2}
    delete_key(d, "x")
    assert d == {"y": 2}
    print("ex02_intermediate: all asserts passed")
