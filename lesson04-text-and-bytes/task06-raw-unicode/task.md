# Raw strings, escapes, and Unicode

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.6 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish raw strings from escaped strings and know when each is correct
- Insert Unicode by code point and by name (\N{...})
- Normalize Unicode text (NFC/NFKC) so equal-looking strings compare equal

## Python features introduced
`raw strings r'...'`, `escape sequences \n \t \\ \" `, `unicode escapes \uXXXX \N{NAME}`, `ord() and chr()`, `unicodedata.normalize (NFC/NFKC)`, `str.encode preview`, `len of multi-codepoint strings`, `combining characters vs precomposed`, `\xNN hex escapes`

## MiniERP increment
Add `task.py` text-normalization for MiniERP search/dedup: `normalize_unicode(s)` applies NFKC so 'café' (combining) and 'café' (precomposed) match, and `currency_symbol(code)` returns the right symbol via \N{...}. Ensures customer/product names dedupe correctly regardless of input source.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import unicodedata

EURO = "\N{EURO SIGN}"

def normalize_unicode(s: str) -> str:
    """Return NFKC-normalized text for reliable comparison."""
    # TODO: unicodedata.normalize("NFKC", s)
    raise NotImplementedError

def code_points(s: str) -> list[int]:
    """Return the ord() of each character."""
    # TODO: [ord(c) for c in s]
    raise NotImplementedError
- **Test focus:** Tests assert that a combining-sequence string and its precomposed form become equal after normalize_unicode, that \N{EURO SIGN} equals '€', and that code_points/ord/chr round-trip.

</div>
