"""suppress, closing, redirect_stdout, nullcontext

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import io
from contextlib import suppress, closing, redirect_stdout, nullcontext

def render_report(report, *, capture: bool) -> str | None:
    buf = io.StringIO()
    target = redirect_stdout(buf) if capture else nullcontext()
    with target:
        report.print_to_stdout()
    # TODO: return buf.getvalue() if capture else None
    ...
    # Also: with suppress(FileNotFoundError): os.remove(stale_cache)
"""

# Your code here.
