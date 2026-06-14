"""ExceptionGroup & except*: Aggregating Batch Failures

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from errors import ValidationError, ConflictError

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
"""

# Your code here.
