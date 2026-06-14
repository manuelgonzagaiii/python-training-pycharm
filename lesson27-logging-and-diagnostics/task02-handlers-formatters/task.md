# Handlers & Formatters: Where Logs Go and How They Look

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Route the same log records to a console stream and a file with different per-handler levels
- Build a Formatter that renders timestamp, level, logger name, and message consistently
- Understand the LogRecord fields available to a format string
- Set a verbose level on the file handler and a terse level on the console

## Python features introduced
`logging.StreamHandler`, `logging.FileHandler`, `logging.Formatter with format/datefmt`, `Handler.setLevel (per-handler thresholds)`, `attaching multiple handlers to one logger`, `LogRecord attributes (levelname, name, asctime, message, funcName, lineno)`, `logging.Formatter style='{' vs '%'`, `exc_info / stack_info formatting hooks`

## MiniERP increment
Adds `configure_basic_logging()` to the logging subsystem: a StreamHandler at INFO for the console and a FileHandler at DEBUG writing `minierp.log`, both attached to the `minierp` root with a shared timestamped Formatter. MiniERP now has a real, dual-sink audit trail any interface can rely on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import logging
from pathlib import Path

FMT = "{asctime} {levelname:<8} {name}: {message}"

def configure_basic_logging(log_path: str | Path = "minierp.log") -> logging.Logger:
    root = logging.getLogger("minierp")
    root.setLevel(logging.DEBUG)
    # TODO: StreamHandler@INFO + FileHandler@DEBUG, both with Formatter(FMT, style='{')
    #       avoid adding duplicate handlers on repeat calls
    raise NotImplementedError
- **Test focus:** Console handler is INFO-level, file handler DEBUG-level; a DEBUG record reaches the file but not the console; formatted output contains level, logger name, and message; repeat calls don't duplicate handlers.

</div>
