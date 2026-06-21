# Stage 3: the deleter and optional fields

A property can also define what `del` does. Together, getter, setter, and **deleter** form the
full triad. This stage adds an *optional* per-product discount: a value that may be present or
absent, that validates when set, and that `del` clears back to "absent". It is a small feature
that exercises the whole property protocol and the `X | None` pattern for optional data.

## An optional attribute

"Optional" in Python usually means "a real value, or `None`". The type is written `int | None`
(an int *or* None — the PEP 604 union you met earlier). The discount starts absent (`None`),
can be set to a number, and can be cleared:

```
    @property
    def discount_cents(self) -> int | None:
        return getattr(self, "_discount_cents", None)

    @discount_cents.setter
    def discount_cents(self, value):
        if value < 0:
            raise ValueError("discount must not be negative")
        self._discount_cents = value

    @discount_cents.deleter
    def discount_cents(self):
        self._discount_cents = None
```

The getter uses `getattr(self, "_discount_cents", None)` so the discount reads as `None` before
it has ever been set — no need to initialise it in `__init__`. The setter validates like the
last stage. The **deleter** runs on `del product.discount_cents` and resets the backing value
to `None`.

Why a deleter instead of just assigning `None`? It expresses intent: `del product.discount_cents`
reads as "remove the discount", which is clearer than `product.discount_cents = None` and gives
you one obvious place to put any cleanup. The triad — read, validate-on-write, clear-on-delete —
is how a property models a managed, optional field.

## Your task

In `domain.py`, finish the `discount_cents` **deleter** so it resets the backing attribute to
`None`. The getter and setter are provided.

## Worked example

```
>>> import domain
>>> p = domain.Product("A-001", "Widget", 1000)
>>> p.discount_cents                 # absent by default
>>> p.discount_cents = 150
>>> p.discount_cents
150
>>> del p.discount_cents             # clear it
>>> p.discount_cents is None
True
```

## What the check verifies, and what it leaves to you

- Enforced: the discount defaults to `None`; setting then reading returns the value; `del`
  resets it to `None`.
- Your free choice: how the deleter clears the value, as long as a subsequent read returns
  `None`.

<div class="hint" title="If you are stuck">

The deleter is one line: `self._discount_cents = None`. The getter's `getattr(..., None)` then
reports it as absent again.

</div>

Reference: Python documentation, "@property" — deleter usage; "del statement" at docs.python.org.
