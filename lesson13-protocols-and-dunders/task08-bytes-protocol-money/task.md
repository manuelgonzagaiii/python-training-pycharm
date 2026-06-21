# Stage 8: byte serialization with __bytes__

To store money in a binary file, append it to an audit log, or send it over a socket, you need
a **byte representation** — and one that survives a round trip exactly, with no float drift and
no locale ambiguity. This stage gives `Money` a fixed-width binary encoding via the `__bytes__`
dunder and the `struct` module, plus a `from_bytes` classmethod to read it back.

## bytes(obj) and __bytes__

`bytes(money)` calls `money.__bytes__()`, which must return a `bytes` object. The goal is a
**fixed-layout** record so any reader knows exactly how to parse it. `struct.pack` builds such
a record from a format string:

```
import struct

    def __bytes__(self):
        return struct.pack("!B3sq", 1, self.currency.encode("ascii"), self.cents)
```

Read the format `"!B3sq"` left to right:

- `!` — **network byte order** (big-endian), the portable choice so a record written on one
  machine reads the same on another.
- `B` — one **unsigned byte**, here a version tag (`1`). Tagging the version means the format
  can evolve later without misreading old records.
- `3s` — a **3-byte** string, the ASCII currency code (`b"USD"`).
- `q` — a **signed 8-byte** integer, the cents. Signed so a negative amount (a credit) encodes
  too; 8 bytes so it never overflows.

That is `1 + 3 + 8 = 12` bytes, every time. The integer-cents representation is what makes this
clean: a fixed-width integer packs exactly, where a float never could.

## Reading it back

`from_bytes` is the inverse — `struct.unpack` with the *same* format returns the fields, which
rebuild the `Money`:

```
    @classmethod
    def from_bytes(cls, data):
        version, currency, cents = struct.unpack("!B3sq", data)
        return cls(cents, currency.decode("ascii"))
```

The contract that matters is the **round-trip invariant**: `Money.from_bytes(bytes(m)) == m`
for every `m`. The test suite enforces it, which is what makes this encoding safe to persist
and reload. (`int.to_bytes`/`int.from_bytes` is the stdlib way to encode a single integer;
`struct` is the right tool here because a record has *several* fixed-width fields.)

## Your task

In `domain.py`, finish the two `struct` calls on `Money`:

1. `__bytes__` — pack the version `1`, the encoded currency, and the cents with the `"!B3sq"`
   layout.
2. `from_bytes` — unpack the same layout from `data`.

## Worked example

```
>>> import domain
>>> m = domain.Money(1599, "USD")
>>> data = bytes(m)
>>> len(data)                        # fixed 12-byte record
12
>>> domain.Money.from_bytes(data) == m
True
>>> domain.Money.from_bytes(bytes(domain.Money(-2500, "EUR"))).cents   # negative survives
-2500
```

## What the check verifies, and what it leaves to you

- Enforced: `bytes(money)` is exactly 12 bytes; `from_bytes(bytes(m))` reconstructs an
  equal `Money` (the round-trip invariant), including negative amounts and non-USD currencies.
- Your free choice: the precise field order is fixed only because both ends must agree; within
  that, the encoding is the point. The check insists on the round trip, because a serialization
  that doesn't read back what it wrote is simply broken.

<div class="hint" title="If you are stuck">

Pack: `struct.pack("!B3sq", 1, self.currency.encode("ascii"), self.cents)`. Unpack:
`struct.unpack("!B3sq", data)` returns `(version, currency, cents)`; decode the currency bytes
back to a string.

</div>

Reference: Python documentation, "struct — Interpret bytes as packed binary data" and "Data
model — object.__bytes__" at docs.python.org.
