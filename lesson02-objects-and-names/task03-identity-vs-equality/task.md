# Stage 3: identity versus equality

Two of the most confused operators in Python are `==` and `is`. They answer different
questions, and using the wrong one causes bugs that are hard to spot because the code
often works by accident. This stage makes the difference precise.

## Two different questions

- `==` asks: **do these two objects have the same value?** This is **equality**.
- `is` asks: **are these two names pointing at the very same object?** This is
  **identity**. It is the same as checking that `id(a) == id(b)`, where `id(x)` is the
  object's address-like number from stage 1.

Picture two identical-looking shopping receipts. `==` asks "do they say the same
thing?" `is` asks "are these literally the same piece of paper?" Two receipts can be
equal in content while being different pieces of paper.

```
>>> x = ["p"]
>>> y = ["p"]
>>> x == y     # same contents
True
>>> x is y     # but two different list objects
False
>>> z = x
>>> x is z     # z is just another name for the same object
True
```

## The rule of thumb

- Compare to `None`, `True`, and `False` with `is` (for example `if value is None:`).
  There is only ever one `None` object, so identity is exactly the right test, and it
  reads clearly.
- Compare ordinary values with `==` (numbers, strings, lists, and so on). You almost
  always care whether the values match, not whether they are the same object.
- Do not use `is` to compare numbers or strings for equal value. It sometimes appears
  to work and then fails for larger or computed values.

## A trap to know about: interning

You may see `2 is 2` return `True`, or two identical short strings share identity. That
is **interning**: as an optimisation, CPython reuses one object for small integers and
some strings. It is an implementation detail, not a language guarantee. It can differ
between Python versions and between how the values were created, so never write code
whose correctness depends on it. The lesson is simply: for value comparison use `==`;
reserve `is` for `None`/`True`/`False` and for genuine "same object" questions.

## What you are building

A helper, `same_object(a, b)`, that returns `True` only when `a` and `b` are the same
object. Later, MiniERP's audit log uses exactly this kind of check to tell whether two
record references point at one record in memory or at two separate records that merely
look alike. That distinction matters when you are deciding whether an edit to one will
show up in the other.

## Your task

Open `main.py` and complete `same_object` so it returns the identity comparison of `a`
and `b`. Use the identity operator, not `==`.

## What the check verifies

This one is strict, because identity is genuinely right or wrong:

- `same_object(x, x)` is `True` (a thing is the same object as itself).
- For two equal-but-distinct lists `x` and `y`, `x == y` is `True` but
  `same_object(x, y)` is `False`. This proves you used `is`, not `==`.
- `same_object(None, None)` is `True`.

There is no free-choice element here: the only correct implementation is the identity
comparison.

<div class="hint" title="The operator">

The identity operator is the word `is`. The whole body is `return a is b`.

</div>

Reference: Python documentation, "Comparisons" and "Built-in Functions: id()" at
docs.python.org.
