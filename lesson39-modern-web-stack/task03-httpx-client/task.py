"""Calling the API with httpx (sync & async)

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import httpx

class ERPClient:
    def __init__(self, base_url: str, token: str | None = None):
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(base_url=base_url, headers=headers, timeout=5.0)

    def list_products(self) -> list[dict]:
        # TODO: GET /products, raise_for_status, return .json()
        raise NotImplementedError

    def create_product(self, name: str, price: float) -> dict:
        # TODO: POST /products with json=...
        raise NotImplementedError

    def close(self):
        self._client.close()
"""

# Your code here.
