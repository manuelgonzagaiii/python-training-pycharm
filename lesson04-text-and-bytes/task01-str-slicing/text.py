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
