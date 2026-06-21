# Stage 6: custom format specs with __format__

You have seen the format-spec mini-language — `f"{x:.2f}"`, `f"{n:>8}"`. The text after the
colon is a **format spec**, and a class can interpret its own specs by implementing
`__format__`. This lets the reporting layer ask a `Money` for exactly the rendering it needs —
a short `$15.00`, a currency-qualified `15.00 USD`, or the raw `1500` cents — all from one
object, just by changing the spec.

## How __format__ is called

When you write `format(money, "full")` or `f"{money:full}"`, Python calls
`money.__format__("full")`. The method receives the spec string (everything after the colon, or
`""` when there is none) and returns the rendered string. You choose what the specs mean:

```
    def __format__(self, spec):
        if spec in ("", "money"):
            return str(self)                 # '$15.00' -- reuse __str__
        if spec == "full":
            sign = "-" if self.cents < 0 else ""
            whole, rem = divmod(abs(self.cents), 100)
            return f"{sign}{whole}.{rem:02d} {self.currency}"   # '15.00 USD'
        if spec == "cents":
            return str(self.cents)           # '1500'
        raise ValueError(f"unknown Money format spec: {spec!r}")
```

Three habits this shows:

- **The empty spec is the default.** `f"{money}"` passes `""`, so handle it (here by delegating
  to `__str__`, which keeps the default rendering in one place).
- **Dispatch on the spec, then build the string.** A simple `if`/`if` chain over known specs is
  perfectly idiomatic; `match`/`case` works too.
- **Reject the unknown.** An unrecognised spec should raise — failing loudly beats silently
  returning the wrong thing. The built-in types do the same (`format(3, "q")` raises).

Because the amount is integer cents, every rendering is built with integer math (`// 100`,
`% 100`) and stays exact — no float, even at the display edge.

## Your task

In `domain.py`, finish `Money.__format__` for the two remaining specs: `"full"` returns
`'15.00 USD'` (dollars, two-digit cents, a space, the currency), and `"cents"` returns the raw
cents as a string. The empty/`"money"` case and the error for unknown specs are provided.

## Worked example

```
>>> import domain
>>> m = domain.Money(1500)
>>> format(m)                 # default spec
'$15.00'
>>> format(m, "full")
'15.00 USD'
>>> format(m, "cents")
'1500'
>>> f"Total: {m:full}"
'Total: 15.00 USD'
>>> format(m, "bogus")
Traceback (most recent call last):
ValueError: unknown Money format spec: 'bogus'
```

## What the check verifies, and what it leaves to you

- Enforced: the default spec gives `'$15.00'`; `"full"` carries the dollars-and-cents and the
  currency code (e.g. `'15.00 USD'`, with no `$`); `"cents"` gives `'1500'`; an unknown spec
  raises `ValueError`.
- Your free choice: the exact text of the `"full"` rendering is yours within reason (dollars,
  cents, and the currency code must all appear, and the check grades for those pieces, not a
  precise layout); the spec *names* are fixed because callers and the reporting layer rely on
  them, and an unknown spec must fail rather than guess.

<div class="hint" title="If you are stuck">

`"full"`: format the dollars and cents (handling a leading sign the way `__str__` does) then a
space and `self.currency` — e.g. `f"{sign}{whole}.{rem:02d} {self.currency}"` after
`whole, rem = divmod(abs(self.cents), 100)`. `"cents"`: `str(self.cents)`. Both go before the
final `raise`, so a known spec returns and only an unknown one falls through to the error.

</div>

Reference: Python documentation, "Data model — object.__format__" and "Format Specification
Mini-Language" at docs.python.org.
