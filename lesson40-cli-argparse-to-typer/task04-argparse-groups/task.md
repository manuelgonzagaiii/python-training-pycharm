# argparse: argument groups & mutual exclusion

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 40.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Organise related options into titled argument groups for readable --help
- Enforce 'exactly one of' with a mutually-exclusive group (e.g. --csv vs --json vs --table output)
- Share common options (e.g. --db-path, --verbose) across subcommands using parents=
- Call parser.error() for cross-argument validation argparse can't express alone

## Python features introduced
`add_argument_group`, `add_mutually_exclusive_group(required=)`, `parser.error()`, `argument titles & descriptions in help`, `epilog`, `parents= parser inheritance`

## MiniERP increment
Add a `report` subcommand with a mutually-exclusive output-format group (--table/--csv/--json) and a shared 'global options' parent parser (--db-path, --verbose) reused by every subcommand. Reports render from the core analytics service in the chosen format.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a common_parser (parent) with --db-path/--verbose and a report subparser missing its mutually-exclusive format group; learner adds the group and the format-dispatch in the handler.
- **Test focus:** Assert passing two formats triggers SystemExit; assert the parent options appear on multiple subcommands; assert the chosen format selects the right renderer over a fixed report payload.

</div>
