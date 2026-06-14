# Stage 4: None and truthiness

This stage covers two everyday tools: the special value `None`, and Python's idea of
"truthy" and "falsy" values. You will use them to write the first piece of input
hardening in MiniERP.

## None: the "nothing here" object

`None` is Python's way of saying "no value". It is a real object (its type is
`NoneType`), and there is only ever one of it in a running program. You use it for a
slot that has not been filled in: a customer with no phone number yet, a setting that
was never provided.

Two important facts:

- A function with no `return` statement (or a bare `return`) returns `None`
  automatically. So a function that only prints actually returns `None`.
- Because there is exactly one `None`, you test for it with identity: write
  `if value is None:`, not `if value == None:`. The `is` version is the documented
  idiom, reads clearly, and cannot be fooled by an object that defines a funny `==`.

## Truthiness: values that act like True or False

Python lets you put any value where a condition is expected, like in an `if`. It then
asks the value whether it counts as true. The built-in `bool(x)` shows you the answer.

These built-in values are **falsy** (they count as false):

- `None`
- `False`
- zero of any number type: `0`, `0.0`
- empty containers and strings: `""`, `[]`, `{}`, `()`, `set()`

Almost everything else is **truthy**. So a non-empty string is truthy and an empty one
is falsy:

```
>>> bool("Ada")
True
>>> bool("")
False
>>> bool("   ")
True
```

Watch that last one: a string of spaces is **not** empty, so it is truthy. That is a
classic source of bugs, and you will handle it deliberately below by trimming first.

## Why lean on truthiness instead of writing it out

You could write `if len(name) > 0:`. Writing `if name:` is shorter, reads like English,
and works for any container, not just strings. It is the idiomatic Python way. The one
thing to stay alert to is the whitespace case above, which is why real input checks
usually `strip()` first and then test.

## What you are building

`display_name(name)`: return a clean name to show in the interface, or a sensible
default when the name is missing. "Missing" means `None`, an empty string, or a string
that is only whitespace. This is the first taste of MiniERP guarding against messy
input; real customer records get the same treatment later.

The shape of the logic:

1. If `name is None`, there is nothing to show, so return the default.
2. Otherwise strip the surrounding whitespace.
3. If what remains is truthy (a non-empty string), return it; if not, return the
   default.

## Your task

Open `main.py` and fill the two blanks in `display_name`: the `None` check, and the
truthiness test on the trimmed string.

## What the check verifies, and what it leaves to you

- Enforced: a real name comes back (and surrounding spaces are trimmed, so
  `"  Bob  "` gives `"Bob"`); `None`, `""`, and `"   "` all fall back to the same
  non-empty default. That defaulting behaviour is the rule.
- Your free choice: the default word. The solution uses `"Guest"`, but `"Customer"` or
  `"Anonymous"` pass just as well, as long as you use it consistently for every missing
  case.

<div class="hint" title="The two blanks">

First blank: the missing check is `name is None`. Second blank: once you have
`cleaned = name.strip()`, the truthiness test is just `cleaned`.

</div>

Reference: Python documentation, "Truth Value Testing" and "Built-in Constants: None"
at docs.python.org.
