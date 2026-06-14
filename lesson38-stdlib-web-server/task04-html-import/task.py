"""Scraping data with html.parser

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from html.parser import HTMLParser

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
"""

# Your code here.
