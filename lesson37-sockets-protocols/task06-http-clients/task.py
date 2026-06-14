"""Fetching with urllib.request and http.client

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import json, urllib.request, urllib.error

def fetch_json(url: str, headers: dict[str, str] | None = None) -> dict:
    """GET url, parse JSON body, raise PriceFeedError on HTTP/URL errors."""
    req = urllib.request.Request(url, headers=headers or {})
    # TODO: urlopen as context manager, read+decode, json.loads
    # TODO: except urllib.error.HTTPError / URLError -> raise PriceFeedError
    raise NotImplementedError

class PriceFeedError(Exception):
    ...
"""

# Your code here.
