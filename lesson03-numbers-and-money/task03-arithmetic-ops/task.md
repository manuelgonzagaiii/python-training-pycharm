# Stage 3: arithmetic, division, and divmod

Now you write code. This stage creates `money.py`, the module that becomes MiniERP's
numeric core — every price, total, and tax in the system will eventually pass through
it. You start it with the plain integer maths an inventory needs, because getting
division and remainders right is the foundation everything else stands on.

## The two divisions Python gives you

Most languages have one `/`. Python has two, on purpose:

- `/` is **true division** and **always returns a float**: `7 / 2` is `3.5`, and even
  `6 / 2` is `3.0`, not `3`.
- `//` is **floor division** and keeps the type: `7 // 2` is `3` (it rounds toward
  negative infinity). `%` is the **modulo** (remainder): `7 % 2` is `1`.

The identity that ties them together, and that you will rely on constantly:

```
(a // b) * b + (a % b) == a
```

In words: the whole part times the divisor, plus the leftover, gives you back the
original. For packing 27 units into cases of 12: `27 // 12` is `2` full cases, `27 % 12`
is `3` loose units, and `2 * 12 + 3` is `27`. Nothing is lost.

## divmod: both answers in one call

When you need *both* the quotient and the remainder — which is almost always, for
packing and change-making — `divmod(a, b)` returns them as a tuple in one step:

```
>>> divmod(27, 12)
(2, 3)
```

That is exactly `(27 // 12, 27 % 12)`, but it does the division once instead of twice,
and it reads as a single idea: "split 27 into groups of 12." Prefer it when you want
both parts.

(You will also meet `pow(base, exp)` — the same as `**` — and its three-argument form
`pow(base, exp, mod)` for modular arithmetic, plus `abs()`, unary minus, and
`round(number, ndigits)`. They are in the feature list for this stage; try them in the
REPL. The task below focuses on the division tools MiniERP leans on most.)

## Your task

Open `money.py` and fill in the blanks in two functions:

1. `units_to_cases(units, per_case)` — return `(full_cases, loose_units)`. Use `divmod`
   to get both at once.
2. `split_evenly(total, parts)` — return `(base_share, remainder)`. Use `//` for the
   base share and `%` for what is left over.

Run it however you like to experiment, then press **Check**.

## Worked example

```
>>> import money
>>> money.units_to_cases(27, 12)
(2, 3)
>>> money.split_evenly(100, 3)      # 100 split 3 ways
(33, 1)                              # 33 each, 1 left over -> 33*3 + 1 == 100
```

## What the check verifies, and what it leaves to you

Following this course's grading rule, the check judges whether your maths is *correct*,
not whether you wrote it the way we did.

- Enforced: `units_to_cases` must return `(full_cases, loose_units)` that reconstruct the
  total (`full * per_case + loose == units`) with a valid remainder; `split_evenly` must
  return shares that add back to `total`. Both must hold for edge cases like `parts == 1`
  and `total == 0`.
- Your free choice: how you write each body. `divmod(units, per_case)` and
  `(units // per_case, units % per_case)` are both accepted, because both are correct.

<div class="hint" title="If you are stuck">

`divmod(a, b)` already returns the `(quotient, remainder)` tuple — for `units_to_cases`
you can return its result directly. For `split_evenly`, `total // parts` is the base
share and `total % parts` is the remainder.

</div>

Reference: Python documentation, "Built-in Functions — divmod()" and "Numeric Types —
int, float, complex" at docs.python.org.
