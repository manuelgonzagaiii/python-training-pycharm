# CSV Dialects & Messy Real Data

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.2 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define and register a custom dialect for a partner's export format
- Auto-detect a dialect from a sample with csv.Sniffer
- Round-trip values that themselves contain commas, quotes and newlines
- Choose escaping vs quoting strategies

## Python features introduced
`csv.Dialect`, `csv.register_dialect`, `csv.Sniffer`, `csv.excel / excel_tab`, `escapechar / doublequote`, `skipinitialspace`, `handling embedded newlines and commas`

## MiniERP increment
Adds a 'partner' dialect to minierp.io.csv_io and import_products_csv(stream, dialect='sniff') so MiniERP can ingest customer/product feeds with semicolon delimiters or tab separation from external systems.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import csv

csv.register_dialect('partner', delimiter=';', quoting=csv.QUOTE_MINIMAL)

def detect_dialect(sample: str):
    return csv.Sniffer().sniff(sample)

def read_with_dialect(stream, dialect) -> list[dict]:
    ...

- **Test focus:** A semicolon file parses via the 'partner' dialect; Sniffer detects a comma vs tab sample; a field containing a delimiter and an embedded newline survives a write/read round-trip.

</div>
