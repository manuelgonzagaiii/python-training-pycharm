# Stage 9: integer-like objects with __index__

An invoice line is often referred to by its number — "line 3". Passing that around as a bare
`int` loses meaning and invites mistakes (which int was a line number, which a quantity?). A
small value object, `LineRef`, makes the intent explicit while still **behaving like an
integer** everywhere a position is needed — because it implements `__index__`.

## __index__: lossless integer conversion

`__index__` is the protocol for "this object IS an integer position". When Python needs a real
integer for indexing, slicing, or `range()`, it calls `__index__`:

```
class LineRef:
    def __init__(self, number):
        if number < 1:
            raise ValueError("line number is 1-based")
        self.number = number

    def __index__(self):
        return self.number
```

With that one method, a `LineRef` works as a list index (`seq[ref]`), inside a slice
(`seq[a:ref]`), as a `range()` argument, and via `operator.index(ref)` — the canonical "give me
a real int, losslessly" call. It also feeds `bin()`, `hex()`, and `oct()`, which call
`operator.index` internally. (Number-base *formatting* like `format(ref, 'x')` is a separate
protocol — `__format__`, not `__index__` — so it would need its own method and is not provided
by `__index__` alone.)

## Why __index__, not __int__

Python has two "make an int" hooks, and the difference is the whole point of this stage:

- `__int__` is for **lossy** conversions — `int(3.7)` truncates to `3`. Float defines it.
- `__index__` is for objects that **are exactly an integer**, with no truncation. Only true
  integer-like types should define it.

By defining `__index__` and *not* `__int__`, `LineRef` guarantees a line position is always an
exact whole number — there is no float-style truncation path. `operator.index()` enforces this:
it accepts `__index__` objects and **rejects** anything that only offers `__int__`, so code that
uses `operator.index` can never silently truncate a float into a line number. Choosing
`__index__` is a correctness statement: positions are integers, full stop.

## Your task

In `domain.py`, finish `LineRef.__index__` so it returns the underlying 1-based `number`. The
constructor (which rejects numbers below 1) and `__repr__` are provided.

## Worked example

```
>>> import domain, operator
>>> operator.index(domain.LineRef(5))
5
>>> [10, 20, 30, 40][domain.LineRef(2)]      # used as a list index
30
>>> list(range(domain.LineRef(1), domain.LineRef(4)))   # used as range bounds
[1, 2, 3]
>>> domain.LineRef(0)
Traceback (most recent call last):
ValueError: line number is 1-based
```

## What the check verifies, and what it leaves to you

- Enforced: `operator.index(ref)` returns the number; a `LineRef` works as a list index and as
  `range()` arguments; a number below 1 raises `ValueError`.
- Your free choice: how you store and return the number, as long as `__index__` yields the
  exact integer. The check uses the value in real indexing/range contexts, so any faithful
  implementation passes.

<div class="hint" title="If you are stuck">

`__index__` is one line: `return self.number`. That single method is what lets the object stand
in for an int in `seq[ref]`, slices, and `range()`.

</div>

Reference: Python documentation, "Data model — object.__index__" and "operator.index" at
docs.python.org.
