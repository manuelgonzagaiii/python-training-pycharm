"""Parsing and building URLs with urllib.parse

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from urllib.parse import urlparse, parse_qs, urlencode, urljoin

def build_query(path: str, **params) -> str:
    """Return path + '?' + url-encoded params (skip None values)."""
    # TODO: filter Nones, urlencode (doseq=True for list values)
    raise NotImplementedError

def split_target(target: str) -> tuple[str, dict[str, list[str]]]:
    """Split an HTTP request target into (path, query_dict)."""
    # TODO: urlparse then parse_qs the .query
    raise NotImplementedError
"""

# Your code here.
