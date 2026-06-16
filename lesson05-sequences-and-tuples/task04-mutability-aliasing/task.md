# Stage 4: aliasing traps — copies vs references

Mutability is powerful, and it has a sharp edge that bites every Python programmer at least
once. This stage is about that edge: when you "copy" a list, you very often do not. MiniERP
needs a function that hands callers a *stable view* of the catalog they can read without
accidentally changing the real one — so you need to understand the trap before you can avoid
it.

## Assignment does not copy

A name in Python is a label stuck to an object. Assigning one name to another sticks a
*second label on the same object* — it does not duplicate anything:

```
>>> a = [1, 2, 3]
>>> b = a          # b is NOT a copy -- it is another name for the same list
>>> b.append(4)
>>> a
[1, 2, 3, 4]       # surprise: a changed too, because a and b are one object
```

`a` and `b` are **aliases**. You can prove it: `a is b` is `True`, and `id(a) == id(b)`.
The `is` operator and `id()` ask about *identity* (same object?), which is different from
`==` (equal contents?). Two different lists can be `==` equal while `is` is `False`.

This is the bug that corrupts shared state: a function "tweaks its copy" of a list and
silently mutates the caller's data.

## Taking a real (shallow) copy

To get an independent list, copy it explicitly. Three equivalent ways:

```
>>> b = a[:]          # slice the whole thing
>>> b = list(a)       # construct a new list from it
>>> b = a.copy()      # the copy method
```

Now `b is a` is `False`, and appending to `b` leaves `a` alone. This is a **shallow** copy:
the new list is independent, but it holds the *same item objects*. That is perfectly safe
here because the items are **immutable tuples** — there is nothing inside a record that could
be mutated through the shared reference. (This is another reason records are tuples: shallow
copies of the catalog are completely safe.)

## Your task

In `catalog.py`, fill in `snapshot_catalog(catalog)` so it returns an independent shallow
copy. A caller must be able to mutate the snapshot without touching the original.

## Worked example

```
>>> import catalog
>>> cat = catalog.seed_catalog()
>>> snap = catalog.snapshot_catalog(cat)
>>> snap is cat
False
>>> snap == cat
True
>>> snap.append(catalog.make_product("Z-9", "New", 100, 1))
>>> len(cat) == len(snap)
False
```

## What the check verifies, and what it leaves to you

- Enforced: the snapshot is a *different* list object (`is not` the original) with equal
  contents, and mutating it does not change the source.
- Your free choice: which copy form you use — `list(catalog)`, `catalog[:]`, and
  `catalog.copy()` all pass, because all three make an independent shallow copy.

<div class="hint" title="If you are stuck">

Any of `list(catalog)`, `catalog[:]`, or `catalog.copy()` returns an independent copy.

</div>

Reference: Python documentation, "Sequence Types — Common Sequence Operations" and "`is` and
`id()`" at docs.python.org.
