"""The buffer protocol & memoryview

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import array


def chunk(buf: bytearray, size: int) -> list[memoryview]:
    """Return zero-copy memoryview slices of `buf`, each `size` bytes (last may be shorter)."""
    raise NotImplementedError


def totals_buffer(values: list[int]) -> array.array:
    """Return a contiguous array('q') of the values (a C-compatible buffer)."""
    raise NotImplementedError

"""

# Your code here.
