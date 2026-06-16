# Stage 1: string indexing and slicing

This lesson builds `text.py`, MiniERP's module for everything to do with text — cleaning
input, formatting output, building identifiers, and turning records into bytes. It
starts where every string operation starts: pulling pieces out of a string by position.
MiniERP's SKUs (stock-keeping unit codes) like `AB-1234-XL` have fixed-position segments,
so slicing is exactly the right tool to read them.

## Indexing: one character by position

A string is a sequence of characters, numbered from `0`. Index with `s[i]`, and use
**negative** indices to count from the end — `s[-1]` is the last character:

```
>>> s = "MiniERP"
>>> s[0], s[-1]
('M', 'P')
```

`len(s)` gives the length. Strings are **immutable**: `s[0] = "x"` is an error, so every
operation here returns a *new* string rather than changing the original.

## Slicing: a whole range at once

`s[start:stop]` returns the substring from `start` up to **but not including** `stop`:

```
>>> "AB-1234-XL"[0:2]      # first two characters
'AB'
>>> "AB-1234-XL"[3:7]      # the number block
'1234'
```

Omit a bound to mean "the end": `s[:n]` is the first `n` characters, `s[-n:]` is the last
`n`. Add a third number, the **step**: `s[::2]` takes every other character, and the
idiom `s[::-1]` walks backwards, reversing the string.

```
>>> code = "AB-1234-XL"
>>> code[:2], code[-2:], code[::-1]
('AB', 'XL', 'LX-4321-BA')
```

One property that saves you constant length-checking: **slices clamp**. Asking for more
than is there just gives you what exists — `"A"[:5]` is `"A"`, never an error. (Plain
indexing past the end, `"A"[5]`, *does* raise `IndexError`; slicing does not.)

## Your task

Fill in the three slices in `text.py`:

1. `sku_prefix(sku, n=2)` — the first `n` characters.
2. `sku_suffix(sku, n=2)` — the last `n` characters, via a negative start.
3. `reversed_code(sku)` — the whole string reversed.

## Worked example

```
>>> import text
>>> text.sku_prefix("AB-1234-XL"), text.sku_suffix("AB-1234-XL")
('AB', 'XL')
>>> text.reversed_code("ABC123")
'321CBA'
>>> text.sku_prefix("A", 2)        # short string: clamps, no error
'A'
```

## What the check verifies, and what it leaves to you

- Enforced: correct prefix/suffix for the default and a custom length, a correct
  reversal, and that short strings clamp instead of raising.
- Your free choice: the exact slice expressions, as long as they produce the right
  substrings.

<div class="hint" title="If you are stuck">

`sku[:n]` is the first `n`; `sku[-n:]` is the last `n`; `sku[::-1]` reverses.

</div>

Reference: Python documentation, "Text Sequence Type — str" and "Common Sequence
Operations" at docs.python.org.
