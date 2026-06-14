"""Serving HTML and decoding form posts

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import html, mimetypes
from pathlib import Path
from urllib.parse import parse_qs

STATIC = Path(__file__).parent / "static"

def render_products(products) -> str:
    """Return an HTML table of products with every field html.escape-d."""
    rows = "".join(
        f"<tr><td>{html.escape(p.name)}</td><td>{p.price}</td></tr>"
        for p in products
    )
    # TODO: wrap rows in a full <html> document
    raise NotImplementedError

def parse_form(body: bytes) -> dict[str, str]:
    """Decode an urlencoded form body into a flat dict (first value per key)."""
    # TODO: parse_qs then take [0] of each list
    raise NotImplementedError
"""

# Your code here.
