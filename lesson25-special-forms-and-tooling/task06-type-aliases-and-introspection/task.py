"""PEP 695 type Aliases & Hint Introspection

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from decimal import Decimal
from typing import Annotated, get_type_hints

type Sku = str
type Money = Annotated[Decimal, 'currency=USD']
type Page[T] = list[T]

def first_page[T](items: list[T], size: int) -> Page[T]:
    ...  # TODO: return items[:size]

def field_types(cls: type) -> dict[str, object]:
    return get_type_hints(cls, include_extras=True)  # resolves strings + keeps Annotated
"""

# Your code here.
