import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if ".json" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            return json.load(file)
