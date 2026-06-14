# Custom codec error handlers: lossless export to legacy systems

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.11 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain what an error handler is in Python's codec machinery and when each of the six built-in handlers ('strict', 'replace', 'ignore', 'backslashreplace', 'xmlcharrefreplace', 'namereplace', plus 'surrogateescape' for decoding) is the right tool.
- Read the attributes of a UnicodeEncodeError / UnicodeDecodeError (.object, .start, .end, .reason, .encoding) to inspect exactly which characters could not be represented.
- Write a custom error handler: a callable that receives a UnicodeError and returns a (replacement_str_or_bytes, resume_index) tuple, then register it under a namespaced name with codecs.register_error so it can be passed as errors='...' to any encode/decode call.
- Use surrogateescape to losslessly round-trip bytes that are not valid in the declared encoding, so a messy imported CSV can be re-exported byte-for-byte.
- Choose the correct handler for a downstream consumer: backslashreplace/namereplace for debuggable logs, xmlcharrefreplace for an XML/HTML export feed, a custom transliterating handler for an ASCII-only accounting partner.

## Python features introduced
`codecs.register_error`, `codecs.lookup_error`, `custom error-handler callables (signature taking a UnicodeError, returning a (replacement, resume_index) tuple)`, `UnicodeEncodeError / UnicodeDecodeError attributes: .object, .start, .end, .reason, .encoding`, `built-in named error handlers: 'backslashreplace', 'xmlcharrefreplace', 'namereplace', 'surrogateescape'`, `contrast with previously-seen 'strict' / 'replace' / 'ignore'`, `str.encode(encoding, errors) and bytes.decode(encoding, errors) with the errors= argument`, `surrogateescape round-tripping of undecodable bytes (\udc80-\udcff smuggling)`, `unicodedata.name lookups for human-readable fallbacks`, `slicing a UnicodeError's .object to read the offending code unit(s)`

## MiniERP increment
Extends the Import/Export module's text layer so MiniERP can hand its catalog to systems that don't speak UTF-8 without ever crashing on an exotic character and without silently corrupting data. You implement an export_record(record, encoding, errors) helper that encodes a customer/product row (names with accents, currency symbols, the em dash in notes) to a target byte encoding using a caller-chosen handler, and a custom handler registered via codecs.register_error('minierp.xref', ...) that replaces any unencodable character with a stable, reversible '[U+XXXX NAME]' token (built from the UnicodeEncodeError attributes and unicodedata.name) so an ASCII-only partner feed stays human-auditable. You also add import_bytes(raw, encoding) that decodes a partner's CSV with errors='surrogateescape' so undecodable bytes survive a later re-export byte-for-byte. This makes the export feed (built in p02 as plain UTF-8 bytes) robust for the legacy/EDI integrations the Reporting and Import/Export modules need later.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** In task.py provide a customer/product record (a dict with fields like name='Renée Müller', note='priority — VIP', price_label='49,99 €'), an unfinished export_record(record, encoding='ascii', errors='strict') that joins fields and calls str.encode, a stub xref_handler(err) the learner completes to return ('[U+%04X %s]' % (cp, unicodedata.name(chr(cp), '?')), err.start+1), a codecs.register_error('minierp.xref', xref_handler) registration line, and import_bytes(raw, encoding) using decode(..., 'surrogateescape'). Seed TODOs where the learner fills the handler body and wires errors= through.
- **Test focus:** Verify: (1) export_record(..., errors='strict') raises UnicodeEncodeError on a non-ASCII record while errors='replace'/'ignore' do not; (2) the four named handlers produce their documented bytes (e.g. backslashreplace yields b'\\u2014' for the em dash, xmlcharrefreplace yields b'—', namereplace yields b'\\N{EM DASH}'); (3) codecs.lookup_error('minierp.xref') returns the registered handler and export_record(..., errors='minierp.xref') turns 'é' into b'[U+00E9 LATIN SMALL LETTER E WITH ACUTE]' with surrounding ASCII intact; (4) the custom handler advances correctly over consecutive non-ASCII chars (no infinite loop, no skipped characters); (5) import_bytes(b'caf\xe9', 'utf-8') decodes via surrogateescape and re-encoding with 'surrogateescape' reproduces the original bytes exactly; (6) a UnicodeEncodeError caught in the test exposes .start/.end/.object pointing at the offending character.

</div>
