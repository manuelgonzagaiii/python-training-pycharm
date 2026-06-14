"""The same REST API in FastAPI

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from fastapi import FastAPI, HTTPException, Depends
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
"""

# Your code here.
