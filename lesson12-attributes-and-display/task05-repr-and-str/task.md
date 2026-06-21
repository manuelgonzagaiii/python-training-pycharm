# Stage 5: __repr__ and __str__

By default, printing an object gives something useless like `<domain.Money object at
0x10f3c2a50>`. Python lets a class control how it appears, through two methods aimed at two
different audiences: `__repr__` for developers and `__str__` for end users. This stage gives
`Money` and `Product` both.

## Two renderings, two audiences

- **`__repr__`** is for **developers**: an unambiguous, ideally **eval-able** string that says
  exactly what the object is. The convention is that `repr(obj)` looks like the code to recreate
  it. It is what you see in the REPL, in a debugger, and inside a list's output.
- **`__str__`** is for **end users**: a readable, friendly rendering. It is what `print(obj)`
  and `str(obj)` show.

```
    def __repr__(self):
        return f"Money(cents={self.cents}, currency={self.currency!r})"

    def __str__(self):
        symbol = "$" if self.currency == "USD" else f"{self.currency} "
        sign = "-" if self.cents < 0 else ""
        whole, rem = divmod(abs(self.cents), 100)
        return f"{sign}{symbol}{whole}.{rem:02d}"
```

So `repr(Money(1500))` is `"Money(cents=1500, currency='USD')"` — paste it back into Python and
you rebuild the object — while `str(Money(1500))` is `"$15.00"`. Note the `!r` in the repr: it
formats `currency` with *its* repr, so the string keeps its quotes (`'USD'`), which is what
makes the whole thing eval-able.

The `__str__` handles a negative amount correctly — money can go negative (a credit, or
`Money(100) - Money(300)`). Splitting the sign off first and formatting the **magnitude** with
`divmod(abs(...), 100)` gives `-$2.50`, not the wrong `$-2.50` you would get from letting
`//` and `%` run on a negative (they round toward negative infinity).

Two practical rules:

- If you define only one, define `__repr__`. When `__str__` is missing, `str()` falls back to
  `__repr__`, so a good repr is never wasted. There is no fallback the other way.
- In an f-string, `f"{obj!r}"` forces the repr and `f"{obj}"` uses the str — the same `!r`
  conversion flag you are using inside `Money.__repr__`.

`Product` gets the same treatment: a repr listing its fields, and a `str` that reuses the
`label()` you already wrote.

## Your task

In `domain.py`, finish two `__repr__` methods:

1. `Money.__repr__` — an eval-able form like `Money(cents=1500, currency='USD')`.
2. `Product.__repr__` — an unambiguous form listing the SKU, name, and price.

The `__str__` methods are provided.

## Worked example

```
>>> import domain
>>> repr(domain.Money(1500, "USD"))
"Money(cents=1500, currency='USD')"
>>> print(domain.Money(1500))
$15.00
>>> repr(domain.Product("A-001", "Widget", 999))
"Product(sku='A-001', name='Widget', price_cents=999)"
>>> print(domain.Product("A-001", "Widget", 999))
A-001 - Widget
```

## What the check verifies, and what it leaves to you

- Enforced: `repr(Money(1500, "USD"))` is eval-able back into an equal-valued `Money` (the
  cents and currency survive a round trip); `Product`'s repr contains its SKU and price; `str`
  produces the human forms.
- Your free choice: the exact repr layout is yours, as long as it is unambiguous and rebuilds
  the value when eval'd. The check evals your `Money` repr and compares the value, so any
  faithful, eval-able form passes — it does not pin one spelling.

<div class="hint" title="If you are stuck">

`Money.__repr__`: `f"Money(cents={self.cents}, currency={self.currency!r})"` — the `!r` keeps
the quotes around the currency so the string is eval-able. `Product.__repr__` follows the same
shape over `sku`, `name`, `price_cents`.

</div>

Reference: Python documentation, "Data model — object.__repr__ and object.__str__" at
docs.python.org.
