# Day 02 — Control Flow

> **TL;DR:** Guard clauses keep functions shallow, `match` makes state machines readable, and loop controls (`break`/`continue`/`for-else`) let you signal success vs exhaustion. `code.py` shows production-style order state handling without hidden fallthroughs.

## Concepts

| Concept | What it does | Why it matters | `code.py` ref |
|---------|-------------|----------------|---------------|
| Guard clauses | Fail fast on invalid input before main logic | Prevents deep nesting and ambiguous state | `normalize_status` |
| `match` state machine | Declarative branching by pattern | Safer than long `if/elif` chains for status flows | `transition_order_status` |
| `for` + `continue` | Skip non-qualifying items without extra flags | Keeps loops readable when filtering streams | `collect_high_value_orders` |
| `for-else` | Run `else` when loop completes without `break` | Clear success/failure signaling in searches | `wait_for_terminal_status` |
| Bounded `while` | Poll with explicit exit to avoid infinite loops | Production-safe retries with timeout | `wait_for_terminal_status` |
| `Iterable[dict[str, object]]` | Type-safe iteration over any order feed | Streams or lists both work without copies | `collect_high_value_orders` |
| `Callable[[], str]` | Declares a zero-arg poller returning status | Easier to mock/inject in tests | `wait_for_terminal_status` |

## Snippets

**Guard clause before work** — exit early when input is unknown.
```python
normalized = raw_status.strip().lower()
if normalized not in {"created", "paid", "shipped", "cancelled"}:
    raise ValueError(f"unsupported status: {raw_status}")
```
> Guard clauses cut off invalid states before branching, reducing cognitive load.

**`match` as a state machine** — explicit transitions per event.
```python
match current, action:
    case "created", "pay":
        return "paid"
    case "paid", "ship":
        return "shipped"
    case "paid", "cancel":
        return "cancelled"
    case _:
        raise ValueError("illegal transition")
```
> `match` makes legal paths obvious and rejects everything else via the catch-all.

**Filtering loop with `continue`** — keep only high-value orders.
```python
selected: list[str] = []
for order in orders:
    if order["total"] < threshold:
        continue
    selected.append(order["id"])
```
> `continue` removes the need for nested `if` blocks when skipping items.

**Typed inputs/outputs** — accept streams and mockable pollers.
```python
def collect_high_value_orders(orders: Iterable[dict[str, object]], threshold: float) -> list[str]:
    ...

def wait_for_terminal_status(poll: Callable[[], str], max_checks: int = 5) -> str:
    ...
```
> `Iterable[...]` handles lists or generators; `Callable[[], str]` pins the poller contract for tests.

**`while` + `else` to detect exhaustion** — signal timeout cleanly.
```python
attempts = 0
while attempts < max_checks:
    status = poll()
    if status in terminal:
        return status
    attempts += 1
else:
    raise TimeoutError("status not reached in time")
```
> The `else` block runs only when the loop never hit `break`, making timeouts explicit.

## Visual / Diagram

Order flow (happy path vs cancellation):
```
created --pay--> paid --ship--> shipped
   \--cancel--> cancelled
```

## Pitfalls

- Allowing implicit fallthrough: missing a default branch makes illegal transitions succeed silently.
- Infinite loops from `while True` without a max-check guard or sleep.
- Mutating loop iterables while iterating, leading to skipped items or RuntimeError.

## Why this design

Functions fail fast with guard clauses, use `match` for exhaustive state handling, and bound loops to avoid runaway retries. This mirrors production services where clarity, explicit errors, and safe timeouts beat cleverness.

## Further reading

- [Real Python — Conditional Statements](https://realpython.com/python-conditional-statements/) — deep dive on branching patterns
- [PEP 634 — Structural Pattern Matching](https://peps.python.org/pep-0634/) — spec behind `match`/`case`
- [Python Docs — for-else](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) — when the `else` clause runs
