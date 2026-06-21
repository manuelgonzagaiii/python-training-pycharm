# Stage 1: literal and capture patterns

This lesson builds MiniERP's command dispatcher — the front door that turns a raw command
into something the rest of the system can act on. It is built entirely on **structural
pattern matching**, the `match`/`case` statement (Python 3.10+). All the code lives in one
new module, `dispatch.py`, which every stage extends.

`match`/`case` is not a C-style switch. A `switch` compares one value against constants; a
`match` compares a value against **patterns** that describe shape and can pull pieces out
as they match. This first stage uses its two simplest patterns.

## Literal patterns and the wildcard

A `match` takes a subject value and tries each `case` top to bottom, running the first that
matches:

```
match token:
    case "add":
        return Command.ADD
    case "price":
        return Command.PRICE
    case _:
        return Command.HELP
```

- A **literal pattern** (`case "add":`) matches when the subject equals that literal. This
  is the part that looks like a switch.
- The **wildcard** `_` matches anything and binds nothing. As the last case it is the
  catch-all — the default. (There is also a **capture pattern**, a bare name like
  `case other:`, which matches anything *and binds* the value to that name; use it when you
  want to keep what you matched, and `_` when you do not.)

Because the first matching case wins and `_` matches everything, putting `_` anywhere but
last would shadow the cases below it.

## StrEnum for the verbs

The set of commands is fixed, so it belongs in an **enum** — a type whose instances are a
fixed set of named constants. `Command` is a `StrEnum` (Python 3.11+), which means each
member *is* a string: `Command.ADD == "add"` is true, and it prints as `add`. That makes it
perfect for a CLI, where commands arrive and leave as text, while your code still gets the
safety and autocompletion of named members.

## Your task

In `dispatch.py`, finish `normalize_verb(token)`. The `Command` enum and most cases are
written. Fill in:

1. the **literal pattern** for the `price` verb, and
2. the **wildcard** catch-all that sends every unrecognized token to `Command.HELP`.

## Worked example

```
>>> import dispatch
>>> dispatch.normalize_verb("add")
<Command.ADD: 'add'>
>>> dispatch.normalize_verb("report")
<Command.REPORT: 'report'>
>>> dispatch.normalize_verb("nonsense")
<Command.HELP: 'help'>
```

## What the check verifies, and what it leaves to you

- Enforced: each known verb maps to its `Command`; any unknown token (including the empty
  string) maps to `Command.HELP`; `Command` members compare equal to their string values.
- Your free choice: the catch-all may be the wildcard `_` or a capture pattern (`case
  other:`) — both pass, since the bound name is unused either way.

<div class="hint" title="If you are stuck">

The price case is `case "price":`. The catch-all is `case _:`.

</div>

Reference: Python documentation, "match Statements" (tutorial) and "The match statement"
(language reference), plus "enum.StrEnum", at docs.python.org.
