# Stage 5: frozenset, and sets that contain sets

A normal set is **mutable** — you can `add` and `discard` items. That flexibility comes
with a restriction: a set's members must be hashable, and mutable things are not hashable,
so **you cannot put a set inside another set**, nor use one as a dict key.

```
>>> {{"new", "sale"}}
Traceback (most recent call last):
TypeError: unhashable type: 'set'
```

This matters the moment you ask a question about tag *combinations* rather than individual
tags. "How many distinct tag combinations does the catalog use?" wants a set whose members
are themselves groups of tags — a set of sets. The plain `set` cannot do it.

## frozenset: an immutable, hashable set

`frozenset` is the immutable sibling of `set`. It supports every read operation (`in`,
`&`, `|`, `<=`) but none that mutate, and because it never changes it **is** hashable. So
a frozenset can live inside another set or act as a dict key:

```
>>> combo = frozenset({"new", "sale"})
>>> {combo, frozenset({"clearance"})}        # a set of frozensets, allowed
{frozenset({'new', 'sale'}), frozenset({'clearance'})}
```

Two more things make this the right tool here. A frozenset ignores order, so
`frozenset({"new", "sale"})` and `frozenset({"sale", "new"})` are **equal and hash the
same** — identical combinations automatically collapse into one. And building a set of
them gives you the distinct combinations for free, with no manual de-duplication.

The general rule worth remembering: reach for `frozenset` whenever a set of values needs
to be used as a *key* or a *member* of another set.

## Your task

In `catalog.py`, finish `catalog_tag_combinations(tags_index)`. For each product's tag
set, add a **frozenset** of those tags to `combinations`. You write the value passed to
`.add(...)`.

## Worked example

```
>>> import catalog
>>> combos = catalog.catalog_tag_combinations(
...     {"A": {"new", "sale"}, "B": {"sale", "new"}, "C": {"clearance"}})
>>> len(combos)              # A and B are the same combination -> collapses to one
2
>>> frozenset({"clearance"}) in combos
True
```

## What the check verifies, and what it leaves to you

- Enforced: the result is a set whose every member is a `frozenset`; two products with the
  same tags (in any order) count as one combination; a known combination is findable in
  the result.
- Your free choice: how you build each frozenset is up to you, as long as the members are
  hashable frozensets and duplicates collapse.

<div class="hint" title="If you are stuck">

Wrap the tag set: `combinations.add(frozenset(tags))`. Passing a plain `set` would raise
`TypeError: unhashable type: 'set'`.

</div>

Reference: Python documentation, "Set Types — set, frozenset" at docs.python.org.
