from datetime import datetime


class SimpleReport:
    @staticmethod
    def get_company_with_most_products(products: list[dict]) -> str:
        company_products = {}
        for product in products:
            if product["nome_da_empresa"] in company_products:
                company_products[product["nome_da_empresa"]] += 1
            else:
                company_products[product["nome_da_empresa"]] = 1

        return max(company_products, key=company_products.get)

    @staticmethod
    def get_oldest_fab_date(products: list[dict]) -> str:
        fab_dates = [
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d").date()
            for product in products
        ]
        return min(fab_dates)

    @staticmethod
    def get_closest_exp_date(products: list[dict]) -> str:
        today_timestamp = datetime.now().timestamp()

        exp_datetimes = [
            datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            for product in products
        ]

        valid_exp_datetimes = [
            exp_datetime
            for exp_datetime in exp_datetimes
            if exp_datetime.timestamp() > today_timestamp
        ]

        closest = valid_exp_datetimes[0]
        for exp_datetime in valid_exp_datetimes:
            if abs(today_timestamp - exp_datetime.timestamp()) < abs(
                today_timestamp - closest.timestamp()
            ):
                closest = exp_datetime

        return closest.date()

    @staticmethod
    def generate(products: list[dict]) -> str:
        oldest_fab_date = SimpleReport.get_oldest_fab_date(products)
        closest_exp_date = SimpleReport.get_closest_exp_date(products)
        company_with_most_products = (
            SimpleReport.get_company_with_most_products(products)
        )
        return (
            f"Data de fabricação mais antiga: {oldest_fab_date}\n"
            + f"Data de validade mais próxima: {closest_exp_date}\n"
            + f"Empresa com mais produtos: {company_with_most_products}"
        )
