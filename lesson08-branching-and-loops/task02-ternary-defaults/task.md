# Stage 2: conditional expressions (the ternary)

An `if/elif/else` is a **statement** — it does something but has no value, so you cannot
put it on the right of an `=`. Often, though, all you want is to choose between two
*values*. Writing a four-line if/else just to assign one of two things is heavy:

```
if currency == "USD":
    symbol = "$"
else:
    symbol = currency + " "
```

A **conditional expression** — the "ternary" — collapses that into one expression that
has a value:

```
symbol = "$" if currency == "USD" else f"{currency} "
```

Read it as "the value `'$'` **if** the currency is USD **else** the other value". The
shape is `A if CONDITION else B`. Because it is an expression, it can go anywhere a value
can: in an assignment, inside an f-string, as a function argument, even inside a larger
expression.

Use it when each branch is a simple value and the whole thing still reads cleanly. When
the branches do real work, or you would have to nest one ternary inside another, a normal
`if` statement is clearer — readability is the deciding factor, not brevity.

## Your task

In `pricing.py`, finish two functions, each with a single conditional expression:

1. `display_price(price_cents, currency='USD')` — pick the currency mark: `'$'` when the
   currency is `'USD'`, otherwise the ISO code followed by a space (so `'EUR'` renders as
   `'EUR 15.00'`). The formatting around it is written for you.
2. `clamp_floor(price_cents)` — return the price unchanged when it is zero or positive,
   but `0` when it is negative. (Stacked discounts could push a price below zero; this
   keeps it from ever displaying as a negative amount.)

## Worked example

```
>>> import pricing
>>> pricing.display_price(1500)
'$15.00'
>>> pricing.display_price(1500, "EUR")
'EUR 15.00'
>>> pricing.clamp_floor(-50), pricing.clamp_floor(250)
(0, 250)
```

## What the check verifies, and what it leaves to you

- Enforced: `display_price` uses `$` for USD and shows the code for anything else, with the
  amount formatted as dollars and cents; `clamp_floor` returns 0 for negatives and the
  value itself otherwise.
- Your free choice: the exact symbol layout for non-USD currencies is yours (a trailing
  space, a colon, whatever reads well) as long as the ISO code is shown and `$` is not. A
  full `if/else` statement instead of a ternary also passes — the ternary is what the
  stage teaches, not what the check demands.

<div class="hint" title="If you are stuck">

The symbol line is `"$" if currency == "USD" else f"{currency} "`. The clamp is
`price_cents if price_cents >= 0 else 0`.

</div>

Reference: Python documentation, "Conditional expressions" at docs.python.org.
