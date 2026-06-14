"""Class Patterns with __match_args__

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class PriceRequest:
    sku: str
    qty: int


def describe(req: object) -> str:
    """Render a summary using class patterns over request dataclasses."""
    match req:
        case PriceRequest(sku=s, qty=q):
            ...
        case _:
            return "unknown request"
"""

# Your code here.
