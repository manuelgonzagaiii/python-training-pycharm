# Stage 7: locking down memory with __slots__

By default every instance stores its attributes in a per-object dictionary, `__dict__`. That is
flexible — you can attach any attribute at any time — but it costs memory, and it silently
accepts typos: `product.prce_cents = 5` creates a brand-new attribute instead of raising. For
**high-cardinality** domain objects — there may be hundreds of thousands of products and line
items in memory — both costs matter. `__slots__` fixes the set of allowed attributes, removing
the per-instance dict.

## What __slots__ does

Declare `__slots__` as a tuple of the instance attribute names, and Python stores those
attributes in fixed slots instead of a dict:

```
class Money:
    __slots__ = ("cents", "currency")
```

Two benefits follow:

- **Less memory.** No per-instance `__dict__`; thousands of objects get noticeably smaller.
- **Typo safety.** Assigning an attribute not in `__slots__` raises `AttributeError`, catching
  `money.cetns = 5` immediately instead of hiding a bug.

The trade is flexibility: you can no longer attach arbitrary attributes. For value objects and
records — which have a fixed, known shape — that restriction is a feature, not a loss.

## The property interaction to get right

`Product` has properties (`price_cents`, `discount_cents`) backed by private attributes
(`_price_cents`, `_discount_cents`). A property is a **class-level** descriptor, not an
instance attribute, so it must **not** appear in `__slots__` — and a name can't be both a slot
and a class attribute. So you slot the **backing** names, not the property names:

```
    __slots__ = ("sku", "name", "_price_cents", "_discount_cents")
```

`sku` and `name` are plain attributes; `_price_cents` and `_discount_cents` are where the
properties store their values. Listing `price_cents` there instead would clash with the
property and fail at class-creation time. (One more subtlety, for the next stage: a slotted
object can't be weak-referenced unless `"__weakref__"` is added to `__slots__` — you will do
exactly that when the weakref registry arrives.)

## Your task

In `domain.py`, finish `Product.__slots__` with the four instance attributes, using the
**backing** names for the two properties. The `__slots__` for `Money`, `LineItem`, and
`Customer` are provided as models.

## Worked example

```
>>> import domain
>>> hasattr(domain.Money(100), "__dict__")     # no per-instance dict
False
>>> domain.Money(100).bogus = 1                # a stray attribute is rejected
Traceback (most recent call last):
AttributeError: 'Money' object has no attribute 'bogus'...
>>> p = domain.Product("A-1", "Widget", 1500)  # properties still work under slots
>>> p.price_dollars
Decimal('15.00')
>>> p.discount_cents = 100
>>> p.discount_cents
100
```

## What the check verifies, and what it leaves to you

- Enforced: the domain classes declare `__slots__`; instances have no `__dict__`; a stray
  attribute assignment raises `AttributeError`; and the existing properties and methods still
  work (so the slot names are correct, including the property backing names).
- Your free choice: nothing meaningful — `__slots__` must list exactly the instance attributes
  for the class to keep working. The check fails a slot list that omits a needed backing name
  (properties break) or names a property (class creation fails), because those are genuinely
  wrong, not stylistic.

<div class="hint" title="If you are stuck">

`Product.__slots__ = ("sku", "name", "_price_cents", "_discount_cents")`. Use the underscore
backing names for the two properties, not `price_cents` / `discount_cents`.

</div>

Reference: Python documentation, "Data model — __slots__" at docs.python.org.
