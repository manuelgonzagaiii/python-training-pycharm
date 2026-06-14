# Binary Records: struct, array & memoryview

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.8 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Pack numbers and fixed-length text into a compact binary record with struct
- Choose byte order and alignment with format-string prefixes
- Use array.array for homogeneous numeric data and memoryview for zero-copy slicing
- Read a record file with Struct.iter_unpack

## Python features introduced
`struct.pack / unpack / calcsize`, `format strings & byte-order (<>!=)`, `struct.Struct compiled object`, `array.array typed buffers`, `memoryview`, `buffer protocol`, `iter_unpack`, `fixed-width record files`

## MiniERP increment
Adds minierp/io/binfmt.py: a compact fixed-width inventory-snapshot format (sku[16s], qty[i], price-cents[q]) packed with struct.Struct, giving MiniERP a tiny portable binary cache read with iter_unpack and sliced via memoryview.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import struct

REC = struct.Struct('<16s i q')  # sku, qty, price_cents

def pack_row(sku: str, qty: int, price_cents: int) -> bytes:
    return REC.pack(sku.encode().ljust(16, b'\x00'), qty, price_cents)

def unpack_all(blob: bytes):
    ...  # REC.iter_unpack(blob)

- **Test focus:** pack_row produces calcsize(REC.format)-length records; iter_unpack restores rows; sku padding is stripped on read; a memoryview slice exposes one record without copying; array.array round-trips numeric data.

</div>
