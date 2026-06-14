"""Closures and the Late-Binding Gotcha

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: def make_coupon(percent: float):
    """Return a closure price->discounted_price capturing percent."""
    def coupon(price: float) -> float:
        ...
    return coupon


def build_coupon_table(percents: list[float]) -> list:
    """Return a list of coupon closures. Avoid the late-binding gotcha."""
    # WRONG: [lambda p: p*(1-pct) for pct in percents]  # all share final pct
    ...
"""

# Your code here.
