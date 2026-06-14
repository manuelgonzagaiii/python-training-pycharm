# Calling the API with httpx (sync & async)

> **Phase:** Networking & the Web  •  **Stage:** 39.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Make sync and async HTTP calls with httpx
- Use a client as a context manager with base_url and shared headers
- Handle responses (json(), status, raise_for_status) and timeouts
- Test a FastAPI app in-process via ASGITransport without binding a port

## Python features introduced
`httpx.Client / httpx.AsyncClient`, `context manager usage`, `client.get/post with json=`, `response.json() / raise_for_status`, `base_url and headers`, `async with + await`, `timeouts`, `ASGITransport to test the app in-process`

## MiniERP increment
Adds erp/web/client.py: a typed MiniERP API client used by other interfaces (the CLI and TUI from earlier phases) to talk to the running API instead of importing services directly — establishing a clean network boundary between front-ends and the core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import httpx

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
- **Test focus:** Wire ERPClient against the FastAPI app via httpx ASGITransport; assert list_products/create_product round-trip, raise_for_status raises on a 404, and an async variant using AsyncClient awaits correctly.

</div>
