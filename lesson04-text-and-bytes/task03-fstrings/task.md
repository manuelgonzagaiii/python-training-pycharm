# Stage 3: f-strings and self-documenting output

You have used f-strings already to build simple messages. This stage goes deeper: running
real expressions inside them, and the `{value=}` debug form that is one of the most
useful small features in modern Python. These two helpers in `text.py` feed MiniERP's
logging and, later, its receipt and CLI output.

## f-strings run expressions, not just names

An f-string is a string prefixed with `f`; anything inside `{ }` is **evaluated as
Python**, not just substituted:

```
>>> qty, price = 3, 9.99
>>> f"{qty} x {price} = {qty * price}"
'3 x 9.99 = 29.97'
>>> f"line for {name.upper()}"     # method calls work too
```

You can also control how a value is rendered with a **conversion flag** before any format
spec:

- `!r` uses `repr()` — quotes strings and shows types, ideal for debugging.
- `!s` uses `str()` — the human-readable form (the default for plain `{x}`).
- `!a` is like `!r` but ASCII-only.

```
>>> name = "Café"
>>> f"{name!r}"     # repr: quoted, escapes preserved
"'Café'"
```

## The self-documenting `{value=}` form

Put an `=` right after the expression and Python prints **both the expression text and its
value** — perfect for logs and quick debugging:

```
>>> sku, qty = "AB-1", 3
>>> f"{sku=} {qty=}"
"sku='AB-1' qty=3"
```

Notice `sku` came out **quoted** (`sku='AB-1'`): the `=` form uses `repr` by default, so
you see the type at a glance. A `Decimal` shows as `price=Decimal('9.99')` — which is
exactly what you want in a debug line, because it proves the value is a `Decimal` and not
a stray float. (For human output you would instead use `!s` or a format spec, which is the
next stage.)

## Your task

Fill in the two f-strings in `text.py`:

1. `debug_line(sku, qty, price)` — a self-documenting line using the `{x=}` form for each
   of `sku`, `qty`, and `price`.
2. `receipt_line(name, total)` — a human line like `Widget: $9.99`, interpolating the name
   and the `Decimal` total.

## Worked example

```
>>> import text
>>> from decimal import Decimal
>>> text.debug_line("AB-1", 3, Decimal("9.99"))
"sku='AB-1' qty=3 price=Decimal('9.99')"
>>> text.receipt_line("Widget", Decimal("9.99"))
'Widget: $9.99'
```

## What the check verifies, and what it leaves to you

- Enforced: `debug_line` is self-documenting (each value labelled `name=`) and uses the
  `repr` form, so `sku` appears quoted; `receipt_line` contains the name and the money as
  `$9.99`.
- Your free choice: spacing and the exact receipt layout, as long as the labelled debug
  values and the `$`-prefixed total are present.

<div class="hint" title="If you are stuck">

`debug_line` is `f"{sku=} {qty=} {price=}"`. `receipt_line` is `f"{name}: ${total}"`.

</div>

Reference: Python documentation, "Lexical analysis — Formatted string literals" at
docs.python.org.
