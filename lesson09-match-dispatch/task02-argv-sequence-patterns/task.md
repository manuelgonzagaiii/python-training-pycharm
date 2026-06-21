# Stage 2: sequence patterns and the token parser

A command line arrives as a list of tokens: `["price", "A-001", "3"]`. The dispatcher needs
to split that into a verb and its arguments. You *could* do it with `len(tokens)` checks and
indexing, but `match` has **sequence patterns** that match a list by its shape and pull the
pieces out in the same step.

## Matching by shape

```
match tokens:
    case []:
        ...                 # the empty list
    case [verb]:
        ...                 # exactly one element, bound to `verb`
    case [verb, *args]:
        ...                 # one or more: first to `verb`, the rest to `args`
```

- `[]` matches only an empty sequence.
- `[verb]` matches a sequence of **exactly one** element and binds it to `verb`. The length
  is part of the pattern — a two-element list will not match here.
- `[verb, *args]` uses a **star pattern**. It matches a sequence of one-or-more, binding the
  first element to `verb` and collecting *everything after* into a new list `args` (which may
  be empty). It is the sequence-pattern cousin of `*rest` in unpacking.

Order still matters: because `[verb]` is tested first, a single-element list is caught there,
so by the time `[verb, *args]` is reached it is effectively handling two-or-more. A pattern
binds names only when it matches, so inside each branch you can safely use the names that
branch introduced.

## Your task

In `dispatch.py`, finish `parse_tokens(tokens)` so it returns a `(Command, args)` pair. The
one-element case is written. Fill in:

1. the pattern for the **empty** token list, and
2. the **star pattern** `[verb, *args]` that captures a verb plus the remaining tokens.

## Worked example

```
>>> import dispatch
>>> dispatch.parse_tokens([])
(<Command.HELP: 'help'>, [])
>>> dispatch.parse_tokens(["report"])
(<Command.REPORT: 'report'>, [])
>>> dispatch.parse_tokens(["price", "A-001", "3"])
(<Command.PRICE: 'price'>, ['A-001', '3'])
```

## What the check verifies, and what it leaves to you

- Enforced: an empty list yields `HELP` with no args; a bare verb yields its command with an
  empty arg list; a verb followed by tokens captures those tokens **as a list**.
- Your free choice: you may collapse the bare-verb and verb-with-args cases into one
  `[verb, *args]` branch if you prefer (a single element gives `args == []`), as long as the
  returned pairs are correct.

<div class="hint" title="If you are stuck">

The empty case is `case []:`. The star pattern is `case [verb, *args]:` — the `*args`
collects everything after the first token into a list.

</div>

Reference: Python documentation, "Patterns with a literal and variable" and "The match
statement" (sequence patterns) at docs.python.org.
