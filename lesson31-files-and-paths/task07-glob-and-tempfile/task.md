# Finding Files: glob, fnmatch & tempfile

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 31.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Locate files by wildcard pattern with Path.glob/rglob and the glob module
- Match and filter names with fnmatch independently of the filesystem
- Create temporary files and directories that auto-clean via context managers
- Use a TemporaryDirectory as a scratch area for safe multi-step operations

## Python features introduced
`glob.glob / iglob`, `Path.glob / rglob`, `fnmatch.fnmatch / filter`, `recursive ** patterns`, `tempfile.NamedTemporaryFile`, `tempfile.TemporaryDirectory`, `tempfile.mkstemp`, `context-managed temp cleanup`

## MiniERP increment
Adds minierp.storage.discovery.find_exports(layout, pattern) returning sorted export files matching e.g. '*.csv', and uses TemporaryDirectory in a stage_then_commit helper that builds output in temp space before moving it into exports/.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import fnmatch
from pathlib import Path

def find_files(root: Path, pattern: str) -> list[Path]:
    # return sorted matches using Path.rglob or glob
    ...

def matches(names: list[str], pattern: str) -> list[str]:
    return fnmatch.filter(names, pattern)

- **Test focus:** find_files locates nested files via ** patterns and returns them sorted; fnmatch.filter selects only matching names; a TemporaryDirectory-based helper cleans up after itself.

</div>
