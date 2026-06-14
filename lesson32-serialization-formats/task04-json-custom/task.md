# Custom JSON: JSONEncoder & object_hook

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.4 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Teach json how to serialize non-native types (Decimal price, datetime, StrEnum) via a custom default()
- Round-trip those types back using an object_hook that reads a _type tag
- Understand why a tagged-dict convention is needed for lossless JSON
- Plug a custom encoder into dumps with cls=

## Python features introduced
`json.JSONEncoder subclass`, `default() method`, `object_hook`, `cls= argument to dumps`, `encoding Decimal/datetime/Enum/dataclass`, `_type tag pattern for round-tripping`, `json.loads(object_hook=...)`

## MiniERP increment
Upgrades json_io to ERPEncoder/erp_object_hook so Product/Customer dataclasses (with Decimal prices and datetime timestamps) serialize losslessly to exports/snapshot.json - the JSON format becomes authoritative for import/export.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import json
from decimal import Decimal
from datetime import datetime

class ERPEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return {'_type': 'Decimal', 'value': str(o)}
        ...  # datetime, dataclasses
        return super().default(o)

def erp_object_hook(d: dict):
    ...  # rebuild based on d.get('_type')

- **Test focus:** Decimal and datetime survive dumps(cls=ERPEncoder) -> loads(object_hook=erp_object_hook) unchanged; unknown types still raise TypeError; a full Product round-trips losslessly.

</div>
