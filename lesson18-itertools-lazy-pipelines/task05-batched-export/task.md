# Chunked streaming export with batched

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 18.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Split a lazy report stream into fixed-size batches with batched()
- Stream an export chunk-by-chunk instead of building one huge string
- Drive csv writing from a generator pipeline
- Understand batched as the streaming-export workhorse

## Python features introduced
`itertools.batched (3.12+)`, `batched strict= (3.13+)`, `chunking a stream for bulk writes`, `generator-driven CSV/JSONL export`, `csv.writer over a generator`, `yielding encoded chunks`, `io.StringIO for in-memory capture`

## MiniERP increment
Deliver the phase's streaming exporter in Import/Export: export_csv_chunks(stream, batch_size) yields CSV text one batch of rows at a time via itertools.batched, so MiniERP can export arbitrarily large reports to a file/HTTP response with bounded memory.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from itertools import batched
import csv, io

def export_csv_chunks(rows, header, batch_size=100):
    """Yield CSV text one batch at a time (header first), for streaming export."""
    buf = io.StringIO(); w = csv.writer(buf)
    w.writerow(header)
    for batch in batched(rows, batch_size):
        # TODO: write each row in the batch, then yield+clear the buffer's text
        ...

- **Test focus:** Header emitted once; rows chunked into batches of the requested size (final short batch handled); concatenating all yielded chunks reproduces the full CSV; memory stays bounded (buffer cleared per batch).

</div>
