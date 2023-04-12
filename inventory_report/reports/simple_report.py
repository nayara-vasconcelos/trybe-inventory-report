from datetime import datetime, date


# Se a data de referência for anterior a outra data,
# retornará um valor negativo
# Caso contrário, retornará um valor positivo
def calc_days_between_dates(reference_date: str, another_date: str) -> int:
    format_date = "%Y-%m-%d"
    main_date = datetime.strptime(reference_date, format_date)
    secondary_date = datetime.strptime(another_date, format_date)
    qty_days = (main_date - secondary_date).days
    return qty_days


class SimpleReport:
    def _get_nearest_expiration_date(self, products) -> str:
        today_date = str(date.today())
        # exclude expired products
        dates_days = [
            (
                product["data_de_validade"],
                abs(
                    calc_days_between_dates(
                        today_date, product["data_de_validade"]
                    )
                ),  # qty of days before getting expired
            )
            for product in products
            if calc_days_between_dates(today_date, product["data_de_validade"])
            < 0
        ]
        diff_days = [date_days[1] for date_days in dates_days]
        date_index = diff_days.index(min(diff_days))
        nearest_exp_date = dates_days[date_index][0]
        return nearest_exp_date

    def _get_oldest_date_of_manufacture(self, products) -> str:
        today_date = str(date.today())
        dates_days = [
            (
                product["data_de_fabricacao"],
                calc_days_between_dates(
                    today_date, product["data_de_fabricacao"]
                ),
            )
            for product in products
        ]
        diff_days = [date_days[1] for date_days in dates_days]
        date_index = diff_days.index(max(diff_days))
        oldest_date_of_manufacture = dates_days[date_index][0]
        return oldest_date_of_manufacture

    def _get_company_with_the_largest_stock(self, products) -> str:
        company_stock = {}
        for product in products:
            if product["nome_da_empresa"] in company_stock:
                company_stock[product["nome_da_empresa"]] += 1
            else:
                company_stock[product["nome_da_empresa"]] = 1

        qty_products = [
            company_qty[1] for company_qty in company_stock.items()
        ]
        index = qty_products.index(max(qty_products))
        company_name = list(company_stock.keys())[index]
        return company_name

    @staticmethod
    def generate(products) -> str:
        simple_report = SimpleReport()
        date_of_manufacture = simple_report._get_oldest_date_of_manufacture(
            products
        )
        expiration_date = simple_report._get_nearest_expiration_date(products)
        company_name = simple_report._get_company_with_the_largest_stock(
            products
        )
        text = (
            "Data de fabricação mais antiga: {0}\n"
            "Data de validade mais próxima: {1}\n"
            "Empresa com mais produtos: {2}"
        )
        report = text.format(
            date_of_manufacture, expiration_date, company_name
        )
        return report


if __name__ == "__main__":
    today_date = str(date.today())
    # print(today_date)
    days = calc_days_between_dates(today_date, "2024-04-11")
    # print(days)
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
    nearest_exp_date = SimpleReport()._get_nearest_expiration_date(products)
    # print(nearest_exp_date)
    oldest_date_of_manufacture = (
        SimpleReport()._get_oldest_date_of_manufacture(products)
    )
    # print(oldest_date_of_manufacture)
    company_name = SimpleReport()._get_company_with_the_largest_stock(products)
    # print(company_name)
    report = SimpleReport.generate(products=products)
    print(report)
