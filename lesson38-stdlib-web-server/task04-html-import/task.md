# Scraping data with html.parser

> **Phase:** Networking & the Web  •  **Stage:** 38.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Subclass HTMLParser and override the start/end/data callbacks
- Track parser state across events to extract structured rows from a table
- Read tag attributes and unescape entity references
- Understand event-driven (SAX-style) parsing vs building a tree

## Python features introduced
`html.parser.HTMLParser subclassing`, `handle_starttag / handle_endtag / handle_data`, `attrs as list of tuples`, `stateful parsing with instance attributes`, `html.unescape`, `extracting a table into rows`

## MiniERP increment
Adds erp/io/html_import.py: a supplier-catalog importer that reads an HTML <table> of products (the kind a vendor emails) and yields parsed product rows into the existing import pipeline. Extends MiniERP's Import/Export module to accept HTML.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from html.parser import HTMLParser

class ProductTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        # TODO: on <tr> start a row, on <td> start a cell buffer
        raise NotImplementedError

    def handle_data(self, data):
        # TODO: if inside a cell, accumulate text
        raise NotImplementedError

    def handle_endtag(self, tag):
        # TODO: on </td> finish cell, on </tr> finish row
        raise NotImplementedError

def parse_catalog(html_text: str) -> list[list[str]]:
    p = ProductTableParser(); p.feed(html_text); return p.rows
- **Test focus:** Feed a small HTML table (with an entity like & and nested formatting tags) and assert parse_catalog returns the expected list of row-lists with text unescaped and whitespace handled.

</div>
