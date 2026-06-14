# suppress, closing, redirect_stdout, nullcontext

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 21.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Replace a try/except-pass with suppress(SomeError)
- Use closing() to guarantee .close() on an object lacking the manager protocol
- Capture a report's printed output with redirect_stdout(StringIO()) and use nullcontext to make the manager optional

## Python features introduced
`contextlib.suppress`, `contextlib.closing`, `contextlib.redirect_stdout / redirect_stderr`, `contextlib.nullcontext`, `io.StringIO as a capture target`, `conditional context via nullcontext fallback`

## MiniERP increment
Builds a render_report(...) helper that optionally captures printed output (redirect_stdout to a buffer for the Web API, nullcontext for the CLI which prints directly), uses suppress around best-effort cache cleanup, and closing() on a file-like export handle.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import io
from contextlib import suppress, closing, redirect_stdout, nullcontext

def render_report(report, *, capture: bool) -> str | None:
    buf = io.StringIO()
    target = redirect_stdout(buf) if capture else nullcontext()
    with target:
        report.print_to_stdout()
    # TODO: return buf.getvalue() if capture else None
    ...
    # Also: with suppress(FileNotFoundError): os.remove(stale_cache)
- **Test focus:** Captured mode returns the printed text; non-captured mode returns None and prints normally; suppress swallows only the named exception.

</div>
