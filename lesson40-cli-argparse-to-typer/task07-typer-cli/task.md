# Re-skin with Typer (Click under the hood)

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 40.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Rebuild the same commands with Typer so type hints generate the parser automatically
- Map argparse concepts onto Typer: Option/Argument, defaults, Enums for choices, callbacks for env
- Appreciate what Typer (and the Click it wraps) buys you vs hand-rolled argparse
- Keep the exact same core-service calls — only the front-end changes

## Python features introduced
`typer.Typer()`, `typer command decorators`, `typer.Argument/Option`, `type hints -> CLI params`, `Enum params`, `typer.Context`, `Click foundation (relationship)`, `rich help output`

## MiniERP increment
Add an alternative Typer-based entry point exposing the identical command surface (products/customers/sales/report) over the same service layer, proving the core is UI-agnostic. Both CLIs coexist.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a Typer app with `products_add` partially defined using typer.Option; learner completes it and the report command with an output-format Enum, reusing the config resolver.
- **Test focus:** Use typer.testing.CliRunner to invoke commands and assert exit_code==0, that the recording service received correctly-typed args, and that an Enum format option is enforced.

</div>
