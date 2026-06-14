# ExceptionGroup & except*: Aggregating Batch Failures

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Collect per-item failures across a batch and raise them together in one ExceptionGroup
- Use except* to handle different leaf exception types from the same group independently
- Split or subgroup an ExceptionGroup to separate, e.g., validation failures from not-found failures
- Understand how except* can run multiple handler blocks for one raised group

## Python features introduced
`ExceptionGroup / BaseExceptionGroup (PEP 654)`, `raising an ExceptionGroup with a message and list of excs`, `except* selective handling by leaf type`, `ExceptionGroup.split() / .subgroup()`, `.exceptions attribute traversal`, `nested exception groups`, `collecting exceptions in a loop then raising once`

## MiniERP increment
Adds `import_products(rows)` to the import/export module: it validates every row, accumulates ValidationError/ConflictError per bad row, imports the good ones, and if any failed raises an `ExceptionGroup("import failed", errors)`. A caller demo uses except* to report validation vs conflict problems separately — the first MiniERP feature that no longer aborts a bulk import on the first bad record.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from errors import ValidationError, ConflictError

def import_products(rows: list[dict]) -> list[dict]:
    """Validate+collect every row. Import the good ones.
    If any failed, raise ExceptionGroup('import failed', errors).
    """
    imported: list[dict] = []
    errors: list[Exception] = []
    for row in rows:
        # TODO: try validate -> append to imported; except ERPError -> errors.append(e)
        ...
    if errors:
        raise ExceptionGroup("import failed", errors)
    return imported
- **Test focus:** Mixed good/bad batch imports all valid rows and raises one ExceptionGroup; except* separates ValidationError leaves from ConflictError leaves; an all-good batch raises nothing.

</div>
