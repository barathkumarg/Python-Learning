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
    # 2) Validate workers > 0
    # 3) Uppercase env and compose exact output format
    # Sample: build_runtime_banner("InventoryAPI", "prod", False, 4)
    # -> "[PROD] app=InventoryAPI debug=False workers=4"
    raise NotImplementedError("Implement build_runtime_banner")


if __name__ == "__main__":
    samples = [
        ("InventoryAPI", "prod", False, 4),
        ("Billing", "dev", True, 2),
        ("", "qa", True, 1),
    ]
    for app_name, env, debug, workers in samples:
        try:
            output = build_runtime_banner(app_name, env, debug, workers)
            print(
                f"input={(app_name, env, debug, workers)!r} output={output!r}",
            )
        except Exception as exc:  # noqa: BLE001
            print(f"input={(app_name, env, debug, workers)!r} error={type(exc).__name__}: {exc}")
