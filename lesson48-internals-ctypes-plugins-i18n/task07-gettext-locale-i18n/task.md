# Internationalize with gettext & locale

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.7 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Mark user-facing strings with _() and resolve them through gettext catalogs
- Fall back gracefully when no catalog exists (NullTranslations)
- Pluralize messages correctly with ngettext
- Format currency, numbers and grouping for a locale with the locale module

## Python features introduced
`gettext (gettext, ngettext, translation, install)`, `gettext.NullTranslations fallback`, `the _() convention`, `locale.setlocale`, `locale.currency / locale.format_string`, `ngettext plural handling`, `LC_ALL / LC_NUMERIC categories`

## MiniERP increment
Internationalizes MiniERP's CLI and Web user-facing text: erp/i18n.py wires gettext (with a packaged fallback) so messages translate per the configured locale, ngettext handles 'N item(s)', and invoice/report money and number formatting flow through locale.currency/format_string — making the ERP localizable.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import gettext, locale


def get_translator(lang: str, localedir: str | None = None) -> gettext.NullTranslations:
    """Return a gettext translation for `lang`, falling back to NullTranslations
    (identity) when no catalog is found."""
    raise NotImplementedError


def item_count_message(n: int, translator: gettext.NullTranslations) -> str:
    """Use translator.ngettext for '1 item' vs 'N items'."""
    raise NotImplementedError


def money(amount: float, loc: str = "en_US.UTF-8") -> str:
    """Format amount as currency for `loc` via locale.currency (restore locale after)."""
    raise NotImplementedError

- **Test focus:** Tests get_translator returns a working translator that echoes the source string when no catalog exists; tests item_count_message produces singular/plural correctly via ngettext; tests money formats with a currency symbol and restores the previous locale afterward (locale-availability guarded).

</div>
