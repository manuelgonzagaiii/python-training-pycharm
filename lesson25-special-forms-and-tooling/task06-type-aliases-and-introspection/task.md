# PEP 695 type Aliases & Hint Introspection

> **Phase:** Modern Type System  •  **Stage:** 25.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define reusable aliases with the modern 'type' statement (type Money = Annotated[Decimal, ...]; type Sku = str)
- Write generic aliases (type Page[T] = list[T]) and use them across the service layer
- Introspect annotations at runtime with get_type_hints (resolving strings and forward refs) and include_extras for Annotated metadata
- Know type-statement aliases are lazily evaluated TypeAliasType objects, not plain assignments

## Python features introduced
`PEP 695 'type' statement`, `type Alias = ...`, `generic type aliases (type Pair[T] = ...)`, `typing.get_type_hints`, `include_extras=`, `__annotations__ introspection`, `TypeAliasType`

## MiniERP increment
Centralizes the project's type vocabulary into one aliases module via the 'type' statement (Money, Sku, CustomerRef, Page[T], Result aliases) and adds an introspection-driven validator that reads get_type_hints(include_extras=True) to enforce Annotated metadata (currency/precision) at import — unifying the domain's type language.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal
from typing import Annotated, get_type_hints

type Sku = str
type Money = Annotated[Decimal, 'currency=USD']
type Page[T] = list[T]

def first_page[T](items: list[T], size: int) -> Page[T]:
    ...  # TODO: return items[:size]

def field_types(cls: type) -> dict[str, object]:
    return get_type_hints(cls, include_extras=True)  # resolves strings + keeps Annotated
- **Test focus:** Tests use Page[T]/first_page at multiple element types and assert slicing; field_types(Invoice) is checked to resolve stringized annotations and preserve Annotated metadata; an isinstance(Money, TypeAliasType)-style check documents the alias object.

</div>
