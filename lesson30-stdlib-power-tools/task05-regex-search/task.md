# Regex-backed search over the catalog

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.5 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compile and reuse patterns with re.compile for efficiency
- Extract structured data with capture and named groups and Match.groupdict
- Use lookahead/lookbehind for context-sensitive matching without consuming text
- Apply flags (IGNORECASE/MULTILINE/VERBOSE) and write readable verbose patterns
- Transform text with re.sub including a function replacement

## Python features introduced
`re.compile`, `re.search / re.match / re.fullmatch`, `re.findall / re.finditer`, `re.sub with replacement and callback`, `capture groups and group(n)`, `named groups (?P<name>...) and Match.groupdict`, `lookahead (?=...) and lookbehind (?<=...)`, `flags (re.IGNORECASE, re.MULTILINE, re.VERBOSE)`, `Match object (group/start/end/span)`, `raw strings for patterns`

## MiniERP increment
Add MiniERP's search facility: a search module that parses SKU codes with a named-group pattern (e.g. (?P<cat>[A-Z]{3})-(?P<num>\d{4})), filters products/customers by a case-insensitive query via finditer, and a redact() using re.sub to mask emails/phone in audit output. The catalog and customers are now searchable and audit output is privacy-aware.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/search.py with parse_sku(code), find_products(query, items), and redact(text); learner writes the compiled patterns (named groups, lookahead, flags) and the sub callback.
- **Test focus:** parse_sku returns the right groupdict and rejects malformed codes; find_products is case-insensitive and uses finditer; redact masks emails/phones via re.sub; lookahead/lookbehind behave as specified.

</div>
