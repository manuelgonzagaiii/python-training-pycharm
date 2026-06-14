# Annotate the Product Domain

> **Phase:** Modern Type System  •  **Stage:** 23.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write parameter and return annotations on __init__ and methods of Product
- Use PEP 585 built-in generic syntax (list[str], dict[str, int]) instead of typing.List/Dict
- Annotate instance attributes and dataclass fields with concrete types
- Run mypy/pyright mentally and reason about what each annotation promises

## Python features introduced
`variable annotations on attributes`, `function parameter and return annotations`, `PEP 585 built-in generics (list[str], dict[str, int])`, `annotating dataclass fields`, `-> None and -> bool returns`

## MiniERP increment
Product and its inventory-related collections (tags: list[str], a per-warehouse stock dict[str, int]) become fully annotated. This is the first typed domain class the rest of MiniERP will rely on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from dataclasses import dataclass, field

@dataclass
class Product:
    sku: str
    name: str
    price: float
    tags: list[str] = field(default_factory=list)
    stock_by_warehouse: dict[str, int] = field(default_factory=dict)

    def total_stock(self) -> int:
        ...  # TODO: sum the per-warehouse quantities

    def add_tag(self, tag: str) -> None:
        ...  # TODO: append tag
- **Test focus:** Tests assert total_stock() returns the int sum and add_tag mutates tags; a check inspects Product.__annotations__ / get_type_hints to confirm fields are annotated with built-in generic types (list[str], dict[str, int]).

</div>
