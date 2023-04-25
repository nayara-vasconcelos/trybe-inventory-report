# from simple_report import SimpleReport, InventoryInfos

from inventory_report.reports.simple_report import SimpleReport, InventoryInfos


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        simple_report = SimpleReport.generate(products)
        company_stock = InventoryInfos.get_company_products_qty(products)
        text = "- {0}: {1}\n"
        complementary_report = ""
        for company, quantity in company_stock:
            complementary_report += text.format(company, str(quantity))
        complete_report = (
            simple_report
            + "\nProdutos estocados por empresa:\n"
            + complementary_report
        )
        return complete_report


if __name__ == "__main__":
    products = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-02-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
        {
            "id": "2",
            "nome_do_produto": "fentanyl citrate",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-06",
            "data_de_validade": "2023-12-25",
            "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "instrucoes_de_armazenamento": "instrucao 2",
        },
        {
            "id": "3",
            "nome_do_produto": "NITROUS OXIDE",
            "nome_da_empresa": "Galena Biopharma",
            "data_de_fabricacao": "2020-12-22",
            "data_de_validade": "2024-11-07",
            "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
            "instrucoes_de_armazenamento": "instrucao 3",
        },
    ]
    report = CompleteReport.generate(products=products)
    print(report)
