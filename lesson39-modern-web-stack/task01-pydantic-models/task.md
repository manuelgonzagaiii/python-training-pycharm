# Validated payloads with pydantic

> **Phase:** Networking & the Web  •  **Stage:** 39.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define typed models with validation constraints
- Validate untrusted dict input and catch ValidationError
- Convert between models and dicts/ORM-like objects (model_dump / from_attributes)
- Add custom validators and computed fields

## Python features introduced
`pydantic.BaseModel`, `type-annotated fields`, `Field with constraints (gt, max_length)`, `field_validator`, `model_validate / model_dump`, `ValidationError`, `computed_field`, `PEP 604 optional fields`, `model_config (from_attributes)`

## MiniERP increment
Adds erp/web/schemas.py: pydantic request/response models (ProductIn, ProductOut, CustomerIn, InvoiceOut) that sit at the API boundary and validate input before it ever reaches the existing domain services, replacing hand-rolled dict checks.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from pydantic import BaseModel, Field, field_validator

class ProductIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    sku: str | None = None

    @field_validator("sku")
    @classmethod
    def upper_sku(cls, v):
        # TODO: normalize sku to uppercase if present
        raise NotImplementedError

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    model_config = {"from_attributes": True}
- **Test focus:** Assert ProductIn rejects price<=0 and empty name with ValidationError, normalizes sku to uppercase, and that ProductOut.model_validate works from a domain product object via from_attributes.

</div>
