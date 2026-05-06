# code.py — Day 09: File I/O

"""
File I/O — production-style reference implementations.

Covers: open(), with, read/write methods, file modes, encoding, pathlib,
CSV (reader/writer/DictReader/DictWriter), JSON (load/dump), JSONL,
tempfile, safe path validation, binary I/O.

Style: typed signatures, Google docstrings, explicit validation,
context-managed handles, no leaked resources.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

_ALLOWED_EXTENSIONS: frozenset[str] = frozenset({".txt", ".csv", ".json", ".jsonl", ".md"})


# ─── Section 1: Text File Reading ───


def read_text_file(path: str | Path, *, encoding: str = "utf-8") -> str:
    """Read an entire text file and return its contents.

    Validates the path exists, is a file, and has an allowed extension.

    Args:
        path: Filesystem path to read.
        encoding: Character encoding (default utf-8).

    Returns:
        The full file content as a string.

    Raises:
        ValueError: If path is empty, has a disallowed extension, or contains '..'.
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> read_text_file("sample.txt")
        'Hello, world!\\n'
    """
    p = Path(path)
    if not str(path).strip():
        raise ValueError("path must not be empty")
    if ".." in p.parts:
        raise ValueError(f"path traversal not allowed, got {path!r}")
    if p.suffix.lower() not in _ALLOWED_EXTENSIONS:
        raise ValueError(
            f"extension {p.suffix!r} not allowed, "
            f"expected one of {sorted(_ALLOWED_EXTENSIONS)}"
        )
    if not p.is_file():
        raise FileNotFoundError(f"no such file: {path!r}")
    with open(p, "r", encoding=encoding) as f:
        return f.read()


# ─── Section 2: Text File Writing ───


def write_lines(
    path: str | Path,
    lines: list[str],
    *,
    mode: str = "w",
    encoding: str = "utf-8",
) -> int:
    """Write a list of strings to a file, one per line.

    Args:
        path: Destination file path.
        lines: Strings to write (newlines appended automatically).
        mode: File mode — 'w' (overwrite) or 'a' (append).
        encoding: Character encoding (default utf-8).

    Returns:
        Number of lines written.

    Raises:
        ValueError: If lines is empty or mode is not 'w' or 'a'.

    Examples:
        >>> write_lines("out.txt", ["alpha", "bravo"])
        2
    """
    if not lines:
        raise ValueError("lines must not be empty")
    if mode not in ("w", "a"):
        raise ValueError(f"mode must be 'w' or 'a', got {mode!r}")
    with open(path, mode, encoding=encoding) as f:
        for line in lines:
            f.write(line + "\n")
    return len(lines)


# ─── Section 3: CSV ───


def read_csv_records(
    path: str | Path,
    *,
    encoding: str = "utf-8",
) -> list[dict[str, str]]:
    """Read a CSV file with headers and return a list of row dicts.

    Args:
        path: Path to the CSV file.
        encoding: Character encoding (default utf-8).

    Returns:
        List of dicts, one per data row, keyed by header names.

    Raises:
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> read_csv_records("users.csv")
        [{'name': 'Alice', 'age': '30'}]
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"no such file: {path!r}")
    with open(p, "r", newline="", encoding=encoding) as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(
    path: str | Path,
    rows: list[dict[str, object]],
    *,
    fieldnames: list[str] | None = None,
    encoding: str = "utf-8",
) -> int:
    """Write a list of dicts to a CSV file with headers.

    Args:
        path: Destination CSV path.
        rows: List of dicts to write.
        fieldnames: Column names. Inferred from first row if None.
        encoding: Character encoding (default utf-8).

    Returns:
        Number of data rows written.

    Raises:
        ValueError: If rows is empty.

    Examples:
        >>> write_csv("out.csv", [{"name": "Alice", "age": 30}])
        1
    """
    if not rows:
        raise ValueError("rows must not be empty")
    headers = fieldnames or list(rows[0].keys())
    with open(path, "w", newline="", encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


# ─── Section 4: JSON & JSONL ───


def load_json_config(path: str | Path, *, encoding: str = "utf-8") -> dict:
    """Load a JSON file and return the parsed dict.

    Args:
        path: Path to the JSON file.
        encoding: Character encoding (default utf-8).

    Returns:
        Parsed JSON as a dict.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.

    Examples:
        >>> load_json_config("config.json")
        {'debug': True, 'port': 8080}
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"no such file: {path!r}")
    with open(p, "r", encoding=encoding) as f:
        return json.load(f)


# ─── Section 5: Industrial — CSV→JSONL ETL ───


def csv_to_jsonl(
    csv_path: str | Path,
    jsonl_path: str | Path,
    *,
    encoding: str = "utf-8",
) -> int:
    """Convert a CSV file to JSONL format (one JSON object per line).

    Args:
        csv_path: Source CSV file with headers.
        jsonl_path: Destination JSONL file.
        encoding: Character encoding (default utf-8).

    Returns:
        Number of records written.

    Raises:
        FileNotFoundError: If the CSV file does not exist.

    Examples:
        >>> csv_to_jsonl("users.csv", "users.jsonl")
        2
    """
    csv_p = Path(csv_path)
    if not csv_p.is_file():
        raise FileNotFoundError(f"no such file: {csv_path!r}")
    count = 0
    with open(csv_p, "r", newline="", encoding=encoding) as fin:
        reader = csv.DictReader(fin)
        with open(jsonl_path, "w", encoding=encoding) as fout:
            for row in reader:
                fout.write(json.dumps(row) + "\n")
                count += 1
    return count


# ─── Self-checks ───

if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)

        # --- write_lines ---
        txt_path = base / "demo.txt"
        n = write_lines(str(txt_path), ["alpha", "bravo", "charlie"])
        print(f"write_lines wrote {n} lines")
        # Expected output: write_lines wrote 3 lines

        # --- read_text_file ---
        content = read_text_file(str(txt_path))
        print(f"read_text_file got {content.count(chr(10))} lines")
        # Expected output: read_text_file got 3 lines

        # --- write_csv / read_csv_records ---
        csv_path = base / "users.csv"
        write_csv(
            str(csv_path),
            [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}],
        )
        records = read_csv_records(str(csv_path))
        print(f"CSV round-trip: {len(records)} records, first name={records[0]['name']}")
        # Expected output: CSV round-trip: 2 records, first name=Alice

        # --- load_json_config ---
        json_path = base / "config.json"
        json_path.write_text(
            json.dumps({"debug": True, "port": 8080}), encoding="utf-8"
        )
        cfg = load_json_config(str(json_path))
        print(f"JSON config: port={cfg['port']}")
        # Expected output: JSON config: port=8080

        # --- csv_to_jsonl ---
        jsonl_path = base / "users.jsonl"
        count = csv_to_jsonl(str(csv_path), str(jsonl_path))
        print(f"csv_to_jsonl converted {count} records")
        # Expected output: csv_to_jsonl converted 2 records

        jsonl_text = jsonl_path.read_text(encoding="utf-8").strip().split("\n")
        first_rec = json.loads(jsonl_text[0])
        print(f"JSONL first record name={first_rec['name']}")
        # Expected output: JSONL first record name=Alice

    print("code.py: all demos passed ✓")
