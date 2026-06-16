# Stage 2: the string method toolbox

Real input is messy: extra spaces, inconsistent capitalisation, accented characters,
comma-separated rows pasted from a spreadsheet. Before MiniERP can store or search a
name, it has to clean it. Python's string methods do almost all of this without regular
expressions, and you will reach for them constantly. This stage adds three input-cleaning
helpers to `text.py`.

## The methods worth knowing now

Strings carry a large method surface. The ones this stage uses, grouped by job:

- **Trim and case:** `strip()` (also `lstrip`/`rstrip`) removes surrounding whitespace.
  For case there is `lower()`, `upper()`, `title()`, `capitalize()` — and `casefold()`,
  which is `lower()` taken further for reliable comparison (it folds tricky characters
  like the German `ß` to `ss`, so `"Straße".casefold()` equals `"STRASSE".casefold()`).
- **Split and join:** `split()` with no arguments splits on *runs* of whitespace and
  drops empties, which is the cleanest way to collapse messy spacing; `split(",")` splits
  on a delimiter; `" ".join(parts)` glues a list back together.
- **Test and search:** `startswith` / `endswith`, `find` / `count`, and the `is...`
  family (`isdigit`, `isalpha`, `isidentifier`, …) answer yes/no questions about content.
- **Edit:** `replace(old, new)`, and the precise `removeprefix` / `removesuffix` (3.9+)
  that strip an exact affix only if present.

The collapse-whitespace idiom is worth memorising: `" ".join(raw.split())` turns
`"  john   smith "` into `"john smith"` in one step — `split()` discards the runs of
spaces, `join` puts single spaces back.

## casefold vs lower (why it matters for a key)

For *display*, `title()` or `lower()` is fine. For a **lookup key** — deciding whether two
names are "the same" — use `casefold()`. It normalises case more aggressively than
`lower()`, so case-insensitive matching works even on non-English text. Using `lower()`
here would quietly fail to match some accented or non-Latin names.

## Your task

Fill in the blanks in `text.py`:

1. `clean_name(raw)` — collapse whitespace and title-case (`"  john  smith "` ->
   `"John Smith"`).
2. `normalize_key(raw)` — strip and casefold, for a case-insensitive lookup key.
3. `parse_csv_line(line)` — split a comma-delimited line; each field is then trimmed for
   you.

## Worked example

```
>>> import text
>>> text.clean_name("  john   smith ")
'John Smith'
>>> text.normalize_key("  Café ") == text.normalize_key("CAFÉ")
True
>>> text.parse_csv_line("a, b ,c")
['a', 'b', 'c']
```

## What the check verifies, and what it leaves to you

- Enforced: whitespace is collapsed and the name title-cased; the key is stripped and
  casefolded (so `"Straße"` and `"STRASSE"` match); a delimited line splits into trimmed
  fields.
- Your free choice: which methods and order you use, as long as the output is right.

<div class="hint" title="If you are stuck">

`clean_name` is `" ".join(raw.split()).title()`. `normalize_key` is
`raw.strip().casefold()`. For `parse_csv_line`, `line.split(",")` gives the fields.

</div>

Reference: Python documentation, "Text Sequence Type — str: String Methods" at
docs.python.org.
