"""Binary Records: struct, array & memoryview

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import struct

REC = struct.Struct('<16s i q')  # sku, qty, price_cents

def pack_row(sku: str, qty: int, price_cents: int) -> bytes:
    return REC.pack(sku.encode().ljust(16, b'\x00'), qty, price_cents)

def unpack_all(blob: bytes):
    ...  # REC.iter_unpack(blob)

"""

# Your code here.
