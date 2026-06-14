# Branching the Taxonomy: Validation, NotFound, Conflict, Permission

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a shallow, intentional exception tree under ERPError instead of reusing generic built-ins
- Give each subclass the extra structured fields its category needs (which entity, which field, which conflicting key)
- Let callers catch broadly (except ERPError) or narrowly (except NotFoundError) from the same hierarchy
- Map each domain failure mode in MiniERP to exactly one exception class

## Python features introduced
`multi-level exception inheritance`, `overriding class attributes per subclass`, `narrowing except by subclass`, `isinstance checks across a hierarchy`, `exception subclass with extra fields (e.g. entity, field)`, `PEP 604 unions in signatures`, `keyword-only constructor args`

## MiniERP increment
Extends `errors.py` with `ValidationError`, `NotFoundError`, `ConflictError`, `PermissionError` (ERP-scoped, not the builtin), and `IntegrityError`, each setting its ErrorCode and carrying relevant fields (entity id, field name, conflicting value). These become the vocabulary every service uses to signal failure.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from errors import ERPError, ErrorCode

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
- **Test focus:** Each subclass is catchable as ERPError, exposes its own code, and carries its category-specific fields; narrow excepts select the right subclass without catching siblings.

</div>
