# The string method toolbox

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.2 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Clean and normalize raw user input with strip/casefold and friends
- Search, test, split, and join strings without regular expressions
- Use removeprefix/removesuffix and translate for precise edits

## Python features introduced
`str.strip/lstrip/rstrip`, `str.lower/upper/casefold/title/capitalize/swapcase`, `str.startswith/endswith`, `str.find/rfind/index/count`, `str.replace`, `str.split/rsplit/splitlines/partition/rpartition`, `str.join`, `str.zfill/center/ljust/rjust`, `str.isdigit/isalpha/isalnum/isspace/isidentifier`, `str.removeprefix/removesuffix`, `str.translate/str.maketrans`, `str.expandtabs`

## MiniERP increment
Add MiniERP input-cleaning helpers to `task.py`: `clean_name(raw)` strips, collapses, and title-cases a customer/product name; `normalize_key(raw)` casefolds and strips for case-insensitive lookups; `parse_csv_line(line)` splits a simple delimited record. These are reused by import and search throughout the ERP.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def clean_name(raw: str) -> str:
    """Trim, collapse internal whitespace, title-case."""
    # TODO: strip + split + join + title
    raise NotImplementedError

def normalize_key(raw: str) -> str:
    """Casefolded, stripped key for case-insensitive lookup."""
    # TODO: strip + casefold
    raise NotImplementedError

def parse_csv_line(line: str, sep: str = ",") -> list[str]:
    """Split a delimited line into trimmed fields."""
    # TODO: split + strip each field
    raise NotImplementedError
- **Test focus:** Tests cover whitespace collapsing, casefold of mixed-case and non-ASCII (e.g. Straße), trimmed field splitting, and isdigit/removeprefix edge cases on messy input.

</div>
