# Slicing lazy streams: islice for pagination

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 18.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Paginate a lazy report with islice(stream, offset, offset+size)
- Slice an iterator you cannot index into (no [] on generators)
- Split one stream into two independent passes with tee()
- Understand tee buffers consumed-but-unread items in memory

## Python features introduced
`itertools.islice`, `islice(start, stop, step)`, `lazy pagination without materializing`, `consuming/advancing an iterator`, `itertools.tee for splitting a stream`, `tee independence and memory caveats`

## MiniERP increment
Add page(stream, page, size) to the reporting module so the CLI and Web UI can request report page N without building the whole report, and use tee() to compute a count and a preview of the same stream in one pass — the basis for paginated report endpoints.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from itertools import islice, tee

def page(stream, page_no, size):
    """Return the rows for a 1-based page from a lazy stream, using islice."""
    start = (page_no - 1) * size
    # TODO: islice the stream from start to start+size
    ...

def count_and_preview(stream, preview_n):
    """Use tee to get both a total count and the first preview_n rows."""
    # TODO: tee the stream into two independent iterators
    ...

- **Test focus:** page() returns correct rows for first/middle/last/out-of-range pages without consuming beyond what's needed; count_and_preview returns the right total and the right preview from a single source via tee.

</div>
