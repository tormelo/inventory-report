from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_csv(cls, path: str) -> list[dict]:
        with open(path) as file:
            reader = csv.DictReader(file)
            return list(reader)

    @classmethod
    def import_json(cls, path: str) -> list[dict]:
        with open(path) as file:
            return json.load(file)

    @classmethod
    def import_xml(cls, path: str) -> list[dict]:
        tree = ET.parse(path)
        root = tree.getroot()

        element_list = []
        for child in root.findall("record"):
            element_list.append({value.tag: value.text for value in child})

        return element_list

    @classmethod
    def get_report(cls, report_type, products: list[dict]) -> str:
        if report_type == "simples":
            return SimpleReport.generate(products)
        if report_type == "completo":
            return CompleteReport.generate(products)

    @classmethod
    def import_data(cls, path: str, report_type: str) -> str:
        if ".csv" in path:
            products = cls.import_csv(path)
        if ".json" in path:
            products = cls.import_json(path)
        if ".xml" in path:
            products = cls.import_xml(path)

        return cls.get_report(report_type, products)
