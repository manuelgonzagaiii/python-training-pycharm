# Composing sub-streams with yield from

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use yield from to delegate iteration to another generator/iterable
- Flatten a stream of sales-per-invoice into a single flat stream of lines
- Recognize yield from as shorthand for `for x in sub: yield x`
- Compose several generators into one readable pipeline

## Python features introduced
`yield from`, `delegating to sub-generators`, `flattening nested iterables`, `yield from vs a manual for/yield loop`, `generator composition into a pipeline`, `yield from over multiple sources`

## MiniERP increment
Add a stream_all_lines(invoices) generator to the reporting module that uses yield from to flatten every invoice's line items into one continuous lazy stream, so cross-invoice reports read from a single source.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def stream_all_lines(invoices):
    """Flatten the line items of many invoices into one lazy stream."""
    for invoice in invoices:
        # TODO: delegate to invoice.lines using yield from
        ...

- **Test focus:** stream_all_lines yields every line across all invoices in order; behaves identically to a nested for/yield; remains lazy; empty invoices contribute nothing.

</div>
