from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list[dict]) -> str:
        company_products = super().get_product_quantity_by_company(products)
        company_tuples = [(k, v) for k, v in company_products.items()]

        new_report = "Produtos estocados por empresa:\n"
        for name, quantity in company_tuples:
            new_report += f"- {name}: {quantity}\n"

        return super().generate(products) + "\n" + new_report
