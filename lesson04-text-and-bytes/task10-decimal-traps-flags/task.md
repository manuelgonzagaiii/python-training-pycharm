# Decimal context traps and signal flags: enforcing penny-exactness

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.10 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain the difference between a Decimal *signal* (a condition like Inexact or InvalidOperation), a *trap* (signals you have asked the context to raise as an exception), and a *flag* (a sticky record that a condition occurred even when not trapped).
- Turn a context trap on for a bounded region with localcontext() and ctx.traps[Inexact] = True, so that an operation that cannot be represented exactly raises instead of silently rounding.
- Use a trapped Inexact as control flow: attempt an exact equal split, and on Inexact fall back to a remainder-distribution algorithm.
- Read getcontext().flags after an untrapped operation to detect that rounding happened, and use ctx.clear_flags() to get a clean reading; understand that localcontext() isolates flags so the surrounding program is unaffected.
- Intentionally raise/catch InvalidOperation to validate user-supplied money strings, translating it into a domain-meaningful ValueError.
- Appreciate why production financial code enforces exactness: a payment allocation must sum back to the original total to the cent, with no money invented or lost.

## Python features introduced
`decimal.localcontext as a parenthesized context manager`, `decimal context traps mapping: ctx.traps[Inexact] = True`, `decimal signals/exceptions: Inexact, InvalidOperation, DivisionByZero, Rounded`, `intentionally raising InvalidOperation (and catching it to re-raise ValueError)`, `reading and clearing accumulated condition flags: getcontext().flags, ctx.flags[Inexact], ctx.clear_flags()`, `the difference between a trapped signal (raises) and an untrapped signal (sets a flag, returns a rounded result)`, `Decimal.quantize with an explicit rounding mode (ROUND_DOWN) for floor-to-cents`, `Decimal.to_integral_value for exact integer extraction`, `try/except inside a context manager; control flow that falls back on a caught signal`, `PEP 604 return annotations (list[Decimal]), walrus operator, f-string '=' self-documenting debug output`

## MiniERP increment
Adds penny-exact money helpers to the MiniERP money module that Sales & Invoicing and Payments depend on. (1) parse_money(text) parses a user/import-supplied amount by trapping nothing extra but catching the default-trapped InvalidOperation and re-raising it as a clear ValueError('not valid money: ...') — this is the first place the ERP deliberately exercises InvalidOperation, the signal later phases only reference. (2) split_payment(total, parts) splits an invoice total across N installments/line items: it first attempts an exact equal share inside localcontext() with traps[Inexact] = True, and only if that raises Inexact does it fall back to a largest-remainder allocation (floor each share with ROUND_DOWN, then hand out the leftover cents one at a time) so the shares always sum back to the original total exactly. (3) had_rounding(total, parts) reports, via getcontext().flags[Inexact] after a cleared-flag division, whether an even split would have lost precision — letting reporting flag invoices that don't divide cleanly. These build only on the Decimal money quantization/rounding work from the earlier decimal-money task; no classes or custom exception types are required yet.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import (
    Decimal, localcontext, getcontext,
    Inexact, InvalidOperation, ROUND_DOWN,
)

CENTS = Decimal("0.01")  # 2-decimal money quantum, as in the earlier decimal-money stage


def parse_money(text: str) -> Decimal:
    """Parse a money string to a cent-quantized Decimal.

    Decimal('not-a-number') raises InvalidOperation (it is trapped by default in
    the standard context). Catch it and re-raise a domain ValueError so callers
    in Sales & Invoicing get a clear message instead of a raw decimal signal.
    """
    try:
        return Decimal(text).quantize(CENTS)
    except InvalidOperation:
        raise ValueError(f"not valid money: {text!r}")


def split_payment(total: Decimal, parts: int) -> list[Decimal]:
    """Split `total` across `parts` shares that sum back to `total` exactly.

    Step 1 — try an exact equal split. Inside localcontext() set
    ``ctx.traps[Inexact] = True`` so that ``(total / parts).quantize(CENTS)``
    RAISES Inexact when the division cannot be represented exactly in cents.
    If it does not raise, return ``[share] * parts``.

    Step 2 — on Inexact, fall back to largest-remainder allocation:
    floor each share with ``.quantize(CENTS, rounding=ROUND_DOWN)``, then
    distribute the leftover cents (total - floored_sum) one cent at a time to
    the first shares. The returned list MUST sum to `total` exactly.
    """
    # TODO: implement Step 1 (trap Inexact) and Step 2 (remainder distribution).
    raise NotImplementedError


def had_rounding(total: Decimal, parts: int) -> bool:
    """Return True if an even split of `total` across `parts` would lose precision.

    Do NOT trap anything. Inside localcontext(): clear_flags(), perform the
    division (no quantize), then read ``ctx.flags[Inexact]``. Because the
    context is local, the surrounding program's flags are untouched.
    """
    # TODO: clear flags, divide, then return the Inexact flag's value.
    raise NotImplementedError


if __name__ == "__main__":
    total = parse_money("100.00")
    for n in (4, 3):
        shares = split_payment(total, n)
        print(f"{total} / {n} -> {[str(s) for s in shares]}  {sum(shares)=}  {had_rounding(total, n)=}")

- **Test focus:** Verify the trap/flag machinery end to end. (1) parse_money: valid strings quantize to 2dp ('19.5' -> Decimal('19.50')); invalid strings ('twelve', '') raise ValueError (not a bare InvalidOperation leaking out). (2) split_payment: an exact case ('100.00', 4) returns four equal Decimal('25.00') shares; an inexact case ('100.00', 3) returns ['33.34','33.33','33.33']; assert across several totals/parts (incl. '9.99'/2, '0.10'/3) that sum(shares) == total EXACTLY and len(shares) == parts and every share is cent-quantized. (3) had_rounding: True for ('100.00', 3) and False for ('100.00', 4). (4) Isolation check: call getcontext().clear_flags(), invoke had_rounding/split_payment, and assert getcontext().flags[Inexact] is still False afterward — proving localcontext() did not leak signal flags into the global context. Optionally assert that an exact split_payment did not need the remainder fallback by checking the shares are all identical.

</div>
