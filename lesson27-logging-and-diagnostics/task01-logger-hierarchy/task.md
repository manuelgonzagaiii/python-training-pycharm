# Named Loggers, Levels & Propagation

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.1 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create one logger per module with getLogger(__name__) and understand the dotted-name tree
- Reason about effective level and how child loggers inherit configuration from parents
- Control whether records propagate to ancestor loggers and the root
- Pass lazy %-style arguments instead of pre-formatting log strings

## Python features introduced
`logging.getLogger(__name__)`, `logger name hierarchy (dotted names)`, `logging levels (DEBUG/INFO/WARNING/ERROR/CRITICAL)`, `Logger.setLevel and effective level`, `logger.propagate`, `root logger vs named loggers`, `logging.NullHandler for libraries`, `%-style log messages with lazy args (logger.info('x=%s', x))`

## MiniERP increment
Adds a `logging_setup.get_logger(name)` factory and gives every MiniERP service package a module logger named under the `minierp.` root (e.g. `minierp.products`, `minierp.sales`). Establishes the logger tree the whole suite logs through, with a NullHandler default so importing the library never spams output.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import logging

ROOT_NAME = "minierp"
logging.getLogger(ROOT_NAME).addHandler(logging.NullHandler())

def get_logger(name: str) -> logging.Logger:
    """Return a logger under the 'minierp.' namespace.
    get_logger('products') -> logger named 'minierp.products'.
    """
    # TODO: normalize to f"{ROOT_NAME}.{name}" unless already namespaced
    raise NotImplementedError
- **Test focus:** get_logger returns correctly named loggers under minierp.*; child loggers share the root; propagation and effective-level inheritance behave as expected (use caplog-style capture or a list handler).

</div>
