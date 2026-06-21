# Stage 4: behavior lives on the object

In earlier phases, turning a price into a display string meant calling a free function and
passing the data in: `display_price(price_cents, currency)`. Now that a product is an object
that already holds its price and knows its currency, that behavior belongs **on the object**
as a method. This stage migrates the display logic onto `Product` so callers write
`product.price_display()` and the method fetches what it needs from `self`.

## A method reads the object through `self`

A method can reach every piece of the instance's state — its instance attributes and the
class attributes — through `self`:

```
    def price_display(self):
        symbol = "$" if self.CURRENCY == "USD" else f"{self.CURRENCY} "
        return f"{symbol}{self.price_cents // 100}.{self.price_cents % 100:02d}"
```

Note what `self` reaches: `self.price_cents` (an instance attribute, different per product)
and `self.CURRENCY` (the class attribute from the last stage, shared). The method does not
take a price argument — it already *is* a product, so it asks itself. That is the shift in
thinking: instead of "a function that operates on a product", a method is "something the
product can do".

A method may also call other methods on the same object via `self.other_method()`, so
behavior composes without any data being threaded through by hand. Keeping the display rule on
the class also means every interface — CLI, web, GUI, TUI — renders a price the same way by
calling the one method, rather than each re-implementing the formatting.

## Your task

In `domain.py`, finish `Product.price_display()` so it returns the price as a currency string
like `'$15.00'`. The `symbol` line (which picks `$` for USD) is provided; you write the
returned string that places the symbol in front of the dollars and zero-padded cents drawn
from `self.price_cents`.

## Worked example

```
>>> import domain
>>> domain.Product("A-001", "Widget", 1500).price_display()
'$15.00'
>>> domain.Product("B-010", "Gizmo", 999).price_display()
'$9.99'
>>> domain.Product("C-1", "Bit", 5).price_display()
'$0.05'
```

## What the check verifies, and what it leaves to you

- Enforced: `price_display()` renders integer cents as dollars and cents with the currency
  symbol — `1500` becomes `'$15.00'`, `5` becomes `'$0.05'` (the cents are always two
  digits).
- Your free choice: how you build the string is yours, as long as the value is right. The
  two-digit cents and the dollar separation are what the check insists on, because a price
  display that drops the leading zero on cents (`$15.0`) is simply wrong.

<div class="hint" title="If you are stuck">

`self.price_cents // 100` is the whole dollars; `self.price_cents % 100` is the leftover
cents. Format the cents with `:02d` so `5` shows as `05`:
`f"{symbol}{self.price_cents // 100}.{self.price_cents % 100:02d}"`.

</div>

Reference: Python documentation, "Classes — Method Objects" at docs.python.org.
