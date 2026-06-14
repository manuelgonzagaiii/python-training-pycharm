# Filesystem Ops: os, os.path & shutil

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 31.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Inspect file metadata (size, mtime) via os.stat and os.path helpers
- Perform atomic writes using a temp file plus os.replace
- Copy, move and recursively delete trees with shutil
- Understand the os.PathLike protocol bridging str and Path

## Python features introduced
`os.stat / st_size / st_mtime`, `os.replace (atomic rename)`, `os.remove / os.rename`, `os.path.getsize/getmtime/splitext`, `shutil.copy2 / copytree / move`, `shutil.rmtree`, `shutil.disk_usage`, `os.fspath / PathLike`

## MiniERP increment
Adds minierp/storage/atomic.py: write_text_atomic(path, text) writes to path.tmp then os.replace()s it into place - the durability primitive used by config saving and exports so a crash never leaves a half-written file.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import os
from pathlib import Path

def write_text_atomic(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + '.tmp')
    # write tmp fully, then os.replace(tmp, path)
    ...

def file_size(path: Path) -> int:
    ...  # via os.stat

- **Test focus:** write_text_atomic leaves no .tmp behind and the target has full content; replacing an existing file works atomically; file_size matches len of bytes written.

</div>
