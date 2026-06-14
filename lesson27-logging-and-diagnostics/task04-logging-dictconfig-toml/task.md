# Declarative Config: dictConfig from a TOML File

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Express the whole logging setup declaratively and load it from a TOML file with tomllib
- Map the dictConfig schema (formatters/filters/handlers/loggers/root) to the objects built by hand earlier
- Wire the custom OperationContextFilter into config by dotted class path
- Understand disable_existing_loggers and per-logger propagate in declarative form

## Python features introduced
`logging.config.dictConfig`, `tomllib.load (binary mode)`, `config schema: version, formatters, filters, handlers, loggers, root`, `referencing custom filter/handler classes by dotted path in config`, `disable_existing_loggers`, `propagate in config`, `pathlib for config path`, `merging file config with code defaults`

## MiniERP increment
Replaces imperative setup with `configure_from_toml('logging.toml')`: a checked-in TOML describing the console+file handlers, the timestamped formatter (now including [op=...]), and the OperationContextFilter, loaded via tomllib and applied with dictConfig. MiniERP's logging is now operator-configurable without code edits — the canonical setup all four interfaces invoke at startup.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import logging.config, tomllib
from pathlib import Path

def configure_from_toml(path: str | Path = "logging.toml") -> None:
    """Load a [logging] table from TOML and apply it via dictConfig."""
    with open(path, "rb") as fh:        # tomllib requires binary mode
        data = tomllib.load(fh)
    cfg = data["logging"]
    # TODO: logging.config.dictConfig(cfg)
    raise NotImplementedError
- **Test focus:** A sample TOML produces the expected loggers/handlers/levels after dictConfig; the custom filter is instantiated from its dotted path; missing file or malformed table raises a clear error.

</div>
