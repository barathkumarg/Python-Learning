# Day 02 — Control Flow (Exercises)

## Learning objectives
- Build guard-clause-driven functions that reject invalid order states early.
- Implement readable control flow with `match`, `if/elif`, and bounded loops.
- Signal success vs exhaustion explicitly using `break`/`continue`/`else` on loops.

## Skills assessed
- PY-04 | Control flow (`if`/`match`/loops) — ex01, ex02, ex03
- PY-03 | Input validation & error handling — ex01, ex02
- PY-16 | Type hints & API clarity — ex01, ex02, ex03

## Exercise specs

### ex01_basic.py — Order status transition
- **Must-pass:** Validate status/action strings; legal transitions: created→paid on `pay`, paid→shipped on `ship`, created/paid→cancelled on `cancel`; raise `ValueError` on anything else.
- **Stretch:** Accept uppercase/mixed-case inputs while keeping outputs lowercase.
- **Failure modes:** Missing default branch allowing illegal transitions; returning `None` instead of raising on invalid input.

### ex02_intermediate.py — Order summary with `continue` / `break`
- **Must-pass:** Iterate a list of order dicts; skip orders missing `total` or below threshold; stop when `max_count` qualifying orders collected; return summary dict with `count` and `total_revenue`.
- **Stretch:** Track the first rejected order ID in summary.
- **Failure modes:** Infinite loop when input is empty; mutating the input list; not guarding negative thresholds.

### ex03_advanced.py — Polling loop with timeout
- **Must-pass:** Poll a callable up to `max_checks`; return status once it is `shipped` or `cancelled`; raise `TimeoutError` if terminal status not seen; preserve last seen status in the error message.
- **Stretch:** Accept optional `sleep_seconds` and call `time.sleep` between polls.
- **Failure modes:** Unbounded loops; swallowing exceptions from the poller; accepting `max_checks < 1`.

## Scoring (per file, 0–100)
- Must-pass behaviors: 40
- Stretch goals: 15
- Inline asserts + AI-verified behavior: 25
- Style (types, docstrings, ruff-clean): 20
- Dimension weights applied in review: D1 0.30, D2 0.15, D3 0.15, D4 0.10, D5 0.10, D6 0.10, D7 0.10

## Suggested Practice
- [LeetCode 1221 — Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) — practice counters and early exits.
- [Real Python — Loop `else` Clauses](https://realpython.com/python-for-else/) — deepen understanding of `for/while` + `else`.

## Evaluation report — 2026-03-28

### Skills assessed
| Skill ID | Skill | Exercise | Proficiency |
|----------|-------|----------|-------------|
| PY-04 | Control flow | ex01, ex02, ex03 | proficient |
| PY-03 | Input validation & error handling | ex01, ex02 | developing |
| PY-16 | Type hints & API clarity | ex01, ex02, ex03 | developing |

### Gate checklist
| Gate | Result | Evidence |
|------|--------|----------|
| G1 Type hints | ✅ | All public funcs typed (ex01:22, ex02:23, ex03:25). |
| G2 Explicit errors | ✅ | ValueError on invalid inputs (ex01:30, ex02:26); TimeoutError on expiry (ex03:44). |
| G3 Inline asserts | ✅ | `python3 ex01_basic.py`, `ex02_intermediate.py`, `ex03_advanced.py` exit cleanly; behaviors align with must-pass specs. |
| G4 Ruff-clean | ❌ | Ruff not installed/offline here; lint not executed. |
| G5 Docstrings | ✅ | Problem docstrings at top of each file (ex01:1, ex02:1, ex03:1). |
| G6 Security | ✅ | Pure in-memory logic; inputs validated; no I/O or subprocess. |
| G7 Observability | ✅ | Inline asserts surface failures; pass banner in `__main__`. |

### Dimension scores
| Dimension | Score | Notes |
|-----------|-------|-------|
| D1 Correctness (0.30) | 4.5 | Meets must-pass behaviors across exercises. |
| D2 Reliability (0.15) | 4.0 | Guard clauses and bounded loops; minor payload validation gap. |
| D3 Maintainability (0.15) | 4.0 | Small, readable functions; clear control flow. |
| D4 API & typing (0.10) | 4.0 | Signatures typed; container types could be tighter. |
| D5 Performance (0.10) | 4.0 | Linear scans and bounded loops only. |
| D6 Security (0.10) | 4.0 | No external surface; validates inputs. |
| D7 Test quality (0.10) | 3.5 | Asserts cover happy path + one failure; missing cancelled and sleep coverage. |
| **Weighted total** | **4.10 / 5** | |

### Per-file scores (0–100)
| Criterion | ex01 | ex02 | ex03 |
|-----------|------|------|------|
| Must-pass behaviors (40) | 40 | 40 | 40 |
| Stretch behaviors (15) | 15 | 15 | 15 |
| Inline asserts + AI behavior coverage (25) | 22 | 22 | 23 |
| Style — types, ruff, docstrings (20) | 18 | 18 | 18 |
| **Total** | **95** | **95** | **96** |

### Top 3 improvements
1) ex02_intermediate.py:35-38 — Guard that accepted orders have a non-empty string `id`; otherwise raise `ValueError` to avoid counting malformed records.  
2) ex01_basic.py:30-43 — Improve error messages by echoing offending status/action and trimming whitespace before validation to make debugging invalid input easier.  
3) ex03_advanced.py:53-65 — Add inline asserts for the `cancelled` path and for `sleep_seconds` behavior to strengthen regression coverage.

### Rewritten snippet (worst issue)
Add strict `id` validation in `summarize_orders` before counting an order:
```python
        order_id = order.get("id")
        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("order must include non-empty string 'id'")
        count += 1
        total_revenue += float(total)
```

### Verdict
REWORK — need a ruff run (G4) and tighter order `id` validation in ex02 for full pass. Once addressed, scores should hold.
