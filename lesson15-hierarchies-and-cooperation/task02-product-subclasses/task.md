# Physical, Digital & Bundle Products

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 15.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Add subclass-specific state (weight/shipping for physical, download size for digital, components for bundle) while reusing the base via super()
- Override price() to add shipping or apply a bundle discount, calling super().price() for the base amount
- Use isinstance for type-directed logic and understand polymorphic dispatch
- Model composition: a BundleProduct contains other Products

## Python features introduced
`subclassing with extra fields`, `super().__init__ with extra args`, `overriding price() with super()`, `isinstance / issubclass`, `polymorphism`, `composition (bundle holds products)`

## MiniERP increment
Completes the Product hierarchy: PhysicalProduct (adds weight/shipping cost), DigitalProduct (no shipping), BundleProduct (sum of components minus discount). Inventory can now hold mixed product types behind one interface.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from product import Product
from money import Money


class PhysicalProduct(Product):
    def __init__(self, *args, shipping: Money, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.shipping = shipping

    def price(self) -> Money:
        # TODO: base price plus shipping
        ...


class BundleProduct(Product):
    # TODO: hold a list of (Product, qty); price() = discounted sum of components
    ...

- **Test focus:** PhysicalProduct.price() adds shipping, DigitalProduct.price() equals base, BundleProduct.price() sums components and applies discount, isinstance relationships hold, polymorphic price() works in a loop.

</div>
