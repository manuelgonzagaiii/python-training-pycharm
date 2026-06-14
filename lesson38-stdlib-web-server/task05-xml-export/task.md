# Reading and writing XML with ElementTree

> **Phase:** Networking & the Web  •  **Stage:** 38.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build an XML document programmatically with Element/SubElement
- Serialize to bytes/str with tostring and pretty-print with ET.indent
- Parse XML and query it with findall/find and simple XPath
- Be aware of XML parsing security caveats

## Python features introduced
`xml.etree.ElementTree`, `Element / SubElement`, `ET.fromstring / ET.tostring`, `findall / find / iter with XPath-lite`, `element.attrib and .text`, `ET.indent for pretty output`, `encoding declaration`, `note on xml security (defusedxml) as a comment`

## MiniERP increment
Adds erp/io/xml_io.py: export the MiniERP product catalog to an interchange XML format and re-import it, round-tripping through the Import/Export module. Complements the HTML importer with a structured machine format.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import xml.etree.ElementTree as ET

def products_to_xml(products) -> bytes:
    """Serialize products to a <catalog> XML document (pretty, utf-8)."""
    root = ET.Element("catalog")
    for p in products:
        # TODO: SubElement(root, 'product', id=...) with name/price children
        ...
    ET.indent(root)
    # TODO: return ET.tostring(root, encoding='utf-8', xml_declaration=True)
    raise NotImplementedError

def products_from_xml(data: bytes) -> list[dict]:
    """Parse the catalog XML back into a list of plain dicts."""
    root = ET.fromstring(data)
    # TODO: for el in root.findall('product'): extract attrib + child text
    raise NotImplementedError
- **Test focus:** Round-trip products_to_xml then products_from_xml and assert the data matches; assert the output contains the XML declaration and that findall locates every product element.

</div>
