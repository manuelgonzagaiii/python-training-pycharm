"""Internationalize with gettext & locale

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
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

"""

# Your code here.
