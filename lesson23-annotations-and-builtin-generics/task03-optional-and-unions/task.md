# Optional, Union & the | Operator

> **Phase:** Modern Type System  •  **Stage:** 23.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Express a nullable field three ways and know that Optional[T] == T | None == Union[T, None]
- Prefer the modern PEP 604 pipe syntax (X | Y, T | None) over typing.Optional/Union
- Handle a multi-type field (e.g. a discount that is a percentage float or a fixed Decimal) with a union and narrow it before use
- Understand that a union value must be narrowed (if/isinstance/match) before type-specific operations

## Python features introduced
`Optional[T]`, `Union[A, B]`, `PEP 604 X | Y union syntax`, `T | None`, `None as a type`, `isinstance narrowing with match/case and if`

## MiniERP increment
Customer gains optional fields (email: str | None, phone: str | None) and Product gains a discount that is float | None now and will widen later. Service lookups start returning Product | None for 'not found', establishing the project-wide not-found convention.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: str
    name: str
    email: str | None = None
    phone: str | None = None

    def contact_label(self) -> str:
        # TODO: return email if present, else phone if present, else 'no contact'
        ...

def find_product(products: list, sku: str):  # TODO: annotate -> Product | None
    ...
- **Test focus:** Tests cover all branches of contact_label (email present, only phone, neither) and that find_product returns a Product or None; an annotation check confirms the return type uses a union with None.

</div>
