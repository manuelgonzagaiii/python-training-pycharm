# Writing a well-behaved decorator with wraps

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.5 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a parameter-forwarding decorator the right way
- Use @wraps to preserve the wrapped function's identity and docstring
- See what breaks (introspection, help text) when wraps is omitted
- Access the original via __wrapped__

## Python features introduced
`functools.wraps`, `writing a custom decorator`, `preserving __name__/__doc__/__wrapped__`, `*args/**kwargs forwarding`, `decorator that logs to the audit log`, `metadata loss without wraps`

## MiniERP increment
Add an @audited decorator to MiniERP's audit-log module that records each service call (name + args) to the audit log while using functools.wraps so the decorated service functions keep their names/docstrings for the CLI help and API docs.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from functools import wraps

def audited(func):
    @wraps(func)                     # preserves name, doc, __wrapped__
    def wrapper(*args, **kwargs):
        # TODO: append a record of (func.__name__, args, kwargs) to the audit log
        result = func(*args, **kwargs)
        return result
    return wrapper

- **Test focus:** Decorated function keeps __name__/__doc__ (thanks to wraps) and exposes __wrapped__; the call is recorded to the audit log once; arguments and return value pass through unchanged.

</div>
