# Stage 3: collect products into a mutable list

A single record is not a catalog. The catalog is the **collection** — a `list` of product
records that grows as products are added. This stage makes that list real, and draws the
line between changing a list *in place* and building a new one, which is the source of a
whole class of bugs you will meet in the next stage.

## A list is the growable collection

The catalog must grow and shrink, so it is a `list`. The two ways to add to one:

- `catalog.append(product)` — add a single item to the end, **in place**. The list object
  itself changes; nothing new is created.
- `catalog.extend(other)` — add all items from another iterable, in place.

"In place" is the key idea. `append` returns `None` — it does not hand you a new list, it
modifies the one you gave it:

```
>>> items = [1, 2]
>>> items.append(3)        # returns None; items is now [1, 2, 3]
>>> items
[1, 2, 3]
```

Contrast that with `items + [3]`, which builds and returns a *new* list and leaves the
original alone. Knowing which you have — same object mutated, or new object returned — is
something you will reason about constantly.

## The list holds references to immutable records

The catalog is a list of tuples. The list is mutable (you can add and remove records), but
each record inside it is an immutable tuple. So the collection changes while the individual
records never do — exactly the "mutable list of immutable records" design from stage 1.

## Your task

In `catalog.py`, fill in:

1. `add_product(catalog, product)` — append the record to the list **in place** (the
   function returns `None`).
2. `seed_catalog()` — return a starting list of a few products. The exact products are your
   choice; build them with `make_product`.

## Worked example

```
>>> import catalog
>>> cat = []
>>> catalog.add_product(cat, catalog.make_product("A-1", "Widget", 999, 5))
>>> cat
[('A-1', 'Widget', 999, 5)]
>>> len(catalog.seed_catalog()) > 0
True
```

## What the check verifies, and what it leaves to you

- Enforced: `add_product` mutates the *same* list object (its id is unchanged) and grows it
  by one, returning `None`; `seed_catalog` returns a non-empty list of valid 4-field
  records.
- Your free choice: which products `seed_catalog` contains — any valid records pass.

<div class="hint" title="If you are stuck">

`add_product` is one line: `catalog.append(product)`. For `seed_catalog`, return a list
literal of `make_product(...)` calls.

</div>

Reference: Python documentation, "Sequence Types — list: Mutable Sequence Types" at
docs.python.org.
