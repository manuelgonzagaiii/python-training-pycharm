# The format-spec mini-language

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.4 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build aligned, fixed-width, zero-padded columns with format specs
- Format currency with thousands separators and two decimals
- Use dynamic (nested) width/precision fields

## Python features introduced
`format-spec mini-language inside f-strings`, `alignment < > ^ and fill chars`, `width and precision .Nf`, `thousands separators , and _`, `sign control +/-/space`, `type codes f d x o b e %`, `{value:>{width}} dynamic width`, `padding numbers with 0`, `format() builtin`

## MiniERP increment
Add MiniERP currency/column formatters to `task.py`: `fmt_money(amount)` renders a Decimal as `$1,234.50`, and `fmt_col(text, width, align)` produces aligned table cells. These power the CLI tables, receipts, and reports across the ERP.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal

def fmt_money(amount: Decimal) -> str:
    """Format as $#,##0.00 using the format-spec mini-language."""
    # TODO: f"${amount:,.2f}"
    raise NotImplementedError

def fmt_col(text: str, width: int, align: str = "<") -> str:
    """Pad/align text to width; align is '<', '>', or '^'."""
    # TODO: f"{text:{align}{width}}"
    raise NotImplementedError
- **Test focus:** Tests check thousands separators and 2-decimal precision (1234.5 -> '$1,234.50'), each alignment mode, dynamic width, and zero-padding behavior.

</div>
