# Arithmetic, division, and divmod

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 3.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish / (always float) from // (floor) and use each deliberately
- Use divmod to get quotient and remainder in one call for packing/change-making
- Use 3-argument pow for modular arithmetic
- Predict results of mixed int/float arithmetic

## Python features introduced
`+ - * operators`, `true division /`, `floor division //`, `modulo %`, `divmod(a, b)`, `pow(base, exp) and ** operator`, `pow(base, exp, mod) 3-arg modular power`, `unary minus and abs()`, `operator precedence`, `round(number, ndigits)`

## MiniERP increment
Create the `task.py` quantity-math helpers MiniERP will reuse: `units_to_cases(units, per_case)` returns (full_cases, loose_units) via divmod, and `split_evenly(total, parts)` returns the base share and remainder for splitting an order. These pure functions start the shared inventory/packing math layer.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def units_to_cases(units: int, per_case: int) -> tuple[int, int]:
    """Return (full_cases, loose_units) for packing `units` into cases."""
    # TODO: use divmod
    raise NotImplementedError

def split_evenly(total: int, parts: int) -> tuple[int, int]:
    """Return (base_share, remainder) when splitting `total` across `parts`."""
    # TODO: use // and %
    raise NotImplementedError
- **Test focus:** Tests assert divmod-based packing (e.g. 27 units / 12 per case -> (2, 3)) and that base_share*parts + remainder == total, including edge cases like parts==1 and total==0.

</div>
