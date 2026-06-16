"""MiniERP text utilities: identifiers, input cleaning, formatting, and bytes.

Pure helpers with no side effects, reused by every interface (CLI, web, GUI,
TUI). The lesson grows this module from basic string slicing up to encoding
records as bytes for storage and export.
"""
import unicodedata
from decimal import Decimal
from string import Template


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


def debug_line(sku: str, qty: int, price: Decimal) -> str:
    """A self-documenting debug string, e.g. sku='AB-1' qty=3 price=Decimal('9.99')."""
    return f"{sku=} {qty=} {price=}"


def receipt_line(name: str, total: Decimal) -> str:
    """A human receipt line, e.g. 'Widget: $9.99'."""
    return f"{name}: ${total}"


def fmt_money(amount: Decimal) -> str:
    """Format a money amount as $1,234.50 using the format-spec mini-language."""
    return f"${amount:,.2f}"


def fmt_col(value: str, width: int, align: str = "<") -> str:
    """Pad and align `value` to a fixed column width. align is '<', '>', or '^'."""
    return f"{value:{align}{width}}"


def render_invoice_header(data: dict) -> str:
    """Fill an invoice header from a record dict, by named field."""
    template = "Invoice {invoice_no} for {customer}"
    return template.format_map(data)


def render_email(template: str, **values: str) -> str:
    """Fill a $-placeholder template, leaving any unknown $placeholder untouched."""
    return Template(template).safe_substitute(values)


def normalize_unicode(s: str) -> str:
    """NFKC-normalize text so strings that look the same compare and hash the same."""
    return unicodedata.normalize("NFKC", s)


def code_points(s: str) -> list[int]:
    """The Unicode code point (the ord) of each character."""
    return [ord(ch) for ch in s]


def currency_symbol(code: str) -> str:
    """The symbol for an ISO currency code, using named Unicode escapes."""
    symbols = {
        "USD": "$",
        "EUR": "\N{EURO SIGN}",
        "GBP": "\N{POUND SIGN}",
        "JPY": "\N{YEN SIGN}",
    }
    return symbols[code]


def make_sku(category: str, number: int, size: str) -> str:
    """Build a canonical SKU 'CAT-0042-XL': upper category, 4-digit number, upper size."""
    return f"{category.upper()}-{number:04d}-{size.upper()}"


def parse_sku(sku: str) -> tuple[str, int, str]:
    """Parse 'CAT-0042-XL' into (category, number, size); raise ValueError if malformed."""
    parts = sku.split("-")
    if len(parts) != 3:
        raise ValueError(f"malformed SKU (need 3 dash-separated parts): {sku!r}")
    category, number, size = parts
    if not number.isdigit():
        raise ValueError(f"SKU number is not numeric: {sku!r}")
    return category.upper(), int(number), size.upper()
