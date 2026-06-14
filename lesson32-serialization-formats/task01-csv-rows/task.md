# CSV I/O: reader, writer & DictWriter

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.1 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write domain records to CSV with DictWriter and a header row
- Read them back with DictReader yielding dicts keyed by column
- Understand why CSV files must be opened with newline=''
- Control quoting and delimiters for spreadsheet compatibility

## Python features introduced
`csv.reader / csv.writer`, `csv.DictReader / csv.DictWriter`, `writeheader / writerows`, `newline='' requirement`, `quoting constants (QUOTE_MINIMAL/NONNUMERIC)`, `delimiter handling`, `iterating rows`

## MiniERP increment
Adds minierp/io/csv_io.py: export_products_csv(products, stream) and import_products_csv(stream) -> list[Product], the first concrete import/export feature, wired so the CLI can dump products to exports/products.csv.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import csv
from minierp.domain import Product  # already exists

FIELDS = ['sku', 'name', 'price', 'quantity']

def export_products_csv(products, stream) -> None:
    writer = csv.DictWriter(stream, fieldnames=FIELDS)
    ...  # writeheader + writerows

def import_products_csv(stream) -> list:
    ...  # DictReader -> [Product(...), ...]

- **Test focus:** Export then import round-trips a list of Products through a StringIO; header is present; price/quantity are converted back to the right numeric types; newline handling verified.

</div>
