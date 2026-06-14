# Descriptor-Validated Fields: SKU, Money, NonNegative, Email (MILESTONE)

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 22.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build SKU, Money, NonNegative, and Email descriptors by overriding validate()
- Enforce invariants at assignment time, not just construction time
- Reuse one descriptor class across Product, Customer, and InvoiceLine

## Python features introduced
`subclassing a descriptor to specialize validate()`, `raising ValueError on invalid assignment`, `regex (re) for SKU/Email`, `decimal.Decimal for Money`, `type-checked & range-checked NonNegative`, `descriptors shared across multiple model classes`

## MiniERP increment
Delivers the phase milestone: descriptor-validated fields wired into the domain models. Product.sku = SKU(), Product.price = Money(), InvoiceLine.qty = NonNegative(), Customer.email = Email() — invalid values now raise on assignment everywhere, in every interface, with zero per-class boilerplate.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import re
from decimal import Decimal
from .fields import Field

class SKU(Field):
    PATTERN = re.compile(r"^[A-Z]{3}-\d{4}$")
    def validate(self, value: str) -> str:
        # TODO: raise ValueError if not PATTERN.fullmatch(value); return value
        ...

class Money(Field):
    def validate(self, value) -> Decimal:
        # TODO: coerce to Decimal, reject negatives / non-numeric
        ...

class NonNegative(Field):
    def validate(self, value: int) -> int: ...

class Email(Field):
    def validate(self, value: str) -> str: ...
- **Test focus:** Valid values assign and round-trip; each invalid value (bad SKU pattern, negative Money, negative qty, malformed Email) raises ValueError on assignment; the same descriptor enforces correctly on two different model classes.

</div>
