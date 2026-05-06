# ex03_advanced.py — Day 09: File I/O — Advanced

"""
Advanced exercises for File I/O.
Covers checklist items: #16–#19, #22.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex03_advanced.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations

import json
import csv
import tempfile
from pathlib import Path

_DEFAULT_ALLOWED: frozenset[str] = frozenset({".txt", ".csv", ".json", ".jsonl", ".md"})


def write_jsonl(
    path: str | Path,
    records: list[dict[str, object]],
    *,
    encoding: str = "utf-8",
) -> int:
    """Write a list of dicts as JSONL (one JSON object per line).

    Concept #16 — JSONL format is append-friendly and stream-parseable.

    Args:
        path: Destination JSONL file path.
        records: List of dicts to serialize.
        encoding: Character encoding (default utf-8).

    Returns:
        Number of records written.

    Raises:
        ValueError: If records is empty.

    Examples:
        >>> write_jsonl("data.jsonl", [{"id": 1}, {"id": 2}])
        2
    """
    # TODO: Implement this function
    # 1. Validate records non-empty
    # 2. Open with "w" and encoding
    # 3. For each record: f.write(json.dumps(rec) + "\n")
    # 4. Return count
    with open(path, 'w', encoding=encoding) as f:
        f.write(json.dumps(records) + "\n")
    return len(records)

def read_jsonl(
    path: str | Path, *, encoding: str = "utf-8"
) -> list[dict[str, object]]:
    """Read a JSONL file and return a list of dicts.

    Each line is one JSON object (concept #16).

    Args:
        path: Path to the JSONL file.
        encoding: Character encoding (default utf-8).

    Returns:
        List of parsed dicts.

    Raises:
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> read_jsonl("data.jsonl")
        [{'id': 1}, {'id': 2}]
    """
    # TODO: Implement this function
    # 1. Open with encoding
    # 2. For each non-empty line: json.loads(line)
    # 3. Return list of dicts
    with open(path, 'r', encoding=encoding) as f:
        content = json.load(f)
        return list(content)


def validate_path(
    path: str | Path,
    allowed_extensions: frozenset[str] | None = None,
) -> bool:
    """Validate that a file path is safe (no traversal, allowed extension).

    Concept #18 — reject paths containing '..' and enforce extension allowlist.

    Args:
        path: Path to validate.
        allowed_extensions: Set of allowed extensions (e.g. {".txt", ".csv"}).
            Uses default allowlist if None.

    Returns:
        True if the path is safe.

    Raises:
        ValueError: If path contains '..', has a disallowed extension, or is empty.

    Examples:
        >>> validate_path("data.csv")
        True
        >>> validate_path("../../etc/passwd")  # raises ValueError
    """
    # TODO: Implement this function
    # 1. Validate path non-empty
    # 2. Check for ".." in Path(path).parts
    # 3. Check suffix against allowed_extensions (or _DEFAULT_ALLOWED)
    # 4. Return True if valid
    if not path:
        raise ValueError("Path not found")
    p = Path(path)
    if ".." in p.parts:
        raise ValueError("Not a valid input")
    allowlist = allowed_extensions if allowed_extensions is not None else _DEFAULT_ALLOWED
    if p.suffix not in allowlist:
        raise ValueError(
            f"Extension {p.suffix!r} is not allowed. Allowed: {allowlist}"
        )

    return True



def copy_binary(src: str | Path, dst: str | Path) -> int:
    """Copy a binary file from src to dst using 'rb'/'wb' modes.

    Concept #19 — binary I/O skips encoding; reads/writes raw bytes.

    Args:
        src: Source file path.
        dst: Destination file path.

    Returns:
        Number of bytes copied.

    Raises:
        FileNotFoundError: If src does not exist.

    Examples:
        >>> copy_binary("image.png", "copy.png")
        1024
    """
    # TODO: Implement this function
    # 1. Open src with "rb", read all bytes
    # 2. Open dst with "wb", write all bytes
    # 3. Return len(data)
    if not src or not dst:
        raise FileNotFoundError("No file path exists")
    with open(src, "rb") as rf:
        data = rf.read()
    with open(dst, "wb") as wf:
        wf.write(data)
    return len(data)
    


def process_in_temp(lines: list[str]) -> str:
    """Write lines to a temp file, read them back, return content.

    Concept #17 — uses `tempfile.NamedTemporaryFile` for safe temp I/O.

    Args:
        lines: Lines to write.

    Returns:
        Content read back from the temp file.

    Raises:
        ValueError: If lines is empty.

    Examples:
        >>> process_in_temp(["hello", "world"])
        'hello\\nworld\\n'
    """
    # TODO: Implement this function
    # 1. Validate lines non-empty
    # 2. Create NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8")
    # 3. Write each line + "\n"
    # 4. Close, then read back with Path(tmp.name).read_text()
    # 5. Clean up with Path(tmp.name).unlink()
    # 6. Return content
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as tmp:
        tmp_path = Path(tmp.name)
        for line in lines:
            tmp.write(line + '\n')

    content = tmp_path.read_text(encoding="utf-8")
    tmp_path.unlink()
    return content
    


    


def csv_to_jsonl(
    csv_path: str | Path,
    jsonl_path: str | Path,
    *,
    encoding: str = "utf-8",
) -> int:
    """Convert a CSV file to JSONL format — full ETL pipeline.

    Concept #22 — industrial CSV→JSONL pattern: read with DictReader,
    write one JSON object per line.

    Args:
        csv_path: Source CSV file with headers.
        jsonl_path: Destination JSONL file.
        encoding: Character encoding (default utf-8).

    Returns:
        Number of records converted.

    Raises:
        FileNotFoundError: If csv_path does not exist.
        ValueError: If CSV file is empty (no data rows).

    Examples:
        >>> csv_to_jsonl("users.csv", "users.jsonl")
        2
    """
    # TODO: Implement this function
    # 1. Validate csv_path exists
    # 2. Open CSV with newline="" and DictReader
    # 3. Open JSONL for writing
    # 4. For each row: write json.dumps(row) + "\n"
    # 5. Return count (raise ValueError if 0)
    if not csv_path:
        raise FileNotFoundError("File not found")
    count = 0
    with open(csv_path, "r", newline= "", encoding=encoding) as csv_file:
       
        with open(jsonl_path, "w", encoding=encoding) as json_file:
            for row in csv.DictReader(csv_file):
                json_file.write(json.dumps(row)+ '\n')
                count +=1
    if count == 0:
        raise ValueError("csv file empty")
    return count



if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)

        # ─── write_jsonl / read_jsonl checks ───
        jl = base / "data.jsonl"
        assert write_jsonl(jl, [{"id": 1}, {"id": 2}, {"id": 3}]) == 3, "wrote 3 records"
        records = read_jsonl(jl)
        assert len(records) == 3, "read 3 records"
        assert records[0]["id"] == 1, "first id"

        # ─── validate_path checks ───
        assert validate_path("report.csv") is True, "valid csv"
        assert validate_path("data.txt") is True, "valid txt"
        try:
            validate_path("../../etc/passwd")
            assert False, "should have raised ValueError"
        except ValueError:
            pass
        try:
            validate_path("script.exe")
            assert False, "should have raised ValueError for .exe"
        except ValueError:
            pass

        # ─── copy_binary checks ───
        src_bin = base / "source.bin"
        src_bin.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 100)
        dst_bin = base / "copy.bin"
        nbytes = copy_binary(src_bin, dst_bin)
        assert nbytes == 108, "copied 108 bytes"
        assert src_bin.read_bytes() == dst_bin.read_bytes(), "binary identical"

        # ─── process_in_temp checks ───
        result = process_in_temp(["hello", "world"])
        assert result == "hello\nworld\n", "temp round-trip"

        # ─── csv_to_jsonl checks ───
        csv_p = base / "users.csv"
        csv_p.write_text("name,age\nAlice,30\nBob,25\n", encoding="utf-8")
        jsonl_p = base / "users.jsonl"
        count = csv_to_jsonl(csv_p, jsonl_p)
        assert count == 2, "converted 2 records"
        

    print("ex03_advanced.py: all asserts passed ✓")
