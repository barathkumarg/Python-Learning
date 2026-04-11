# Day 03 Exercises - Functions, Arguments & Lambda

## Learning objectives

- Write functions that return values instead of printing directly.
- Use defaults, positional-only or keyword-only options, and `*args` or `**kwargs` intentionally.
- Practice designing function signatures that are flexible but still readable.
- Use a short `lambda` only where it keeps sorting or key selection simple.

---

## Exercise specs

Implementation note (Day 03+):
- Show expected outputs in each exercise file using module docstring examples and/or short comments near `__main__` sample calls/asserts.

### ex01_basic.py - Full name formatter

**Must pass:**
- Implement `format_full_name(first_name: str, last_name: str, *, title: str | None = None) -> str`.
- Trim whitespace from `first_name`, `last_name`, and optional `title`.
- Return names in title case, for example `Ada Lovelace`.
- Raise `ValueError` if either required name is empty after trimming.

**Stretch:**
- Ignore an empty `title` after trimming instead of including extra spaces.

**Failure modes:**
- Must NOT print instead of returning.
- Must NOT mutate incoming arguments.

**Example:**
- Input: `(" ada ", " lovelace ")` -> Output: `"Ada Lovelace"`

---

### ex02_intermediate.py - Collect missing fields with `*args`

**Must pass:**
- Implement `collect_missing_fields(form_data: dict[str, str], *required_fields: str, trim_values: bool = True) -> list[str]`.
- Raise `ValueError` if no `required_fields` are provided.
- Return missing field names in the same order they were requested.
- When `trim_values=True`, treat whitespace-only strings as missing.

**Stretch:**
- Accept unpacked input naturally, for example `collect_missing_fields(form_data, *["email", "role"])`.

**Failure modes:**
- Must NOT mutate the incoming dictionary.
- Must NOT sort or deduplicate missing field names unless the spec says so.

**Example:**
- Input: `{"email": " ada@example.com ", "role": "   "}`, required fields `"email", "role"` -> Output: `["role"]`

---

### ex03_advanced.py - Flexible event message builder

**Must pass:**
- Implement `build_event_message(name: str, /, *tags: str, uppercase: bool = False, **details: str) -> str`.
- Trim `name` and raise `ValueError` if it is empty after trimming.
- If `uppercase=True`, convert the event name to uppercase.
- If tags are provided, append `tags=...` using comma-separated trimmed tag values.
- If keyword details are provided, append them as `key=value` pairs sorted by key.

**Stretch:**
- Use a short `lambda` with `sorted()` when ordering the detail pairs.

**Failure modes:**
- Must NOT include blank tags after trimming.
- Must NOT mutate `details`.
- Must NOT accept `name=` as a keyword argument because the signature is positional-only.

**Example:**
- Input: `build_event_message("signup", "python", "day3", level="basic")`
- Output: `"signup | tags=python,day3 | level=basic"`

---

## Skills assessed

| Skill ID | Skill | Exercise |
|----------|-------|----------|
| PY-02 | String operations & formatting | ex01, ex03 |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 |
| PY-05 | Functions, args, kwargs, lambda | ex01, ex02, ex03 |
| PY-16 | Type hints & API clarity | ex01, ex02, ex03 |

---

## Scoring (per file, 0-100)

| Criterion | Points |
|-----------|--------|
| All **must-pass** behaviors implemented | 40 |
| **Stretch** behaviors (partial credit ok) | 15 |
| **Inline asserts + AI-verified** behavior coverage | 25 |
| **Style** - types, ruff-clean, docstrings | 20 |
| **Total** | **100** |

**Pass:** >= 75 per file and gates G1-G4 satisfied.

## Dimension weights (from docs/EVALUATION_RUBRIC.md)

| Dimension | Weight |
|-----------|--------|
| D1 Correctness | 0.30 |
| D2 Reliability | 0.15 |
| D3 Maintainability | 0.15 |
| D4 API & typing | 0.10 |
| D5 Performance | 0.10 |
| D6 Security & safety | 0.10 |
| D7 Code quality | 0.10 |

**Professional pass:** weighted average >= 3.5 and no dimension below 2.

---

## Self-check

```bash
python exercise/python_basic/day_03_functions/ex01_basic.py
python exercise/python_basic/day_03_functions/ex02_intermediate.py
python exercise/python_basic/day_03_functions/ex03_advanced.py
ruff check exercise/python_basic/day_03_functions/
```

---

## Suggested Practice

- [Real Python - Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/) - deeper practice on parameters, defaults, and flexible signatures
- [Real Python - How to Use Python Lambda Functions](https://realpython.com/python-lambda/) - practical guidance on small, readable `lambda` usage
