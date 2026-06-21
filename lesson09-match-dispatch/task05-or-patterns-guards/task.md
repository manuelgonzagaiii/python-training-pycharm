# Stage 5: OR patterns and guards

Two more pattern tools turn the matcher into a real router: combining patterns with `|`, and
attaching a runtime condition to a case with a guard.

## OR patterns

When several cases should run the **same** body, an OR pattern joins them with `|`:

```
case Command.HELP | Command.REPORT:
    return "read-only command"
```

This matches if the subject matches *either* alternative — no need to duplicate the body. If
the alternatives capture names, every alternative must bind the **same** names (so the body
can rely on them); here the members bind nothing, so there is no constraint.

## Guards

A pattern describes *shape*. Sometimes you also need a *condition* the shape cannot express —
"a price command, but only if it actually has arguments". That is a **guard**: an `if` after
the pattern.

```
case Command.PRICE if args:
    return f"pricing {len(args)} item(s)"
case Command.PRICE:
    return "usage: price <sku> [qty]"
```

The case matches only when the pattern matches **and** the guard is true. This is where case
**order** becomes a correctness issue, not just style: the guarded `Command.PRICE if args`
must come before the bare `Command.PRICE`. Reverse them and the bare case — which matches
every PRICE — would win first, and the guarded one would never run.

## Your task

In `dispatch.py`, finish `route_command(cmd, args)`. The bare-PRICE, ADD/DISCOUNT, and
fallback cases are written. Fill in:

1. the **OR pattern** that lets `HELP` and `REPORT` share one read-only handler, and
2. the **guarded** `PRICE` case that fires only when `args` is non-empty.

## Worked example

```
>>> import dispatch
>>> C = dispatch.Command
>>> dispatch.route_command(C.HELP, []) == dispatch.route_command(C.REPORT, [])
True
>>> dispatch.route_command(C.PRICE, ["A-001", "2"])
'pricing 2 item(s)'
>>> dispatch.route_command(C.PRICE, [])
'usage: price <sku> [qty]'
```

## What the check verifies, and what it leaves to you

- Enforced: `HELP` and `REPORT` produce the same handler result; `PRICE` with arguments
  routes to pricing; `PRICE` without arguments produces a different, usage-style result.
- Your free choice: the exact handler strings are yours; the check compares behaviour (same
  vs different, and that the with-args and without-args results differ), not literal text.

<div class="hint" title="If you are stuck">

The OR pattern is `case Command.HELP | Command.REPORT:`. The guard is `case Command.PRICE if
args:` — and it must sit above the bare `case Command.PRICE:`.

</div>

Reference: Python documentation, "The match statement" (OR patterns and guards) at
docs.python.org.
