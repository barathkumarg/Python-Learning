# Day 09 — File I/O: Exercises

## Learning objectives

After completing these exercises you will be able to:
1. Open, read, and write text files using `open()` with context managers and explicit encoding (concepts 1–7).
2. Navigate and construct paths with `pathlib.Path`, and perform CSV/JSON round-trips (concepts 8–15).
3. Work with JSONL, temp files, binary I/O, safe path validation, and build an ETL pipeline (concepts 16–22).

## Skills assessed

| Skill ID | Skill | Exercise | Proficiency target |
|----------|-------|----------|-------------------|
| PY-07 | File I/O, pathlib, CSV, JSON | ex01, ex02, ex03 | proficient |
| PY-03 | Input validation & error handling | ex01, ex02, ex03 | developing |
| PY-06 | Data structures (list, dict, set, tuple) | ex02, ex03 | developing |

## Concept coverage map

| Checklist # | Concept | Covered in |
|-------------|---------|------------|
| 1 | `open()` | ex01 — `read_file_content` |
| 2 | `with` context manager | ex01 — `read_file_content` |
| 3 | Read methods | ex01 — `read_file_content`, `count_lines` |
| 4 | Write methods | ex01 — `write_lines` |
| 5 | File modes | ex01 — `append_line` |
| 6 | Newline handling | ex02 — `write_csv_file` |
| 7 | Encoding parameter | ex01 — `read_file_content` |
| 8 | `pathlib.Path` basics | ex01 — `file_info` |
| 9 | `pathlib` read/write | ex01 — `pathlib_read_write` |
| 10 | `pathlib` navigation | ex02 — `list_by_extension` |
| 11 | `pathlib` construction | ex02 — `build_output_path` |
| 12 | CSV reading | ex02 — `read_csv_as_dicts` |
| 13 | CSV writing | ex02 — `write_csv_file` |
| 14 | JSON reading | ex02 — `load_json` |
| 15 | JSON writing | ex02 — `save_json` |
| 16 | JSONL | ex03 — `write_jsonl` |
| 17 | `tempfile` | ex03 — `process_in_temp` |
| 18 | Safe paths | ex03 — `validate_path` |
| 19 | Binary I/O | ex03 — `copy_binary` |
| 20 | Anti-pattern: no `with` | ex01 — `read_file_content` (must use `with`) |
| 21 | Anti-pattern: no encoding | ex01 — `read_file_content` (must pass encoding) |
| 22 | Industrial: CSV→JSONL ETL | ex03 — `csv_to_jsonl` |

---

## ex01_basic.py — File Basics and Pathlib (Checklist items #1–#5, #7–#9, #20–#21)

**Must-pass behaviors:**
- Read a text file using `with open(...)` and explicit encoding.
- Write a list of lines to a file; append a single line.
- Return basic path info using `pathlib.Path`.
- Use `Path.read_text()` / `.write_text()` for one-liner I/O.

**Stretch behaviors:**
- Handle non-existent file paths gracefully with descriptive errors.

### Functions to implement:
1. `read_file_content(path, encoding)` — Read and return the entire file content.
2. `count_lines(path)` — Return the number of lines in a text file.
3. `write_lines(path, lines)` — Write a list of strings to a file (one per line).
4. `append_line(path, line)` — Append a single line to an existing file.
5. `file_info(path)` — Return a dict with `name`, `suffix`, `exists`, `size` using pathlib.
6. `pathlib_read_write(path, content)` — Write content with `.write_text()`, read it back with `.read_text()`, return the read content.

---

## ex02_intermediate.py — CSV, JSON, and Path Construction (Checklist items #6, #10–#15)

**Must-pass behaviors:**
- Read a CSV file into a list of dicts using `DictReader`.
- Write a list of dicts to a CSV file using `DictWriter`.
- Load and save JSON files with proper indentation.
- Build output paths using pathlib `/` operator.
- List files matching a specific extension using `.glob()`.

**Stretch behaviors:**
- Handle malformed JSON gracefully with descriptive error.

### Functions to implement:
1. `read_csv_as_dicts(path)` — Read CSV and return list of `dict[str, str]`.
2. `write_csv_file(path, rows, fieldnames)` — Write dicts to CSV with headers.
3. `load_json(path)` — Load and return parsed JSON dict from file.
4. `save_json(path, data, indent)` — Save dict to JSON file with specified indent.
5. `build_output_path(base_dir, name, extension)` — Construct a path using pathlib `/`.
6. `list_by_extension(directory, ext)` — Return sorted list of filenames matching extension.

---

## ex03_advanced.py — JSONL, Temp Files, Binary, ETL (Checklist items #16–#19, #22)

**Must-pass behaviors:**
- Write records as JSONL (one JSON per line).
- Validate file paths for safety (reject traversal, enforce extensions).
- Copy a binary file faithfully.
- Convert CSV to JSONL in a single pipeline function.

**Stretch behaviors:**
- Use `tempfile.NamedTemporaryFile` for intermediate processing.

### Functions to implement:
1. `write_jsonl(path, records)` — Write a list of dicts as JSONL.
2. `read_jsonl(path)` — Read a JSONL file and return list of dicts.
3. `validate_path(path, allowed_extensions)` — Return True if safe, raise ValueError if not.
4. `copy_binary(src, dst)` — Copy a binary file using `"rb"` / `"wb"` modes.
5. `process_in_temp(lines)` — Write lines to a temp file, read them back, return content.
6. `csv_to_jsonl(csv_path, jsonl_path)` — Full ETL: read CSV → write JSONL, return count.

---

## Failure modes to watch for
- Forgetting `encoding="utf-8"` — tests will enforce it.
- Using `"w"` when `"a"` is intended — data silently lost.
- Not passing `newline=""` for CSV — double newlines on Windows.
- `json.load()` vs `json.loads()` confusion — one takes a file, one takes a string.
- Not closing files — always use `with`.
- Path traversal (`..`) in user-supplied paths — must be rejected.

## Scoring

| Criterion | Max | ex01 | ex02 | ex03 |
|-----------|-----|------|------|------|
| Must-pass behaviors | 40 | | | |
| Stretch behaviors | 15 | | | |
| Inline asserts + AI-verified | 25 | | | |
| Style (types, ruff, docstrings) | 20 | | | |
| **Total** | **100** | | | |

## Suggested practice
- [Exercism — Python track](https://exercism.org/tracks/python) — file-based exercises
- [Real Python — Read and Write Files](https://realpython.com/read-write-files-python/) — practical walkthrough

## Self-check commands
```bash
ruff check exercise/python_basic/day_09_file_io/
python exercise/python_basic/day_09_file_io/ex01_basic.py
python exercise/python_basic/day_09_file_io/ex02_intermediate.py
python exercise/python_basic/day_09_file_io/ex03_advanced.py
```
