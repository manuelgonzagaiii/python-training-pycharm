"""A Single Root: the ERPError Base Class

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from enum import StrEnum

class ErrorCode(StrEnum):
    UNKNOWN = "unknown"
    VALIDATION = "validation"
    NOT_FOUND = "not_found"
    CONFLICT = "conflict"
    PERMISSION = "permission"
    INTEGRITY = "integrity"

class ERPError(Exception):
    """Root of every MiniERP domain exception."""
    code: ErrorCode = ErrorCode.UNKNOWN

    def __init__(self, message: str, *, context: dict | None = None) -> None:
        # TODO: store message + context, call super().__init__(message)
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO: render like "[validation] message (context...)"
        raise NotImplementedError
"""

# Your code here.
