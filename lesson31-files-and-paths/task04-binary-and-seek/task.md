# Binary Mode, seek() and tell()

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 31.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Read and write raw bytes and convert to/from text explicitly with encode/decode
- Move a file pointer with seek() using SEEK_SET/CUR/END and inspect it with tell()
- Read a fixed number of bytes and understand partial reads
- Truncate a file in place

## Python features introduced
`binary mode 'rb'/'wb'`, `bytes vs str`, `file.seek(offset, whence)`, `os.SEEK_SET/CUR/END`, `file.tell()`, `file.read(n) partial reads`, `file.truncate()`, `encode/decode`

## MiniERP increment
Adds a fixed-width record probe read_record(path, index, size) to minierp/storage that seeks to index*size and reads one record - the conceptual seed for the struct-based snapshot format two lessons later.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from pathlib import Path

def write_blob(path: Path, data: bytes) -> None:
    ...

def read_record(path: Path, index: int, size: int) -> bytes:
    # seek to index*size, read exactly size bytes
    ...

def tail_bytes(path: Path, n: int) -> bytes:
    # seek from END, read last n bytes
    ...

- **Test focus:** Write a blob, read_record returns the correct slice via seek; tail_bytes uses SEEK_END to fetch the final n bytes; tell() reports expected offsets.

</div>
