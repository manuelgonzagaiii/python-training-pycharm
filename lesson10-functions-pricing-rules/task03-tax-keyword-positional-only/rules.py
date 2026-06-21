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


def stack_discounts(price_cents: int, *percents: int, **options: object) -> int:
    """Apply each percent in *percents to the price in turn, then read options.

    *percents collects any number of positional discount percents into a tuple;
    **options collects any keyword options into a dict. Pass clamp_floor=True to
    floor the result at zero so an over-stacked discount never goes negative.
    """
    result = price_cents
    for percent in percents:
        result = apply_percent(result, percent)
    if options.get("clamp_floor"):
        result = result if result >= 0 else 0
    return result


def apply_tax(amount_cents: int, /, *, rate_bps: int, inclusive: bool = False) -> int:
    """Compute the tax on an amount, in cents, at a basis-point rate.

    `amount_cents` is positional-only (before the `/`): an internal value callers
    should not bind by an unstable keyword name. `rate_bps` and `inclusive` are
    keyword-only (after the `*`): they MUST be named, so apply_tax(price,
    rate_bps=825) reads clearly. With inclusive=True the amount already contains the
    tax, so the tax portion is extracted instead of added.
    """
    if inclusive:
        base = amount_cents * 10000 // (10000 + rate_bps)
        return amount_cents - base
    return (amount_cents * rate_bps + 5000) // 10000
