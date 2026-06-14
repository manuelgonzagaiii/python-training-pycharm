"""__new__ vs __init__: Who Builds the Object

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: class Product:
    _by_sku: dict[str, "Product"] = {}

    def __new__(cls, sku: str, name: str, price_cents: int) -> "Product":
        ...  # if sku in cls._by_sku: return cached; else create via super().__new__(cls)

    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        ...  # set fields; cache self in cls._by_sku
"""

# Your code here.
