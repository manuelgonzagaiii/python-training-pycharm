# Stage 2: define the Product class

Time to write the first real class. A class definition has two parts you meet here: the
`__init__` method, which sets up each new instance, and ordinary methods, which give the
object behavior. Both take a first parameter named `self` — the specific instance being
worked on.

## `__init__` and `self`

When you call `Product("A-001", "Widget", 999)`, Python creates a fresh, empty Product and
then calls its `__init__` (the **initializer**) to fill it in. The first parameter, `self`,
is that fresh instance; the rest are the arguments you passed. Inside `__init__` you attach
data to the object by assigning to `self.<name>`:

```
class Product:
    def __init__(self, sku, name, price_cents):
        self.sku = sku            # store on this instance
        self.name = name
        self.price_cents = price_cents
```

Each `self.sku = sku` creates an **instance attribute** — a value stored on that one object.
Two different products have two independent sets of these. (`__init__` is often loosely
called "the constructor"; strictly it *initializes* an already-created object. The actual
construction step, `__new__`, comes in the last stage of this lesson — for now `__init__` is
all you need.)

`self` is not a keyword; it is just the conventional name for that first parameter, and every
method gets it. You never pass it explicitly — `product.label()` automatically hands the
product in as `self`.

## Methods

A **method** is a function defined inside the class. It reaches the instance's data through
`self`:

```
    def label(self):
        return f"{self.sku} - {self.name}"
```

`product.label()` returns something like `'A-001 - Widget'`. The method belongs to the class,
but it reads *this* product's `self.sku` and `self.name`.

## Your task

In `domain.py`, finish `Product.__init__` so it stores the three arguments (`sku`, `name`,
`price_cents`) as instance attributes on `self`. The `label` method is written for you so you
can see a method in full.

## Worked example

```
>>> import domain
>>> p = domain.Product("A-001", "Widget", 999)
>>> p.sku, p.name, p.price_cents
('A-001', 'Widget', 999)
>>> p.label()
'A-001 - Widget'
>>> q = domain.Product("B-010", "Gizmo", 250)   # an independent instance
>>> q.sku
'B-010'
```

## What the check verifies, and what it leaves to you

- Enforced: a constructed Product exposes `sku`, `name`, and `price_cents` as attributes
  holding the values passed in; `label()` includes the SKU and the name.
- Your free choice: the attribute *names* are fixed here because the rest of the course reads
  `product.sku` and so on, but how you write the assignments is yours (three lines, or any
  equivalent). The exact text `label` returns is open — the check looks for the SKU and name,
  not a precise format.

<div class="hint" title="If you are stuck">

Assign each parameter to the matching attribute on `self`:
`self.sku = sku`, then `self.name = name`, then `self.price_cents = price_cents`.

</div>

Reference: Python documentation, "Classes — Class Objects and Instance Objects", and "Data
model — object.__init__" at docs.python.org.
