import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def get_report(path: str, report_type: str) -> str:
    if ".csv" in path:
        return InventoryRefactor(CsvImporter).import_data(path, report_type)
    if ".json" in path:
        return InventoryRefactor(JsonImporter).import_data(path, report_type)
    if ".xml" in path:
        return InventoryRefactor(XmlImporter).import_data(path, report_type)


def main():
    try:
        _, path, report_type = sys.argv
        print(get_report(path, report_type), end="")
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
