"""Self, Never & LiteralString

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import Self, Never, LiteralString, assert_never

class InvoiceBuilder:
    def with_customer(self, c: CustomerId) -> Self:
        ...  # TODO: set and return self
    def with_line(self, p: ProductId, qty: int) -> Self:
        ...  # TODO: append and return self

def handle(status: Status) -> str:
    match status:
        case 'draft' | 'sent' | 'paid' | 'void':
            return status
        case _ as unreachable:
            assert_never(unreachable)  # Never

def sql(fragment: LiteralString) -> None: ...  # rejects f-strings built from user input
"""

# Your code here.
