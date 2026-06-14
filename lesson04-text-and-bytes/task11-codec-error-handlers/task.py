"""Custom codec error handlers: lossless export to legacy systems

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: In task.py provide a customer/product record (a dict with fields like name='Renée Müller', note='priority — VIP', price_label='49,99 €'), an unfinished export_record(record, encoding='ascii', errors='strict') that joins fields and calls str.encode, a stub xref_handler(err) the learner completes to return ('[U+%04X %s]' % (cp, unicodedata.name(chr(cp), '?')), err.start+1), a codecs.register_error('minierp.xref', xref_handler) registration line, and import_bytes(raw, encoding) using decode(..., 'surrogateescape'). Seed TODOs where the learner fills the handler body and wires errors= through.
"""

# Your code here.
