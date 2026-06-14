"""Capturing Deprecation Warnings with catch_warnings

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: In task.py, MiniERP already exposes legacy helpers that emit warnings, e.g.:

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
"""

# Your code here.
