# Compression: gzip & a Compressed Snapshot

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.7 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compress and decompress bytes with gzip.compress/decompress
- Write a gzipped text file with gzip.open in text mode
- Trade speed vs ratio with compresslevel
- Produce a compressed JSON snapshot to save disk space

## Python features introduced
`gzip.open`, `gzip.compress / decompress`, `compresslevel`, `wrapping a JSON dump in gzip`, `bytes vs text in gzip`, `zlib overview`, `streaming compression`

## MiniERP increment
Adds minierp.backup.snapshot_gz writing exports/snapshot.json.gz - the JSON snapshot from lesson 2 is now stored compressed, the first piece of the backup subsystem.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import gzip
import json

def write_json_gz(path, data: dict) -> None:
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        json.dump(data, f)

def read_json_gz(path) -> dict:
    ...

- **Test focus:** A dict round-trips through write_json_gz/read_json_gz; the .gz file is smaller than the plain JSON for repetitive data; gzip.compress/decompress round-trips raw bytes.

</div>
