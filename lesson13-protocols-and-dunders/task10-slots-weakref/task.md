# Stage 10: slots, weak references, and a one-instance-per-SKU registry

Back in lesson 11, `Product.__new__` interned products in a plain dict so a SKU always mapped to
one canonical object. That dict was a deliberate placeholder with a known flaw: it holds a
**strong** reference to every product forever, so nothing is ever freed — a slow memory leak.
This final stage fixes it properly with **weak references**, and in doing so meets the one
remaining wrinkle of `__slots__`.

## The slots-versus-weakref wrinkle

A normal object can always be weak-referenced. A **slotted** object cannot — unless you opt in
by adding `"__weakref__"` to its `__slots__`:

```
    __slots__ = ("sku", "name", "_price_cents", "_discount_cents", "__weakref__")
```

Without that entry, `weakref.ref(product)` raises `TypeError: cannot create weak reference`.
This is the cost of slots the last stage hinted at: by removing the per-instance dict, you also
removed the hidden slot that normally supports weak references, so you add it back explicitly
when you need it. And you need it now, because the registry holds products *weakly*.

## A weak identity map

`weakref.WeakValueDictionary` is a dict whose **values** are held only weakly: when a value is
no longer referenced anywhere else, it is dropped from the dict automatically. That is exactly
right for an identity map — it tracks the products currently in use and forgets the rest:

```
import weakref

class ProductRegistry:
    def __init__(self):
        self._by_sku = weakref.WeakValueDictionary()

    def canonical(self, product):
        existing = self._by_sku.get(product.sku)
        if existing is not None:
            return existing
        self._by_sku[product.sku] = product
        return product

    def get(self, sku):
        return self._by_sku.get(sku)
```

`canonical(product)` returns the one shared instance for a SKU — the same object every time, so
inventory edits, price changes, and audit entries all act on a single `Product` rather than
diverging copies. But because the references are weak, a product dropped everywhere else is
**evicted automatically**, so the registry shrinks with the working set instead of leaking.
This is the proper replacement for lesson 11's strong dict, and the interning cache
`Product._instances` is upgraded to a `WeakValueDictionary` in the same spirit (which is *why*
`Product` needs `"__weakref__"` in its slots — a weak map's values must be weak-referenceable).

The mental model: a **strong** reference keeps an object alive; a **weak** reference lets you
reach an object *without* keeping it alive. Caches and registries want weak references so they
help while the object is in use and get out of the way when it is not.

## Your task

In `domain.py`, finish `ProductRegistry.__init__` so `self._by_sku` is a dictionary that holds
its values **weakly**. `Product.__slots__` already includes `"__weakref__"`, and the
`canonical`/`get` methods are provided.

## Worked example

```
>>> import domain, weakref, gc
>>> p = domain.Product("W-1", "Widget", 100)
>>> weakref.ref(p)() is p              # weak ref works -- "__weakref__" is in __slots__
True
>>> reg = domain.ProductRegistry()
>>> reg.canonical(p) is p              # registers and returns the canonical instance
True
>>> reg.get("W-1") is p
True
>>> domain.Product._instances.clear(); del p; _ = gc.collect()
>>> reg.get("W-1")                     # dropped everywhere else -> evicted, returns None
```

## What the check verifies, and what it leaves to you

- Enforced: a `Product` can be weak-referenced (so `"__weakref__"` is in its slots); the
  registry returns one canonical instance per SKU; and a product dropped everywhere else is
  evicted from the registry after garbage collection.
- Your free choice: the registry's internals beyond "values held weakly" are yours. A plain
  dict here would pass the identity checks but **fail** the eviction check — it would leak,
  which is the exact bug this stage exists to fix, so the weak map is genuinely required, not a
  preference.

<div class="hint" title="If you are stuck">

`self._by_sku = weakref.WeakValueDictionary()`. Its values are held weakly, so when a product
is no longer referenced elsewhere it disappears from the registry on its own.

</div>

Reference: Python documentation, "weakref — Weak references (WeakValueDictionary)" and "Data
model — __slots__ and __weakref__" at docs.python.org.
