"""Integer-Like Objects with __index__

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import operator
from dataclasses import dataclass


@dataclass(slots=True, frozen=True, order=True)
class LineRef:
    """A 1-based reference to a line on an invoice/order.

    LineRef is *integer-like*: it implements __index__ so an instance can be
    used as a sequence index, in a slice, and as an argument to range(),
    bin(), hex(), oct(), and operator.index(). It does NOT define __int__,
    which proves the point: __index__ is the lossless integer protocol.
    """

    number: int  # human-facing, 1-based (line 1 is the first line)

    def __post_init__(self) -> None:
        # TODO: reject non-int / non-positive line numbers with a clear error.
        # A LineRef must be an exact, positive integer position.
        ...

    def __index__(self) -> int:
        # TODO: return the underlying int LOSSLESSLY.
        # This is what makes LineRef usable as lines[ref], in lines[a:b],
        # and in range(ref) / bin(ref) / hex(ref) / format(ref, '04x').
        ...

    @property
    def zero_based(self) -> int:
        """Index into 0-based internal storage (number - 1)."""
        ...

    @property
    def code(self) -> str:
        """Stable fixed-width hex line code for audit/export, e.g. 'L-000a'."""
        # Hint: f"L-{self:04x}" works *because* __index__ exists.
        ...

    def __repr__(self) -> str:
        ...


def line_at(lines: list, ref: LineRef):
    """Return the line a LineRef points to from 0-based storage.

    Use operator.index(ref) to coerce ref to a real int the library-author
    way; it raises TypeError if handed something that only defines __int__.
    """
    ...


def line_numbers(count: int) -> list:
    """Return [LineRef(1), ..., LineRef(count)] for a count of lines."""
    ...

"""

# Your code here.
