# Stage 7: unpacking in calls and definitions (* and **)

The `*` and `**` operators do two complementary jobs depending on which side they appear.
In a **function definition** they *collect* extra arguments; in a **call** (or a literal)
they *spread* a collection out. You met collecting in the last stage (`*overrides`); this
stage covers spreading, and pairs the two.

## Collecting with *args and **kwargs

A `*name` parameter gathers any number of positional arguments into a tuple; a `**name`
parameter gathers any number of keyword arguments into a dict:

```
>>> def f(*args, **kwargs):
...     return args, kwargs
>>> f(1, 2, x=3)
((1, 2), {'x': 3})
```

`merge_catalogs(*catalogs)` uses this to accept "any number of catalogs" — each argument
becomes one element of the `catalogs` tuple, and a nested comprehension flattens them into
one list. `build_product(**fields)` uses it to accept "whatever named fields you pass".

## Spreading with * and ** in a call

The same operators, used at a **call site**, do the reverse — they take a collection and
hand its items over as separate arguments:

```
>>> def make(sku, name, price_cents, qty): ...
>>> row = ("A-001", "Widget", 999, 5)
>>> make(*row)                       # spreads the tuple into four positional args
>>> fields = {"sku": "A-001", "name": "Widget", "price_cents": 999, "qty": 5}
>>> make(**fields)                   # spreads the dict into four keyword args
```

`build_product(**fields)` receives the fields as a dict and then spreads that dict straight
back into the `ProductRecord(...)` constructor as keyword arguments — turning a `{name:
value}` mapping into a real record. This is the everyday bridge between "data as a dict"
(what you read from a CSV row or a JSON object) and "data as a typed record". The dict keys
must match the field names exactly, and `**` requires string keys.

## Your task

In `catalog.py`, finish two functions:

1. `merge_catalogs(*catalogs)` — flatten the collected catalogs into one list, in order.
   Write the nested comprehension: each product, for each catalog in `catalogs`.
2. `build_product(**fields)` — construct a `ProductRecord` by **spreading** `fields` in as
   keyword arguments.

## Worked example

```
>>> import catalog
>>> a = [catalog.make_product("A-001", "Widget", 999, 5)]
>>> b = [catalog.make_product("B-001", "Gadget", 250, 12)]
>>> catalog.merge_catalogs(a, b) == a + b
True
>>> catalog.merge_catalogs()          # no catalogs -> empty list
[]
>>> catalog.build_product(sku="A-001", name="Widget", price_cents=999, qty=5).sku
'A-001'
```

## What the check verifies, and what it leaves to you

- Enforced: `merge_catalogs` concatenates the catalogs in argument order and returns `[]`
  for no arguments; `build_product` produces a record equal to the same fields passed to
  `make_product`.
- Your free choice: `merge_catalogs` need not be a comprehension — a loop that extends a
  list, or `itertools.chain`, gives the same result and passes.

<div class="hint" title="If you are stuck">

The flatten is `[product for catalog in catalogs for product in catalog]`. The build is
`ProductRecord(**fields)` — the `**` spreads the dict into keyword arguments.

</div>

Reference: Python documentation, "Unpacking Argument Lists" and "Arbitrary Argument Lists"
(the tutorial, Defining Functions section) at docs.python.org.
