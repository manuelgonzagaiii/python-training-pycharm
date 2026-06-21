# Stage 6: nested patterns and the full dispatcher

This stage assembles everything into `dispatch()` — MiniERP's single command entry point.
One `match` accepts every shape a request can arrive in (a CLI token list, a JSON-style dict,
or an already-built request object) and returns a typed request object the pricing layer can
later execute.

## Patterns nest

The power of structural matching is that patterns compose: a subpattern can itself be any
pattern. So a sequence pattern can contain literals and captures, and a mapping pattern can
have a sequence pattern as one of its values:

```
match request:
    case ["add", sku, qty]:
        return AddRequest(sku, int(qty))
    case {"op": "discount", "rules": [*rules]}:
        return DiscountRequest(rules)
    case PriceRequest() | AddRequest() | DiscountRequest():
        return request          # already typed -- pass it straight through
```

- `["add", sku, qty]` is a three-element sequence whose **first element is the literal**
  `"add"` and whose other two are captures — match the shape and pull out the fields at once.
- `{"op": "discount", "rules": [*rules]}` is a mapping pattern whose `"rules"` value is itself
  a **sequence pattern**, capturing the rule list. Structure inside structure.
- A class pattern with empty parentheses, `PriceRequest()`, is a pure type check; joined with
  `|` it lets any already-built request pass through untouched.

This is the design goal of the whole lesson: one declarative `match` that reads like a table
of the shapes MiniERP accepts, instead of a tangle of `if`/`isinstance`/index checks.

## Your task

In `dispatch.py`, finish `dispatch(request)`. The price-list, passthrough, and fallback cases
are written. Fill in:

1. the nested **sequence pattern** `["add", sku, qty]`, and
2. the nested **mapping-with-sequence** pattern `{"op": "discount", "rules": [*rules]}`.

## Worked example

```
>>> import dispatch
>>> dispatch.dispatch(["add", "A-001", "3"])
AddRequest(sku='A-001', qty=3)
>>> dispatch.dispatch({"op": "discount", "rules": [10, 5]})
DiscountRequest(rules=[10, 5])
>>> r = dispatch.PriceRequest("A-001", 1)
>>> dispatch.dispatch(r) is r          # already typed -> passed through
True
>>> dispatch.dispatch(["bogus"])
<Command.HELP: 'help'>
```

## What the check verifies, and what it leaves to you

- Enforced: an `["add", sku, qty]` list becomes an `AddRequest` (qty converted to int); a
  discount mapping becomes a `DiscountRequest` carrying the rules; an existing request object
  passes through unchanged; anything unrecognized returns `Command.HELP`.
- Your free choice: you may add more accepted shapes or order the cases differently, as long
  as the shapes above produce these typed results.

<div class="hint" title="If you are stuck">

The add pattern is `case ["add", sku, qty]:`. The discount pattern nests a list pattern
inside a mapping: `case {"op": "discount", "rules": [*rules]}:`.

</div>

Reference: Python documentation, "The match statement" (nested patterns) at docs.python.org.
