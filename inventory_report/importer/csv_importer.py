import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            reader = csv.DictReader(file)
            return list(reader)
