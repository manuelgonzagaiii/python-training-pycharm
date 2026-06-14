# f-strings and self-documenting debug output

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.3 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Interpolate expressions and method calls directly inside f-strings
- Use the {expr=} self-documenting form for debugging and logging
- Apply !r/!s/!a conversions inside an f-string

## Python features introduced
`f-string interpolation`, `f-string expression evaluation {a+b}`, `self-documenting f-strings {value=}`, `nested quotes in f-strings`, `f-string with method calls {name.upper()}`, `multiline f-strings`, `conversion flags !r !s !a in f-strings`, `f-string over Decimal`

## MiniERP increment
Add `task.py` line-rendering helpers used by MiniERP logging and the future CLI: `debug_line(sku, qty, price)` emits a self-documenting `f"{sku=} {qty=} {price=}"` audit string, and `receipt_line(name, total)` interpolates a Decimal money value into a human line. Foundation for the CLI/receipt output.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal

def debug_line(sku: str, qty: int, price: Decimal) -> str:
    """Self-documenting debug string: sku='...' qty=... price=..."""
    # TODO: f"{sku=} {qty=} {price=}"
    raise NotImplementedError

def receipt_line(name: str, total: Decimal) -> str:
    """Render 'NAME: $TOTAL' using an f-string."""
    # TODO: f-string interpolation
    raise NotImplementedError
- **Test focus:** Tests assert the exact self-documenting layout (e.g. "sku='AB-1' qty=3 price=9.99"), correct !r quoting, and that Decimal totals appear verbatim in the rendered line.

</div>
