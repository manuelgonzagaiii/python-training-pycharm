# Sequence Patterns and the Token Parser

> **Phase:** Control Flow & Functions  •  **Stage:** 9.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Destructure an argv-style token list with sequence patterns
- Capture a variable-length tail using *rest
- Match on structure (arity) rather than writing manual length checks

## Python features introduced
`sequence patterns in match`, `fixed-length sequence patterns [a, b]`, `star pattern [head, *rest]`, `capturing the tail with *rest`, `len()-aware matching`, `list vs tuple in patterns`

## MiniERP increment
Add parse_tokens(tokens) to cli/dispatch.py that matches the token list: [] -> HELP request, [verb] -> bare command, [verb, *args] -> command with captured args. Returns a (Command, args) pair, giving the dispatcher its structured input from a CLI line.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def parse_tokens(tokens: list[str]) -> tuple[Command, list[str]]:
    """Destructure argv-style tokens with sequence patterns."""
    match tokens:
        case []:
            return (Command.HELP, [])
        case [verb]:
            ...
        case [verb, *args]:
            ...
- **Test focus:** Empty list yields a HELP request; single token yields verb with empty args; multi-token yields verb plus the exact captured tail list.

</div>
