# A Single Root: the ERPError Base Class

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Design a project-wide base exception that carries structured data (code, message, context dict) beyond a plain string
- Override __init__ and __str__ so the exception both reads well to humans and exposes machine-readable fields
- Understand why one shared root exception lets callers catch all domain errors with a single except
- Attach a stable, enumerated error code to each exception for logging and API responses

## Python features introduced
`custom exception subclass of Exception`, `__init__ calling super().__init__()`, `instance attributes on exceptions`, `__slots__ on an exception (note interaction with __dict__/args)`, `default/overridable error message`, `__str__ override`, `class-level attributes for error code`, `StrEnum for an error-code enum (reused from earlier phase)`

## MiniERP increment
Creates the cornerstone `errors.py` module for MiniERP with `class ERPError(Exception)` carrying a StrEnum `code`, a human `message`, and a `context: dict` payload. This base is what every service and every later interface (CLI/Web/GUI/TUI) will catch and serialize.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from enum import StrEnum

class ErrorCode(StrEnum):
    UNKNOWN = "unknown"
    VALIDATION = "validation"
    NOT_FOUND = "not_found"
    CONFLICT = "conflict"
    PERMISSION = "permission"
    INTEGRITY = "integrity"

class ERPError(Exception):
    """Root of every MiniERP domain exception."""
    code: ErrorCode = ErrorCode.UNKNOWN

    def __init__(self, message: str, *, context: dict | None = None) -> None:
        # TODO: store message + context, call super().__init__(message)
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO: render like "[validation] message (context...)"
        raise NotImplementedError
- **Test focus:** Check ERPError is an Exception subclass, stores message/context, exposes a code, and __str__ embeds the code; subclasses can override the class-level code.

</div>
