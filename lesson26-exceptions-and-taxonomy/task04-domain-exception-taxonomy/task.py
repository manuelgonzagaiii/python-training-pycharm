"""Branching the Taxonomy: Validation, NotFound, Conflict, Permission

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from errors import ERPError, ErrorCode

class ValidationError(ERPError):
    code = ErrorCode.VALIDATION
    def __init__(self, message: str, *, field: str | None = None, **kw) -> None:
        # TODO: keep `field`, pass message+context up
        raise NotImplementedError

class NotFoundError(ERPError):
    code = ErrorCode.NOT_FOUND
    def __init__(self, entity: str, key: object, **kw) -> None:
        # TODO: build message like f"{entity} {key!r} not found"; store entity/key
        raise NotImplementedError

# TODO: ConflictError (CONFLICT), PermissionError (PERMISSION), IntegrityError (INTEGRITY)
"""

# Your code here.
