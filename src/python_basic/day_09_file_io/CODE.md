# Day 09 — File I/O

> **TL;DR:** File I/O is how Python reads from and writes to the filesystem —
> text files, CSV, JSON, and binary blobs. Day 09 covers `open()` with context
> managers, `pathlib.Path` for modern path handling, structured formats (CSV,
> JSON, JSONL), temp files, safe path validation, and binary mode. `code.py`
> demonstrates typed, validated helpers that never leak file handles.

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|-------------|----------------|---------------|---------------|
| 1 | `open()` | `open(p, "r", encoding="utf-8")` | Opens a file and returns a file object | Foundation of all file I/O | Every backend reads config / data files | `read_text_file` |
| 2 | `with` context manager | `with open(p) as f:` | Guarantees the file is closed even on error | Prevents handle leaks in long-running services | Standard in production code | `read_text_file` |
| 3 | Read methods | `.read()`, `.readline()`, `.readlines()` | Pull content from an open file | Different granularity for different workloads | `.read()` for small, iteration for large | `read_text_file` |
| 4 | Write methods | `.write()`, `.writelines()` | Push content to a file | Persist state, logs, exports | `.write()` for single, `.writelines()` for bulk | `write_lines` |
| 5 | File modes | `"r"`, `"w"`, `"a"`, `"x"`, `"r+"`, `"b"` | Control read/write/append/create/binary behavior | Wrong mode silently destroys data (`"w"` truncates) | `"x"` for safe-create, `"a"` for logs | snippet |
| 6 | Newline handling | `newline=""` | Prevents double newlines in CSV on Windows | Cross-platform CSV correctness | Always pass `newline=""` when using `csv` module | `write_csv` |
| 7 | Encoding parameter | `encoding="utf-8"` | Specifies character encoding | Platform defaults differ (Windows = cp1252) | Always explicit in production | all functions |
| 8 | `pathlib.Path` basics | `Path(p).exists()`, `.is_file()` | Object-oriented filesystem checks | Cleaner than `os.path.exists()` | Replacing legacy `os.path` across codebases | `read_text_file` |
| 9 | `pathlib` read/write | `.read_text()`, `.write_text()` | One-liner file I/O | Eliminates boilerplate open/close | Quick scripts and config files | snippet |
| 10 | `pathlib` navigation | `.parent`, `.name`, `.suffix`, `.glob()` | Explore directory structure | Navigate project trees programmatically | Build pipelines, asset discovery | snippet |
| 11 | `pathlib` construction | `/` operator, `.resolve()` | Build and normalize paths | No string concatenation bugs | Cross-platform path building | snippet |
| 12 | CSV reading | `csv.reader()`, `csv.DictReader()` | Parse comma-separated data into rows | Standard data interchange format | ETL ingestion, report parsing | `read_csv_records` |
| 13 | CSV writing | `csv.writer()`, `csv.DictWriter()` | Serialize rows to CSV | Standard data export | Report generation, data exports | `write_csv` |
| 14 | JSON reading | `json.load()`, `json.loads()` | Parse JSON from file or string | API configs, data exchange | Config files, REST payloads | `load_json_config` |
| 15 | JSON writing | `json.dump()`, `indent=` | Serialize data to JSON | Human-readable persistence | Config export, API responses | snippet |
| 16 | JSONL | One JSON object per line | Stream-friendly JSON | Append-friendly, line-by-line processing | Log aggregation, ML data pipelines | `csv_to_jsonl` |
| 17 | `tempfile` | `NamedTemporaryFile()`, `mkdtemp()` | Create temporary files/dirs safely | No name collisions, auto-cleanup | Test fixtures, staging areas | snippet |
| 18 | Safe paths | Validate extensions, reject traversal | Prevent path-traversal attacks | Security-critical for any user-supplied path | Upload handlers, CLI tools | `read_text_file` |
| 19 | Binary I/O | `"rb"`, `"wb"` | Read/write raw bytes | Images, protobuf, compressed data | Media processing, binary protocols | snippet |
| 20 | Anti-pattern: no `with` | `f = open(); f.read(); f.close()` | Manual close is fragile — exceptions skip it | Handle leak in production | Always use `with` | snippet |
| 21 | Anti-pattern: no encoding | `open(p)` without `encoding=` | Uses platform default, breaks cross-platform | Mojibake on Windows ↔ Linux | Always pass `encoding="utf-8"` | snippet |
| 22 | Industrial: CSV→JSONL ETL | Read CSV → transform → write JSONL | Full file pipeline pattern | Real-world data engineering | ETL scripts, data migration | `csv_to_jsonl` |

## Snippets

### 1. Opening and reading a text file

The `with` block guarantees the file is closed when the block exits.

```python
from pathlib import Path

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content[:50])
```

Expected output:
```text
(first 50 characters of data.txt)
```

> 💡 Always pass `encoding="utf-8"` — the platform default varies.

### 2. Writing and appending

`"w"` truncates; `"a"` appends; `"x"` fails if the file exists.

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("new entry\n")
```

Expected output:
```text
(line appended to log.txt)
```

> 💡 Use `"x"` mode when you need safe-create without overwriting.

### 3. `pathlib` one-liners

`Path.read_text()` and `.write_text()` handle open/close for you.

```python
from pathlib import Path

p = Path("greeting.txt")
p.write_text("Hello, pathlib!\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
```

Expected output:
```text
Hello, pathlib!
```

> 💡 `.read_text()` is ideal for small files; iterate line-by-line for large ones.

### 4. `pathlib` navigation and construction

Use `/` for path building — no string concatenation needed.

```python
from pathlib import Path

base = Path("/home/user/project")
config = base / "config" / "settings.json"
print(config.suffix)     # .json
print(config.parent)     # /home/user/project/config
print(config.name)       # settings.json
```

Expected output:
```text
.json
/home/user/project/config
settings.json
```

> 💡 `.resolve()` returns the absolute path with symlinks resolved.

### 5. CSV round-trip with `DictReader` / `DictWriter`

Always pass `newline=""` when opening files for `csv`.

```python
import csv

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})

