# Day 08 — Strings and Encoding

> **TL;DR:** Strings are immutable sequences of Unicode characters. Python separates
> text (`str`) from raw bytes (`bytes`), requiring explicit encode/decode at I/O
> boundaries. `code.py` demonstrates search, transform, format, and encoding functions
> with typed signatures, validation, and industrial patterns like slugify and sanitize.

## Concepts

| # | Concept | Syntax / Example | What it does | Why it matters | Industrial use | `code.py` ref |
|---|---------|-----------------|-------------|----------------|---------------|---------------|
| 1 | String creation | `'hi'`, `"hi"`, `'''multi'''` | Creates str objects | Foundation of all text handling | Config values, messages | snippet 1 |
| 2 | Raw strings | `r"no\nescape"` | Backslashes kept literal | Regex patterns, Windows paths | `re.compile(r"\d+")` | snippet 1 |
| 3 | Indexing / negative | `s[0]`, `s[-1]` | Access single character | Random access into text | Parsing fixed-width fields | snippet 2 |
| 4 | Slicing | `s[1:5]`, `s[::-1]` | Extract substring | Substrings without copies of data | Log prefix extraction | snippet 2 |
| 5 | Immutability | Cannot `s[0] = 'x'` | Strings never change in-place | Thread-safe, hashable for dict keys | Cache keys, frozen configs | snippet 2 |
| 6 | `len()` | `len(s)` | Character count | Input validation, truncation | Max-length guards | `validate_and_search` |
| 7 | Case methods | `.upper()`, `.lower()`, `.casefold()` | Case conversion | Case-insensitive comparison | Normalizing user input | `transform_case` |
| 8 | Search methods | `.find()`, `.index()`, `.rfind()` | Locate substring | Parsing structured text | Log parsing, header extraction | `validate_and_search` |
| 9 | Boolean checks | `.startswith()`, `.isdigit()`, `.isalpha()` | Test string properties | Input validation guards | Form validation, token checks | `validate_and_search` |
| 10 | Strip | `.strip()`, `.lstrip()`, `.rstrip()` | Remove leading/trailing chars | Clean user input | Sanitizing form data | `sanitize_text` |
| 11 | Split / join | `.split(sep)`, `sep.join(iter)` | Break apart / reassemble | CSV-like parsing, path building | Log field extraction | snippet 4 |
| 12 | Replace | `.replace(old, new)` | Substitute substrings | Text cleanup, template filling | Slug generation | `slugify` |
| 13 | f-strings advanced | `f"{val:.2f}"`, `f"{x = }"` | Formatted interpolation | Readable, efficient formatting | Logging, reports | snippet 5 |
| 14 | Legacy formatting | `.format()`, `%` | Older interpolation | Reading legacy codebases | Maintaining old code | snippet 5 |
| 15 | Concatenation / repetition | `+`, `*` | Build new strings | Quick assembly | Banners, separators | snippet 3 |
| 16 | `in` substring check | `"sub" in s` | Membership test | O(n) but readable | Keyword filtering | `validate_and_search` |
| 17 | Character frequency | `Counter(s)` | Count occurrences | Text analysis | Anagram detection, analytics | `char_frequency` |
| 18 | `bytes` vs `str` | `.encode()`, `.decode()` | Text ↔ binary conversion | I/O boundary correctness | Network protocols, file I/O | `encode_decode_demo` |
| 19 | `bytearray` | `bytearray(b"hello")` | Mutable byte sequence | In-place binary edits | Protocol buffers, streaming | snippet 7 |
| 20 | Unicode normalization | `unicodedata.normalize()` | Canonical form | Consistent comparison across encodings | Internationalized search | snippet 8 |
| 21 | Regex preview | `re.search()`, `re.sub()` | Pattern matching | Complex text extraction | Email validation, parsing | snippet 8 |
| 22 | Multi-line / textwrap | `'''...'''`, `dedent()` | Multi-line strings | Templates, SQL, help text | CLI help, email bodies | snippet 6 |
| 23 | `translate()` / `maketrans()` | `s.translate(table)` | Character-level mapping | Fast bulk character replacement | Cipher, punctuation removal | `sanitize_text` |
| 24 | Anti-pattern: str + bytes | Always encode/decode | Mixing raises TypeError | Silent corruption in Python 2 legacy | Explicit I/O boundaries | snippet 9 |
| 25 | Industrial: slugify, sanitizer | Strip, lower, replace | URL-safe identifiers | SEO, APIs, filenames | Blog platforms, REST APIs | `slugify` |

