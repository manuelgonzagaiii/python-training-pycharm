"""Default Arguments and the Mutable-Default Gotcha

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: def apply_percent(price: float, percent: float = 0.0) -> float:
    """Reduce price by percent (0..1). Default percent leaves price unchanged."""
    ...


def accumulate_discounts(amount: float, applied: list[float] | None = None) -> list[float]:
    """Append amount to a per-call history list. Use the None sentinel, NOT a mutable default."""
    if applied is None:
        applied = []
    ...
"""

# Your code here.
