# open(): Modes, Encodings & Buffering

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 31.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Choose the right mode (write vs append vs exclusive-create) and know when 'x' raises
- Always specify encoding='utf-8' for text files and understand errors= policies
- Control newline translation with newline=''
- Read and write text files through a with-block so handles always close

## Python features introduced
`open()`, `modes r/w/a/x/r+/b/t`, `encoding= and errors=`, `newline= argument`, `with-statement context manager`, `file.read/readline/readlines/write`, `buffering= argument`, `FileExistsError on 'x'`

## MiniERP increment
Adds minierp/storage/textfiles.py with write_text_atomic-precursor helpers: save_note(path, text) and load_note(path) used later for human-readable export headers and README stamps in exports/.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from pathlib import Path

def save_note(path: Path, text: str) -> int:
    # write text as UTF-8, return number of characters written
    ...

def load_note(path: Path) -> str:
    # read it back as UTF-8
    ...

def create_exclusive(path: Path, text: str) -> bool:
    # use mode 'x'; return False if file already exists
    ...

- **Test focus:** Round-trip text via UTF-8; create_exclusive returns True first time and False (catching FileExistsError) the second; verify content with non-ASCII chars survives.

</div>
