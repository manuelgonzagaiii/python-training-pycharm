# Configuration from os.environ

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 40.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Read configuration (DB path, default output format, page size) from environment variables
- Implement a clear precedence: explicit CLI flag overrides env var overrides hard-coded default
- Safely coerce env strings to bool/int/Path
- Keep config resolution in one place the whole app can reuse

## Python features introduced
`os.environ`, `os.environ.get with defaults`, `os.getenv`, `precedence (flag > env > built-in default)`, `pathlib.Path for paths`, `bool/int parsing from strings`, `argparse default= from env`

## MiniERP increment
Add a config resolver so `MINIERP_DB`, `MINIERP_FORMAT`, and `MINIERP_PAGE_SIZE` set defaults for every command, overridable per-invocation by flags. The CLI and (later) other front-ends share this resolver.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide resolve_config(env, args) -> Config dataclass with the precedence half-implemented; learner completes coercion and precedence and wires defaults into the parsers.
- **Test focus:** With a fake env dict, assert env supplies defaults, a flag overrides env, and bad MINIERP_PAGE_SIZE raises a clear error; assert a Path is returned for the DB.

</div>
