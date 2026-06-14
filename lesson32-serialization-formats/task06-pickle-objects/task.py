"""pickle: Protocols & Object State

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import pickle
from pathlib import Path

class CatalogState:
    def __init__(self, products):
        self.products = products
        self._index = {p.sku: p for p in products}  # transient

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_index']
        return state

    def __setstate__(self, state):
        ...  # restore + rebuild _index

"""

# Your code here.
