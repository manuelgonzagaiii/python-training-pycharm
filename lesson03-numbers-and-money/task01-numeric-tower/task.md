# The numeric tower: int, float, bool, complex

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 3.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that Python int has unbounded precision while float is a fixed-width binary double
- Know that bool is a subclass of int (True == 1) and where that helps and hurts
- Recognize complex as a first-class numeric type and when it is irrelevant to business code
- Read integer literals in hex, octal, binary, and with digit-group underscores

## Python features introduced
`int (arbitrary precision)`, `float (IEEE-754 double)`, `bool as int subclass`, `complex literals (3+4j)`, `int/float/bool/complex constructors`, `type()`, `isinstance()`, `numbers ABC hierarchy intro`, `int methods: .bit_length()`, `underscores in numeric literals (1_000_000)`, `0x/0o/0b integer literal prefixes`

## MiniERP increment
Read-only concept page framed around MiniERP: explains why we will choose specific numeric types for quantities (int), money (Decimal, coming soon), and never complex. No code changes to the shared module yet; sets up the design decisions for the rest of the phase.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Concept page only. Sample snippets the learner can run in the console:
#   big = 2 ** 200            # int never overflows
#   print(big.bit_length())
#   print(True + True)        # 2  -> bool is an int
#   print(0xFF, 0o17, 0b1010, 1_000_000)
#   z = 3 + 4j; print(z.real, z.imag, abs(z))
# No task.py edits required for this theory task.
- **Test focus:** No automated checks (theory page). Comprehension is reinforced by the following choice task.

</div>
