# Stage 4: LineItem and container dunders

With `Money` arithmetic in place, two new domain objects fall out naturally: a `LineItem` (one
product and a quantity, whose total is `Money`) and an `Invoice` (a collection of line items).
This stage builds both, and makes `Invoice` behave like a real Python container by implementing
the **container protocol** — the dunders behind `len()`, `in`, iteration, and indexing.

## Composition: a LineItem is built from other objects

`LineItem` holds a `Product` and a quantity, and computes its money total from them:

```
class LineItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @property
    def line_total(self):
        return Money(self.product.price_cents) * self.quantity
```

This is **object composition**: a LineItem is *made of* a Product and reuses `Money`'s
multiplication (from the last stage) to compute `price * quantity`. The objects you built
earlier become the parts of the ones you build now.

## The container protocol

An `Invoice` wraps a list of line items. Implementing a handful of dunders makes it usable
exactly like a built-in collection, so callers never reach for `invoice.lines` directly:

- `__len__(self)` -> `len(invoice)`
- `__bool__(self)` -> truthiness (`if invoice:`). If you omit `__bool__`, Python falls back to
  `__len__` (zero is falsy); here both are defined so the intent is explicit.
- `__getitem__(self, index)` -> `invoice[0]`
- `__iter__(self)` -> `for line in invoice:`
- `__contains__(self, product)` -> `product in invoice`

```
    def __len__(self):
        return len(self.lines)

    def __contains__(self, product):
        return any(line.product == product for line in self.lines)
```

The mental model: these dunders are the **protocol** the language calls behind familiar syntax.
By implementing them, your class plugs into `for`, `in`, `len`, and `[]` for free — duck
typing at the language level. `__contains__` here leans on the `Product.__eq__` you wrote in
stage 1, so `product in invoice` matches by SKU.

## Your task

In `domain.py`, finish two pieces:

1. `LineItem.line_total` — the product's price as `Money`, multiplied by the quantity.
2. `Invoice.__contains__` — `True` when any line's product equals the given product.

The other container dunders (`__len__`, `__bool__`, `__getitem__`, `__iter__`) are provided.

## Worked example

```
>>> import domain
>>> p = domain.Product("A-1", "Widget", 1000)
>>> domain.LineItem(p, 3).line_total.cents
3000
>>> inv = domain.Invoice([domain.LineItem(p, 1), domain.LineItem(p, 2)])
>>> len(inv), bool(inv), bool(domain.Invoice())
(2, True, False)
>>> inv[0].quantity
1
>>> p in inv
True
>>> [line.quantity for line in inv]      # iteration
[1, 2]
```

## What the check verifies, and what it leaves to you

- Enforced: `line_total` is a `Money` equal to price times quantity; `len`, truthiness,
  indexing, iteration, and `in` all behave like a real container.
- Your free choice: how you compute `line_total` and test membership, as long as the behavior
  matches. The check exercises the protocols, not the bodies.

<div class="hint" title="If you are stuck">

`line_total`: `Money(self.product.price_cents) * self.quantity` (reusing `Money.__mul__`).
`__contains__`: `any(line.product == product for line in self.lines)`.

</div>

Reference: Python documentation, "Data model — emulating container types (__len__,
__getitem__, __iter__, __contains__)" at docs.python.org.
