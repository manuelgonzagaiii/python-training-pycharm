"""@overload, cast, assert_type & reveal_type

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import overload, cast, assert_type

class Repository[T]:
    @overload
    def get(self, key: str) -> T | None: ...
    @overload
    def get[D](self, key: str, default: D) -> T | D: ...
    def get(self, key, default=None):  # single impl backs both
        ...  # TODO

# raw: dict[str, object] from json.load
# dto = cast(InvoiceDTO, raw)        # assert the shape to the checker
# assert_type(repo.get('x'), 'Product | None')  # verify inference
"""

# Your code here.
