"""TypedDict for Import/Export DTOs

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import TypedDict, NotRequired, Required

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
"""

# Your code here.
