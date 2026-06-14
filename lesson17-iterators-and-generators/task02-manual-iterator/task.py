"""A hand-written iterator over sales lines

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from dataclasses import dataclass

# `SaleLine` already exists in the domain model from earlier phases:
#   SaleLine(product_sku: str, qty: int, unit_price: float)

class SalesLineCursor:
    """A single-pass iterator over a sequence of SaleLine objects."""
    __slots__ = ("_lines", "_pos")

    def __init__(self, lines):
        self._lines = list(lines)
        self._pos = 0

    def __iter__(self):
        # TODO: an iterator's __iter__ should return itself
        ...

    def __next__(self):
        # TODO: return the next SaleLine, or raise StopIteration when exhausted
        ...

"""

# Your code here.
