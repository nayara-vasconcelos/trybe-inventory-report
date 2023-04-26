from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Produto Teste",
        nome_da_empresa="Empresa Teste",
        data_de_fabricacao="2023-01-01",
        data_de_validade="2025-01-01",
        numero_de_serie="FR29 5951 7573 23OY XKGX 6CSG D23",
        instrucoes_de_armazenamento="Instruções",
    )

    expected = (
        "O produto Produto Teste"
        " fabricado em 2023-01-01"
        " por Empresa Teste com validade"
        " até 2025-01-01"
        " precisa ser armazenado Instruções."
    )

    assert str(product) == expected
