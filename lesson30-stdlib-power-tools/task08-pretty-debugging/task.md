# Readable output with pprint and reprlib

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.8 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Pretty-print nested ERP structures with pprint (width, depth, sort_dicts)
- Produce bounded, non-flooding reprs of large collections with reprlib
- Decide between pprint for humans and reprlib for log lines
- Format diagnostics that stay readable as data grows

## Python features introduced
`pprint.pprint / pprint.pformat`, `pprint width/sort_dicts/depth options`, `reprlib.repr (truncated repr)`, `reprlib.Repr customization (maxlist, maxstring)`, `custom __repr__ vs reprlib`, `diagnostic output formatting`

## MiniERP increment
Finish the phase with diagnostics polish: dump_state() pretty-prints a snapshot of the in-memory MiniERP (products, customers, recent audit) with pprint.pformat, and short_repr() yields truncated reprlib reprs for log lines so big catalogs do not flood the audit log. MiniERP's debug/admin output is now tidy and bounded.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/debug.py with dump_state(store) using pprint.pformat and short_repr(obj) using reprlib; learner sets width/depth and reprlib limits to match the documented shape.
- **Test focus:** dump_state returns a pformat string with sorted keys and the configured width; short_repr truncates long lists/strings within the configured maxlist/maxstring limits.

</div>
