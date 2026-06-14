# Text tooling: textwrap, difained and unicode

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.6 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Format report blocks with textwrap (fill/shorten/indent/dedent)
- Suggest corrections for typo'd product names with difflib.get_close_matches
- Produce a unified diff of two record versions with difflib.unified_diff
- Normalize and fold Unicode (NFKD, casefold, strip accents) for robust search/sorting
- Build safe templated strings with string.Template

## Python features introduced
`string module (Template, capwords, ascii_letters, digits, punctuation)`, `textwrap (wrap, fill, shorten, indent, dedent)`, `difflib (SequenceMatcher, get_close_matches, unified_diff)`, `unicodedata (normalize NFC/NFKD, name, category)`, `str.casefold for caseless compare`, `stripping accents via unicodedata`

## MiniERP increment
Polish MiniERP's text layer: a text module that wraps invoice/report line items to a fixed width (textwrap), offers 'did you mean?' product suggestions (difflib.get_close_matches), diffs two versions of a record for the audit log (unified_diff), and normalizes names for accent-insensitive search (unicodedata + casefold). Reports look clean and search tolerates accents and typos.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/textfmt.py with wrap_lines(), suggest(name, known), diff_records(a, b), and normalize(name); learner implements with textwrap, difflib, unicodedata, string.
- **Test focus:** wrap_lines respects width/indent; suggest returns near matches; diff_records produces a unified diff; normalize folds accents/case so 'José' matches 'jose'.

</div>
