"""MiniERP text utilities: identifiers, input cleaning, formatting, and bytes.

Pure helpers with no side effects, reused by every interface (CLI, web, GUI,
TUI). The lesson grows this module from basic string slicing up to encoding
records as bytes for storage and export.
"""


def sku_prefix(sku: str, n: int = 2) -> str:
    """The first n characters of a SKU -- its category code."""
    return sku[:n]


def sku_suffix(sku: str, n: int = 2) -> str:
    """The last n characters of a SKU -- its size code -- via negative slicing."""
    return sku[-n:]


def reversed_code(sku: str) -> str:
    """The SKU reversed, used as a simple check code."""
    return sku[::-1]


def clean_name(raw: str) -> str:
    """Trim, collapse internal whitespace, and title-case a name."""
    return " ".join(raw.split()).title()


def normalize_key(raw: str) -> str:
    """A casefolded, stripped key for case-insensitive lookups."""
    return raw.strip().casefold()


def parse_csv_line(line: str) -> list[str]:
    """Split a simple comma-delimited record, trimming each field."""
    parts = line.split(",")
    return [field.strip() for field in parts]
