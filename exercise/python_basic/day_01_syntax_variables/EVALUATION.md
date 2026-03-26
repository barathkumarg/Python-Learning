# Day 01 Evaluation - Syntax and Variables

## Learning objectives
- Use type hints and clear signatures for basic utility functions.
- Apply input validation with explicit error messages.
- Write predictable string formatting with f-strings.
- Pass behavior-focused pytest tests.

## Must-pass vs stretch

### ex01_basic.py
Must-pass:
- Trim, lowercase, and underscore username.
- Raise `ValueError` on blank input.

Stretch:
- Collapse multiple spaces into a single underscore.

### ex02_intermediate.py
Must-pass:
- Parse string to int.
- Enforce range 0..5 inclusive.
- Raise clear `ValueError` for non-int and out-of-range.

Stretch:
- Accept and trim surrounding spaces before parsing.

### ex03_advanced.py
Must-pass:
- Validate app name and workers.
- Produce exact banner format with uppercase env.

Stretch:
- Normalize app name by trimming whitespace.

## Per-file scoring (0-100)
- Must-pass behaviors implemented: 40
- Stretch behaviors: 15
- Tests cover must-pass and at least one edge case: 25
- Style (types, ruff, docstrings): 20

Pass rule per file:
- Score >= 75
- Gates G1-G4 satisfied

## Dimension weights (from docs/EVALUATION_RUBRIC.md)
- D1 Correctness: 0.30
- D2 Reliability: 0.15
- D3 Maintainability: 0.15
- D4 API and typing: 0.10
- D5 Performance: 0.10
- D6 Security and safety: 0.10
- D7 Test quality: 0.10

Overall professional pass bar:
- Weighted average >= 3.5 and no dimension below 2
