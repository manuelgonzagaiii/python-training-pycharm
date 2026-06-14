# base64: Binary Inside Text

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.9 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Encode arbitrary bytes as ASCII-safe base64 text and decode them back
- Use URL-safe alphabet for tokens/filenames
- Understand base64 size overhead and padding
- Embed a small binary blob (the struct snapshot) inside a JSON/text field

## Python features introduced
`base64.b64encode / b64decode`, `urlsafe_b64encode / b64decode`, `base64.b32/b16`, `bytes <-> ascii str boundary`, `binascii.Error handling`, `padding rules`, `embedding binary blobs in JSON`

## MiniERP increment
Adds minierp.io.blob helpers so the struct inventory snapshot can be base64-embedded inside the JSON snapshot's 'inventory_blob' field, letting one JSON export carry both human-readable rows and the compact binary cache.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import base64

def to_b64(data: bytes) -> str:
    return base64.b64encode(data).decode('ascii')

def from_b64(text: str) -> bytes:
    ...

def to_urlsafe(data: bytes) -> str:
    ...

- **Test focus:** Round-trip arbitrary bytes through to_b64/from_b64; urlsafe output contains no + or /; decoding malformed input raises binascii.Error; a struct blob survives embedding in and extraction from a dict.

</div>
