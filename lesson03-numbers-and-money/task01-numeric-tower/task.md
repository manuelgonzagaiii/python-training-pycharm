# Stage 1: the numeric tower — int, float, bool, complex

Before MiniERP touches a single price, you need to choose the right *kind* of number
for each job. Python gives you four built-in numeric types, and picking the wrong one
is how real accounting systems end up a cent off on a million-dollar invoice. This
stage has no code to submit. It builds the mental model that every later money decision
rests on.

## int: whole numbers with no ceiling

A Python `int` is a whole number with **arbitrary precision** — it grows as large as
your memory allows and never silently overflows the way integers do in C or Java.

```
>>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376
>>> (2 ** 200).bit_length()
201
```

That matters for MiniERP: quantities, counts, and (later) money stored as whole cents
are all `int`. You will never lose precision on them. The `.bit_length()` method tells
you how many binary digits a number needs — useful when we get to bit flags in stage 5.

You can write integer literals in several bases, and group digits with underscores for
readability (the underscores are ignored by Python):

```
>>> 1_000_000          # one million, easy to read
1000000
>>> 0xFF, 0o17, 0b1010 # hex, octal, binary -> all plain ints
(255, 15, 10)
```

## float: fast, but only an approximation

A `float` is an **IEEE-754 double**: a fixed-width binary fraction. It is fast and fine
for measurements and science, but it **cannot represent most decimal fractions
exactly** — including ordinary prices like `0.10`. That is not a Python quirk; it is how
binary fractions work, and every language with floats has it.

```
>>> 0.1 + 0.2
0.30000000000000004
```

Hold onto that result. The next stage is a quiz built entirely around it, and it is the
single reason MiniERP will store money as `Decimal` (stage 6) and never as `float`.

## bool: True and False are integers

`bool` is a **subclass of `int`**. `True` is `1` and `False` is `0`, and they do
arithmetic:

```
>>> True + True
2
>>> isinstance(True, int)
True
```

This is occasionally handy — `sum(line.taxable for line in lines)` counts how many
lines are taxable — but it also bites people: a function that returns `True`/`False`
will quietly pass where an `int` is expected. Know that the overlap exists so it never
surprises you.

## complex: real, and almost always irrelevant here

`complex` numbers (written `3 + 4j`) are first-class in Python, with `.real`, `.imag`,
and `abs()` for magnitude:

```
>>> z = 3 + 4j
>>> z.real, z.imag, abs(z)
(3.0, 4.0, 5.0)
```

They are genuinely useful for signal processing and geometry — Lesson 4 uses them for
2-D coordinates — but they have **no place in business arithmetic**. You will not see
`complex` anywhere near a MiniERP price. It is on this list so that when you meet it,
you recognise it and move on.

## How to tell what you have

Two built-ins answer "what type is this?":

- `type(x)` returns the exact type object.
- `isinstance(x, int)` asks whether `x` is an `int` **or a subclass** (so it is `True`
  for a `bool`). Prefer `isinstance` for checks, because it respects subclassing.

```
>>> type(42), type(3.5), type(True)
(<class 'int'>, <class 'float'>, <class 'bool'>)
>>> isinstance(True, int)   # bool counts as int
True
```

## The design decision this sets up

Here is the rule the rest of the phase enforces, decided now on purpose:

- **Quantities and counts** (units in stock, items per case) -> `int`. Exact, unbounded.
- **Money** -> `Decimal` (stage 6), never `float`. Cents must be exact.
- **Exact ratios** (a tax rate like 8.25%) -> `Fraction` (stage 7).
- **`complex`** -> never, in business code.

There is nothing to run through the checker here. Try the snippets above in the REPL,
make sure the `0.1 + 0.2` result genuinely surprises you, then move to the quiz.

Reference: Python documentation, "Built-in Types — Numeric Types" at docs.python.org.
