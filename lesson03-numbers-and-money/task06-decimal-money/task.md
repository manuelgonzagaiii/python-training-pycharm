# Modeling money with Decimal

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 3.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Construct Decimal from strings to preserve exact decimal values
- Set and read the decimal context and choose an explicit rounding mode for money
- Quantize amounts to two decimal places (cents) deterministically
- Explain why Decimal('0.1') + Decimal('0.2') == Decimal('0.3')

## Python features introduced
`decimal.Decimal`, `Decimal from str vs float (why str)`, `decimal.getcontext()`, `decimal.localcontext()`, `ROUND_HALF_UP / ROUND_HALF_EVEN rounding modes`, `Decimal.quantize()`, `Decimal exact arithmetic`, `Decimal('0.01') cent unit`, `context precision (prec)`

## MiniERP increment
Establish MiniERP's canonical money representation in `task.py`: `money(value)` builds a Decimal from a string/int safely, and `round_money(amount)` quantizes to cents with a documented rounding mode. This is the money foundation every monetary value in the ERP will pass through from now on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")

def money(value: str | int) -> Decimal:
    """Build an exact money Decimal. Reject float input."""
    # TODO: Decimal(str(value)); raise on float
    raise NotImplementedError

def round_money(amount: Decimal) -> Decimal:
    """Quantize to cents using ROUND_HALF_UP."""
    # TODO: amount.quantize(CENTS, rounding=ROUND_HALF_UP)
    raise NotImplementedError
- **Test focus:** Tests assert money('0.1')+money('0.2')==money('0.3'), that float input is rejected, and that round_money applies ROUND_HALF_UP correctly (e.g. 2.005 -> 2.01) and produces exactly two decimal places.

</div>
