# Stage 6: raw strings, escapes, and Unicode

MiniERP stores names and notes from every corner of the world: `Renée`, `Müller`, `café`,
`€`. To search and deduplicate them reliably, you need to understand what a string really
is — a sequence of Unicode code points — and how to write and normalize those code points.
This stage adds the normalization helpers MiniERP's search and dedup depend on.

## Escapes and raw strings

In an ordinary string, a backslash starts an **escape**: `\n` is a newline, `\t` a tab,
`\\` a literal backslash, `\"` a quote. That is usually what you want — but not when the
backslashes are *data*, like a Windows path or a regex. A **raw string**, prefixed `r`,
turns escaping off:

```
>>> "C:\name"      # \n is a newline -- almost certainly a bug
'C:\name'          # (prints as C:, newline, ame)
>>> r"C:\name"     # raw: backslash is literal
'C:\\name'
```

Rule of thumb: use a raw string whenever a backslash should mean a backslash.

## Writing a character by code point

Every character has a numeric **code point**. You can write one by its hex value or, more
readably, by its official **name**:

- `\xNN` — a 2-hex-digit code point (0-255), e.g. `\xe9`.
- `\uXXXX` — a 4-hex-digit code point, e.g. `\u20ac` (the euro sign).
- `\N{NAME}` — by Unicode name, e.g. `\N{EURO SIGN}`. This is self-documenting: a reader
  sees what it is without looking it up.

`ord(ch)` gives a character's code point and `chr(n)` goes back — inverses of each other:

```
>>> ord("€"), chr(0x20ac)
(8364, '€')
>>> "\N{EURO SIGN}" == "\u20ac" == "€"
True
```

## Why normalization matters

Here is the subtle one. The text `café` can be stored two different ways: as `é` (one code
point, U+00E9), or as `e` followed by a *combining* accent (U+0301). They **look
identical** but are different strings, so `==` says they are not equal and a naive search
misses one of them.

`unicodedata.normalize` fixes this by rewriting text into a canonical form. **NFC** composes
characters; **NFKC** goes further, also folding compatibility variants (like a full-width
digit to a normal one). For search keys, normalize first and the two `café`s become the
same string:

```
>>> import unicodedata
>>> a = "caf" + chr(0x00e9)      # composed
>>> b = "cafe" + chr(0x0301)     # decomposed
>>> a == b
False
>>> unicodedata.normalize("NFKC", a) == unicodedata.normalize("NFKC", b)
True
```

## Your task

Fill in the three blanks in `text.py`:

1. `normalize_unicode(s)` — return the NFKC-normalized text.
2. `code_points(s)` — the list of `ord()` for each character.
3. `currency_symbol(code)` — supply the euro symbol using a `\N{...}` named escape (the
   pound and yen entries show the pattern).

## What the check verifies, and what it leaves to you

- Enforced: a composed and a decomposed `café` become equal after `normalize_unicode`;
  `currency_symbol("EUR")` is the euro sign; `code_points`/`chr` round-trip.
- Your free choice: little here — these wrap exact stdlib behaviour, so the behaviour is
  the point.

<div class="hint" title="If you are stuck">

`normalize_unicode` is `unicodedata.normalize("NFKC", s)`. `code_points` is
`[ord(ch) for ch in s]`. The euro entry is `"\N{EURO SIGN}"`.

</div>

Reference: Python documentation, "unicodedata" and "Lexical analysis — String and Bytes
literals (escape sequences)" at docs.python.org.
