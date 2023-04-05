from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_csv(cls, path: str) -> list[dict]:
        with open(path) as file:
            reader = csv.DictReader(file)
            return list(reader)

    @classmethod
    def import_data(cls, path: str, report_type: str) -> str:
        if ".csv" in path:
            products = cls.import_csv(path)

        if report_type == "simples":
            return SimpleReport.generate(products)
        if report_type == "completo":
            return CompleteReport.generate(products)
