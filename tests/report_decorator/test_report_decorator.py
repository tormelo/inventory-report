import pytest
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


@pytest.fixture
def products():
    return [
        {
            "id": 1,
            "nome_do_produto": "Cafe",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao",
        },
        {
            "id": 2,
            "nome_do_produto": "MESA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-05-04",
            "data_de_validade": "2023-04-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
        },
        {
            "id": 3,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-03-19",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
    ]


def test_decorar_relatorio(products):
    colored_report = ColoredReport(SimpleReport)
    report = colored_report.generate(products)

    assert (
        "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m2020-07-04\033[0m\n"
        + "\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m2023-04-09\033[0m\n"
        + "\033[32mEmpresa com mais produtos:\033[0m "
        + "\033[31mForces of Nature\033[0m"
    ) == report
