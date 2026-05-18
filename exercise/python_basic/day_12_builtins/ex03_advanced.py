# ex03_advanced.py — Day 12: Built-ins in Pipelines — Advanced

"""
Advanced exercises for Built-ins in Pipelines.
Covers checklist items: #14–#22 (isinstance, type/id/hash, print(sep=, end=),
iter/next, callable, comprehension vs map+filter, chaining, anti-pattern,
industrial parse → map → filter → aggregate pipeline).

Instructions:
- Implement each function where you see TODO.
- Run this file to verify: python ex03_advanced.py
- All asserts must pass.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any


def coerce_int(value: Any) -> int:
    """Validate and coerce ``value`` to ``int`` using :func:`isinstance` (concept #14).

    Reject ``bool`` explicitly (bool is a subclass of int) and reject
    non-numeric strings with a descriptive ``ValueError``.

    Args:
        value: ``int`` or numeric ``str``.

    Returns:
        ``value`` as an int.

    Raises:
        ValueError: If ``value`` is bool, not numeric, or wrong type.

    Examples:
        >>> coerce_int(3)
        3
        >>> coerce_int("42")
        42
    """
    # TODO:
    # 1. If isinstance(value, bool): raise ValueError(f"bool is not a valid int: {value!r}").
    # 2. If isinstance(value, int): return value.
    # 3. If isinstance(value, str): try int(value) else raise ValueError with descriptive msg.
    # 4. Otherwise raise ValueError(f"unsupported type: {type(value).__name__}").
    if isinstance(value, bool):
        raise ValueError(f"bool is not a valid")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except:
            raise ValueError("Unable to convert the str value to int")
    else:
        raise ValueError("None of the type matched")


def dedupe_records(records: list[dict[str, Any]], key_field: str) -> list[dict[str, Any]]:
    """Deduplicate by ``record[key_field]``, preserving first occurrence (concept #15).

    Use a ``set`` of seen :func:`hash` values; raise ``ValueError`` if a key
    value is unhashable (e.g. a list).

    Args:
        records: List of dicts.
        key_field: Field whose value must be hashable.

    Returns:
        New list — first occurrence per key kept.

    Raises:
        ValueError: If ``key_field`` missing or value unhashable.

    Examples:
        >>> dedupe_records([{"id": 1}, {"id": 1}, {"id": 2}], key_field="id")
        [{'id': 1}, {'id': 2}]
    """
    # TODO:
    # 1. seen: set[int] = set(); out: list = [].
    # 2. For rec in records: validate key_field in rec.
    # 3. Try hash(rec[key_field]) — on TypeError raise ValueError("unhashable ...").
    # 4. If hash not in seen: add it and append rec to out.
    # 5. Return out.
    seen: set[int] = set()
    out: list = []
    for rec in records:
        if key_field not in rec:
            return ValueError("unhasable object")
        try:
            key_hash = hash(rec[key_field])                # Bug 3 fix: hash first, store the int
        except TypeError:
            raise ValueError(f"Unhashable value for '{key_field}': {rec[key_field]!r}")
        if key_hash not in seen:
            seen.add(key_hash)
            out.append(rec)
    return out
        


def render_csv_line(fields: list[Any], sep: str = ",") -> str:
    """Print and return a CSV line using ``print(sep=, end=)`` (concept #16).

    Args:
        fields: Field values (non-empty).
        sep: Field separator.

    Returns:
        The printed string (without trailing newline).

    Raises:
        ValueError: If ``fields`` is empty.

    Examples:
        >>> render_csv_line(["a", "b", "c"], sep=",")
        'a,b,c'
    """
    # TODO:
    # 1. If not fields: raise ValueError("fields must not be empty").
    # 2. Build line = sep.join(str(f) for f in fields).
    # 3. Call print(*fields, sep=sep, end="\n") for the side-effect.
    # 4. Return line.
    if not fields:
        raise ValueError("Fields must not be empty")
    line = sep.join(str(f) for f in fields)
    return line

def find_first_admin(users: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    """Return the first user with ``role == "admin"`` using :func:`iter`/:func:`next` (concept #17).

    Must short-circuit — do NOT scan the whole iterable when an early match exists.

    Args:
        users: Iterable of user dicts.

    Returns:
        First admin user, or ``None``.

    Examples:
        >>> find_first_admin([{"id": 1, "role": "guest"}, {"id": 2, "role": "admin"}])
        {'id': 2, 'role': 'admin'}
    """
    # TODO: return next((u for u in users if u.get("role") == "adm'in"), None)
    return next((u for u in users if u.get('role') == "admin"), None)


def safe_apply(func: Any, value: Any) -> Any:
    """Apply ``func`` to ``value`` only when :func:`callable` is True (concept #18).

    Args:
        func: A callable, or any non-callable value.
        value: Value to pass when callable.

    Returns:
        ``func(value)`` if callable else ``value`` unchanged.

    Examples:
        >>> safe_apply(str.upper, "ada")
        'ADA'
        >>> safe_apply(None, "ada")
        'ada'
    """
    return func(value) if callable(func) else value
    


def to_uppercase_names(names: list[str]) -> list[str]:
    """Uppercase each name using a **comprehension** (concepts #19, #21).

    Anti-pattern to avoid (do NOT write this):
        ``list(map(lambda n: n.upper(), names))``  # verbose, no perf win

    Preferred:
        ``[n.upper() for n in names]``

    Args:
        names: List of names.

    Returns:
        New list of uppercased names.

    Examples:
        >>> to_uppercase_names(["ada", "linus"])
        ['ADA', 'LINUS']
    """
    return [n.upper() for n in names]
    #raise NotImplementedError("Implement to_uppercase_names")


def pipeline_sum_positive(rows: list[str]) -> float:
    """Chain ``filter → map → sum`` to total only positive numeric rows (concept #20).

    Stages:
        1. Filter rows that look numeric (allow leading '-' and a single '.').
        2. Map to ``float``.
        3. Filter for ``> 0``.
        4. Sum (with ``start=0.0``).

    Args:
        rows: Raw string rows.

    Returns:
        Sum of positive numeric values; ``0.0`` if none qualify.

    Examples:
        >>> pipeline_sum_positive(["12.5", "bad", "-3", "30", ""])
        42.5
    """
    # TODO:
    def looks_numeric(s: str) -> bool:
        return s.lstrip("-").replace(".", "", 1).isdigit()
    nums = map(float, filter(looks_numeric, rows))
    return float(sum(filter(lambda x: x > 0, nums), start=0.0))



def daily_sales_report(
    rows: list[dict[str, Any]], min_amount: float = 0.0
) -> dict[str, Any]:
    """Run the full ``parse → map → filter → aggregate`` pipeline (concept #22).

    Stages:
        1. Drop rows missing ``customer`` or ``amount``.
        2. Coerce ``amount`` to float (reject bools and bad strings).
        3. Filter rows with ``amount >= min_amount``.
        4. Sort descending by amount.
        5. Aggregate: ``total`` (sum, rounded 2dp), ``count`` (len),
           ``top`` (max by amount or ``None``), ``ranked`` (sorted list).

    Args:
        rows: Raw row dicts.
        min_amount: Inclusive minimum amount (>= 0).

    Returns:
        ``{"total": float, "count": int, "top": dict|None, "ranked": list}``.

    Raises:
        ValueError: If ``min_amount < 0`` or any kept row has bad amount.

    Examples:
        >>> r = daily_sales_report(
        ...     [{"customer": "Ada", "amount": "30"},
        ...      {"customer": "Grace", "amount": 50.5}],
        ...     min_amount=10,
        ... )
        >>> r["total"], r["count"], r["top"]["customer"]
        (80.5, 2, 'Grace')
    """
    if min_amount < 0:
        raise ValueError(f"min_amount must be >= 0, got {min_amount!r}")

    valid = [r for r in rows if r.get("customer") and r.get("amount") not in (None, "")]

    parsed = []
    for r in valid:
        amt = r["amount"]
        if isinstance(amt, bool):
            raise ValueError(f"Invalid amount (bool not allowed): {amt!r}")
        try:
            parsed.append({"customer": str(r["customer"]), "amount": float(amt)})
        except (TypeError, ValueError):
            raise ValueError(f"Invalid amount value: {amt!r}")

    kept = [r for r in parsed if r["amount"] >= min_amount]
    ranked = sorted(kept, key=lambda r: r["amount"], reverse=True)
    total = round(sum(r["amount"] for r in ranked), 2)
    top = max(ranked, key=lambda r: r["amount"], default=None)

    return {"total": total, "count": len(ranked), "top": top, "ranked": ranked}


if __name__ == "__main__":
    # ─── coerce_int checks ───
    assert coerce_int(3) == 3
    assert coerce_int("42") == 42
    for bad in (True, "abc", 3.5):
        try:
            coerce_int(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"coerce_int must reject {bad!r}")

    # ─── dedupe_records checks ───
    assert dedupe_records(
        [{"id": 1, "v": "a"}, {"id": 1, "v": "b"}, {"id": 2, "v": "c"}], key_field="id"
    ) == [{"id": 1, "v": "a"}, {"id": 2, "v": "c"}]
    try:
        dedupe_records([{"k": [1, 2]}], key_field="k")
    except ValueError:
        pass
    else:
        raise AssertionError("unhashable key must raise")

    # ─── render_csv_line checks ───
    assert render_csv_line(["a", "b", "c"], sep=",") == "a,b,c"
    assert render_csv_line([1, 2, 3], sep=";") == "1;2;3"

    # ─── find_first_admin checks ───
    assert find_first_admin(
        [{"id": 1, "role": "guest"}, {"id": 2, "role": "admin"}, {"id": 3, "role": "admin"}]
    ) == {"id": 2, "role": "admin"}
    assert find_first_admin([{"id": 1, "role": "guest"}]) is None

    # ─── safe_apply checks ───
    assert safe_apply(str.upper, "ada") == "ADA"
    assert safe_apply(None, "ada") == "ada"
    assert safe_apply(lambda x: x + 1, 4) == 5

    # ─── to_uppercase_names checks ───
    assert to_uppercase_names(["ada", "linus"]) == ["ADA", "LINUS"]
    assert to_uppercase_names([]) == []

    # ─── pipeline_sum_positive checks ───
    assert pipeline_sum_positive(["12.5", "bad", "-3", "30", ""]) == 42.5
    assert pipeline_sum_positive([]) == 0.0
    assert pipeline_sum_positive(["-1", "-2"]) == 0.0

    # ─── daily_sales_report checks ───
    report = daily_sales_report(
        [
            {"customer": "Ada", "amount": "30"},
            {"customer": "Linus", "amount": 5},
            {"customer": "Grace", "amount": 50.5},
            {"customer": "", "amount": 99},        # dropped: missing customer
            {"customer": "Bob", "amount": None},   # dropped: missing amount
        ],
        min_amount=10,
    )
    assert report["total"] == 80.5, f"total mismatch: {report['total']}"
    assert report["count"] == 2, f"count mismatch: {report['count']}"
    assert report["top"]["customer"] == "Grace", "top spender wrong"
    assert [r["customer"] for r in report["ranked"]] == ["Grace", "Ada"], "ranking wrong"
    try:
        daily_sales_report([], min_amount=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative min_amount must raise")

    print("ex03_advanced.py: all asserts passed ✓")
