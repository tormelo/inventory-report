from inventory_report.inventory.product import Product


def test_relatorio_produto():
    prod_name = "farinha"
    company_name = "Farinini"
    fab_date = "2023-01-03"
    exp_date = "2023-06-03"
    prod_instructions = "ao abrigo da luz"

    product = Product(
        1,
        prod_name,
        company_name,
        fab_date,
        exp_date,
        1200,
        prod_instructions,
    )
    expected_report = (
        f"O produto {prod_name} "
        + f"fabricado em {fab_date} "
        + f"por {company_name} "
        + f"com validade até {exp_date} "
        + f"precisa ser armazenado {prod_instructions}."
    )
    assert str(product) == expected_report
