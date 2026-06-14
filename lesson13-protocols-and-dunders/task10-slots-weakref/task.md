# Slots vs. weak references: a one-instance-per-SKU registry

> **Phase:** OOP Foundations  •  **Stage:** 13.10 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain why a class with __slots__ silently loses the ability to be weakly referenced, and name the exact error you get (TypeError: cannot create weak reference to ... object).
- Add '__weakref__' to a class's __slots__ to restore weakref support without giving up the memory/typo-safety benefits of slots.
- Use weakref.WeakValueDictionary to build an identity cache whose entries disappear automatically once no strong references remain, so the cache never keeps objects alive on its own.
- Understand that weakref support is inherited: a subclass of a weakrefable (slotted) base is itself weakrefable even if its own __slots__ omits '__weakref__' — and that repeating '__weakref__' in the subclass is an error.
- Distinguish object identity (is) from equality (==) and see why an identity cache must hand back the same instance, not just an equal one.

## Python features introduced
`__slots__`, `__weakref__ slot`, `weakref.ref`, `weakref.WeakValueDictionary`, `TypeError: cannot create weak reference to ... object`, `__weakref__ descriptor on the class`, `slots inheritance of weakref support (subclass of a weakrefable base)`, `gc.collect for deterministic eviction in tests`, `@classmethod alternative constructor`, `is identity vs == equality`

## MiniERP increment
Extends the slotted `Product` domain object (built earlier in this phase's `slots-optimization` task) so the service layer can guarantee a single canonical in-memory instance per SKU. You add `'__weakref__'` to `Product.__slots__`, then implement an `EntityRegistry` (or `ProductRegistry`) backed by `weakref.WeakValueDictionary` exposing `canonical(product)` / `get(sku)`: the first time a SKU is seen the registry stores and returns that instance; later loads of the same SKU return the *same* object (verified with `is`), so inventory adjustments, price edits, and audit entries all act on one shared Product rather than diverging copies. Because the dictionary holds only weak references, a Product that is dropped everywhere else is evicted from the registry automatically — the cache shrinks with the working set instead of leaking every Product the app has ever touched. This identity map is the foundation later interfaces (CLI/Web/GUI/TUI) reuse so concurrent views of the same SKU stay consistent.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Given the slotted `Product` from `slots-optimization`, first try to build a `WeakValueDictionary` cache and watch it raise `TypeError: cannot create weak reference to 'Product' object`; then fix it. `class Product:\n    __slots__ = ('sku', 'name', 'price_cents', 'qty_on_hand', '__weakref__')  # <- add __weakref__\n    ...\n\nimport weakref\nclass ProductRegistry:\n    def __init__(self) -> None:\n        self._by_sku: 'weakref.WeakValueDictionary[str, Product]' = weakref.WeakValueDictionary()\n    def canonical(self, product: Product) -> Product:\n        existing = self._by_sku.get(product.sku)\n        if existing is not None:\n            return existing\n        self._by_sku[product.sku] = product\n        return product\n    def get(self, sku: str) -> Product | None:\n        return self._by_sku.get(sku)`
- **Test focus:** Verify (1) the fixed slotted Product can be weakly referenced: weakref.ref(product) succeeds and `'__weakref__'` is in Product.__slots__ (the class still uses slots, so setting an undeclared attribute still raises AttributeError); (2) ProductRegistry.canonical returns the *same* object (assertIs) for two equal Products sharing a SKU, and a later get(sku) returns that identical instance; (3) the registry does not keep Products alive — after dropping all strong refs and calling gc.collect(), get(sku) returns None and len shrinks (entry auto-evicted via the WeakValueDictionary); (4) a regression guard reproducing the gotcha: a sibling slotted class WITHOUT '__weakref__' raises TypeError when inserted into a WeakValueDictionary, with the message containing 'cannot create weak reference'; (5) a subclass of Product that adds its own slots but omits '__weakref__' is still weakrefable (inherited).

</div>
