# Stage 5: alternate constructors with @classmethod

`Product("A-001", "Widget", 999)` builds a product from three separate arguments. But real
data arrives in other shapes: a CSV row `("A-001", "Widget", 999)`, or a dict from a JSON
request `{"sku": "A-001", ...}`. You could make every caller unpack those before calling
`Product(...)`, but it is cleaner to give the class **alternate constructors** that accept
those shapes directly. In Python that is what `@classmethod` is for.

## What a classmethod is

A method decorated with `@classmethod` receives the **class itself** as its first parameter,
named `cls`, instead of an instance (`self`). Because it has the class in hand, it can build
and return a new instance with `cls(...)`:

```
    @classmethod
    def from_row(cls, row):
        sku, name, price_cents = row
        return cls(sku, name, price_cents)
```

You call it on the class — `Product.from_row(("A-001", "Widget", 999))` — and it hands back a
fully built Product. This is the idiomatic "factory method" pattern: the normal `__init__`
stays focused on the canonical arguments, while named classmethods document and handle each
alternative input shape.

Why `cls` rather than just writing `Product(...)` directly? Using `cls` means a subclass that
inherits `from_row` builds an instance of *the subclass*, not always a base `Product` — the
factory follows the class it was called on. That correctness-under-inheritance is the whole
reason classmethods take `cls`.

## Your task

In `domain.py`, finish two classmethods:

1. `from_row(cls, row)` — the row is already unpacked into `sku, name, price_cents`; return a
   product built from them using `cls`.
2. `from_dict(cls, data)` — written for you as a model, building from `data["sku"]` and the
   other keys.

## Worked example

```
>>> import domain
>>> p = domain.Product.from_row(("A-001", "Widget", 999))
>>> p.label(), p.price_cents
('A-001 - Widget', 999)
>>> q = domain.Product.from_dict({"sku": "B-010", "name": "Gizmo", "price_cents": 250})
>>> q.sku
'B-010'
>>> isinstance(p, domain.Product)
True
```

## What the check verifies, and what it leaves to you

- Enforced: `from_row` and `from_dict` each return a real `Product` whose fields match the
  input.
- Your free choice: how you construct it. `cls(sku, name, price_cents)` is the recommended,
  inheritance-safe form, but `Product(sku, name, price_cents)` produces the same object and
  also passes — the check grades the resulting instance, not the spelling.

<div class="hint" title="If you are stuck">

`from_row` ends with `return cls(sku, name, price_cents)` — the three names were unpacked from
`row` on the line above.

</div>

Reference: Python documentation, "@classmethod" (Built-in Functions) and "Classes" at
docs.python.org.
