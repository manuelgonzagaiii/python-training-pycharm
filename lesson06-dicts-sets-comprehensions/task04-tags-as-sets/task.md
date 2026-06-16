# Stage 4: tags as sets, and set algebra

Products carry tags: `new`, `sale`, `clearance`, `fragile`. The right container for the
tags on one product is a **set** — an unordered collection of unique items. A set cannot
hold the same tag twice (tagging something `sale` twice is meaningless), and it answers
the questions you actually ask about tags directly, with operators borrowed from
mathematics.

```
>>> tags = {"new", "sale"}
>>> "sale" in tags          # membership, fast
True
>>> tags.add("sale")        # already present -> no change
>>> tags
{'new', 'sale'}
```

(Note `{...}` with values is a set, but `{}` alone is an empty *dict*; use `set()` for an
empty set.)

## The operators you need

Set algebra lets you express tag filters without writing loops of `if`:

- `a & b` — **intersection**: items in both. A non-empty `a & b` means "they share at
  least one tag".
- `a | b` — **union**: items in either.
- `a - b` — **difference**: in `a` but not `b`.
- `a >= b` — **superset test**: every item of `b` is also in `a`. This is how you ask
  "does this product have *all* of the required tags?"
- `a <= b` — **subset test**: the mirror image.

```
>>> {"new", "sale", "fragile"} >= {"new", "sale"}   # has all required?
True
>>> {"new", "sale"} & {"clearance", "sale"}         # any tag in common?
{'sale'}
```

Two storefront queries fall straight out of these. "Show products tagged with *all* of
X" is a superset test. "Show products tagged with *any* of X" is a non-empty
intersection.

## Your task

In `catalog.py`, finish the two conditions:

1. `products_with_all_tags(tags_index, required)` — keep a SKU when its tag set is a
   **superset** of `required`.
2. `products_with_any_tags(tags_index, wanted)` — keep a SKU when its tag set **shares at
   least one** tag with `wanted`.

Each is the single boolean expression inside an `if`.

## Worked example

```
>>> import catalog
>>> tags = {"A": {"new", "sale"}, "B": {"sale"}, "C": {"clearance"}}
>>> sorted(catalog.products_with_all_tags(tags, {"new", "sale"}))
['A']
>>> sorted(catalog.products_with_all_tags(tags, {"sale"}))
['A', 'B']
>>> sorted(catalog.products_with_any_tags(tags, {"clearance", "new"}))
['A', 'C']
```

## What the check verifies, and what it leaves to you

- Enforced: "all tags" behaves as a superset test (requiring `{new, sale}` excludes a
  product tagged only `sale`); "any tags" matches on a shared tag; both return **sets**.
- Your free choice: an equivalent spelling is fine — `required <= tags` is the same test
  as `tags >= required`, and `tags.isdisjoint(wanted)` (negated) expresses "any" too.
  Anything that computes the correct set passes.

<div class="hint" title="If you are stuck">

"All required" is `tags >= required`. "Any in common" is a non-empty intersection, which
in a boolean context is just `tags & wanted` (an empty set is falsey).

</div>

Reference: Python documentation, "Set Types — set, frozenset" at docs.python.org.
