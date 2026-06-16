# Stage 7: build and parse canonical SKUs

A SKU (stock-keeping unit) is the identifier that ties together inventory, sales, and
reporting. If half the system writes `cat-42-xl` and the other half writes `CAT-0042-XL`,
nothing matches and the data quietly rots. The fix is a **single canonical format** that
one function produces and one function reads back — and that is what you build here. It
ties together the slicing, methods, and format specs from the whole lesson.

The canonical SKU is `CAT-0042-XL`: an upper-case category, a **four-digit zero-padded**
number, and an upper-case size, joined by dashes.

## Building it: format specs do the normalizing

`make_sku` composes the parts and normalizes them as it goes — the format-spec mini-language
from stage 4 does the zero-padding, and `.upper()` from stage 2 the casing:

```
>>> f"{'cat'.upper()}-{42:04d}-{'xl'.upper()}"
'CAT-0042-XL'
```

`{number:04d}` means "this integer, base-10, at least 4 wide, zero-padded" — so `42`
becomes `0042` and `7` becomes `0007`. Padding to a fixed width is what makes SKUs sort
correctly and line up in a column.

## Parsing it back: split, then validate

`parse_sku` reverses the process and **validates** as it goes. Splitting on `-` and
unpacking the parts is the easy half; the important half is rejecting bad input loudly:

```
>>> "CAT-0042-XL".split("-")
['CAT', '0042', 'XL']
```

A real parser does not trust its input. If the SKU does not have exactly three parts, or
the middle is not a number, the right move is to raise a clear `ValueError` rather than
return something half-broken. The two guards are written for you; you supply the final
normalization — upper-case the text parts and turn the number into an `int`.

## Your task

Fill in the two blanks in `text.py`:

1. `make_sku(category, number, size)` — build `CAT-0042-XL` with an f-string: upper-case
   the category and size, zero-pad the number to four digits.
2. `parse_sku(sku)` — after the validity guards, return `(category, number, size)` with the
   text parts upper-cased and the number converted to `int`.

## Worked example

```
>>> import text
>>> text.make_sku("cat", 42, "xl")
'CAT-0042-XL'
>>> text.parse_sku("CAT-0042-XL")
('CAT', 42, 'XL')
>>> text.parse_sku("CAT-0042")        # wrong shape
ValueError: malformed SKU (need 3 dash-separated parts): 'CAT-0042'
```

## What the check verifies, and what it leaves to you

- Enforced: the canonical format (upper-case, four-digit zero-padding); a clean round-trip
  `make_sku` -> `parse_sku`; and a `ValueError` for the wrong segment count or a
  non-numeric middle.
- Your free choice: the exact error message wording, and how you build the string, as long
  as the canonical output and the validation are correct.

<div class="hint" title="If you are stuck">

`make_sku` is `f"{category.upper()}-{number:04d}-{size.upper()}"`. For `parse_sku`, the
final line is `category.upper(), int(number), size.upper()`.

</div>

Reference: Python documentation, "Format Specification Mini-Language" and "Text Sequence
Type — str" at docs.python.org.
