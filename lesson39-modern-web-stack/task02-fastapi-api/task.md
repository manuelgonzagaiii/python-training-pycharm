# The same REST API in FastAPI

> **Phase:** Networking & the Web  •  **Stage:** 39.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define routed endpoints with typed path/query parameters
- Bind pydantic models as request bodies and response_model
- Inject the existing service layer with Depends
- Raise HTTPException for error cases and get OpenAPI docs for free

## Python features introduced
`FastAPI app`, `path operation decorators (@app.get/@app.post)`, `path & query parameters with type hints`, `response_model`, `Depends for injecting the service layer`, `HTTPException and status codes`, `async def endpoints over the async core`, `automatic OpenAPI`

## MiniERP increment
Adds erp/web/app.py: the MiniERP REST API rebuilt in FastAPI with the exact same routes as the stdlib api.py (GET/POST /products, /customers, plus POST /sales to create an invoice), now async over the existing async services with automatic validation and /docs.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from fastapi import FastAPI, HTTPException, Depends
from .schemas import ProductIn, ProductOut

app = FastAPI(title="MiniERP")

def get_products_service():
    # TODO: provide the existing product service (Depends target)
    raise NotImplementedError

@app.get("/products", response_model=list[ProductOut])
async def list_products(svc=Depends(get_products_service)):
    # TODO: return await svc.list()
    raise NotImplementedError

@app.post("/products", response_model=ProductOut, status_code=201)
async def create_product(body: ProductIn, svc=Depends(get_products_service)):
    # TODO: create via service; raise HTTPException(409) on duplicate sku
    raise NotImplementedError
- **Test focus:** Use FastAPI's TestClient (httpx-backed) to GET /products (200 list), POST a valid product (201, matches response_model), POST an invalid one (422 from validation), and GET an unknown product id (404).

</div>
