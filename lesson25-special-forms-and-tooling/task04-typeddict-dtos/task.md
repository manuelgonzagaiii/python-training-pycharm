# TypedDict for Import/Export DTOs

> **Phase:** Modern Type System  •  **Stage:** 25.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Model a JSON/CSV record shape with a class-based TypedDict and access keys with checked types
- Control optionality with total=False plus Required[...]/NotRequired[...] per key
- Choose TypedDict for boundary/serialized data and dataclass for in-memory domain objects
- Nest TypedDicts to model line items inside an invoice export

## Python features introduced
`typing.TypedDict`, `total=False`, `typing.Required`, `typing.NotRequired`, `functional and class-based TypedDict syntax`, `TypedDict vs dataclass trade-off`, `nested TypedDict`

## MiniERP increment
Defines ProductDTO, CustomerDTO and InvoiceDTO (with NotRequired optional fields and nested LineItemDTO) as the typed contract for the Import/Export module, so to_dict()/from_dict() round-trips are statically checked against the wire format.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import TypedDict, NotRequired, Required

class LineItemDTO(TypedDict):
    product_id: str
    qty: int
    unit_price: str  # Decimal serialized as string

class InvoiceDTO(TypedDict):
    number: str
    status: str
    lines: list[LineItemDTO]
    note: NotRequired[str]   # optional on the wire

def invoice_to_dto(inv: Invoice) -> InvoiceDTO:
    ...  # TODO: build the dict matching InvoiceDTO exactly
- **Test focus:** Tests round-trip an Invoice through invoice_to_dto and back, asserting required keys present, optional 'note' omitted when absent, and nested line items typed; a check confirms the dict matches the TypedDict shape.

</div>