## Snippets

### 1. String Creation and Raw Strings

Strings can be created with single, double, or triple quotes. Raw strings suppress escape processing.

```python
single = 'hello'
double = "world"
multi  = """line one
line two"""
raw    = r"C:\new\test"   # backslashes kept literal

print(single, double)
print(repr(raw))
```

Expected output:
```text
hello world
'C:\\new\\test'
```

> 💡 Use raw strings for regex patterns and Windows paths to avoid accidental escapes.

### 2. Indexing, Slicing, and Immutability

Strings support zero-based indexing and slicing but cannot be mutated in place.

```python
s = "Python"
print(s[0], s[-1])       # first, last
print(s[1:4], s[::-1])   # slice, reverse

try:
    s[0] = "J"
except TypeError as exc:
    print(f"Immutable: {exc}")
```

Expected output:
```text
P n
yth nohtyP
Immutable: 'str' object does not support item assignment
```

> 💡 Slicing always returns a new string — the original is never modified.

### 3. Concatenation, Repetition, and Membership

The `+` operator joins strings, `*` repeats, and `in` tests substrings.

```python
greeting = "Hello" + ", " + "World"
banner   = "=-" * 20
print(greeting)
print(banner)
print("World" in greeting)   # True
print("xyz"  in greeting)    # False
```

Expected output:
```text
Hello, World
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
True
False
```

> 💡 Avoid `+=` in tight loops — use `"".join(parts)` for O(n) instead of O(n²).

### 4. Split, Join, and Strip

`.split()` breaks a string into a list; `sep.join()` reassembles. `.strip()` removes whitespace.

```python
csv_line = "  alice, bob , charlie  "
names = [n.strip() for n in csv_line.strip().split(",")]
print(names)
print(" | ".join(names))
```

Expected output:
```text
['alice', 'bob', 'charlie']
alice | bob | charlie
```

> 💡 Always `.strip()` user input before processing — invisible whitespace causes subtle bugs.

### 5. f-strings and Legacy Formatting

f-strings (3.6+) are the preferred way to embed expressions. Older code uses `.format()` or `%`.

```python
name, score = "Alice", 95.678
print(f"{name}: {score:.1f}")       # f-string with format spec
print(f"{len(name) = }")            # debug format (3.8+)
print("{}: {:.1f}".format(name, score))  # .format()
print("%s: %.1f" % (name, score))        # %-style
```

Expected output:
```text
Alice: 95.7
len(name) = 5
Alice: 95.7
Alice: 95.7
```

> 💡 Prefer f-strings for new code — they're faster and more readable than `.format()`.

### 6. Multi-line Strings and textwrap.dedent

Triple-quoted strings preserve indentation. `textwrap.dedent()` strips common leading whitespace.

```python
from textwrap import dedent

sql = dedent("""\
    SELECT name, score
    FROM   students
    WHERE  score > 90
""")
print(sql)
```

Expected output:
```text
SELECT name, score
FROM   students
WHERE  score > 90

```

> 💡 Use `dedent()` for embedded SQL, HTML, or help text to keep code indentation clean.

### 7. bytes, bytearray, and Encoding

`str.encode()` converts text to bytes; `bytes.decode()` reverses it. `bytearray` is mutable.

```python
text = "café"
encoded = text.encode("utf-8")
print(encoded, len(encoded))   # 5 bytes (é = 2 bytes in UTF-8)

ba = bytearray(b"hello")
ba[0:5] = b"HELLO"
print(ba.decode("ascii"))
```

