from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id="11",
        nome_do_produto="Teste Nome Produto",
        nome_da_empresa="Teste Nome Empresa",
        data_de_fabricacao="2023-01-30",
        data_de_validade="2025-01-30",
        numero_de_serie="GT73 LHWJ FCXL JNQT ZCXM 4777 NPSP",
        instrucoes_de_armazenamento="Algumas instruções",
    )

    assert product.id == "11"
    assert product.nome_do_produto == "Teste Nome Produto"
    assert product.nome_da_empresa == "Teste Nome Empresa"
    assert product.data_de_fabricacao == "2023-01-30"
    assert product.data_de_validade == "2025-01-30"
    assert product.numero_de_serie == "GT73 LHWJ FCXL JNQT ZCXM 4777 NPSP"
    assert product.instrucoes_de_armazenamento == "Algumas instruções"
