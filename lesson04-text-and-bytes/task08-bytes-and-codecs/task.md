# Stage 8: bytes, codecs, and base64

Everything so far has been `str` — Python's in-memory text. But a file on disk, a network
packet, a database blob: those are **bytes**, raw 8-bit values with no inherent meaning.
The boundary between the two is where data is saved and sent, and crossing it correctly is
how MiniERP avoids the classic "mojibake" bug where `café` arrives as `cafÃ©`. This stage
adds MiniERP's serialization primitives and completes `text.py`.

## str vs bytes, and the codec between them

- A `str` is a sequence of Unicode **code points** (characters).
- A `bytes` is a sequence of **integers 0–255**. Its literal is `b"..."`.

To go from text to bytes you **encode**; to go back you **decode**. Both need a
**codec** — and you should always name it explicitly:

```
>>> "café".encode("utf-8")
b'caf\xc3\xa9'
>>> b'caf\xc3\xa9'.decode("utf-8")
'café'
```

**UTF-8** is the right default everywhere: it encodes all of Unicode and is the web's
standard. Notice the length changed — `"café"` is 4 characters but **5 bytes**, because `é`
takes two bytes in UTF-8. That is why you never measure storage in `len(str)`; once it is
bytes, count bytes.

Encoding can fail when a character does not fit the target codec. The `errors=` argument
decides what happens — `"strict"` (the default) raises, `"replace"` inserts `?`, `"ignore"`
drops it. You will build a custom handler for this in the last stage; for now, knowing UTF-8
encodes everything is enough.

## base64: bytes that survive a text-only channel

Some channels (an email body, a JSON string, a URL) only carry text. **base64** re-encodes
arbitrary bytes into a safe ASCII alphabet so they pass through unharmed, at the cost of
~33% more size. It is *not* encryption — just a transport-safe representation.

```
>>> import base64
>>> token = base64.b64encode("café".encode("utf-8"))   # bytes -> base64 bytes
>>> token
b'Y2Fmw6k='
>>> token.decode("ascii")                               # -> an ASCII str to send
'Y2Fmw6k='
```

The round trip is encode-to-UTF-8 → base64-encode → decode-the-base64-to-ASCII-text, and
exactly the reverse coming back.

## Your task

Fill in the four blanks in `text.py`:

1. `encode_record(s)` — UTF-8 encode to `bytes`.
2. `decode_record(data)` — UTF-8 decode back to `str`.
3. `to_b64(s)` — base64-encode the UTF-8 bytes (the `.decode("ascii")` to a string is
   given).
4. `from_b64(s)` — base64-decode back to bytes (the UTF-8 decode is given).

## Worked example

```
>>> import text
>>> data = text.encode_record("café")
>>> data, len(data)
(b'caf\xc3\xa9', 5)
>>> text.decode_record(data)
'café'
>>> text.from_b64(text.to_b64("café"))
'café'
```

## What the check verifies, and what it leaves to you

- Enforced: `encode_record` returns `bytes`; encode/decode round-trips non-ASCII text;
  a one-character accented string is two UTF-8 bytes; base64 round-trips and its output is
  pure ASCII.
- Your free choice: little — these wrap the standard encode/decode and `base64` calls, so
  the behaviour is fixed.

<div class="hint" title="If you are stuck">

`encode_record` is `s.encode("utf-8")`; `decode_record` is `data.decode("utf-8")`. For
base64, `base64.b64encode(raw)` and `base64.b64decode(s)`.

</div>

Reference: Python documentation, "Built-in Types — bytes" and "base64 — Base16, Base32,
Base64 Data Encodings" at docs.python.org.
