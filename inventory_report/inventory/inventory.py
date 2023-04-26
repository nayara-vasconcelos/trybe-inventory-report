import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


report_options = ["simples", "completo"]


class Inventory:
    @staticmethod
    def import_data(filename, report_type):
        if report_type not in report_options:
            raise ValueError("Tipo de relatório inválido")

        inventory = []
        if filename.endswith(".csv"):
            with open(filename, encoding="utf-8") as file:
                content = csv.DictReader(file, delimiter=",", quotechar='"')
                inventory = [row for row in content]
        else:
            raise ValueError("Arquivo inválido")

        report = (
            SimpleReport.generate(inventory)
            if report_type == report_options[0]
            else CompleteReport.generate(inventory)
        )

        return report
