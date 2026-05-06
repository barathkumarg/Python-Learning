# ex02_intermediate.py — Day 09: File I/O — Intermediate

"""
Intermediate exercises for File I/O.
Covers checklist items: #6, #10–#15.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex02_intermediate.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


def read_csv_as_dicts(
    path: str | Path, *, encoding: str = "utf-8"
) -> list[dict[str, str]]:
    """Read a CSV file and return rows as a list of dicts.

    Uses `csv.DictReader` (concept #12). Opens with `newline=""` (concept #6).

    Args:
        path: Path to the CSV file.
        encoding: Character encoding (default utf-8).

    Returns:
        List of dicts keyed by header names.

    Raises:
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> read_csv_as_dicts("users.csv")
        [{'name': 'Alice', 'age': '30'}]
    """
    # TODO: Implement this function
    # 1. Open with newline="" and encoding
    # 2. Use csv.DictReader
    # 3. Return list(reader)
    if not path:
        raise FileNotFoundError("Path not found")
    with open(path, 'r', encoding=encoding) as f:
        data = csv.DictReader(f)
        return list(data)
            



def write_csv_file(
    path: str | Path,
    rows: list[dict[str, object]],
    fieldnames: list[str],
    *,
    encoding: str = "utf-8",
) -> int:
    """Write a list of dicts to a CSV file with headers.

    Uses `csv.DictWriter` (concept #13). Opens with `newline=""` (concept #6).

    Args:
        path: Destination CSV file path.
        rows: Data rows as dicts.
        fieldnames: Column header names.
        encoding: Character encoding (default utf-8).

    Returns:
        Number of data rows written.

    Raises:
        ValueError: If rows is empty or fieldnames is empty.

    Examples:
        >>> write_csv_file("out.csv", [{"name": "Alice"}], ["name"])
        1
    """
    # TODO: Implement this function
    # 1. Validate rows and fieldnames non-empty
    # 2. Open with "w", newline="", encoding
    # 3. Create DictWriter, writeheader, writerows
    # 4. Return len(rows)
    if not path:
        raise FileNotFoundError("Path not found")
    with open (path, 'w', encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        return len(rows)
    


def load_json(path: str | Path, *, encoding: str = "utf-8") -> dict:
    """Load a JSON file and return the parsed dict.

    Uses `json.load()` (concept #14).

    Args:
        path: Path to the JSON file.
        encoding: Character encoding (default utf-8).

    Returns:
        Parsed JSON as a dict.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.

    Examples:
        >>> load_json("config.json")
        {'debug': True}
    """
    # TODO: Implement this function
    # 1. Validate file exists
    # 2. Open with encoding, json.load(f)
    if not path:
        raise FileNotFoundError("Path not found")
    with open (path, 'r', encoding=encoding) as f:
        return json.load(f)


def save_json(
    path: str | Path,
    data: dict,
    *,
    indent: int = 2,
    encoding: str = "utf-8",
) -> None:
    """Save a dict to a JSON file with specified indentation.

    Uses `json.dump()` with `indent` (concept #15).

    Args:
        path: Destination JSON file path.
        data: Dict to serialize.
        indent: Indentation level (default 2).
        encoding: Character encoding (default utf-8).

    Raises:
        ValueError: If data is not a dict.

    Examples:
        >>> save_json("out.json", {"key": "value"})
    """
    # TODO: Implement this function
    # 1. Validate data is a dict
    # 2. Open with "w" and encoding
    # 3. json.dump(data, f, indent=indent)
    if not path:
        raise FileNotFoundError("Path not found")
    with open (path, 'w', encoding=encoding) as f:
        json.dump(data, f, indent=indent )
        return None


def build_output_path(
    base_dir: str | Path, name: str, extension: str
) -> Path:
    """Construct an output file path using pathlib `/` operator.

    Uses pathlib construction (concept #11).

    Args:
        base_dir: Base directory.
        name: File name without extension.
        extension: File extension including dot (e.g. ".csv").

    Returns:
        Constructed Path object.

    Raises:
        ValueError: If name is empty or extension doesn't start with '.'.

    Examples:
        >>> build_output_path("/tmp", "report", ".csv")
        PosixPath('/tmp/report.csv')
    """
    # TODO: Implement this function
    # 1. Validate name non-empty and extension starts with '.'
    # 2. Return Path(base_dir) / (name + extension)
    base = Path(base_dir)
    config = base / (name + extension)
    return config 

def list_by_extension(
    directory: str | Path, ext: str
) -> list[str]:
    """List filenames in a directory matching a given extension.

    Uses `pathlib` `.glob()` and navigation (concept #10).

    Args:
        directory: Directory to search.
        ext: Extension to match (e.g. ".txt").

    Returns:
        Sorted list of matching filenames (names only, not full paths).

    Raises:
        ValueError: If ext doesn't start with '.'.
        FileNotFoundError: If directory doesn't exist.

    Examples:
        >>> list_by_extension("/data", ".csv")
        ['report.csv', 'users.csv']
    """
    # TODO: Implement this function
    # 1. Validate ext starts with '.'
    # 2. Path(directory).glob(f"*{ext}")
    # 3. Return sorted list of .name for each match
    # 1. Validate extension format
    if not ext.startswith('.'):
        raise ValueError(f"Extension '{ext}' must start with a dot (e.g., '.txt')")

    path_obj = Path(directory)

    # 2. Validate directory existence
    if not path_obj.is_dir():
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    # 3. Use glob to find matches, extract the .name, and sort the result
    # We use f"*{ext}" to match any file ending with that extension
    matches = [file.name for file in path_obj.glob(f"*{ext}")]
    
    return sorted(matches)


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)

        # ─── write_csv_file / read_csv_as_dicts checks ───
        csv_path = base / "test.csv"
        rows = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
        assert write_csv_file(csv_path, rows, ["name", "age"]) == 2, "wrote 2 rows"

        loaded = read_csv_as_dicts(csv_path)
        assert len(loaded) == 2, "read 2 rows"
        assert loaded[0]["name"] == "Alice", "first name"
        assert loaded[1]["age"] == "25", "second age"

        # ─── save_json / load_json checks ───
        json_path = base / "config.json"
        save_json(json_path, {"debug": True, "port": 8080})
        cfg = load_json(json_path)
        assert cfg["debug"] is True, "debug flag"
        assert cfg["port"] == 8080, "port number"

        # ─── build_output_path checks ───
        out = build_output_path(base, "report", ".csv")
        assert out == base / "report.csv", "path construction"
        assert out.suffix == ".csv", "suffix matches"

        # ─── list_by_extension checks ───
        (base / "a.txt").write_text("x", encoding="utf-8")
        (base / "b.txt").write_text("y", encoding="utf-8")
        (base / "c.csv").write_text("z", encoding="utf-8")
        txt_files = list_by_extension(base, ".txt")
        assert txt_files == ["a.txt", "b.txt"], "two txt files sorted"

    print("ex02_intermediate.py: all asserts passed ✓")
