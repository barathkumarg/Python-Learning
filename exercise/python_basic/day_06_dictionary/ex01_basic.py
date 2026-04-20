"""Exercise 01: Dictionary Lookup & Safe Access.

Problem:
    Implement `safe_lookup(d: dict, key, default=None)` that returns the value for `key` if present, else `default`.

Examples:
    safe_lookup({"a": 1}, "a") -> 1
    safe_lookup({"a": 1}, "b", 0) -> 0
"""

def safe_lookup(d: dict, key, default=None):
    """Return the value for key if present, else default."""
    # Your code here
    
    pass

if __name__ == "__main__":
    assert safe_lookup({"a": 1}, "a") == 1
    assert safe_lookup({"a": 1}, "b", 0) == 0
    print("ex01_basic: all asserts passed")
