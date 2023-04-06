from collections.abc import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer) -> None:
        # super().__init__()
        self.importer = importer
        self.data = []

    def import_data(self, path: str, report_type: str) -> None:
        self.data = self.data + self.importer.import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(self.data)
        if report_type == "completo":
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
