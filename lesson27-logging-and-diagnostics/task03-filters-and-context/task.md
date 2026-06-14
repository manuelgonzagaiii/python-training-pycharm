# Filters & Correlation Context (request/operation ids)

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a logging.Filter that attaches a correlation id to every record
- Carry an ambient operation id through call stacks with contextvars instead of threading it manually
- Use a LoggerAdapter or extra= to add per-call context fields
- Reference injected fields from the Formatter so every line is traceable to one operation

## Python features introduced
`logging.Filter subclass with filter()`, `injecting attributes onto LogRecord via a Filter`, `logging.LoggerAdapter for contextual logging`, `contextvars.ContextVar for ambient request/operation id`, `Formatter referencing custom record fields (e.g. {op_id})`, `filter attached to handler vs logger`, `extra= dict on logging calls`

## MiniERP increment
Adds an `OperationContextFilter` plus an `operation_id` ContextVar and wires the formatter to print `[op=...]`, so every log line emitted while handling a CLI command / HTTP request / GUI action is tagged with the same correlation id. This is the backbone for tracing a single MiniERP operation across services in the audit log.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import logging
from contextvars import ContextVar

operation_id: ContextVar[str] = ContextVar("operation_id", default="-")

class OperationContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        # TODO: record.op_id = operation_id.get(); return True (filters never drop here)
        raise NotImplementedError
- **Test focus:** Filter sets record.op_id from the ContextVar; records emitted under a set operation_id carry that id; the default '-' applies when unset; filter returns True so nothing is dropped.

</div>
