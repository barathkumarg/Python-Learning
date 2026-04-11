# Day 03 — Functions, Arguments & Lambda

> **TL;DR:** Functions package reusable logic behind a name, a signature, and a return value. Day 03 moves from basic `def` usage to defaults, keyword-only arguments, `*args`, `**kwargs`, unpacking, and small `lambda` helpers so your code stays flexible without becoming messy.

## Concepts

| Concept | What it does | Why it matters | `code.py` ref |
|---------|-------------|----------------|---------------|
| `def` + `return` | Defines reusable logic and sends a result back | Returned values are easier to test and reuse than printed output | `build_greeting` |
| Positional vs keyword args | Controls how values are passed at call sites | Readable calls reduce mistakes in real services and CLIs | `describe_order` |
| Default arguments | Makes common values optional | Keeps simple calls short without losing flexibility | `build_greeting`, `collect_missing_fields` |
| Positional-only `/` | Forces some arguments to stay positional | Useful when a parameter is short and obvious at the call site | `describe_order`, `build_event_message` |
| Keyword-only `*` | Acts as a separator so parameters after it must be named | Makes flags like `price=` or `uppercase=` clearer | `describe_order`, `build_student_profile`, `build_event_message` |
| `*args` | Collects extra positional values into a tuple | Good when the number of inputs varies | `collect_missing_fields`, `build_event_message` |
| `**kwargs` | Collects extra named values into a dict | Good for optional metadata and flexible formatting | `build_event_message` |
| Unpacking with `*` / `**` | Expands a list or dict into function arguments | Lets you call functions cleanly when data already lives in containers | `__main__` examples |
| Small `lambda` | Creates a short one-expression helper | Best for tiny sort keys or local transformations | `sort_records` |

## Snippets

**`def` + `return`** — reusable functions return values instead of printing them.
```python
def build_greeting(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"
```
Expected output:
```text
build_greeting("Ada") -> "Hello, Ada!"
```
> Returning data keeps the function reusable in tests, APIs, and CLI wrappers.

**Positional and keyword calls** — the same function can support both styles clearly.
```python
label = describe_order("Notebook", 3, price=49.99)
same_label = describe_order("Notebook", quantity=3, price=49.99)
```
Expected output:
```text
label == same_label == "3 x Notebook -> USD 149.97"
```
> Keyword arguments make the call self-documenting when there are multiple values.

**Default arguments** — give callers a sensible default for the common case.
```python
def build_greeting(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```
Expected output:
```text
build_greeting("Maya") -> "Hello, Maya!"
build_greeting("Maya", greeting="Welcome") -> "Welcome, Maya!"
```
> Defaults are great for optional behavior, but avoid using them to hide required data.

**Keyword-only options** — force important flags to be written explicitly.
```python
def describe_order(item: str, /, quantity: int, *, price: float) -> str:
    return f"{quantity} x {item} = {quantity * price:.2f}"
```
Expected output:
```text
describe_order("Notebook", 3, price=49.99) -> "3 x Notebook = 149.97"
```
> `price` is easier to read as `price=49.99` than as a bare third positional value.

**What bare `*` means in a function declaration** — it is a separator, not a normal parameter.
```python
def build_student_profile(name: str, *, track: str, level: str = "beginner") -> str:
    return f"{name} -> {track} ({level})"

build_student_profile("Barath", track="python")
# build_student_profile("Barath", "python")  # TypeError
```
Expected output:
```text
build_student_profile("Barath", track="python") -> "Barath -> python (beginner)"
build_student_profile("Barath", "python") -> TypeError
```
> Everything after `*` must be passed with the parameter name, like `track="python"`.

**`*args` for flexible input** — accept any number of required field names.
```python
def collect_missing_fields(data: dict[str, str], *required_fields: str) -> list[str]:
    return [field for field in required_fields if not data.get(field, "").strip()]
```
Expected output:
```text
collect_missing_fields({"email": "a@b.com", "role": " "}, "email", "role") -> ["role"]
```
> Inside the function, `required_fields` becomes a tuple.

**`**kwargs` for metadata** — gather extra named details into one dict.
```python
def build_event_message(name: str, /, **details: str) -> str:
    return " | ".join([name, *[f"{key}={value}" for key, value in details.items()]])
```
Expected output:
```text
build_event_message("signup", level="basic") -> "signup | level=basic"
```
> `details` is a dictionary of extra named values passed by the caller.

**Unpacking at the call site** — reuse existing containers directly.
```python
required = ["email", "role"]
options = {"price": 49.99, "currency": "USD"}

missing = collect_missing_fields(form_data, *required)
label = describe_order("Notebook", 3, **options)
```
Expected output:
```text
missing -> ["role"]
label -> "3 x Notebook -> USD 149.97"
```
> Use `*` for iterables and `**` for dictionaries when calling a function.

**Small `lambda` keys** — keep lambdas tiny and local.
```python
records = [("Maya", 88), ("Arun", 91), ("Lina", 84)]
sorted_by_name = sorted(records, key=lambda record: record[0].lower())
```
Expected output:
```text
sorted_by_name -> [("Arun", 91), ("Lina", 84), ("Maya", 88)]
```
> A short `lambda` is fine for a one-line key function used once.

**Anti-pattern -> corrected pattern** — avoid printing inside reusable helpers.
```python
def show_total(total: float) -> None:
    print(total)

def get_total(total: float) -> float:
    return total
```
Expected output:
```text
show_total(42.0) prints: 42.0
get_total(42.0) returns: 42.0
```
> Printing belongs at the edge of the program; reusable functions should usually return values.

## Pitfalls

- Printing from reusable functions instead of returning values.
- Using mutable defaults like `items=[]`; use `None` and create a new object inside.
- Reaching for `*args` or `**kwargs` when a fixed, clearer signature would do.
- Writing long `lambda` expressions that should really be named functions.
- Forgetting that positional arguments must come before keyword arguments in a call.

## Why this design

The reference code follows a practical flow: define a simple function, shape the signature, then add flexibility with `*args`, `**kwargs`, and unpacking. The examples stay small, but they use realistic tasks like form validation, order formatting, and event metadata instead of toy-only math snippets.

## Further reading

- [Python docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) — official guide to parameters, defaults, and returns
- [Real Python — Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/) — beginner-to-practical function patterns
- [Real Python — Python Lambda](https://realpython.com/python-lambda/) — where `lambda` helps and where a named `def` is clearer
