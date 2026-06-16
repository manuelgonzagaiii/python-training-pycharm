"""MiniERP's numeric core.

Pure helper functions, reused by every later interface (CLI, web, GUI, TUI).
This module grows across the lesson: it starts with the integer quantity math
an inventory needs and builds up to exact, cents-accurate Decimal money.
"""


def units_to_cases(units: int, per_case: int) -> tuple[int, int]:
    """Split a pile of `units` into (full_cases, loose_units).

    Example: 27 units packed 12 to a case is (2, 3) -- two full cases and three
    loose units. One call gives both the quotient and the remainder.
    """
    return divmod(units, per_case)


def split_evenly(total: int, parts: int) -> tuple[int, int]:
    """Split `total` across `parts`: return (base_share, remainder).

    Every part gets `base_share`; `remainder` parts get one extra so the shares
    add back up to `total`. Used later to divide an order across boxes or a bill
    across people.
    """
    base_share = total // parts
    remainder = total % parts
    return base_share, remainder


def running_total(prices: list[int]) -> int:
    """Add up a list of prices, accumulating the subtotal in place with +=."""
    total = 0
    for price in prices:
        total += price
    return total


def in_stock_range(qty: int, low: int, high: int) -> bool:
    """True when `qty` is between `low` and `high`, inclusive on both ends."""
    return low <= qty <= high


# Product attribute flags. Each is a single distinct bit, so several booleans
# fit in one integer field. (This is the same idea the Users & Roles permission
# bitset will use later.)
TAXABLE = 1 << 0
DISCOUNTABLE = 1 << 1
RETURNABLE = 1 << 2


def has_flag(flags: int, mask: int) -> bool:
    """True when every bit set in `mask` is also set in `flags`."""
    return flags & mask == mask


def set_flag(flags: int, mask: int) -> int:
    """Return `flags` with the bits in `mask` turned on."""
    return flags | mask


def clear_flag(flags: int, mask: int) -> int:
    """Return `flags` with the bits in `mask` turned off, leaving the rest alone."""
    return flags & ~mask
