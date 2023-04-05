from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "test_name",
        "test_company_name",
        "test_fab_date",
        "test_exp_date",
        1200,
        "test_instructions",
    )

    assert product.id == 1
    assert product.nome_do_produto == "test_name"
    assert product.nome_da_empresa == "test_company_name"
    assert product.data_de_fabricacao == "test_fab_date"
    assert product.data_de_validade == "test_exp_date"
    assert product.numero_de_serie == 1200
    assert product.instrucoes_de_armazenamento == "test_instructions"
