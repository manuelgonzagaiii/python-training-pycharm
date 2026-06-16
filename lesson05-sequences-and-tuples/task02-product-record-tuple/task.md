# Stage 2: model a product as a tuple record

Time to build. This stage creates `catalog.py` and the atomic unit of the whole phase: a
single product, stored as a **tuple record**. Every later function — the list, the dict
index, the reports — manipulates these records, so getting the shape right matters.

## Why a tuple for a record

A product always has the same four fields in the same order: `(sku, name, price_cents,
qty)`. That **fixed shape** is exactly what a tuple expresses. Two payoffs:

- **Immutability.** A tuple cannot be changed after it is built, so a record can never be
  half-edited by a stray line of code. To "change" a product you build a *new* record —
  which keeps history honest.
- **It can be a key later.** Because tuples are immutable (and hashable), a record — or part
  of one — can be a dict key or a set member. Lists cannot. You will rely on this in the
  next lessons.

Building a tuple is just commas; the parentheses are optional but worth keeping for clarity:

```
>>> ("A-1", "Widget", 999, 5)
('A-1', 'Widget', 999, 5)
```

Access fields by index, the way you indexed strings: `record[0]` is the sku, `record[2]` is
the price in cents.

## Naming the shape once: a type alias

Writing `tuple[str, str, int, int]` everywhere is noise, and it does not say what the fields
*mean*. A **type alias** names the shape in one place. Modern Python (3.12+) writes it with
the `type` keyword:

```python
type Product = tuple[str, str, int, int]  # (sku, name, price_cents, qty)
```

Now every function can say `-> Product` and a reader knows precisely what that is. (The
older way was `Product = tuple[str, str, int, int]` as a plain assignment; the `type`
statement is the current, clearer form.)

## Your task

In `catalog.py`, fill in `make_product` so it returns the four fields as a tuple record in
order `(sku, name, price_cents, qty)`.

## Worked example

```
>>> import catalog
>>> catalog.make_product("A-1", "Widget", 999, 5)
('A-1', 'Widget', 999, 5)
```

## What the check verifies, and what it leaves to you

- Enforced: the result is a 4-element `tuple` in the correct field order, and it is
  immutable (assigning to an element raises).
- Your free choice: nothing much here — the record shape is the contract the whole phase
  depends on.

<div class="hint" title="If you are stuck">

Return the four parameters as a tuple: `(sku, name, price_cents, qty)`.

</div>

Reference: Python documentation, "Sequence Types — Tuples" and "type statement (PEP 695)" at
docs.python.org.
