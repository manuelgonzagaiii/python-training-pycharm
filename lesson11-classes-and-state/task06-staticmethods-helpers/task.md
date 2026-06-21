# Stage 6: stateless helpers with @staticmethod

Some logic is *about* products but needs no particular product to run. "Is this string a
valid SKU?" is a rule you want to check **before** you have a Product at all — during import,
or while validating a form. It belongs with `Product` conceptually, but it touches neither a
specific instance (`self`) nor the class (`cls`). That is exactly what `@staticmethod` is for.

## What a staticmethod is

A `@staticmethod` is a plain function that lives inside the class for organisation, but
receives **no** automatic first argument:

```
    @staticmethod
    def is_valid_sku(value):
        return bool(value) and all(ch.isalnum() or ch == "-" for ch in value)
```

You call it on the class — `Product.is_valid_sku("A-001")` — and it just runs. No instance is
created, no `self`, no `cls`. It is namespaced on `Product` because that is where a reader
expects to find "the rule for what a valid SKU looks like".

## Choosing between the three method kinds

This completes the trio. The mental model for which to use:

- **Instance method** (`self`): needs a particular object's data. `product.price_display()`.
- **Classmethod** (`cls`): needs the class, usually to build an instance. `Product.from_row(...)`.
- **Staticmethod** (no `self`/`cls`): needs neither — a related helper that just happens to
  belong here. `Product.is_valid_sku(...)`.

A fair question: why not a module-level free function instead of a staticmethod? Either works;
the staticmethod wins when the helper is tightly bound to the class's rules and you want
`Product.is_valid_sku` to be discoverable right on the type. It also lets a subclass override
the rule. Use a free function when the helper is general and not really "about" the class.

## Your task

In `domain.py`, finish `Product.is_valid_sku(value)` so it returns `True` only when `value`
is non-empty and every character is alphanumeric or a hyphen.

## Worked example

```
>>> import domain
>>> domain.Product.is_valid_sku("A-001")
True
>>> domain.Product.is_valid_sku("AB12")
True
>>> domain.Product.is_valid_sku("")          # empty -> not valid
False
>>> domain.Product.is_valid_sku("bad sku")   # a space is not allowed
False
```

## What the check verifies, and what it leaves to you

- Enforced: an empty string is rejected; a string with a space or punctuation is rejected; a
  string of letters, digits, and hyphens is accepted.
- Your free choice: how you express the rule. A loop, a regular expression, or the
  `all(...)` generator shown all pass — the check grades which strings are accepted and
  rejected, not the technique.

<div class="hint" title="If you are stuck">

`bool(value)` is `True` for a non-empty string. `all(ch.isalnum() or ch == "-" for ch in
value)` checks every character. Combine them with `and`.

</div>

Reference: Python documentation, "@staticmethod" (Built-in Functions) at docs.python.org.
