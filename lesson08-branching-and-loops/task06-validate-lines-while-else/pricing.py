"""MiniERP pricing engine: tiered prices, cart totals, and line checks.

Money is integer cents everywhere (never float), the same representation the
catalog uses. Discounts are whole-percent integers applied with round-half-up,
so totals stay exact to the cent. Every function here is pure -- no input,
output, or shared state -- which is what lets the command dispatcher and all four
front-ends reuse the same business rules.
"""


def quantity_tier(qty: int) -> str:
    """Classify an order quantity into a discount tier.

    Bands: 1-9 -> 'none', 10-49 -> 'bulk', 50 and up -> 'wholesale'. An
    if/elif/else runs only its first matching branch, so each test can assume the
    ones above it already failed -- that is why a plain `qty < 50` is enough for
    the bulk band without also writing `qty >= 10`.
    """
    if qty <= 0:
        raise ValueError("qty must be positive")
    if qty < 10:
        return "none"
    elif qty < 50:
        return "bulk"
    else:
        return "wholesale"


_TIER_DISCOUNT = {"none": 0, "bulk": 5, "wholesale": 10}  # whole percent off, per tier


def unit_price_for(base_price_cents: int, qty: int) -> int:
    """Per-unit price in cents after the quantity-tier discount.

    Reuses quantity_tier to pick the band, looks up that band's whole-percent
    discount, and takes it off the base price, rounded to the nearest cent.
    """
    percent = _TIER_DISCOUNT[quantity_tier(qty)]
    return base_price_cents - (base_price_cents * percent + 50) // 100


def display_price(price_cents: int, currency: str = "USD") -> str:
    """Render an integer-cent price for display, e.g. 1500 -> '$15.00'.

    Picks the currency mark with a conditional expression (a ternary): '$' for
    USD, otherwise the ISO code and a space, e.g. 'EUR 15.00'. A ternary is an
    expression, so its result can be assigned in one line -- shorter than a
    four-line if/else when each branch is just a value.
    """
    symbol = "$" if currency == "USD" else f"{currency} "
    return f"{symbol}{price_cents // 100}.{price_cents % 100:02d}"


def clamp_floor(price_cents: int) -> int:
    """Clamp a computed price up to zero so stacked discounts never go negative."""
    return price_cents if price_cents >= 0 else 0


def cart_subtotal(lines: list[tuple[str, int, int]]) -> int:
    """Total a cart of (sku, base_price_cents, qty) lines, in cents.

    Iterates the lines, prices each unit at its quantity tier, and accumulates
    qty * unit price into a running subtotal -- the classic accumulator pattern.
    """
    subtotal = 0
    for sku, base_price_cents, qty in lines:
        subtotal += qty * unit_price_for(base_price_cents, qty)
    return subtotal


def all_lines_valid(lines: list[tuple[str, int, int]]) -> bool:
    """True only if every cart line is valid: qty > 0 and base price >= 0.

    Walks the lines with an index-driven while loop and breaks on the first bad
    line. The loop's own `else` runs only if the loop finished WITHOUT breaking,
    which is exactly 'no bad line was found' -- so the else returns True and the
    line after the loop returns False.
    """
    i = 0
    while i < len(lines):
        sku, base_price_cents, qty = lines[i]
        if qty <= 0 or base_price_cents < 0:
            break
        else:
            pass  # a valid line -- nothing to do, just advance
        i += 1
    else:
        return True
    return False
