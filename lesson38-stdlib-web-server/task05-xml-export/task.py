"""Reading and writing XML with ElementTree

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import xml.etree.ElementTree as ET

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
"""

# Your code here.
