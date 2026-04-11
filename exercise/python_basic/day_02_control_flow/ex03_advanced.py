"""ex03_advanced — Bounded polling loop with timeout handling.

Problem: Call a status fetcher repeatedly until a terminal status is seen or a
maximum number of checks is reached.
Signature: wait_for_completion(poll, max_checks=5, sleep_seconds=None) -> str
Constraints:
- Terminal statuses: shipped, cancelled (case-insensitive comparison).
- `max_checks` must be >= 1; raise ValueError otherwise.
- On timeout, raise TimeoutError and include the last observed status.
- Optional `sleep_seconds` pauses between polls when provided.

Examples:
>>> wait_for_completion(lambda: "shipped", max_checks=3)
'shipped'
>>> wait_for_completion(iter(["created", "paid"]).__next__, max_checks=1)
TimeoutError
"""

from __future__ import annotations

import time
from typing import Callable


def wait_for_completion(poll: Callable[[], str], max_checks: int = 5, sleep_seconds: float | None = None) -> str:
    """Poll until terminal status or raise TimeoutError with context."""
    # validate max_checks >= 1 else raise ValueError
    TERMINATE_STATUS = {"shipped", "cancelled"} 
    if max_checks < 1:
        raise ValueError("Max checks value was less than 1")
    attempts = 0
    while max_checks > attempts:
        status = poll()
        if status in TERMINATE_STATUS:
            return status
        attempts+=1
    raise TimeoutError("Timeout error")


if __name__ == "__main__":
    statuses = ["created", "paid", "shipped"]

    def poller() -> str:
        return statuses.pop(0)

    assert wait_for_completion(poller, max_checks=3) == "shipped"

    single = ["created"]

    def poll_once() -> str:
        return single.pop(0)

    try:
        wait_for_completion(poll_once, max_checks=1)
    except TimeoutError:
        pass
    else:
        raise AssertionError("expected TimeoutError when terminal status not reached")

    print("ex03: all asserts passed ✓")
