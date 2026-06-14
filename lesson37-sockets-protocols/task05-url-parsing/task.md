# Parsing and building URLs with urllib.parse

> **Phase:** Networking & the Web  •  **Stage:** 37.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Decompose a URL into scheme/host/path/query/fragment
- Parse and build query strings, handling repeated keys and percent-encoding
- Resolve relative URLs against a base with urljoin
- Treat URL handling as parsing, not string slicing

## Python features introduced
`urllib.parse.urlparse`, `urlsplit`, `parse_qs / parse_qsl`, `urlencode`, `quote / unquote`, `urljoin`, `urlunparse`, `ParseResult namedtuple`

## MiniERP increment
Adds erp/net/urls.py: URL helpers the API client and (later) the router reuse — building paginated endpoint URLs like /products?page=2&q=widget and parsing inbound request targets into a normalized (path, query-dict) pair.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from urllib.parse import urlparse, parse_qs, urlencode, urljoin

def build_query(path: str, **params) -> str:
    """Return path + '?' + url-encoded params (skip None values)."""
    # TODO: filter Nones, urlencode (doseq=True for list values)
    raise NotImplementedError

def split_target(target: str) -> tuple[str, dict[str, list[str]]]:
    """Split an HTTP request target into (path, query_dict)."""
    # TODO: urlparse then parse_qs the .query
    raise NotImplementedError
- **Test focus:** Round-trip build_query then split_target and assert params survive; check repeated keys (q=a&q=b) parse to a list and that a value with spaces/&/= is correctly percent-encoded and decoded.

</div>
