# Catalog Search with for/else

> **Phase:** Control Flow & Functions  •  **Stage:** 8.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use the rare for/else to express 'searched everything and found nothing'
- Understand that else runs only when the loop completes without break
- Combine continue to skip non-matching items

## Python features introduced
`for-else clause`, `break`, `continue`, `else-runs-when-no-break semantics`, `linear search idiom`

## MiniERP increment
Add find_in_catalog(catalog, sku) to inventory.py that linearly scans the in-memory catalog (built in earlier phases), continues past mismatches, breaks on a hit returning the product, and uses the for/else to raise KeyError('unknown sku') when the loop exhausts without breaking.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def find_in_catalog(catalog: list[dict], sku: str) -> dict:
    """Linear search; for/else raises KeyError when sku is absent."""
    for product in catalog:
        if product["sku"] != sku:
            continue
        ...
    else:
        ...
- **Test focus:** Returns the matching product dict; raises KeyError for an absent sku (proves the else branch fired); skips earlier non-matches via continue.

</div>
