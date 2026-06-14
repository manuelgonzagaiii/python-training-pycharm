# Build and parse canonical SKUs

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.7 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compose a canonical identifier from parts using format specs and joins
- Parse an identifier back into validated components
- Validate identifier shape and raise clear errors on bad input

## Python features introduced
`f-string format-spec for zero-padding {n:0>4} / {n:04d}`, `str.upper/str.strip for normalization`, `str.split('-') and unpacking`, `str.zfill`, `str.isalnum validation`, `slicing for fixed segments`, `join with separators`, `ValueError for invalid input`

## MiniERP increment
Capstone identifier task: add `make_sku(category, number, size)` and `parse_sku(sku)` to `task.py`, producing/reading the canonical 'CAT-0042-XL' format (zero-padded number, upper-cased segments). This is the single SKU format the entire MiniERP (inventory, sales, reporting) standardizes on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def make_sku(category: str, number: int, size: str) -> str:
    """Build 'CAT-0042-XL': upper category, 4-digit zero-padded number, upper size."""
    # TODO: f"{category.upper()}-{number:04d}-{size.upper()}"
    raise NotImplementedError

def parse_sku(sku: str) -> tuple[str, int, str]:
    """Split into (category, number, size); raise ValueError if malformed."""
    # TODO: split('-'), validate, int(number)
    raise NotImplementedError
- **Test focus:** Tests verify round-trip make_sku/parse_sku, zero-padding (number 42 -> '0042'), upper-casing, and that malformed SKUs (wrong segment count, non-numeric middle) raise ValueError.

</div>
