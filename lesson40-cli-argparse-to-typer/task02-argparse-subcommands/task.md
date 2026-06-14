# argparse: subcommands for ERP modules

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 40.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a top-level parser and attach per-module subparsers (products, customers, sales, report)
- Use set_defaults(func=handler) so each subcommand dispatches to its own function
- Translate a parsed Namespace into a single call against the core service layer
- Return process exit codes from handlers

## Python features introduced
`argparse.ArgumentParser`, `add_subparsers(dest=, required=)`, `set_defaults(func=)`, `parser.parse_args`, `Namespace`, `command dispatch pattern`

## MiniERP increment
Implement the command dispatcher so `products list` and `customers list` work end-to-end: argparse parses the subcommand, the handler calls the existing service (list_products / list_customers), and results are printed. The CLI now genuinely drives the core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide build_parser() returning a configured ArgumentParser with subparsers; learner adds the `products` and `customers` subparsers and their handlers that call the core services.
- **Test focus:** Parse argv lists like ['products','list'] and assert the right handler runs and calls the right service (inject a fake/recording service); assert dispatch on an unknown command errors.

</div>
