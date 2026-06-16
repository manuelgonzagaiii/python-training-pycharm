"""MiniERP record export: encode catalog rows for systems that are not UTF-8.

Some downstream systems accept only ASCII or a legacy codec, so encoding a row
can fail on an accent or a currency symbol. The errors= policy decides what
happens on a failure, and a custom error handler lets us export losslessly as
escapes instead of crashing or silently corrupting data.
"""
import codecs


def xref_handler(error: UnicodeEncodeError) -> tuple[str, int]:
    """A custom encode-error handler: replace each unencodable character with an XML ref.

    Python calls a handler with the UnicodeEncodeError and expects a
    (replacement, resume_index) pair back. We read the failed slice from the
    error's attributes and turn each character into '&#<codepoint>;', so an em
    dash (U+2014) becomes '&#8212;'.
    """
    bad = error.object[error.start:error.end]
    replacement = "".join(f"&#{ord(ch)};" for ch in bad)
    return replacement, error.end


codecs.register_error("xref", xref_handler)


def export_record(record: dict, encoding: str = "ascii", errors: str = "strict") -> bytes:
    """Join a record's values with '|' and encode to `encoding` using the `errors` policy."""
    line = "|".join(str(value) for value in record.values())
    return line.encode(encoding, errors=errors)
