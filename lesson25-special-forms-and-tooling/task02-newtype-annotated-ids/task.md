# NewType & Annotated for IDs and Money

> **Phase:** Modern Type System  •  **Stage:** 25.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create distinct types with NewType (CustomerId, ProductId) so an int/str can't be passed where the wrong id is expected
- Attach machine-readable metadata to a type with Annotated[Decimal, Currency('USD')] without changing its runtime type
- Read Annotated metadata via get_type_hints(include_extras=True) for validation
- Understand NewType is zero-cost at runtime (just an identity function) but distinct to the checker

## Python features introduced
`typing.NewType`, `typing.Annotated`, `PEP 593 metadata`, `distinct nominal types over a base`, `attaching validation/units metadata`, `reading Annotated metadata at runtime`

## MiniERP increment
Introduces ProductId, CustomerId, InvoiceId NewTypes and a Money = Annotated[Decimal, ...] convention across the domain, so the service layer cannot accidentally swap a customer id for a product id and money fields carry currency/precision metadata used by validators and reporting.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import NewType, Annotated
from decimal import Decimal

ProductId = NewType('ProductId', str)
CustomerId = NewType('CustomerId', str)

class Currency:
    def __init__(self, code: str) -> None: self.code = code
Money = Annotated[Decimal, Currency('USD')]

def charge(customer: CustomerId, amount: Money) -> None:
    # TODO: record the charge; passing a ProductId here must be a type error
    ...
- **Test focus:** Tests confirm NewType wrappers behave as the base at runtime (ProductId('x') == 'x') and that Annotated metadata is recoverable via get_type_hints(include_extras=True); a documented case shows passing CustomerId where ProductId is required is a type error.

</div>
