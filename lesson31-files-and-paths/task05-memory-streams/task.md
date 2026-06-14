# In-Memory Files: StringIO & BytesIO

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 31.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use StringIO/BytesIO as drop-in file objects for testing and buffering
- Build text or bytes in memory and extract it with getvalue()
- Pass an in-memory stream to any function that expects a file-like object
- Understand why streams make code testable without touching the disk

## Python features introduced
`io.StringIO`, `io.BytesIO`, `getvalue()`, `seek/read on streams`, `file-like duck typing`, `io.TextIOBase concepts`, `writing to a stream then flushing to disk`

## MiniERP increment
Refactors export helpers to accept any text stream (file or StringIO), enabling minierp.export.render_to(stream, rows) so the same code serves disk export, HTTP responses, and unit tests.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import io

def render_lines(stream, rows: list[str]) -> None:
    # write each row + newline to the given text stream
    ...

def render_to_string(rows: list[str]) -> str:
    buf = io.StringIO()
    render_lines(buf, rows)
    ...  # return buf.getvalue()

- **Test focus:** render_lines works against both a real file (tmp_path) and a StringIO; render_to_string returns the joined content; a BytesIO variant round-trips encoded bytes.

</div>
