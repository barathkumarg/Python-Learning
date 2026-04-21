"""Exercise 02: Config merger.

Problem:
    Implement `merge_configs(defaults: dict[str, object], overrides: dict[str, object]) -> dict[str, object]`.
    Return a new dict where overrides values take precedence over defaults.

    Stretch: Implement `deep_merge(base: dict, patch: dict) -> dict`.
    Recursively merge nested dicts; non-dict values in patch replace base values.

Constraints:
    - Raise `TypeError` if either argument is not a `dict`.
    - Do NOT mutate `defaults` or `overrides`.
    - Keys that exist only in `defaults` must be preserved.

Examples:
    merge_configs({"color": "green", "width": 80}, {"color": "red", "height": 24})
        -> {"color": "red", "width": 80, "height": 24}
    deep_merge({"db": {"host": "localhost", "port": 5432}}, {"db": {"port": 3306}})
        -> {"db": {"host": "localhost", "port": 3306}}
"""

from __future__ import annotations


def merge_configs(
    defaults: dict[str, object],
    overrides: dict[str, object],
) -> dict[str, object]:
    """Merge overrides onto defaults, returning a new dict.

    Args:
        defaults: Base configuration dict.
        overrides: Dict whose values take precedence on key collisions.

    Returns:
        A new merged dict.

    Raises:
        TypeError: If either argument is not a dict.
    """
    # TODO: validate both inputs are dicts, raise TypeError with descriptive message
    # TODO: create a new dict from defaults (use {**defaults} or .copy())
    # TODO: update with overrides using update() or |
    # TODO: return the merged dict — verify originals are unchanged
    raise NotImplementedError()


def deep_merge(base: dict[str, object], patch: dict[str, object]) -> dict[str, object]:
    """Recursively merge patch into base.

    When both base[k] and patch[k] are dicts, merge recursively.
    Otherwise patch[k] replaces base[k].

    Args:
        base: Base dict to merge into.
        patch: Dict whose values override or extend base.

    Returns:
        A new deeply merged dict.

    Raises:
        TypeError: If either argument is not a dict.
    """
    # TODO: validate both inputs are dicts
    # TODO: start with a shallow copy of base
    # TODO: for each key in patch:
    #   - if key exists in result AND both values are dicts → recurse
    #   - otherwise → result[key] = patch[key]
    # TODO: return result
    raise NotImplementedError()


if __name__ == "__main__":
    try:
        # --- merge_configs ---
        defaults = {"color": "green", "width": 80, "debug": False}
        overrides = {"color": "red", "height": 24}
        merged = merge_configs(defaults, overrides)
        # Expected output: {'color': 'red', 'width': 80, 'debug': False, 'height': 24}
        assert merged["color"] == "red"
        assert merged["width"] == 80
        assert merged["height"] == 24
        assert defaults["color"] == "green", "defaults must not be mutated"

        # TypeError checks
        try:
            merge_configs("not a dict", {})  # type: ignore[arg-type]
            raise AssertionError("should have raised TypeError")
        except TypeError:
            pass

        # --- deep_merge (stretch) ---
        base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
        patch = {"db": {"port": 3306, "ssl": True}, "debug": True}
        result = deep_merge(base, patch)
        # Expected output: {'db': {'host': 'localhost', 'port': 3306, 'ssl': True}, 'debug': True}
        assert result["db"]["host"] == "localhost"  # type: ignore[index]
        assert result["db"]["port"] == 3306  # type: ignore[index]
        assert result["db"]["ssl"] is True  # type: ignore[index]
        assert result["debug"] is True
        assert base["db"]["port"] == 5432, "base must not be mutated"  # type: ignore[index]

        print("ex02_intermediate: all asserts passed")
    except NotImplementedError:
        print("ex02_intermediate: implement merge_configs to run self-checks.")
