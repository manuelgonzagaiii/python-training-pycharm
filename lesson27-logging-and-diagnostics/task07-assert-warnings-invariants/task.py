"""assert, __debug__ & the warnings Module

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import warnings
from errors import ValidationError

class DeprecatedFieldWarning(UserWarning):
    """Raised when a caller uses a legacy field name."""

def apply_stock_delta(current: int, delta: int) -> int:
    if current + delta < 0:                 # user-facing condition -> raise
        raise ValidationError("insufficient stock", field="stock")
    result = current + delta
    assert result >= 0, "invariant: stock must never be negative"  # internal check
    # TODO: if a legacy field is in play elsewhere, warnings.warn(..., DeprecatedFieldWarning)
    return result
"""

# Your code here.
