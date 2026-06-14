"""An optional ctypes speed-up

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
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

"""

# Your code here.