with open("users.csv", "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row)
```

Expected output:
```text
{'name': 'Alice', 'age': '30'}
```

> 💡 CSV values are always strings — cast numerics explicitly.

### 6. JSON load and dump

`json.load()` reads from a file object; `json.loads()` reads from a string.

```python
import json

data = {"name": "Bob", "scores": [95, 87, 92]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["name"])
```

Expected output:
```text
Bob
```

> 💡 Use `indent=2` for human-readable output; omit it for compact wire format.

### 6.1 `json.load()` vs `json.loads()` — Key Differences

| Aspect | `json.load()` | `json.loads()` |
|--------|--------------|----------------|
| **Input** | A **file object** (or any `.read()`-supporting stream) | A **string** (or `bytes`) |
| **Typical source** | Files on disk | API responses, environment vars, literals |
| **Signature** | `json.load(fp)` | `json.loads(s)` |
| **Memory** | Reads from stream incrementally | Entire string must already be in memory |
| **Common mistake** | Passing a file *path* string → `TypeError` | Passing a file *object* → `TypeError` |

```python
import json

# --- json.load(): reads from a FILE OBJECT ---
with open("data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)          # f is a file object
print(data_from_file)

# --- json.loads(): reads from a STRING ---
json_string = '{"language": "Python", "version": 3.12}'
data_from_string = json.loads(json_string) # pass a str, not a file
print(data_from_string)
```

Expected output:
```text
{'name': 'Bob', 'scores': [95, 87, 92]}
{'language': 'Python', 'version': 3.12}
```

Similarly for writing:
- `json.dump(obj, fp)` — writes to a **file object**.
- `json.dumps(obj)` — returns a **string**.

> ⚠️ Mixing them up is a common bug:
> `json.loads(open("f.json"))` → `TypeError` (passed a file object, not a string).
> `json.load('{"a":1}')` → `AttributeError` (string has no `.read()` method).

### 7. JSONL — one JSON per line

JSONL is append-friendly and stream-parseable.

```python
import json

records = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}]
with open("data.jsonl", "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec) + "\n")
```

Expected output:
```text
(data.jsonl contains two lines, one JSON object each)
```

> 💡 JSONL is the standard for streaming logs and ML training data.

### 8. `tempfile` — safe temporary files

Temporary files avoid name collisions and can auto-delete.

```python
import tempfile
from pathlib import Path

with tempfile.NamedTemporaryFile(
    mode="w", suffix=".txt", delete=False, encoding="utf-8"
) as tmp:
    tmp.write("temp data\n")
    print(Path(tmp.name).name)
```

Expected output:
```text
tmpXXXXXXXX.txt  (random name)
```

> 💡 Use `delete=False` when you need the file to persist after the `with` block.

### 9. Binary I/O

Binary mode (`"rb"` / `"wb"`) skips encoding — you get raw `bytes`.

```python
data = bytes([0x89, 0x50, 0x4E, 0x47])  # PNG magic bytes
with open("header.bin", "wb") as f:
    f.write(data)

with open("header.bin", "rb") as f:
    magic = f.read(4)
print(magic)
```

Expected output:
```text
b'\x89PNG'
```

> 💡 Never open binary files in text mode — encoding will corrupt the data.

## Anti-patterns

### Anti-pattern: no `with` — handle leak
```python
# ❌ Bad — if an exception occurs, the file stays open
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()

# ✅ Corrected — guaranteed close on any exit
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```
> In long-running services, leaked handles accumulate until the OS refuses to open more files.

### Anti-pattern: no encoding — platform-dependent behavior
```python
# ❌ Bad — uses cp1252 on Windows, utf-8 on Linux
with open("data.txt") as f:
    text = f.read()

# ✅ Corrected — explicit encoding
with open("data.txt", encoding="utf-8") as f:
    text = f.read()
```
> Cross-platform bugs from encoding mismatches are extremely hard to debug.

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| CSV→JSONL ETL | Read CSV with `DictReader`, transform, write JSONL | Data migration, log normalization |
| Config loading | `json.load()` with schema validation | Application startup |
| Safe temp staging | `tempfile.mkdtemp()` + process + cleanup | Test fixtures, atomic writes |
| Path validation | Reject `..` segments, enforce allowlisted extensions | Any user-supplied file path |

## Pitfalls

- **`"w"` mode silently truncates** — existing data is gone. Use `"a"` to append or `"x"` for safe-create.
- **CSV values are always strings** — forgetting to cast `int(row["age"])` causes downstream type errors.
- **`json.load()` vs `json.loads()`** — one takes a file object, the other a string. Mixing them up raises `TypeError`.
- **`pathlib` `/` operator** — left operand must be a `Path`, not a plain string.
- **Large files with `.read()`** — loads the entire file into memory. Iterate line-by-line or use chunked reads for big files.

## Why this design

`code.py` wraps each I/O operation in a typed function with path validation,
explicit encoding, and context-managed handles. This pattern prevents the three
most common file I/O bugs: leaked handles, encoding mismatches, and silent
data truncation.

## Further reading

- [Python docs — open()](https://docs.python.org/3/library/functions.html#open) — canonical reference for modes and encoding
- [Python docs — pathlib](https://docs.python.org/3/library/pathlib.html) — full Path API reference
- [Python docs — csv](https://docs.python.org/3/library/csv.html) — reader, writer, dialects
- [Real Python — Read and Write Files](https://realpython.com/read-write-files-python/) — practical tutorial with examples
