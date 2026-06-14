# Logging Failures: exc_info, traceback & sys.exc_info

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Log a caught exception with its full traceback using logger.exception() and exc_info
- Retrieve the active exception triple with sys.exc_info() and format it with the traceback module
- Produce a human-readable crash report string from a TracebackException
- Combine the ERPError taxonomy with logging so each failure logs its code and root cause

## Python features introduced
`logger.exception() inside an except block`, `logger.error(..., exc_info=True)`, `sys.exc_info()`, `traceback.format_exc / format_exception / TracebackException`, `stack_info=True on logging calls`, `logging the ERPError code alongside the traceback`, `walrus in the except for capturing the instance`

## MiniERP increment
Adds a `report_failure(logger, exc)` crash-reporter used by the service layer's outermost handler: it logs the ERPError code at ERROR with exc_info, builds a readable diagnostic via traceback.TracebackException (walking __cause__ chains created in Lesson 1), and returns the formatted report for an interface to display. Any uncaught service failure now becomes a logged, legible diagnostic.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import logging, traceback
from errors import ERPError

def report_failure(logger: logging.Logger, exc: BaseException) -> str:
    code = exc.code if isinstance(exc, ERPError) else "unhandled"
    logger.error("operation failed [%s]", code, exc_info=exc)
    # TODO: build a readable report from traceback.TracebackException.from_exception(exc)
    #       (chain=True so __cause__/__context__ frames are included) and return it
    raise NotImplementedError
- **Test focus:** report_failure logs at ERROR with the exception's traceback; the returned string contains the chained cause and the ERPError code; non-ERP exceptions log as 'unhandled' without crashing the reporter.

</div>
