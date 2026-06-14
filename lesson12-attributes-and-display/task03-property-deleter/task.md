# The Deleter and Optional Fields

> **Phase:** OOP Foundations  •  **Stage:** 12.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement the third property hook, the deleter, triggered by del obj.attr
- Model an optional field (e.g. a discount) that can be cleared
- See the complete getter/setter/deleter triad on one attribute
- Understand when a deleter is appropriate (resetting/clearing optional state)

## Python features introduced
`@<name>.deleter`, `del statement on an attribute`, `optional attribute via X | None`, `resetting state`, `property full triad`

## MiniERP increment
Add an optional discount_cents property to Product with a deleter that clears it back to None, giving the pricing model a clearable per-product discount used later by Sales.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    @property
    def discount_cents(self) -> int | None:
        return self._discount_cents

    @discount_cents.setter
    def discount_cents(self, value: int | None) -> None:
        ...  # validate and store

    @discount_cents.deleter
    def discount_cents(self) -> None:
        ...  # reset self._discount_cents = None
- **Test focus:** Assert the getter/setter round-trip works; assert `del product.discount_cents` resets the value to None via the deleter; assert an invalid discount raises.

</div>
