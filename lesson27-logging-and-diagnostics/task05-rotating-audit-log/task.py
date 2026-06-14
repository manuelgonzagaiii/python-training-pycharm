"""The Audit Log: RotatingFileHandler & Per-Operation Records

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import json, logging
from logging_setup import operation_id

_audit = logging.getLogger("minierp.audit")
_audit.propagate = False  # audit lines must not leak to the console handler

def audit(actor: str, action: str, entity: str, **fields) -> None:
    record = {"actor": actor, "action": action, "entity": entity,
              "op_id": operation_id.get(), **fields}
    # TODO: _audit.info(json.dumps(record))
    raise NotImplementedError
"""

# Your code here.
