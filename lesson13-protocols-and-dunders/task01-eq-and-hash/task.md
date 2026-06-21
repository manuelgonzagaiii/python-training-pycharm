# Stage 1: value equality and hashing

By default, two distinct objects are "equal" only if they are the *same* object — `==` falls
back to identity. For domain types that is usually wrong: two `Money` objects holding 1500
cents in USD represent the same amount and should compare equal, and a product should be
recognised by its SKU. This stage gives `Money` and `Product` **value equality** with `__eq__`
and the matching `__hash__` they need to live in sets and dicts.

## `__eq__`: equal by value

`a == b` calls `a.__eq__(b)`. You decide what equality means — usually "the identifying fields
match":

```
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self.cents, self.currency) == (other.cents, other.currency)
```

Two details matter. First, **guard the type**: if `other` is not a `Money`, return the special
`NotImplemented` (not `False`). That tells Python "I don't know how to compare these", so it
can try `other.__eq__(self)` or fall back to identity — which is how `Money(100) == "hi"`
correctly comes out `False` rather than crashing. Second, compare a **tuple of the
identifying fields**, the clean way to compare several fields at once.

## `__hash__`: equal things must hash equally

To put an object in a `set` or use it as a `dict` key, it must be **hashable**, and the rule
is strict: **objects that are equal must have the same hash**. So hash on the *same fields*
`__eq__` compares:

```
    def __hash__(self):
        return hash((self.cents, self.currency))
```

There is a trap Python sets for you here: **defining `__eq__` automatically sets `__hash__`
to `None`**, making instances unhashable, unless you also define `__hash__`. That is deliberate
— a custom equality with the *default* identity hash would violate the equal-implies-same-hash
rule. So `__eq__` and `__hash__` are a pair: define them together. (This also implies a value
object should be treated as immutable once created; mutating a field would change its hash and
corrupt any set or dict holding it. The frozen-dataclass version in a later lesson enforces
that.)

`Product` gets the same treatment, keyed on its SKU: two products with the same SKU are equal
and hash the same, so the catalog can dedupe products in a `set`.

## Your task

In `domain.py`, finish two pieces:

1. `Product.__eq__` — return `True` when the two products' SKUs match. (`Product.__hash__` on
   the SKU is provided.)
2. `Money.__hash__` — hash a tuple of the identifying fields (cents and currency).
   (`Money.__eq__` is provided as the model.)

## Worked example

```
>>> import domain
>>> domain.Money(1500, "USD") == domain.Money(1500, "USD")
True
>>> domain.Money(1500, "USD") == domain.Money(1500, "EUR")
False
>>> len({domain.Money(1500), domain.Money(1500), domain.Money(250)})   # a set dedupes
2
>>> a = domain.Product("A-1", "Widget", 100)
>>> a == domain.Product("A-1", "Other price", 999)   # same SKU
True
```

## What the check verifies, and what it leaves to you

- Enforced: equal-by-value for the right fields; unequal across different values or
  currencies; the objects are hashable and equal objects share a hash (so sets dedupe and dict
  lookups work); comparison with an unrelated type yields `False`, not an error.
- Your free choice: how you compare and hash, as long as the equal-implies-same-hash invariant
  holds. Hashing a different but consistent set of fields would be a real bug, not a style
  choice, so the check insists the fields line up.

<div class="hint" title="If you are stuck">

`Product.__eq__`: `self.sku == other.sku`. `Money.__hash__`: `hash((self.cents,
self.currency))` — hash the *tuple* of the same fields `__eq__` compares.

</div>

Reference: Python documentation, "Data model — object.__eq__ and object.__hash__" at
docs.python.org.
