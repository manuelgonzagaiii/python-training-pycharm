"""Decimal context traps and signal flags: enforcing penny-exactness

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from decimal import (
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

"""

# Your code here.
