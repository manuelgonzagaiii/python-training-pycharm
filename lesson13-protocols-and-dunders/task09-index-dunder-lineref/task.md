# Integer-Like Objects with __index__

> **Phase:** OOP Foundations  •  **Stage:** 13.9 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain why __index__ exists separately from __int__: it promises a *lossless* integer (no rounding/truncation), so Python trusts it for positions, slices, and base conversions where a float would be nonsense.
- Implement __index__ on a domain value object so an instance can be used directly as a list/tuple index (lines[ref]), inside a slice (lines[a:b]), and as an argument to range(), bin(), hex(), and oct().
- Use operator.index(x) as the library-author way to coerce 'something integer-like' to a real int, and know it raises TypeError (not a silent truncation) when the object only defines __int__.
- Distinguish the three integer-ish protocols: __int__ (may lose information, used by int()), __index__ (lossless, used by indexing/slicing/bin/hex/oct/range), and plain construction.
- Apply this in the ERP: build a 1-based LineRef value object that indexes 0-based storage correctly and renders as a fixed-width hex code in audit output.

## Python features introduced
`__index__`, `operator.index`, `difference between __index__ and __int__ (lossless integer-only conversion)`, `objects usable as sequence indices (seq[obj]) and in slices (seq[obj:obj])`, `bin() / hex() / oct() / format(x, 'b'|'x'|'o') accepting __index__ objects`, `range(start, stop, step) and itertools/range arguments via __index__`, `operator.index() as the canonical 'give me a real int, losslessly' protocol`, `TypeError raised by operator.index when __index__ is absent (vs silent __int__ truncation)`, `dataclasses with slots=True, frozen=True`, `__post_init__ validation`, `comparison via @functools.total_ordering or explicit __eq__/__lt__`, `__repr__ and __str__ on a value object`, `raising TypeError/ValueError with informative messages`

## MiniERP increment
Adds a LineRef integer-like value object to the Sales/Invoicing domain and wires it into the line-item container built earlier in p05 (the Invoice/order that already implements __len__/__bool__). LineRef wraps a human-facing 1-based line number for an invoice line. Because it implements __index__, a LineRef can index the invoice's 0-based internal line storage directly (invoice.line_at(ref) does lines[operator.index(ref) - 1] or, after offset, lines[ref]), appear in slices when printing a range of lines, and be passed to range() when iterating line numbers. The same __index__ powers a stable, fixed-width hex line code (e.g. format(ref, '04x') -> 'L-000a') used in the audit log and export so every line has a compact machine code. LineRef deliberately does NOT define __int__-only behavior: it defines __index__, so operator.index works and float-style truncation is impossible — guaranteeing invoice line positions are always exact integers. This turns 'which line?' from a bare int passed around into a validated, self-describing domain type that still behaves like an int everywhere a position is needed.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import operator
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

- **Test focus:** Verify __index__ is the lossless integer protocol and is correctly wired into ERP line addressing. (1) A LineRef instance indexes a real list directly: ['a','b','c'][LineRef(1).zero_based] == 'a', and slicing with derived ints works. (2) operator.index(LineRef(10)) == 10 and returns a real int. (3) bin/hex/oct/format accept a LineRef: hex(LineRef(10)) == '0xa', format(LineRef(10), '04x') == '000a', LineRef(10).code == 'L-000a'. (4) range(LineRef(3)) == range(3) -> consumes to [0,1,2], and LineRef works as a range bound. (5) Crucially, LineRef does NOT define __int__: assert that calling int(LineRef(5)) still works *only because __index__ is the fallback for int()* (int() honors __index__) but that a sibling Bad class defining only __int__ raises TypeError under operator.index(Bad()) — proving __index__ != __int__. (6) line_at(lines, ref) returns the correct 0-based element and raises TypeError when passed a float-like/only-__int__ object. (7) __post_init__ rejects LineRef(0), LineRef(-1), and non-int numbers with ValueError/TypeError. (8) line_numbers(3) == [LineRef(1), LineRef(2), LineRef(3)] and ordering/equality (frozen+order dataclass) behave.

</div>
