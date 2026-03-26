# Day 01 - Syntax and Variables (Python Basic)

## Why this matters in production
Syntax and variables look simple, but they are where reliability starts. Clear names, correct types, and predictable formatting reduce bugs and make code review faster.

## What this module covers
- Primitive data types: `int`, `float`, `str`, `bool`, `None`
- Naming conventions and constants
- f-strings for readable output
- Basic input validation and explicit errors
- Small utility functions with type hints and docstrings
- Concept notes for Python features used in the reference code

## How `code.py` is structured
- Starts with a module-level docstring explaining design choices
- Uses strongly typed helper functions
- Includes practical examples that mirror backend tasks
- Keeps examples small and testable

## Documentation step to preserve
- Keep concept notes inside this `CODE.md` so learners have code, rationale, and concepts in one place.
- Use the inline template below when adding new concepts.
- Each concept entry includes: `Explanation`, `Technical terms`, `Code`.

## Concept note template (inline)
- Purpose: keep explanations close to code; document built-ins, exceptions, syntax, and typing used here.
- Structure:
  - `Explanation`: what it does and why it’s used.
  - `Technical terms`: 2–3 short definitions.
  - `Code`: a small example focused on the concept.

Template snippet:
```markdown
### Concept: `<name>`

#### Explanation
Explain what the concept does in simple language and why it is used in this code.

#### Technical terms
- Term: short meaning
- Term: short meaning

#### Code
```python
# Small example focused on the concept
```
```

Example (from this module):
```markdown
### Concept: `strip()`

#### Explanation
`strip()` removes whitespace from the beginning and end of a string. It is useful when user input may include extra spaces that should not affect validation.

#### Technical terms
- Whitespace: blank characters such as spaces, tabs, and new lines
- String method: a method available on string values
- Validation: checking whether input follows the expected rules

#### Code
```python
raw_name = "  Barath  "
clean_name = raw_name.strip()
print(clean_name)  # Barath
```
```

## Concept notes for Day 01

### Concept: `strip()`
#### Explanation
`strip()` removes whitespace from the start and end of a string. In the reference code, it is used to clean `user_name` before checking whether the value is blank.
#### Technical terms
- Whitespace: spaces, tabs, and line breaks
- String: text data in Python
- Validation: checking whether an input value satisfies a rule
#### Code
```python
user_name = "  Barath  "
cleaned_name = user_name.strip()
print(cleaned_name)  # Barath
```

### Concept: `ValueError`
#### Explanation
`ValueError` is raised when a value is present but does not satisfy the expected rules. Here it is used for blank names, invalid retry counts, negative prices, and invalid worker counts.
#### Technical terms
- Exception: an error that interrupts normal execution
- Raise: manually trigger an exception with `raise`
- Input validation: checking that provided values are acceptable
#### Code
```python
workers = 0

if workers <= 0:
    raise ValueError("workers must be > 0")
```

### Concept: `int()`
#### Explanation
`int()` converts a value into an integer when possible. Here it is used to parse retry counts that arrive as strings.
#### Technical terms
- Integer: a whole number like `0`, `2`, or `10`
- Type conversion: changing data from one type to another
- Parsing: turning raw input into a usable value
#### Code
```python
raw_value = "2"
count = int(raw_value)
print(count)  # 2
```

### Concept: `round()`
#### Explanation
`round()` returns a number rounded to a given number of decimal places. The invoice example uses it to keep totals in a clean currency-like format.
#### Technical terms
- Decimal places: digits to the right of the decimal point
- Float: a number that can contain a fractional part
- Precision: how detailed a numeric value is
#### Code
```python
total = 471.9764
final_total = round(total, 2)
print(final_total)  # 471.98
```

### Concept: `Final`
#### Explanation
`Final` is a typing hint that marks a variable as intended to stay constant. It helps readers understand that values like app-level settings should not be reassigned later.
#### Technical terms
- Type hint: metadata that describes the expected type of a value
- Constant: a value intended not to change
- Static analysis: tooling that checks code without running it
#### Code
```python
from typing import Final

APP_NAME: Final[str] = "Python Learning"
```

### Concept: f-string
#### Explanation
An f-string lets you place variables directly inside a string using curly braces. The reference code uses f-strings to build readable messages and logs.
#### Technical terms
- Interpolation: inserting values into a string
- Placeholder: the location where a value is inserted
- Formatted output: text built in a controlled and readable way
#### Code
```python
name = "Barath"
message = f"Welcome {name}! Ready to master Python?"
print(message)
```

### Concept: type hints
#### Explanation
Type hints show the expected types of parameters and return values. They improve readability and make functions easier to understand, test, and review.
#### Technical terms
- Parameter: an input accepted by a function
- Return type: the type of value a function gives back
- Annotation: extra information attached to code
#### Code
```python
def parse_retry_count(raw_value: str) -> int:
    return int(raw_value)
```

## Pitfalls to avoid
- Mixing string and number operations without conversion
- Using unclear variable names (`x`, `temp`) in business logic
- Silent fallback behavior when inputs are invalid
- Printing data instead of returning data from reusable functions

## Why this design
The reference examples prefer pure functions and explicit return values. This style is easier to test and reuse in APIs, CLIs, and data pipelines.
