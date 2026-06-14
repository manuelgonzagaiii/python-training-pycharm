# Protocols & Structural Typing

> **Phase:** Modern Type System  •  **Stage:** 24.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define a Protocol that describes required methods/attributes without any inheritance relationship
- See that any class with a matching shape satisfies the Protocol structurally (no 'implements' needed)
- Apply @runtime_checkable to enable isinstance() checks and know its limits (shape-only, not signature)
- Compare Protocol (structural) to ABC (nominal) and pick Protocol for cross-cutting service boundaries

## Python features introduced
`typing.Protocol`, `structural (duck) typing`, `Protocol with methods and attributes`, `@runtime_checkable`, `isinstance against a runtime-checkable Protocol`, `Protocol vs ABC`

## MiniERP increment
Introduces SupportsTotal (anything with total() -> Decimal) and Persisted (has .id and .to_dict()) protocols. Invoice, Payment and Product satisfy them structurally, so reporting can total anything 'totalable' across modules without a shared base class.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import Protocol, runtime_checkable
from decimal import Decimal

@runtime_checkable
class SupportsTotal(Protocol):
    def total(self) -> Decimal: ...

def grand_total(items: list[SupportsTotal]) -> Decimal:
    # TODO: sum item.total() across items
    ...

# Invoice and Payment already have .total(); they satisfy this with NO inheritance.
- **Test focus:** Tests pass a mix of Invoice/Payment-like objects (structurally matching) to grand_total and assert the summed Decimal; an isinstance(obj, SupportsTotal) check confirms @runtime_checkable behavior, and a shape-mismatch object is rejected.

</div>
