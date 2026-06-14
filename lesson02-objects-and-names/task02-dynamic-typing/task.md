# Stage 2: variables are names, not boxes

This stage fixes the most important beginner misconception about Python variables. Get
this right and a whole class of bugs disappears.

## The wrong model and the right model

Many languages teach you that a variable is a **box** that holds a value. You put a
value in the box; the box has a fixed size and type. Python does not work that way.

In Python a variable is a **name** that points at an object. The object lives
somewhere; the name is just a label attached to it. Assignment does not copy a value
into a box; it points a name at an object.

```
>>> x = 42        # the name x now points at the int object 42
>>> x = "MiniERP" # the SAME name now points at a str object instead
```

Nothing about `x` was "the integer variable". `x` is just a label, and you moved the
label from one object to another. This is what **dynamic typing** means: the type
belongs to the object, not to the name. A name can point at an int now and a string a
moment later.

You can watch it happen with `type()`:

```
>>> x = 42
>>> type(x)
<class 'int'>
>>> x = "MiniERP"
>>> type(x)
<class 'str'>
```

The type reported is always the type of the object the name currently points at.

## Why the right model matters

- It explains why Python never complains that you "changed the type of a variable".
  There is no typed box to violate; you just moved a label.
- It is the foundation for understanding the next stage (identity versus equality) and,
  much later, why two names can point at the same list and a change through one is seen
  through the other. The box model cannot explain that; the name model makes it
  obvious.

## What you are building

A small helper, `describe(value)`, that reports what a value currently is. It will
become a debugging aid that MiniERP uses to print configuration values with their
types (handy when a setting is the string `"30"` but should have been the number
`30`). For now it shows that one function, through one name `value`, can handle objects
of any type.

Two tools do the work:

- `type(value).__name__` gives the type's short name, for example `int`, `str`, or
  `NoneType`.
- The `!r` conversion inside an f-string inserts the value's `repr`, the unambiguous
  form. For a string that means it keeps the quotes, so `'x'` is clearly a string and
  not the bare letter x.

```
>>> f"{42!r} is a {type(42).__name__}"
'42 is a int'
>>> f"{'x'!r} is a {type('x').__name__}"
"'x' is a str"
```

(The grammar reads "42 is a int" rather than "an int"; correct articles are not worth
the complexity here, and real tools usually do not bother either.)

## Your task

Open `main.py`. Fill the blank in `describe` so it returns a string that includes the
value's `repr` (use `!r`) and its type name (`type(value).__name__`). Try it in the
REPL with an int, a string, and `None`, then press Check.

## What the check verifies, and what it leaves to you

- Enforced: `describe(value)` returns a string that contains both the value's `repr`
  and its type name, for several different types including `None`. These are true facts
  about the object, so they are the rule.
- Your free choice: the wording around them. "42 is a int", "42 (int)", or
  "int: 42" all pass, because all contain the two required facts.

> Design note: this helper lives in `main.py` for now because we have only one file so
> far. When the course reaches modules and packages, helpers like this move to their
> proper home. Watching that reorganisation happen is part of the point.

<div class="hint" title="Building the string">

An f-string with two slots does it in one line:
`f"{value!r} is a {type(value).__name__}"`.

</div>

Reference: Python documentation, "Built-in Functions: type()" and the f-string
conversion field `!r` in the language reference, at docs.python.org.
