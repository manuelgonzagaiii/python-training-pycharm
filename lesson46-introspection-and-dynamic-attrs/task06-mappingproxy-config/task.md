# Read-only config with MappingProxyType

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.6 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Hand out a config mapping that callers can read but not mutate
- Understand a proxy is a live view, not a frozen copy
- Choose MappingProxyType over copy.deepcopy for cheap immutability
- Recognize mappingproxy as the type behind every class __dict__

## Python features introduced
`types.MappingProxyType`, `read-only mapping views`, `TypeError on write attempts`, `mapping protocol (keys/items/__getitem__)`, `shallow-view semantics vs copy`, `class __dict__ is a mappingproxy (note)`

## MiniERP increment
erp/config.py exposes settings() returning a MappingProxyType over the loaded ERP settings (currency, tax rate, locale) so front-ends and plugins can read configuration but cannot corrupt it.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
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

- **Test focus:** Tests settings() supports reads (indexing, keys, items); asserts assignment/deletion through the proxy raises TypeError; asserts update_setting changes the backing dict and is reflected live in a previously-returned proxy view.

</div>