Expected output:
```text
b'caf\xc3\xa9' 5
HELLO
```

> 💡 Always specify encoding explicitly — the platform default is not guaranteed to be UTF-8.

### 8. Unicode Normalization and Regex Preview

`unicodedata.normalize()` ensures consistent Unicode forms. `re` provides pattern matching.

```python
import unicodedata, re

# NFC vs NFD: same visual, different bytes
s1 = "café"                          # composed (NFC)
s2 = "cafe\u0301"                    # decomposed (NFD)
print(s1 == s2)                      # False
print(unicodedata.normalize("NFC", s2) == s1)  # True

# Regex: extract digits
print(re.findall(r"\d+", "order-42-item-7"))
```

Expected output:
```text
False
True
['42', '7']
```

> 💡 Normalize Unicode **before** comparing or storing user-supplied text.

### 9. Anti-pattern: Mixing str and bytes

Concatenating `str` with `bytes` raises `TypeError`. Always encode/decode at I/O boundaries.

```python
# ❌ Bad — mixing types
try:
    result = "hello" + b" world"
except TypeError as exc:
    print(f"Error: {exc}")

# ✅ Corrected — decode bytes first
raw = b" world"
result = "hello" + raw.decode("utf-8")
print(result)
```

Expected output:
```text
Error: can only concatenate str (not "bytes") to str
hello world
```

> Why it's wrong: Python 3 enforces the str/bytes boundary. Mixing silently corrupted data in Python 2; now it fails loudly — always decode at the I/O edge.

## Anti-patterns

### Anti-pattern: Loop concatenation

```python
# ❌ Bad — O(n²) string building
result = ""
for word in ["hello", "world", "foo"]:
    result += word + " "

# ✅ Corrected — O(n) with join
result = " ".join(["hello", "world", "foo"])
```

> Each `+=` creates a new string object. `str.join()` pre-allocates once.

### Anti-pattern: Comparing without normalization

```python
# ❌ Bad — visual match but fails
user_input = "cafe\u0301"
if user_input == "café":
    print("match")  # never reached

# ✅ Corrected — normalize first
import unicodedata
if unicodedata.normalize("NFC", user_input) == "café":
    print("match")  # works
```

> Different Unicode representations look identical but compare as unequal.

## Industrial Practices

| Practice | Example | When to use |
|----------|---------|-------------|
| Slugify | `re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")` | URL paths, filenames |
| Input sanitization | `strip() + translate(maketrans)` to remove control chars | User-facing forms, APIs |
| Encoding sandwich | Decode at input → process as `str` → encode at output | Network I/O, file pipelines |
| `casefold()` comparison | `s1.casefold() == s2.casefold()` | Locale-safe case-insensitive match |

## Pitfalls

- **`s.find()` returns -1 on miss** — use `in` for boolean checks or `.index()` if you want an exception.
- **`len("café")` is 4 characters but 5 UTF-8 bytes** — be careful when slicing binary data.
- **`.split()` with no args splits on any whitespace and strips empties**, but `.split(" ")` keeps them.
- **`str.replace()` replaces all occurrences** — there is no "replace first" without a count arg.
- **Triple-quoted strings capture indentation** — use `textwrap.dedent()` to clean up.

## Why this design

`code.py` groups functions by responsibility: validation/search, case transforms, frequency
analysis, encoding, and industrial patterns (slugify, sanitize). Each function validates
input, uses typed signatures, and returns explicit results rather than printing.

## Further reading

- [Python docs — str type](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) — authoritative method reference
- [Real Python — Strings](https://realpython.com/python-strings/) — comprehensive tutorial with examples
- [Python docs — re module](https://docs.python.org/3/library/re.html) — regex patterns and substitution
- [Python docs — unicodedata](https://docs.python.org/3/library/unicodedata.html) — Unicode character database and normalization
