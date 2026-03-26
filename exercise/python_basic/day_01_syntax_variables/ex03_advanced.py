"""Exercise 03: Complete the function logic.

Problem:
    Implement `build_runtime_banner` to produce a startup log line.

Function signature:
    build_runtime_banner(app_name: str, env: str, debug: bool, workers: int) -> str

Input/Output:
    - Inputs: app name, environment, debug flag, worker count
    - Output: formatted startup banner string

Constraints:
    - app_name must be non-empty
    - workers must be > 0
    - env must be uppercased in output
    - Output format must be exact:
      "[ENV] app=<name> debug=<bool> workers=<num>"

Examples:
    build_runtime_banner("InventoryAPI", "prod", False, 4)
    -> "[PROD] app=InventoryAPI debug=False workers=4"
    build_runtime_banner("Billing", "dev", True, 2)
    -> "[DEV] app=Billing debug=True workers=2"
"""


def build_runtime_banner(app_name: str, env: str, debug: bool, workers: int) -> str:
    """Build a startup banner string for logs."""
    # TODO:
    # 1) Validate app_name is not blank
    if not app_name:
        raise ValueError("Name was null")
    # 2) Validate workers > 0
    if workers <=0:
        raise ValueError("Vlaue less or equal to 0")
    # 3) Uppercase env and compose exact output format
    env = env.upper()
    # Sample: build_runtime_banner("InventoryAPI", "prod", False, 4)
    # -> "[PROD] app=InventoryAPI debug=False workers=4"
    return f'[{env}] app={app_name} debug={debug} workers={workers}'
    # raise NotImplementedError("Implement build_runtime_banner")


if __name__ == "__main__":
    # Self-check: all asserts must pass before AI evaluation
    assert build_runtime_banner("InventoryAPI", "prod", False, 4) == (
        "[PROD] app=InventoryAPI debug=False workers=4"
    ), "standard happy path"
    assert build_runtime_banner("Billing", "dev", True, 2) == (
        "[DEV] app=Billing debug=True workers=2"
    ), "dev env with debug"
    for args in [("", "prod", False, 4), ("App", "prod", True, 0)]:
        try:
            build_runtime_banner(*args)
            raise AssertionError(f"should raise ValueError for {args!r}")
        except ValueError:
            pass  # expected
    print("ex03: all asserts passed ✓")
