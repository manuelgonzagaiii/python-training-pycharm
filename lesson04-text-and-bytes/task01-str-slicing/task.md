# String indexing and slicing

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.1 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Index strings with positive and negative positions
- Slice with start/stop/step including reversal and skipping
- Rely on slice bound-clamping instead of manual length checks

## Python features introduced
`str indexing s[i]`, `negative indexing s[-1]`, `slicing s[start:stop]`, `slice with step s[::2]`, `negative step / reverse s[::-1]`, `slice bounds clamping`, `len()`, `immutability of str`, `slice objects`

## MiniERP increment
Add SKU-field extractors to `task.py`: a SKU like 'AB-1234-XL' has fixed-position segments; `sku_prefix(sku)`, `sku_suffix(sku)`, and `reversed_code(sku)` use slicing to pull the category prefix, size suffix, and a reversed check code. First step of the identifier toolkit MiniERP uses everywhere.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def sku_prefix(sku: str, n: int = 2) -> str:
    """First n characters (category code)."""
    # TODO: slice
    raise NotImplementedError

def sku_suffix(sku: str, n: int = 2) -> str:
    """Last n characters (size code) via negative slicing."""
    # TODO: slice with negative start
    raise NotImplementedError

def reversed_code(sku: str) -> str:
    """The SKU reversed."""
    # TODO: s[::-1]
    raise NotImplementedError
- **Test focus:** Tests check prefix/suffix extraction for varied lengths, negative-index correctness, reversal via [::-1], and graceful behavior on short strings (slice clamping, no IndexError).

</div>
