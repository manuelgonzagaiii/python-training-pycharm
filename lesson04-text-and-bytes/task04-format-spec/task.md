# Stage 4: the format-spec mini-language

An f-string can do more than insert a value — after a colon you can give a **format spec**
that controls width, alignment, padding, thousands separators, and decimal places. This is
the little language behind every aligned table, every `$1,234.50`, every zero-padded
number you will print. MiniERP's receipts, CLI tables, and reports all run on the two
helpers you write here.

## The shape of a format spec

Inside `{value:spec}`, the spec reads (each part optional):

```
[fill][align][sign][#][0][width][grouping][.precision][type]
```

The parts you will use most:

- **align**: `<` left, `>` right, `^` centre. A **fill** character can go before it
  (`*^10` centres in 10 columns padded with `*`). `0` before the width zero-pads numbers.
- **width**: the minimum number of columns.
- **grouping**: `,` inserts thousands commas (`_` groups with underscores).
- **.precision** with type **`f`**: fixed-point with that many decimals. Other types:
  `d` integer, `x`/`o`/`b` hex/octal/binary, `%` percentage, `e` scientific.

```
>>> f"{1234.5:,.2f}"      # comma grouping, two decimals
'1,234.50'
>>> f"{'Hi':>8}"          # right-align in 8 columns
'      Hi'
>>> f"{7:03d}"            # zero-pad an int to width 3
'007'
```

A `Decimal` honours the same spec, so `f"{amount:,.2f}"` formats money correctly without
ever converting to float.

## Dynamic (nested) fields

Width and precision can themselves come from variables, by nesting `{ }` inside the spec.
This is how you align to a width computed at runtime:

```
>>> width, align = 10, "^"
>>> f"{'Hi':{align}{width}}"     # centre in a width decided by code
'    Hi    '
```

## Your task

Fill in the two format specs in `text.py`:

1. `fmt_money(amount)` — render a `Decimal` as `$1,234.50`: a literal `$`, then comma
   grouping and two decimals.
2. `fmt_col(value, width, align)` — pad and align `value` to `width`, where `align` is one
   of `<`, `>`, `^` chosen at runtime (a nested field).

## Worked example

```
>>> import text
>>> from decimal import Decimal
>>> text.fmt_money(Decimal("1234.5"))
'$1,234.50'
>>> text.fmt_col("Hi", 6, "^")
'  Hi  '
```

## What the check verifies, and what it leaves to you

- Enforced: `fmt_money` produces a leading `$`, thousands commas, and exactly two
  decimals (`1234.5` -> `$1,234.50`, `1000000` -> `$1,000,000.00`); `fmt_col` pads to the
  given width and honours each alignment.
- Your free choice: how you write the spec, as long as the output matches. The format-spec
  form and an equivalent built using `str.format()` or `format()` would both be accepted.

<div class="hint" title="If you are stuck">

`fmt_money` is `f"${amount:,.2f}"`. `fmt_col` nests the alignment and width:
`f"{value:{align}{width}}"`.

</div>

Reference: Python documentation, "Format Specification Mini-Language" at docs.python.org.
