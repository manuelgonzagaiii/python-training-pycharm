# Tax, discounts, and exact ratios with Fraction

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 3.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Represent a tax or discount rate as an exact ratio rather than a binary float
- Apply a rate to a money amount and round the result to cents once, at the end
- Understand when Fraction (exact ratio) vs Decimal (fixed decimal) is the right tool

## Python features introduced
`fractions.Fraction`, `Fraction(numerator, denominator)`, `Fraction.limit_denominator()`, `Fraction from Decimal`, `mixing Fraction and Decimal carefully`, `Decimal * Decimal for rates`, `quantize after multiply`, `as_integer_ratio()`

## MiniERP increment
Extend `task.py` with `apply_rate(amount, rate)` that multiplies a money Decimal by an exact rate and rounds to cents, and `tax_for(amount, percent)` built on Fraction (e.g. 8.25% as Fraction). MiniERP can now compute taxes and percentage discounts on invoices exactly.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal
from fractions import Fraction

def apply_rate(amount: Decimal, rate: Decimal) -> Decimal:
    """Multiply money by a rate and round to cents."""
    # TODO: round_money(amount * rate)
    raise NotImplementedError

def tax_for(amount: Decimal, percent: Fraction) -> Decimal:
    """Tax on `amount` given `percent` as a Fraction of 100."""
    # TODO: convert percent/100 and apply; round once at the end
    raise NotImplementedError
- **Test focus:** Tests check exact tax computations (e.g. 8.25% of 100.00 -> 8.25), single final rounding (no double-rounding drift), and that a discount + tax pipeline totals to the expected cent value.

</div>
