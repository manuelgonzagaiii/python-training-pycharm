"""Slots vs. weak references: a one-instance-per-SKU registry

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: Given the slotted `Product` from `slots-optimization`, first try to build a `WeakValueDictionary` cache and watch it raise `TypeError: cannot create weak reference to 'Product' object`; then fix it. `class Product:\n    __slots__ = ('sku', 'name', 'price_cents', 'qty_on_hand', '__weakref__')  # <- add __weakref__\n    ...\n\nimport weakref\nclass ProductRegistry:\n    def __init__(self) -> None:\n        self._by_sku: 'weakref.WeakValueDictionary[str, Product]' = weakref.WeakValueDictionary()\n    def canonical(self, product: Product) -> Product:\n        existing = self._by_sku.get(product.sku)\n        if existing is not None:\n            return existing\n        self._by_sku[product.sku] = product\n        return product\n    def get(self, sku: str) -> Product | None:\n        return self._by_sku.get(sku)`
"""

# Your code here.
