# Stage 5: str.format, %-formatting, and Template

f-strings are the modern default, but Python has three other formatting systems, and you
need to recognise all of them: you will read `%`-style in older code, reach for
`str.format` / `format_map` when the template is separate from the data, and use
`string.Template` when the template comes from a *user* and running arbitrary expressions
would be unsafe. This stage adds two document helpers to `text.py`.

## str.format and format_map

`str.format` fills `{}` fields in a template string that does not have to be an f-string —
useful when the template is defined somewhere else (a constant, a config value):

```
>>> "Invoice {invoice_no} for {customer}".format(invoice_no="INV-1", customer="Acme")
'Invoice INV-1 for Acme'
```

When your data is already a **dict**, `format_map` fills directly from it (no `**`
unpacking):

```
>>> data = {"invoice_no": "INV-1", "customer": "Acme"}
>>> "Invoice {invoice_no} for {customer}".format_map(data)
'Invoice INV-1 for Acme'
```

A missing key raises `KeyError` — which is what you want for a required invoice field:
fail loudly rather than print a blank.

## %-formatting (printf style)

The oldest system, still everywhere in legacy code and logging: `%s` for a string, `%d`
for an integer, `%0.2f` for two decimals. Read it; reach for f-strings or `format` in new
code.

```
>>> "%s = %0.2f" % ("total", 9.5)
'total = 9.50'
```

## string.Template — safe for user-supplied templates

When the *template itself* comes from outside (a user-editable email or notification),
f-strings and `format` are the wrong tool: they can evaluate expressions or be tricked by
stray braces. `string.Template` uses plain `$name` placeholders and does nothing else, so
it is safe to hand to a user. `safe_substitute` fills the names it knows and **leaves
unknown `$placeholders` untouched** instead of raising — ideal when a template may contain
markers you have not filled yet:

```
>>> from string import Template
>>> Template("Hi $name from $company").safe_substitute(name="Sam")
'Hi Sam from $company'
```

## Your task

Fill in the two blanks in `text.py`:

1. `render_invoice_header(data)` — fill the given template from the `data` dict with
   `format_map`.
2. `render_email(template, **values)` — fill a user-supplied `$`-placeholder template with
   `Template` and `safe_substitute`, leaving unknown placeholders in place.

## Worked example

```
>>> import text
>>> text.render_invoice_header({"invoice_no": "INV-1", "customer": "Acme"})
'Invoice INV-1 for Acme'
>>> text.render_email("Hi $name from $company", name="Sam")
'Hi Sam from $company'
```

## What the check verifies, and what it leaves to you

- Enforced: `render_invoice_header` fills both named fields and raises on a missing key;
  `render_email` substitutes known names and keeps unknown `$placeholders` rather than
  raising.
- Your free choice: nothing about the wording here — these wrap specific stdlib behaviours,
  so the behaviour is the whole point.

<div class="hint" title="If you are stuck">

`render_invoice_header` is `template.format_map(data)`. `render_email` is
`Template(template).safe_substitute(values)`.

</div>

Reference: Python documentation, "Custom String Formatting" (str.format) and "string —
Common string operations: Template strings" at docs.python.org.
