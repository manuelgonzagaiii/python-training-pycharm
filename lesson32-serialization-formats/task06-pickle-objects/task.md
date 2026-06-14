# pickle: Protocols & Object State

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.6 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Serialize live Python objects (not just plain data) with pickle and restore them
- Customize what gets pickled via __getstate__/__setstate__ (e.g. drop a cached/derived field)
- Understand __reduce__ as the low-level pickle protocol
- Internalize the security rule: pickle executes code, so only load trusted files

## Python features introduced
`pickle.dumps / loads`, `pickle.dump / load`, `pickle protocols (HIGHEST_PROTOCOL)`, `__getstate__ / __setstate__`, `__reduce__`, `pickling dataclasses`, `security warning (never unpickle untrusted data)`, `picklable vs unpicklable objects`

## MiniERP increment
Adds minierp/io/snapshot.py: save_state(obj, path) / load_state(path) giving MiniERP a fast native-object snapshot of the full in-memory repository, with a CatalogState class using __getstate__ to exclude a transient index that is rebuilt in __setstate__.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import pickle
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

- **Test focus:** CatalogState pickles without _index and rebuilds it on unpickle; round-trip via dump/load preserves products and a working _index; HIGHEST_PROTOCOL is used.

</div>
