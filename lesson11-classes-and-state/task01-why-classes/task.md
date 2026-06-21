# Stage 1: why objects? dicts versus classes

For several phases MiniERP has represented a product as a plain data structure — a tuple
like `("A-001", "Widget", 999, 5)` or a dict like `{"sku": "A-001", "name": "Widget",
"price_cents": 999}` — and operated on it with free functions: `describe(product)`,
`unit_price_for(price, qty)`, `is_valid_sku(value)`. That has carried us a long way. This
phase changes the representation: a product becomes a **class**, and the functions that act
on it become **methods** that live on the object. Before writing any code, it is worth being
clear about what that buys us and why it is the right move now.

## What a class is

A **class** is a blueprint for making objects. An **object** (or **instance**) is one thing
built from that blueprint — it has its own data and shares the blueprint's behavior. You have
already used classes without defining them: `str`, `list`, `dict`, and `Decimal` are all
classes, and `"hi"`, `[1, 2]`, and `Decimal("1.50")` are instances of them. When you write
`"hi".upper()`, you are calling a **method** — a function that belongs to the `str` class and
acts on that particular string. Defining your own classes means giving MiniERP's own concepts
— Product, Money, Invoice — the same treatment the built-in types already get.

## The problem with bare dicts

A dict-based product works, but nothing about it is enforced or self-describing:

- **No guarantees.** Any code can write `product["price_cents"] = -5`, or misspell a key as
  `product["pirce"]`, and Python will not object until something breaks far away.
- **Behavior lives elsewhere.** To get a display label you must remember which free function
  does it and import it. The data (`product`) and the code that understands it (`label`,
  `price_display`) are separated, so a reader assembles the picture from scattered pieces.
- **No identity of type.** Every product is just "a dict". You cannot meaningfully ask "is
  this a Product?", and an invoice dict and a product dict look identical to the language.

## What a class gives you

Rebuilding Product as a class fixes each of those:

- **Data and behavior travel together.** `product.label()` and `product.price_display()` are
  reached straight from the object, so everything a Product can do lives in one place — the
  class body.
- **A real type.** `isinstance(p, Product)` is meaningful; a Product is distinguishable from
  an Invoice; tools and type checkers can reason about it.
- **A controlled surface.** Later stages add validation (a price can never go negative), a
  single canonical instance per SKU, and a fixed set of allowed attributes — guarantees a
  loose dict cannot offer.

The mental model: a dict is a **bag of values**; a class is a **concept with rules and
behavior**. Use a dict when you genuinely just need a flexible mapping; reach for a class when
a thing has invariants (things that must stay true) and behavior of its own. A Product has
both, so it earns a class. You will still use dicts constantly — as the *input* to
`from_dict`, for instance — but the product itself becomes an object.

## Where this phase goes

Over the next stages you build the `Product` class up one capability at a time: its
initializer and a first method; the difference between data shared by every product and data
unique to one; behavior as methods; alternate ways to construct it; a stateless helper; and
finally the two-step creation protocol behind every Python object. By the end, the loose
product dict is a real domain object — the foundation the rest of the OOP phase builds on.

There is no code to write in this stage. Continue when you are ready to define the class.

Reference: Python documentation, "Classes" (the tutorial) and "Data model — objects, values
and types" at docs.python.org.
