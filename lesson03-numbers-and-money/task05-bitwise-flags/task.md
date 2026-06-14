# Bitwise operators and bit flags

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 3.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Combine, test, and clear boolean attributes packed into a single integer using masks
- Read and write shifts and understand << as multiply-by-power-of-two
- Use int.bit_count() to count set bits

## Python features introduced
`bitwise AND &`, `bitwise OR |`, `bitwise XOR ^`, `bitwise NOT ~`, `left shift <<`, `right shift >>`, `bit masks and 1 << n`, `int.bit_count() (popcount)`, `binary literals 0b...`

## MiniERP increment
Add a compact product-attribute flag system to `task.py` (a precursor to the later Users & Roles permission bitset): constants like TAXABLE, DISCOUNTABLE, RETURNABLE as 1<<n, plus `has_flag(flags, mask)`, `set_flag`, and `clear_flag`. Lets MiniERP store several product booleans in one int field.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** TAXABLE = 1 << 0
DISCOUNTABLE = 1 << 1
RETURNABLE = 1 << 2

def has_flag(flags: int, mask: int) -> bool:
    # TODO: use &
    raise NotImplementedError

def set_flag(flags: int, mask: int) -> int:
    # TODO: use |
    raise NotImplementedError

def clear_flag(flags: int, mask: int) -> int:
    # TODO: use & and ~
    raise NotImplementedError
- **Test focus:** Tests set/clear/test individual flags, verify combinations via |, confirm clear uses & ~mask without disturbing other bits, and may check int.bit_count() on a combined flag value.

</div>
