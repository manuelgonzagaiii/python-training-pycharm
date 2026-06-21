"""MiniERP discount and tax rules: the composable functions behind every total.

Money is integer cents. Discounts are whole-percent integers and tax is in basis
points (1 bp = 0.01%, so 825 bp = 8.25%), both applied with round-half-up so totals
stay exact to the cent. Every function here is pure -- no I/O, no shared state -- so
the dispatcher and all four front-ends share one rules engine.
"""


def apply_percent(price_cents: int, percent: int = 0) -> int:
    """Take `percent` percent off a price, rounded to the nearest cent.

    `percent` defaults to 0, so apply_percent(price) leaves the price unchanged --
    a default argument lets the common 'no discount' call omit the second value.
    """
    discount = (price_cents * percent + 50) // 100
    return price_cents - discount


def accumulate_discounts(amount: int, applied: list[int] | None = None) -> list[int]:
    """Append `amount` to a running list of applied discounts and return it.

    The default is None, not []. A default value is created ONCE, when the function
    is defined, so a mutable [] default would be SHARED by every call and grow
    across calls -- the classic mutable-default bug. The None-sentinel idiom makes
    a fresh list per call instead.
    """
    if applied is None:
        applied = []
    applied.append(amount)
    return applied
