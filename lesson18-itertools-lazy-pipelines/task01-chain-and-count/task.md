# Endless and concatenated streams: count, cycle, chain

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 18.1 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Generate row numbers with count() instead of a manual counter
- Concatenate multiple ledgers' line streams with chain / chain.from_iterable
- Understand infinite iterators must be sliced/zipped to terminate
- Use cycle() to round-robin a repeating label sequence

## Python features introduced
`itertools.count`, `itertools.cycle`, `itertools.chain`, `itertools.chain.from_iterable`, `infinite iterators (must be bounded by the consumer)`, `lazy concatenation`

## MiniERP increment
Add a numbered, multi-source report stream to the reporting module: chain together several ledgers into one lazy line stream and pair each line with a sequential row number from count(1), so consolidated reports span branches without copying data.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from itertools import count, chain

def numbered_stream(*ledgers):
    """Yield (row_no, line) starting at row 1, across all ledgers, lazily."""
    combined = chain(*ledgers)            # one lazy stream over every ledger
    # TODO: pair each line with an incrementing row number from count(1)
    ...

- **Test focus:** Rows are numbered from 1 with no gaps; lines from all ledgers appear in order; the result is lazy (count is never fully consumed); zero-ledger and empty-ledger cases behave.

</div>
