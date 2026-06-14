"""Read-only config with MappingProxyType

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
from types import MappingProxyType

_SETTINGS: dict[str, object] = {
    "currency": "USD",
    "tax_rate": 0.08,
    "locale": "en_US",
}


def settings() -> MappingProxyType:
    """Return a read-only view of _SETTINGS."""
    raise NotImplementedError


def update_setting(key: str, value: object) -> None:
    """The only sanctioned mutation path (writes the backing dict)."""
    raise NotImplementedError

"""

# Your code here.
