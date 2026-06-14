# Bytes, bytearray, memoryview, and codecs

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.8 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Convert between str and bytes with explicit encodings and error policies
- Use bytearray for in-place mutation and memoryview for zero-copy slicing
- Serialize a record to bytes (and base64/hex) for storage and export

## Python features introduced
`bytes literals b'...'`, `str.encode / bytes.decode`, `UTF-8 and other codecs (latin-1, ascii)`, `encode errors (errors='strict'/'replace'/'ignore')`, `bytearray (mutable)`, `memoryview (zero-copy view)`, `bytes.hex() / bytes.fromhex()`, `base64 module`, `codecs module intro`, `len(bytes) vs len(str) for non-ASCII`

## MiniERP increment
Add MiniERP's serialization primitives to `task.py`: `encode_record(text)` UTF-8 encodes a record line to bytes for the file store, `decode_record(data)` reverses it, and `to_b64(text)`/`from_b64(s)` produce a transport-safe form for the future import/export module. Completes the phase's storage-ready text+bytes foundation.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import base64

def encode_record(text: str) -> bytes:
    """UTF-8 encode a record for the byte store."""
    # TODO: text.encode("utf-8")
    raise NotImplementedError

def decode_record(data: bytes) -> str:
    """Decode UTF-8 bytes back to text."""
    # TODO: data.decode("utf-8")
    raise NotImplementedError

def to_b64(text: str) -> str:
    """Base64 (ASCII) form of the UTF-8 bytes."""
    # TODO: base64.b64encode(text.encode()).decode('ascii')
    raise NotImplementedError
- **Test focus:** Tests round-trip encode/decode on non-ASCII text (e.g. 'café'), confirm len(bytes) != len(str) for multibyte chars, verify base64/hex round-trips, and check that errors='replace' vs 'strict' behave as documented.

</div>
