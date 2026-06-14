# The buffer protocol & memoryview

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.4 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Wrap binary ERP data in a memoryview to slice it without copying
- Understand zero-copy semantics and why it matters for large import files
- Cast a memoryview between formats and read sizes
- Prepare contiguous numeric buffers for handing to C code next task

## Python features introduced
`memoryview`, `buffer protocol`, `bytearray / bytes`, `memoryview slicing (zero-copy)`, `memoryview.cast / .tobytes / .nbytes`, `struct (pack/unpack) interop`, `array.array as a buffer source`

## MiniERP increment
The bulk import/export path gains zero-copy parsing: fixed-width binary inventory records are sliced via memoryview over a bytearray instead of copying substrings, and a contiguous array.array of line totals is prepared for the ctypes speed-up.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import array


def chunk(buf: bytearray, size: int) -> list[memoryview]:
    """Return zero-copy memoryview slices of `buf`, each `size` bytes (last may be shorter)."""
    raise NotImplementedError


def totals_buffer(values: list[int]) -> array.array:
    """Return a contiguous array('q') of the values (a C-compatible buffer)."""
    raise NotImplementedError

- **Test focus:** Tests chunk returns memoryview slices that are views (mutating the bytearray is visible through them) of the right lengths; tests totals_buffer produces an array whose memoryview reports the expected nbytes/format for handing to ctypes.

</div>
