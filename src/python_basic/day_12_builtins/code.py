# code.py — Day 12: Built-ins in Pipelines

"""Built-ins in Pipelines — production-style reference implementations.

Covers concepts #1–#22: enumerate, zip / zip(strict=True), sorted, reversed,
map, filter, any, all, sum, min/max with default, abs/round/divmod, len/range,
isinstance, type/id/hash, print(sep=, end=), iter/next, callable, the
comprehension-vs-map trade-off, chained pipelines, the ``list(map(lambda …))``
anti-pattern, and a full ``parse → map → filter → aggregate`` data pipeline.

Style: typed signatures, Google docstrings, explicit validation, lazy
iterators in the middle of the pipeline and materialization only at the edge.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from typing import Any


# ─── Section 1: Iteration helpers (concepts #1, #2, #3) ───


def enumerate_rows(rows: list[str], *, start: int = 1) -> list[str]:
    """Number each row using :func:`enumerate` (concept #1).

    Args:
        rows: Lines/records to number.
        start: First index to use (defaults to 1 for human-readable reports).

    Returns:
        ``["{i}. {row}", ...]`` strings.

    Raises:
        ValueError: If ``start`` is negative.

    Examples:
        >>> enumerate_rows(["a", "b"])
        ['1. a', '2. b']
    """
    if start < 0:
        raise ValueError(f"start must be >= 0, got {start!r}")
    return [f"{i}. {row}" for i, row in enumerate(rows, start=start)]


def zip_columns(header: list[str], row: list[Any]) -> dict[str, Any]:
    """Pair a header with a row using :func:`zip` (concept #2).

    ``zip`` stops at the shortest input — silently truncating data. Use
    :func:`zip_columns_strict` in ETL code.

    Args:
        header: Column names.
        row: Row values.

    Returns:
        ``{column: value}`` dict (truncated to the shorter side).

    Raises:
        ValueError: If ``header`` is empty.

    Examples:
        >>> zip_columns(["id", "name"], [7, "Ada"])
        {'id': 7, 'name': 'Ada'}
    """
    if not header:
        raise ValueError("header must not be empty")
    return dict(zip(header, row))


def zip_columns_strict(header: list[str], row: list[Any]) -> dict[str, Any]:
    """Strict variant — raises on length mismatch (concept #3, PEP 618).

    Args:
        header: Column names.
        row: Row values; must match ``header`` length exactly.

    Returns:
        ``{column: value}`` dict.

    Raises:
        ValueError: If lengths differ (re-raised from ``zip(..., strict=True)``)
            or if ``header`` is empty.

    Examples:
        >>> zip_columns_strict(["a", "b"], [1, 2])
        {'a': 1, 'b': 2}
    """
    if not header:
        raise ValueError("header must not be empty")
    return dict(zip(header, row, strict=True))


# ─── Section 2: Ordering (concepts #4, #5) ───


def sort_records(
    records: list[dict[str, Any]], *, key_field: str, reverse: bool = False
) -> list[dict[str, Any]]:
    """Sort dict records by a key field using :func:`sorted` (concept #4).

    ``sorted`` is stable: equal keys keep their original order, which is what
    you usually want for leaderboards.

    Args:
        records: List of dicts.
        key_field: Field name to sort by.
        reverse: Descending if True.

    Returns:
        New list (input is not mutated).

    Raises:
        ValueError: If ``key_field`` is missing from any record.

    Examples:
        >>> sort_records([{"a": 2}, {"a": 1}], key_field="a")
        [{'a': 1}, {'a': 2}]
    """
    for rec in records:
        if key_field not in rec:
            raise ValueError(f"missing key_field {key_field!r} in record {rec!r}")
    return sorted(records, key=lambda r: r[key_field], reverse=reverse)


def reverse_history(events: list[str]) -> list[str]:
    """Return ``events`` newest-first using :func:`reversed` (concept #5).

    ``reversed`` returns a lazy iterator; we materialize once at the edge.

    Args:
        events: Chronological event list.

    Returns:
        New list in reverse order.

    Examples:
        >>> reverse_history(["a", "b", "c"])
        ['c', 'b', 'a']
    """
    return list(reversed(events))


# ─── Section 3: Transform & select (concepts #6, #7) ───


def transform_prices(prices: Iterable[float], *, vat: float = 0.20) -> Iterator[float]:
    """Apply a VAT multiplier to each price using :func:`map` (concept #6).

    Returns a lazy iterator — caller decides when to materialize.

    Args:
        prices: Iterable of non-negative prices.
        vat: VAT rate, e.g. ``0.20`` for 20%.

    Returns:
        Iterator of ``price * (1 + vat)``.

    Raises:
        ValueError: If ``vat`` is negative.

    Examples:
        >>> list(transform_prices([10.0, 20.0], vat=0.10))
        [11.0, 22.0]
    """
    if vat < 0:
        raise ValueError(f"vat must be >= 0, got {vat!r}")
    return map(lambda p: p * (1 + vat), prices)


def keep_active(users: Iterable[dict[str, Any]]) -> Iterator[dict[str, Any]]:
    """Keep only users with ``active=True`` using :func:`filter` (concept #7).

    Args:
        users: Iterable of user dicts.

    Returns:
        Iterator of active user dicts.

    Examples:
        >>> list(keep_active([{"id": 1, "active": True}, {"id": 2, "active": False}]))
        [{'id': 1, 'active': True}]
    """
    return filter(lambda u: bool(u.get("active")), users)


# ─── Section 4: Boolean aggregations (concepts #8, #9) ───


def has_failed_job(jobs: Iterable[dict[str, str]]) -> bool:
    """Return True if **any** job failed, short-circuiting (concept #8).

    Args:
        jobs: Iterable of job dicts with a ``status`` key.

    Returns:
        ``True`` as soon as a failed job is seen.

    Examples:
        >>> has_failed_job([{"status": "ok"}, {"status": "failed"}])
        True
    """
    return any(j.get("status") == "failed" for j in jobs)


def all_fields_present(record: dict[str, Any], required: list[str]) -> bool:
    """Return True iff **all** required fields are non-empty (concept #9).

    Args:
        record: Record to check.
        required: Field names that must be present and truthy.

    Returns:
        ``True`` iff every field is present and truthy.

    Raises:
        ValueError: If ``required`` is empty.

    Examples:
        >>> all_fields_present({"a": 1, "b": 2}, ["a", "b"])
        True
        >>> all_fields_present({"a": 1, "b": ""}, ["a", "b"])
        False
    """
    if not required:
        raise ValueError("required must not be empty")
    return all(record.get(f) for f in required)


# ─── Section 5: Numeric aggregations (concepts #10, #11, #12) ───


def total_revenue(amounts: Iterable[float]) -> float:
    """Sum ``amounts`` with :func:`sum` (concept #10).

    Args:
        amounts: Iterable of numeric amounts.

    Returns:
        Total as a float; ``0.0`` on empty input.

    Examples:
        >>> total_revenue([1.5, 2.5, 3.0])
        7.0
    """
    return float(sum(amounts, start=0.0))


def top_spender(
    customers: list[dict[str, Any]], *, default: dict[str, Any] | None = None
) -> dict[str, Any] | None:
    """Return the customer with the highest ``amount`` using :func:`max` (concept #11).

    Uses ``default=`` so an empty list does not raise ``ValueError``.

    Args:
        customers: List of customer dicts with an ``amount`` key.
        default: Fallback returned when ``customers`` is empty.

    Returns:
        Customer dict with the largest ``amount``, or ``default``.

    Raises:
        ValueError: If any customer record is missing ``amount``.

    Examples:
        >>> top_spender([{"id": 1, "amount": 10}, {"id": 2, "amount": 30}])
        {'id': 2, 'amount': 30}
        >>> top_spender([], default=None) is None
        True
    """
    for c in customers:
        if "amount" not in c:
            raise ValueError(f"missing 'amount' in customer {c!r}")
    return max(customers, key=lambda c: c["amount"], default=default)


def format_duration(seconds: int) -> str:
    """Format ``seconds`` as ``HH:MM:SS`` using :func:`divmod` (concept #12).

    Args:
        seconds: Non-negative duration in seconds.

    Returns:
        Zero-padded ``HH:MM:SS`` string.

    Raises:
        ValueError: If ``seconds`` is negative.

    Examples:
        >>> format_duration(3725)
        '01:02:05'
    """
    if seconds < 0:
        raise ValueError(f"seconds must be >= 0, got {seconds!r}")
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def round_amount(amount: float, *, places: int = 2) -> float:
    """Round ``amount`` to ``places`` decimals using :func:`round` (concept #12).

    Uses :func:`abs` to validate the magnitude is finite.

    Args:
        amount: Value to round.
        places: Decimal places (>= 0).

    Returns:
        Rounded float.

    Raises:
        ValueError: If ``places`` is negative.

    Examples:
        >>> round_amount(3.14159, places=2)
        3.14
        >>> round_amount(-2.715, places=2)
        -2.71
    """
    if places < 0:
        raise ValueError(f"places must be >= 0, got {places!r}")
    _ = abs(amount)  # demonstrate abs(); also asserts amount is numeric
    return round(amount, places)


# ─── Section 6: Sizing & batching (concept #13) ───


def batched_indices(total: int, *, size: int) -> list[tuple[int, int]]:
    """Generate ``(start, end)`` slice indices using :func:`range` and :func:`len`.

    Concept #13 — sequencing with ``range`` and using ``len`` to check bounds.

    Args:
        total: Total item count (>= 0).
        size: Batch size (> 0).

    Returns:
        List of half-open ``(start, end)`` index pairs covering ``total`` items.

    Raises:
        ValueError: If ``total < 0`` or ``size <= 0``.

    Examples:
        >>> batched_indices(7, size=3)
        [(0, 3), (3, 6), (6, 7)]
    """
    if total < 0:
        raise ValueError(f"total must be >= 0, got {total!r}")
    if size <= 0:
        raise ValueError(f"size must be > 0, got {size!r}")
    pairs = [(i, min(i + size, total)) for i in range(0, total, size)]
    assert len(pairs) == (total + size - 1) // size if total else len(pairs) == 0
    return pairs


# ─── Section 7: Introspection (concepts #14, #15, #18) ───


def coerce_amount(value: Any) -> float:
    """Validate and coerce ``value`` to ``float`` using :func:`isinstance` (concept #14).

    Args:
        value: ``int``, ``float``, or numeric string.

    Returns:
        ``value`` as a float.

    Raises:
        ValueError: If ``value`` is not a numeric type or not numeric-looking.

    Examples:
        >>> coerce_amount(3)
        3.0
        >>> coerce_amount("4.5")
        4.5
    """
    if isinstance(value, bool):  # bool is a subclass of int — reject explicitly
        raise ValueError(f"bool is not a valid amount: {value!r}")
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError as exc:
            raise ValueError(f"amount must be numeric, got {value!r}") from exc
    raise ValueError(f"unsupported amount type: {type(value).__name__}")


def dedupe_by_key(records: list[dict[str, Any]], *, key_field: str) -> list[dict[str, Any]]:
    """Deduplicate ``records`` by ``record[key_field]`` (concept #15).

    Uses :func:`hash` implicitly via a ``set`` of seen keys, and demonstrates
    :func:`type` / :func:`id` checks in the validation step.

    Args:
        records: List of dicts.
        key_field: Field whose value must be hashable.

    Returns:
        New list preserving first occurrence per key.

    Raises:
        ValueError: If ``key_field`` is missing or its value is unhashable.

    Examples:
        >>> dedupe_by_key([{"id": 1}, {"id": 1}, {"id": 2}], key_field="id")
        [{'id': 1}, {'id': 2}]
    """
    seen: set[int] = set()
    out: list[dict[str, Any]] = []
    for rec in records:
        if key_field not in rec:
            raise ValueError(f"missing key_field {key_field!r} in record {rec!r}")
        key_value = rec[key_field]
        try:
            key_hash = hash(key_value)
        except TypeError as exc:
            raise ValueError(
                f"unhashable {type(key_value).__name__} for {key_field!r}: {key_value!r}"
            ) from exc
        if key_hash not in seen:
            seen.add(key_hash)
            out.append(rec)
    return out


def apply_if_callable(maybe_func: Any, value: Any) -> Any:
    """Apply ``maybe_func`` to ``value`` only if it is callable (concept #18).

    Args:
        maybe_func: A function, lambda, class, or non-callable object.
        value: Value to pass when callable.

    Returns:
        ``maybe_func(value)`` if callable, else ``value`` unchanged.

    Examples:
        >>> apply_if_callable(str.upper, "ada")
        'ADA'
        >>> apply_if_callable(None, "ada")
        'ada'
    """
    if callable(maybe_func):
        return maybe_func(value)
    return value


# ─── Section 8: I/O & manual iteration (concepts #16, #17) ───


def print_report(rows: list[str], *, sep: str = " | ", end: str = "\n") -> str:
    """Render ``rows`` as a single line using ``print(sep=, end=)`` (concept #16).

    Returns the same string for testability without capturing stdout.

    Args:
        rows: Pre-formatted row strings.
        sep: Separator between rows.
        end: Trailing string (kept in the return value too).

    Returns:
        The joined report line.

    Raises:
        ValueError: If ``rows`` is empty.

    Examples:
        >>> print_report(["a", "b", "c"], sep=", ", end="!")
        'a, b, c!'
    """
    if not rows:
        raise ValueError("rows must not be empty")
    line = sep.join(rows) + end
    print(*rows, sep=sep, end=end)
    return line


def first_match(items: Iterable[Any], pred: Callable[[Any], bool], default: Any = None) -> Any:
    """Return the first item satisfying ``pred`` using :func:`iter` / :func:`next` (concept #17).

    Args:
        items: Iterable to scan.
        pred: Predicate function.
        default: Returned if no element matches.

    Returns:
        First matching item or ``default``.

    Raises:
        ValueError: If ``pred`` is not callable.

    Examples:
        >>> first_match([1, 2, 3, 4], lambda x: x > 2)
        3
        >>> first_match([1, 2], lambda x: x > 99, default=-1)
        -1
    """
    if not callable(pred):
        raise ValueError(f"pred must be callable, got {type(pred).__name__}")
    it: Iterator[Any] = iter(items)
    return next((x for x in it if pred(x)), default)


# ─── Section 9: Style trade-off & chaining (concepts #19, #20, #21) ───


def comprehension_vs_map(nums: list[int]) -> tuple[list[int], list[int]]:
    """Compare a comprehension and a ``map`` call (concept #19).

    Both produce the same result; the comprehension is the Pythonic default
    when no named function is available.

    Args:
        nums: Integer inputs.

    Returns:
        ``(comprehension_result, map_result)`` — equal lists.

    Examples:
        >>> comprehension_vs_map([1, 2, 3])
        ([2, 4, 6], [2, 4, 6])
    """
    by_comprehension = [x * 2 for x in nums]
    by_map = list(map(lambda x: x * 2, nums))
    assert by_comprehension == by_map
    return by_comprehension, by_map


def pipeline_total(rows: list[str]) -> float:
    """Chain ``filter → map → sum`` in one pass (concept #20).

    Args:
        rows: Strings that may or may not be numeric.

    Returns:
        Sum of numeric rows; ``0.0`` if none parse.

    Examples:
        >>> pipeline_total(["12.5", "bad", "30.0", "", "7.25"])
        49.75
    """
    def looks_numeric(s: str) -> bool:
        return s.replace(".", "", 1).lstrip("-").isdigit()

    return float(sum(map(float, filter(looks_numeric, rows)), start=0.0))


def anti_pattern_list_map(nums: list[int]) -> list[int]:
    """Show the ``list(map(lambda ...))`` anti-pattern next to the fix (concept #21).

    Args:
        nums: Integer inputs.

    Returns:
        Doubled values — produced via the *clean* comprehension form.

    Examples:
        >>> anti_pattern_list_map([1, 2, 3])
        [2, 4, 6]
    """
    # ❌ Anti-pattern (kept here only to document what NOT to write):
    #     bad = list(map(lambda x: x * 2, nums))
    # ✅ Preferred:
    return [x * 2 for x in nums]


# ─── Section 10: Industrial pipeline (concept #22) ───


def daily_revenue_report(
    raw_rows: list[dict[str, Any]], *, min_amount: float = 0.0
) -> dict[str, Any]:
    """Full ``parse → map → filter → aggregate`` pipeline (concept #22).

    Stages:
        1. **Validate** each row's required fields with :func:`all`.
        2. **Parse** amounts with :func:`coerce_amount` (uses ``isinstance``).
        3. **Filter** rows below ``min_amount``.
        4. **Sort** descending by amount with :func:`sorted`.
        5. **Aggregate** with :func:`sum`, :func:`max`, :func:`len`.

    Args:
        raw_rows: Each row has ``{"customer": str, "amount": numeric}``.
        min_amount: Drop rows below this amount.

    Returns:
        Report dict with ``total``, ``count``, ``top``, and ``ranked`` keys.

    Raises:
        ValueError: If ``min_amount`` is negative or rows are malformed.

    Examples:
        >>> r = daily_revenue_report(
        ...     [{"customer": "Ada", "amount": "30"},
        ...      {"customer": "Linus", "amount": 5},
        ...      {"customer": "Grace", "amount": "50.5"}],
        ...     min_amount=10,
        ... )
        >>> r["total"], r["count"], r["top"]["customer"]
        (80.5, 2, 'Grace')
    """
    if min_amount < 0:
        raise ValueError(f"min_amount must be >= 0, got {min_amount!r}")

    required = ["customer", "amount"]
    valid_rows = [r for r in raw_rows if all_fields_present(r, required)]

    parsed = [
        {"customer": str(r["customer"]), "amount": coerce_amount(r["amount"])}
        for r in valid_rows
    ]
    kept = [r for r in parsed if r["amount"] >= min_amount]
    ranked = sort_records(kept, key_field="amount", reverse=True)

    return {
        "total": round_amount(total_revenue(r["amount"] for r in ranked)),
        "count": len(ranked),
        "top": top_spender(ranked, default=None),
        "ranked": ranked,
    }


# ─── __main__: runnable demos (no asserts — those live in exercise files) ───


if __name__ == "__main__":
    print("── enumerate / zip ──")
    print(enumerate_rows(["alpha", "beta", "gamma"]))
    # Expected output: ['1. alpha', '2. beta', '3. gamma']

    print(zip_columns(["id", "name"], [7, "Ada"]))
    # Expected output: {'id': 7, 'name': 'Ada'}

    try:
        zip_columns_strict(["id", "name", "email"], [7, "Ada"])
    except ValueError as exc:
        print("strict mismatch ->", exc)
    # Expected output: strict mismatch -> zip() argument 2 is shorter than argument 1

    print("\n── sorted / reversed ──")
    print(sort_records(
        [{"name": "Ada", "amt": 30}, {"name": "Grace", "amt": 50}, {"name": "Linus", "amt": 30}],
        key_field="amt", reverse=True,
    ))
    # Expected output: [{'name': 'Grace', 'amt': 50}, {'name': 'Ada', 'amt': 30}, {'name': 'Linus', 'amt': 30}]
    print(reverse_history(["login", "purchase", "logout"]))
    # Expected output: ['logout', 'purchase', 'login']

    print("\n── map / filter ──")
    print(list(transform_prices([10.0, 20.0], vat=0.10)))
    # Expected output: [11.0, 22.0]
    print(list(keep_active([{"id": 1, "active": True}, {"id": 2, "active": False}])))
    # Expected output: [{'id': 1, 'active': True}]

    print("\n── any / all ──")
    print(has_failed_job([{"status": "ok"}, {"status": "failed"}]))
    # Expected output: True
    print(all_fields_present({"a": 1, "b": 2}, ["a", "b"]))
    # Expected output: True

    print("\n── numeric helpers ──")
    print(total_revenue([1.5, 2.5, 3.0]))
    # Expected output: 7.0
    print(top_spender([{"id": 1, "amount": 10}, {"id": 2, "amount": 30}]))
    # Expected output: {'id': 2, 'amount': 30}
    print(format_duration(3725))
    # Expected output: 01:02:05
    print(round_amount(3.14159))
    # Expected output: 3.14

    print("\n── batching / introspection ──")
    print(batched_indices(7, size=3))
    # Expected output: [(0, 3), (3, 6), (6, 7)]
    print(coerce_amount("4.5"), coerce_amount(3))
    # Expected output: 4.5 3.0
    print(dedupe_by_key([{"id": 1}, {"id": 1}, {"id": 2}], key_field="id"))
    # Expected output: [{'id': 1}, {'id': 2}]
    print(apply_if_callable(str.upper, "ada"), apply_if_callable(None, "ada"))
    # Expected output: ADA ada

    print("\n── I/O & iter/next ──")
    print_report(["a", "b", "c"], sep=", ", end="\n")
    # Expected output: a, b, c
    print(first_match([1, 2, 3, 4], lambda x: x > 2))
    # Expected output: 3

    print("\n── style & chain ──")
    print(comprehension_vs_map([1, 2, 3]))
    # Expected output: ([2, 4, 6], [2, 4, 6])
    print(pipeline_total(["12.5", "bad", "30.0", "", "7.25"]))
    # Expected output: 49.75
    print(anti_pattern_list_map([1, 2, 3]))
    # Expected output: [2, 4, 6]

    print("\n── industrial: daily_revenue_report ──")
    report = daily_revenue_report(
        [
            {"customer": "Ada", "amount": "30"},
            {"customer": "Linus", "amount": 5},
            {"customer": "Grace", "amount": "50.5"},
            {"customer": "", "amount": 99},     # dropped: missing customer
        ],
        min_amount=10,
    )
    print(report["total"], report["count"], report["top"]["customer"])
    # Expected output: 80.5 2 Grace
