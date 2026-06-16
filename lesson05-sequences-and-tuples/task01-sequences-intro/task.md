# Stage 1: why containers? Sequences as the catalog's spine

So far MiniERP has handled one value at a time — a price, a name, a SKU. A real catalog has
*many* products, each made of *several* fields. This phase builds the structure that holds
them: starting here with **sequences**, the ordered collections Python gives you. There is
no code to write on this page; it sets the design the rest of the lesson implements.

## A sequence is an ordered, indexable collection

`list`, `tuple`, `range`, and `str` are all **sequences**: they keep their items in order,
you index them with `s[i]`, slice them with `s[a:b]`, measure them with `len(s)`, and loop
over them. You already used this protocol on strings in Lesson 4 — the same operations work
on lists and tuples. Learn it once, use it everywhere.

The one headline difference between them:

- **`list`** is **mutable** — you can append, replace, and remove items in place. Written
  with square brackets: `[1, 2, 3]`.
- **`tuple`** is **immutable** — once built, it cannot change. Written with commas (parens
  optional): `(1, 2, 3)`.
- **`range`** is an immutable, lazy sequence of integers — `range(5)` is `0,1,2,3,4` without
  storing them all.
- **`str`** is an immutable sequence of characters.

Mutability is not a detail; it is a design tool. You choose a mutable type when something
*should* change and an immutable type when it *should not*, and the language then enforces
your intent.

## The design decision for MiniERP's catalog

Here is the architecture the next tasks build, decided on purpose:

- **Each product is a `tuple`** of `(sku, name, price_cents, qty)`. A product record has a
  **fixed shape** — always those four fields, in that order — so a tuple is exactly right.
  Immutability means a record cannot be half-edited by accident, and (a property you will
  need later) a tuple can be a dict key while a list cannot.
- **The catalog is a `list`** of those tuple records. The collection **grows and shrinks**
  as products come and go, so it must be mutable.
- **Prices are integer cents** (`price_cents`), never a float — the same money discipline
  from Lesson 3, carried into how records store amounts.

So: a mutable list of immutable records. That single sentence is the whole design. Over the
next stages you will build `catalog.py` — make a record, collect records into a list, learn
the aliasing traps that mutability brings, slice the catalog for pagination, and unpack
records cleanly. Later lessons re-index this same catalog with dicts, tag it with sets, and
upgrade it with the `collections` module.

There is nothing to submit here. When the design makes sense, move on and start building it.

Reference: Python documentation, "Sequence Types — list, tuple, range" at docs.python.org.
