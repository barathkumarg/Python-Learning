# ex01_basic.py — Day 09: File I/O — Basic

"""
Basic exercises for File I/O.
Covers checklist items: #1–#5, #7–#9, #20–#21.

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex01_basic.py
- All asserts must pass before moving to the next exercise.
"""

from __future__ import annotations

from pathlib import Path


def read_file_content(path: str | Path, *, encoding: str = "utf-8") -> str:
    """Read and return the entire content of a text file.

    Must use a `with` block and pass `encoding` explicitly (concepts #1, #2, #7).
    Anti-patterns #20 and #21: never open without `with` or without encoding.

    Args:
        path: Path to the text file.
        encoding: Character encoding (default utf-8).

    Returns:
        Full file content as a string.

    Raises:
        ValueError: If path is empty.
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> read_file_content("hello.txt")
        'Hello, world!\\n'
    """
    # TODO: Implement this function
    # 1. Validate path is non-empty
    # 2. Use `with open(path, "r", encoding=encoding) as f:`
    # 3. Return f.read()
    if not path:
        raise FileNotFoundError("Path not found") 
    with open (path, 'r', encoding=encoding) as f:
        return f.read()


def count_lines(path: str | Path, *, encoding: str = "utf-8") -> int:
    """Count the number of lines in a text file.

    Uses the read method `.readlines()` (concept #3).

    Args:
        path: Path to the text file.
        encoding: Character encoding (default utf-8).

    Returns:
        Number of lines (including empty lines).

    Raises:
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> count_lines("three_lines.txt")
        3
    """
    # TODO: Implement this function
    # 1. Open with `with` and encoding
    # 2. Use .readlines() and return len()
    if not path:
        raise FileNotFoundError("Path not found")
    with open (path, 'r', encoding=encoding) as f:
        lines = f.readlines()
        return (len(lines))


def write_lines(
    path: str | Path, lines: list[str], *, encoding: str = "utf-8"
) -> int:
    """Write a list of strings to a file, one per line.

    Uses write mode `"w"` (concept #4, #5).

    Args:
        path: Destination file path.
        lines: Strings to write (newlines appended automatically).
        encoding: Character encoding (default utf-8).

    Returns:
        Number of lines written.

    Raises:
        ValueError: If lines is empty.

    Examples:
        >>> write_lines("out.txt", ["alpha", "bravo"])
        2
    """
    # TODO: Implement this function
    # 1. Validate lines is non-empty
    # 2. Open with "w" mode and encoding
    # 3. Write each line + "\n"
    # 4. Return len(lines)
    if not path:
        raise FileNotFoundError("Path not found")
    with open (path, 'w', encoding=encoding) as f:
        for line in lines:
            f.write(line + '\n')
        return len(lines)
        
    


def append_line(
    path: str | Path, line: str, *, encoding: str = "utf-8"
) -> None:
    """Append a single line to an existing file.

    Uses append mode `"a"` (concept #5).

    Args:
        path: File to append to.
        line: Text to append (newline appended automatically).
        encoding: Character encoding (default utf-8).

    Raises:
        ValueError: If line is empty after stripping.

    Examples:
        >>> append_line("log.txt", "new entry")
    """
    # TODO: Implement this function
    # 1. Validate line is non-empty after strip
    # 2. Open with "a" mode and encoding
    # 3. Write line + "\n"
    if not path:
        raise FileNotFoundError("Path not found")
    with open (path, 'a', encoding=encoding) as f:
       f.write(line + '\n')
    


def file_info(path: str | Path) -> dict[str, object]:
    """Return basic information about a file path using pathlib.

    Uses `pathlib.Path` properties (concept #8).

    Args:
        path: Filesystem path.

    Returns:
        Dict with keys: 'name' (str), 'suffix' (str), 'exists' (bool),
        'size' (int or 0 if not exists).

    Examples:
        >>> file_info("hello.txt")
        {'name': 'hello.txt', 'suffix': '.txt', 'exists': True, 'size': 14}
    """
    # TODO: Implement this function
    # 1. Create Path object
    # 2. Return dict with .name, .suffix, .exists(), .stat().st_size (or 0)
    if not path:
        raise FileNotFoundError("Path not found")
    base = Path(path)
    return {
         "name": base.name,
         "suffix": base.suffix,
         "exists": base.exists(),
         "size": base.stat().st_size
    }


def pathlib_read_write(
    path: str | Path, content: str, *, encoding: str = "utf-8"
) -> str:
    """Write content and read it back using pathlib one-liners.

    Uses `.write_text()` and `.read_text()` (concept #9).

    Args:
        path: File path.
        content: Text to write.
        encoding: Character encoding (default utf-8).

    Returns:
        The content read back from the file.

    Raises:
        ValueError: If content is empty.

    Examples:
        >>> pathlib_read_write("demo.txt", "hello pathlib")
        'hello pathlib'
    """
    # TODO: Implement this function
    # 1. Validate content non-empty
    # 2. Path(path).write_text(content, encoding=encoding)
    # 3. Return Path(path).read_text(encoding=encoding)
    if not path:
        raise FileNotFoundError("Path not found")
    p = Path(path)
    p.write_text(content, encoding=encoding)
    return Path(path).read_text(encoding=encoding)
    
    


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)

        # ─── write_lines checks ───
        txt = base / "test.txt"
        assert write_lines(txt, ["alpha", "bravo", "charlie"]) == 3, "wrote 3 lines"

        # ─── read_file_content checks ───
        content = read_file_content(txt)
        assert "alpha" in content, "content contains alpha"
        assert content.count("\n") == 3, "3 newlines"

        # ─── count_lines checks ───
        assert count_lines(txt) == 3, "3 lines"

        # ─── append_line checks ───
        append_line(txt, "delta")
        assert count_lines(txt) == 4, "4 lines after append"

        # ─── file_info checks ───
        info = file_info(txt)
        assert info["name"] == "test.txt", "name matches"
        assert info["suffix"] == ".txt", "suffix matches"
        assert info["exists"] is True, "file exists"
        assert isinstance(info["size"], int) and info["size"] > 0, "size > 0"

        # ─── pathlib_read_write checks ───
        p2 = base / "pathlib_demo.txt"
        result = pathlib_read_write(p2, "hello pathlib")
        assert result == "hello pathlib", "round-trip matches"

    print("ex01_basic.py: all asserts passed ✓")
