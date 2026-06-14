# Capturing Deprecation Warnings with catch_warnings

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.8 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that warnings.catch_warnings() snapshots the global warnings filter state on entry and *restores it on exit*, so any simplefilter/filterwarnings changes you make inside the block are temporary
- Use catch_warnings(record=True) together with simplefilter("always") to capture emitted warnings into a list instead of printing them, then inspect each WarningMessage (its .category and .message)
- Distinguish capturing/recording warnings from merely suppressing them, and know why the catch_warnings block must wrap simplefilter to avoid leaking filter changes to the rest of the program
- Know that the global __warningregistry__ can hide an already-shown warning, and that simplefilter("always") inside the block forces every warning through so audits are reliable
- Call warnings.resetwarnings() to clear all configured filters back to a known baseline, and understand when that is appropriate (test setup / a global 'show everything' diagnostic mode) versus dangerous
- Build a small reusable @contextmanager that suppresses a given warning category for a noisy bulk operation and guarantees the previous filter state returns even on error

## Python features introduced
`warnings.catch_warnings (context manager)`, `catch_warnings(record=True) to record into a list`, `warnings.simplefilter("always") / simplefilter("ignore")`, `warnings.resetwarnings()`, `warnings.warn with DeprecationWarning / PendingDeprecationWarning categories`, `stacklevel argument to warnings.warn`, `WarningMessage attributes (.message, .category, .filename, .lineno)`, `reading w[-1].category / str(w[-1].message)`, `parenthesized context managers (with (a, b):)`, `@contextlib.contextmanager for a reusable suppress-and-restore helper`, `try/finally restoration semantics already seen in earlier tasks`

## MiniERP increment
Adds a deprecation-policy audit to MiniERP's Import/Export and pricing code. Several legacy helpers are now deprecated: the v1 CSV row parser, a flat-discount pricing helper, and an old customer-tier label. These call warnings.warn(..., DeprecationWarning, stacklevel=2) (PendingDeprecationWarning for the not-yet-removed one). You implement `audit_import(rows)` which runs a batch import inside a `with warnings.catch_warnings(record=True) as caught:` block (after `warnings.simplefilter("always")`) and returns an ImportAudit dataclass: the successfully parsed records plus a list of DeprecationNotice entries (category name, message text, and source line) gathered from the recorded WarningMessage objects — without leaking any filter changes to the rest of the running ERP. You also implement `quiet_bulk_load(category)`, a @contextmanager built on catch_warnings that suppresses one warning category during a large trusted bulk load and then restores the prior filters, and `reset_warning_filters()` which calls warnings.resetwarnings() so the CLI's `--show-all-warnings` diagnostic flag starts from a clean, fully-visible baseline. This lets operators see every deprecated code path exercised during a real import run, on the foundation the earlier p10 tasks built (warnings.warn, categories, simplefilter/filterwarnings, captureWarnings).

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** In task.py, MiniERP already exposes legacy helpers that emit warnings, e.g.:

    import warnings
    from dataclasses import dataclass, field

    def parse_row_v1(row: list[str]) -> dict:
        warnings.warn(
            "parse_row_v1 is deprecated; use parse_row_v2",
            DeprecationWarning, stacklevel=2,
        )
        return {"sku": row[0], "name": row[1], "qty": int(row[2])}

    @dataclass(slots=True)
    class DeprecationNotice:
        category: str
        message: str
        lineno: int

    @dataclass(slots=True)
    class ImportAudit:
        records: list[dict] = field(default_factory=list)
        notices: list[DeprecationNotice] = field(default_factory=list)

Learners implement:
    def audit_import(rows: list[list[str]]) -> ImportAudit: ...        # uses `with warnings.catch_warnings(record=True) as caught:` + simplefilter("always")
    @contextmanager
    def quiet_bulk_load(category: type[Warning]): ...                  # catch_warnings + simplefilter("ignore", category), restores on exit
    def reset_warning_filters() -> None: ...                          # warnings.resetwarnings()

Key hint: changes made via simplefilter INSIDE a catch_warnings block are undone on exit, so audit_import must not affect warnings seen elsewhere.
- **Test focus:** Verify: (1) audit_import returns the right parsed records and a notices list whose entries have category == 'DeprecationWarning' (and the pending one as 'PendingDeprecationWarning'), with message text matching the emitted warnings; (2) after audit_import runs, the GLOBAL warnings filter state is unchanged — assert by emitting a warning afterward inside the test's own catch_warnings and confirming default behavior, proving the inner simplefilter("always") did not leak; (3) inside quiet_bulk_load(DeprecationWarning) the chosen category is suppressed (record list stays empty), and immediately after the with-block the prior filters are restored; (4) reset_warning_filters() empties warnings.filters then a subsequently warned DeprecationWarning is visible again under simplefilter('default'). Tests use warnings.catch_warnings(record=True) themselves (mirroring pytest.warns) and never rely on stderr text. Also assert ImportAudit/DeprecationNotice are dataclasses with slots.

</div>
