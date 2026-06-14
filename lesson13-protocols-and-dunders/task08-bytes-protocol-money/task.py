"""Byte Serialization with __bytes__

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: Reuse the Money value object from the money-value-object stage (frozen, slots=True, kw_only=True dataclass with fields `amount: int` for minor units and `currency: str` for the ISO code). Add `import struct` and the constant `_FORMAT = "!B3sq"` (network order: version byte, 3-byte currency, signed 8-byte amount) and `_VERSION = 1`. Implement `def __bytes__(self) -> bytes:` returning `struct.pack(_FORMAT, _VERSION, self.currency.encode("ascii"), self.amount)`. Add `@classmethod` `def from_bytes(cls, data: bytes) -> "Money":` that calls `struct.unpack(_FORMAT, data)`, validates the version byte equals `_VERSION` (raise ValueError otherwise), decodes the currency with `.decode("ascii").rstrip("\\x00")`, and returns `cls(amount=amount, currency=currency)`. Leave the existing __repr__/__str__/__format__ from the prior stage untouched.
"""

# Your code here.
