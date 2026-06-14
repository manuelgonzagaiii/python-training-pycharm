# OR Patterns and Guards

> **Phase:** Control Flow & Functions  •  **Stage:** 9.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Collapse equivalent cases with the | OR pattern
- Refine a case with an if-guard evaluated after the pattern binds
- Order cases so the most specific guarded case wins

## Python features introduced
`OR patterns (pattern1 | pattern2)`, `guards (case ... if condition)`, `combining capture with guard`, `ordering of cases matters`, `binding constraints in OR patterns`

## MiniERP increment
Add route_command(cmd, args) to cli/dispatch.py: an alias OR pattern (Command.HELP | Command.REPORT) shares a read-only handler, while a guard (case Command.PRICE if args) requires arguments before pricing and otherwise emits a usage error — encoding real dispatch rules.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def route_command(cmd: Command, args: list[str]) -> str:
    """Route with OR patterns and guards."""
    match cmd:
        case Command.HELP | Command.REPORT:
            return "read-only"
        case Command.PRICE if args:
            ...
        case Command.PRICE:
            return "usage: price <sku> <qty>"
        case _:
            ...
- **Test focus:** HELP and REPORT share the read-only branch; PRICE with args routes to pricing; PRICE without args hits the usage guard; unknown verbs fall through.

</div>
