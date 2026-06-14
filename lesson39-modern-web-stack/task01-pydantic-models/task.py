"""Validated payloads with pydantic

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from pydantic import BaseModel, Field, field_validator

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
"""

# Your code here.
