# Fetching with urllib.request and http.client

> **Phase:** Networking & the Web  •  **Stage:** 37.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Issue GET/POST requests with urllib.request and read status, headers, and body
- Add custom headers (Accept, Authorization) via Request
- Catch HTTPError vs URLError and inspect the error response
- Use the lower-level http.client.HTTPConnection and see what urllib wraps

## Python features introduced
`urllib.request.urlopen`, `urllib.request.Request`, `adding headers`, `urllib.error.HTTPError / URLError`, `reading response, status, getheader`, `http.client.HTTPConnection`, `json.loads on a response body`, `with for the response object`

## MiniERP increment
Adds erp/net/pricefeed.py: an outbound HTTP client that fetches an external JSON price feed and updates product list prices through the existing product service. Built two ways (urllib and http.client) so learners see the layering; errors are surfaced as the project's own domain exception.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import json, urllib.request, urllib.error

def fetch_json(url: str, headers: dict[str, str] | None = None) -> dict:
    """GET url, parse JSON body, raise PriceFeedError on HTTP/URL errors."""
    req = urllib.request.Request(url, headers=headers or {})
    # TODO: urlopen as context manager, read+decode, json.loads
    # TODO: except urllib.error.HTTPError / URLError -> raise PriceFeedError
    raise NotImplementedError

class PriceFeedError(Exception):
    ...
- **Test focus:** Point fetch_json at a local ThreadingHTTPServer fixture returning JSON and assert the dict parses; start a server that returns 404/500 and assert PriceFeedError is raised; assert a custom Accept header reaches the server.

</div>
