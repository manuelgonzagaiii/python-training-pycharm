# Stage 11: custom codec error handlers

Stage 8 encoded text to bytes with UTF-8, which can represent everything. The hard case is
when a *downstream system cannot* — an old accounting package that speaks only ASCII or
Latin-1. Encoding `Renée` or an em dash to ASCII fails, and you have to decide: crash,
drop the character, or translate it. This final stage of the lesson gives MiniERP's export
layer that control, including a **custom** handler — a genuinely advanced corner of the
standard library, and the kind of thing that separates "it works on my data" from "it works
on everyone's data".

## The errors= policy

Every `encode` (and `decode`) takes an `errors=` argument that decides what happens when a
character does not fit the target codec. The built-in handlers:

- `"strict"` (default) — raise `UnicodeEncodeError`. Correct when bad data must not pass
  silently.
- `"replace"` — substitute `?` for each bad character. Safe, but lossy.
- `"ignore"` — drop bad characters entirely. Lossier still.
- `"backslashreplace"` / `"xmlcharrefreplace"` / `"namereplace"` — lossless escapes
  (`\u2014`, `&#8212;`, `\N{EM DASH}`) you can later reverse.

```
>>> "Renée".encode("ascii", errors="replace")
b'Ren?e'
>>> "Renée".encode("ascii", errors="strict")
UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' ...
```

## Writing your own handler

When none of the built-ins fit, you register your own. A handler is a function that Python
calls with a `UnicodeEncodeError` and that returns a **`(replacement, resume_index)`** pair:
the text to substitute, and the index to carry on encoding from — which must point *past*
the failure (use `error.end`); a smaller index makes the encoder call your handler at the
same spot forever. The error object tells you exactly what failed:

- `error.object` — the whole string being encoded.
- `error.start` / `error.end` — the slice that could not be encoded.

`codecs.register_error("name", handler)` makes it available as `errors="name"`. The
`xref_handler` here turns each bad character into an XML character reference
(`&#8212;` for an em dash) — a real format legacy systems accept.

## Your task

Fill in the three blanks:

1. In `xref_handler`, read the failed slice: `error.object[error.start:error.end]`.
2. Return the `(replacement, error.end)` pair.
3. In `export_record`, encode the joined line with the chosen `encoding` and `errors`.

## Worked example

```
>>> import export
>>> export.export_record({"name": "Renee", "note": "ok"}, "ascii", "strict")
b'Renee|ok'
>>> export.export_record({"x": "\N{EM DASH}"}, "ascii", "xref")
b'&#8212;'
>>> export.export_record({"name": "Ren\N{LATIN SMALL LETTER E WITH ACUTE}e"}, "ascii", "strict")
UnicodeEncodeError: ...
```

## What the check verifies, and what it leaves to you

- Enforced: `"strict"` raises on a non-ASCII record while `"replace"` and `"ignore"` do
  not; an ASCII record encodes exactly; the custom `"xref"` handler emits `&#8212;` for an
  em dash.
- Your free choice: the join separator detail and the handler's exact escape format are
  fixed here because the test pins the documented behaviour; the wording of nothing else
  matters.

<div class="hint" title="If you are stuck">

The failed slice is `error.object[error.start:error.end]`; the handler returns
`replacement, error.end`; and the encode is `line.encode(encoding, errors=errors)`.

</div>

Reference: Python documentation, "codecs — Error Handlers and register_error" and "Built-in
Types — bytes.decode / str.encode" at docs.python.org.
