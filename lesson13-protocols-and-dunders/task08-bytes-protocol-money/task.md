# Byte Serialization with __bytes__

> **Phase:** OOP Foundations  •  **Stage:** 13.8 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain that bytes(obj) calls obj.__bytes__() and must return a real bytes object, contrasting it with __repr__/__str__/__format__ which all return str.
- Implement __bytes__ on the existing Money value object to emit a compact, fixed-width binary record using struct.pack with an explicit byte order.
- Choose and read a struct format string deliberately: network byte order, a signed 8-byte integer for minor-unit amounts, and a fixed-width currency field.
- Provide a Money.from_bytes classmethod that reverses __bytes__ with struct.unpack, establishing the round-trip invariant Money.from_bytes(bytes(m)) == m.
- Distinguish bytes (immutable), bytearray (mutable), and memoryview (zero-copy view), and know when bytes(int) builds a zero-filled buffer instead of calling __bytes__.
- Recognize that returning anything other than bytes from __bytes__ makes bytes(obj) raise TypeError.

## Python features introduced
`__bytes__ dunder method`, `bytes(obj) protocol / bytes constructor dispatch`, `struct.pack / struct.unpack for fixed binary layout`, `struct format strings (network byte order '!', signed long long 'q', unsigned 'B')`, `classmethod alternate constructor (from_bytes)`, `@classmethod decorator`, `int.from_bytes / int.to_bytes (big-endian, signed) as a stdlib contrast`, `bytes vs bytearray vs memoryview (immutability and views)`, `len(bytes) and indexing/slicing of bytes objects`, `enum/StrEnum member encoded as a fixed-width byte`, `.encode('utf-8') / bytes.decode('utf-8') for the currency code`, `round-trip invariant (obj == from_bytes(bytes(obj)))`, `TypeError raised by bytes(obj) when __bytes__ returns a non-bytes value`

## MiniERP increment
Adds a stable on-the-wire binary encoding to the MiniERP core domain. The Money value object (built in the earlier money-value-object stage, an immutable kw_only slotted dataclass storing an integer minor-unit amount plus a 3-letter ISO currency code) gains a __bytes__ method that packs each value into a fixed 12-byte record via struct: a 1-byte version tag, a 3-byte ASCII currency code, and a signed 8-byte big-endian minor-unit amount, all in network byte order. A Money.from_bytes(data) classmethod unpacks that record back into an equal Money, giving the domain layer a deterministic, length-prefixable serialization that downstream phases reuse for the append-only audit log, binary import/export files, and length-framed records sent over sockets. Because the encoding is fixed-width and version-tagged, MiniERP can persist and re-read monetary amounts without floating-point drift or locale ambiguity, and the round-trip invariant becomes a guarantee the test suite enforces.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Reuse the Money value object from the money-value-object stage (frozen, slots=True, kw_only=True dataclass with fields `amount: int` for minor units and `currency: str` for the ISO code). Add `import struct` and the constant `_FORMAT = "!B3sq"` (network order: version byte, 3-byte currency, signed 8-byte amount) and `_VERSION = 1`. Implement `def __bytes__(self) -> bytes:` returning `struct.pack(_FORMAT, _VERSION, self.currency.encode("ascii"), self.amount)`. Add `@classmethod` `def from_bytes(cls, data: bytes) -> "Money":` that calls `struct.unpack(_FORMAT, data)`, validates the version byte equals `_VERSION` (raise ValueError otherwise), decodes the currency with `.decode("ascii").rstrip("\\x00")`, and returns `cls(amount=amount, currency=currency)`. Leave the existing __repr__/__str__/__format__ from the prior stage untouched.
- **Test focus:** Verify bytes(Money(amount=12345, currency="USD")) returns a bytes object of length exactly 12 (struct.calcsize("!B3sq")), that its first byte is the version tag 1, and that bytes 1..4 decode to b"USD". Assert the round-trip invariant Money.from_bytes(bytes(m)) == m across several amounts including negative (e.g. -500 for a refund) and zero. Confirm from_bytes raises ValueError on a record whose version byte is not 1, and that supplying a wrong-length buffer raises struct.error. Include a check that bytes(m) is an instance of bytes (not bytearray) so a __bytes__ returning the wrong type would fail. Optionally assert the encoding is deterministic (two equal Money objects produce identical bytes).

</div>
