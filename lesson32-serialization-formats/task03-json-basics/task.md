# JSON: dumps, loads & the Type Mapping

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.3 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Serialize nested dicts/lists to a pretty-printed JSON string and back
- Map Python types to JSON types and know what is NOT representable (sets, tuples become lists, datetimes)
- Control output with indent, sort_keys, ensure_ascii and separators
- Read/write JSON files via json.dump/load

## Python features introduced
`json.dumps / json.loads`, `json.dump / json.load`, `indent / sort_keys`, `ensure_ascii`, `separators`, `Python<->JSON type table`, `parse_float / parse_int hooks`, `handling None/bool`

## MiniERP increment
Adds minierp/io/json_io.py: dump_snapshot(data, stream) / load_snapshot(stream) producing exports/snapshot.json - a full plain-data dump of products and customers used for human-readable backups.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import json

def dump_snapshot(data: dict, stream) -> None:
    json.dump(data, stream, indent=2, sort_keys=True)

def load_snapshot(stream) -> dict:
    return json.load(stream)

- **Test focus:** Nested data round-trips; indent and sort_keys produce stable output; non-ASCII names survive with ensure_ascii=False; loading restores equal data.

</div>
