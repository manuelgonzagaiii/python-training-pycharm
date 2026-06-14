"""UserDict & UserList: a validating catalog wrapper

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: # catalog.py (continued)
from collections import UserDict

class Catalog(UserDict):
    """A SKU-keyed catalog that validates products on insertion."""
    def __setitem__(self, sku: str, product: ProductRecord) -> None:
        # validate sku non-empty and price/qty non-negative, then store
        ...
"""

# Your code here.
