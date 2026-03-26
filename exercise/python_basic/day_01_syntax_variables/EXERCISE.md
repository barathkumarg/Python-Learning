# Day 01 Exercises - Syntax and Variables

Implement the following exercises in platform style: complete the function logic in each `exNN_*.py` file.

## ex01_basic.py - Username formatter
Must pass:
- Remove leading/trailing spaces.
- Convert to lowercase.
- Replace internal spaces with underscores.
- Raise `ValueError` when input is empty after trimming.

Example:
- Input: `"  Alice Doe  "`
- Output: `"alice_doe"`

## ex02_intermediate.py - Retry count parser
Must pass:
- Accept input as string.
- Convert to integer.
- Value must be between 0 and 5 (inclusive).
- Raise `ValueError` with clear messages for invalid values.

Example:
- Input: `"3"`
- Output: `3`

## ex03_advanced.py - Build runtime banner
Must pass:
- Validate `app_name` is non-empty.
- Validate `workers` is greater than 0.
- Build banner string with f-string format:
  `"[ENV] app=<name> debug=<bool> workers=<num>"`
- `env` must be uppercased in output.

Example:
- Input: `app_name="InventoryAPI", env="prod", debug=False, workers=4`
- Output: `"[PROD] app=InventoryAPI debug=False workers=4"`

## Run tests
```bash
pytest exercise/python_basic/day_01_syntax_variables/test_exercises.py -v
```
