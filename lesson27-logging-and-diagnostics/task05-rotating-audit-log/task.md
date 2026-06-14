# The Audit Log: RotatingFileHandler & Per-Operation Records

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Configure a size-based rotating file handler so the audit trail never grows unbounded
- Run a dedicated, non-propagating audit logger separate from diagnostic logging
- Emit structured (JSON) audit records capturing actor, action, entity, and operation id
- Decide what mutating operations deserve an audit record at INFO

## Python features introduced
`logging.handlers.RotatingFileHandler (maxBytes/backupCount)`, `logging.handlers.TimedRotatingFileHandler (overview)`, `dedicated audit logger with propagate=False`, `structured audit messages (actor, action, entity, op_id)`, `json.dumps for a machine-readable log line`, `logging at INFO for successful mutations`, `isolating audit handler from console handler`

## MiniERP increment
Adds an `audit(actor, action, entity, **fields)` function backed by a `minierp.audit` logger with a RotatingFileHandler (audit.log, capped + rotated) and propagate=False, emitting one JSON line per mutation. Services now call audit() on every create/update/delete — delivering the phase's audit-log capability with bounded, rotating storage.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import json, logging
from logging_setup import operation_id

_audit = logging.getLogger("minierp.audit")
_audit.propagate = False  # audit lines must not leak to the console handler

def audit(actor: str, action: str, entity: str, **fields) -> None:
    record = {"actor": actor, "action": action, "entity": entity,
              "op_id": operation_id.get(), **fields}
    # TODO: _audit.info(json.dumps(record))
    raise NotImplementedError
- **Test focus:** audit() emits a single parseable JSON line containing actor/action/entity/op_id; the audit logger does not propagate to the root/console; rotation config (maxBytes/backupCount) is set on its handler.

</div>
