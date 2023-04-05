import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path)
        root = tree.getroot()

        element_list = []
        for child in root.findall("record"):
            element_list.append({value.tag: value.text for value in child})

        return element_list
