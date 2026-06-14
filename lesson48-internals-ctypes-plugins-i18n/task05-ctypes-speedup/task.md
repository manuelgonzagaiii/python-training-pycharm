# An optional ctypes speed-up

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.5 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Load a C library and declare a function's argtypes/restype
- Define a ctypes.Structure mirroring a C struct layout
- Pass a Python buffer (array/memoryview) into C with from_buffer for in-place work
- Know when ctypes is appropriate and how cffi/Cython compare

## Python features introduced
`ctypes (CDLL/cdll)`, `ctypes.Structure (with _fields_)`, `argtypes/restype`, `ctypes from_buffer / passing a buffer pointer`, `ctypes.util.find_library`, `POINTER / c_int64 / c_double`, `cffi & Cython as OSS alternatives (note)`

## MiniERP increment
Delivers the optional ctypes speed-up: erp/fastsum.py sums the line-totals buffer via a C routine from the system C library (e.g. summing through a pointer), with a pure-Python fallback when the library is unavailable — fulfilling the optional-ctypes-speedup milestone without adding a paid dependency.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import array, ctypes, ctypes.util


class Pair(ctypes.Structure):
    _fields_ = [("lo", ctypes.c_int64), ("hi", ctypes.c_int64)]


def load_libc() -> ctypes.CDLL | None:
    """Load the C library via ctypes.util.find_library('c'); return None if absent."""
    raise NotImplementedError


def fast_sum(buf: array.array) -> int:
    """Sum int64 values in `buf`. Use ctypes over the buffer if available,
    else a pure-Python fallback. Must return the same result either way."""
    raise NotImplementedError

- **Test focus:** Tests fast_sum returns the correct total and equals the pure-Python sum for several arrays including empty; tests load_libc returns a CDLL or None gracefully; verifies the Structure _fields_ layout and that the function works whether or not the C library loads (fallback path is exercised).

</div>
