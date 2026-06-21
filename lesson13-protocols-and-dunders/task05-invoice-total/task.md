# Stage 5: compose the invoice total

The `Invoice` can already be measured, iterated, and indexed. Now it earns its keep: a `total`
that sums every line into one `Money`, and a `__str__` that renders the whole invoice as
printable text. This stage is where the pieces from the last four stages click together —
`Money` arithmetic, the computed `line_total`, and the container you just built.

## A computed total from object arithmetic

The total is the sum of the line totals, and because `Money` knows how to add itself (stage 3),
you can `sum()` them directly:

```
    @property
    def total(self):
        return sum((line.line_total for line in self.lines), Money(0))
```

Two things to notice. It is a **computed property**, so the total is always current — add a
line and `invoice.total` reflects it immediately, with nothing to keep in sync. And `sum()` is
given a **start value of `Money(0)`** rather than the default integer `0`. That keeps an empty
invoice's total a `Money` (a zero amount), not a bare `int`, so callers always get a `Money`
back. (Stage 3's `__radd__` would let a start-less `sum()` work for a non-empty invoice, but
the explicit `Money(0)` start handles the empty case cleanly too.)

## A readable rendering with __str__

`__str__` composes the line and total renderings — reusing `Product.label()`, `Money.__str__`,
and `total` — into a human-readable block:

```
    def __str__(self):
        rendered = "\n".join(
            f"  {line.product.label()} x{line.quantity}  {line.line_total}"
            for line in self.lines
        )
        return f"Invoice:\n{rendered}\n  Total: {self.total}"
```

Every interface built later — CLI, web, GUI, TUI — can print an invoice by calling `str()` on
it, because the rendering rule lives in one place on the object.

## Your task

In `domain.py`, finish `Invoice.total` so it sums the line totals into a single `Money`,
starting from `Money(0)`. The `__str__` rendering is provided.

## Worked example

```
>>> import domain
>>> p1 = domain.Product("A", "Widget", 1000)
>>> p2 = domain.Product("B", "Gizmo", 250)
>>> inv = domain.Invoice([domain.LineItem(p1, 2), domain.LineItem(p2, 4)])   # 2000 + 1000
>>> inv.total.cents
3000
>>> domain.Invoice().total.cents      # an empty invoice still totals to Money zero
0
>>> print(inv)
Invoice:
  A - Widget x2  $20.00
  B - Gizmo x4  $10.00
  Total: $30.00
```

## What the check verifies, and what it leaves to you

- Enforced: `total` is a `Money` equal to the summed line totals; an empty invoice totals to
  `Money(0)` (still a `Money`, not an int); `str(invoice)` includes the line products and the
  grand total.
- Your free choice: the exact layout of the printed invoice is yours (the check looks for the
  product names and the total amount, not a precise format); what is fixed is that `total` is a
  correct `Money`.

<div class="hint" title="If you are stuck">

`total`: `sum((line.line_total for line in self.lines), Money(0))` — the second argument is the
start value, which keeps an empty invoice's total a `Money`.

</div>

Reference: Python documentation, "sum" (Built-in Functions) and "Data model — object.__str__"
at docs.python.org.
