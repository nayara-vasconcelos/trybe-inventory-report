import sys

from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter


# Ref:
# https://www.freecodecamp.org/portuguese/news/nova-linha-em-python-e-como-usar-print-em-python-sem-uma-nova-linha/
# Course da Trybe


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    filename = sys.argv[1]
    report_type = sys.argv[2]
    report_options = ["simples", "completo"]

    if filename.endswith(".csv"):
        inventory = InventoryRefactor(CsvImporter)
        report = inventory.import_data(filename, report_type)
        print(report, end="") if report_type == report_options[0] else print(
            report
        )
        return

    if filename.endswith(".json"):
        inventory = InventoryRefactor(JsonImporter)
        report = inventory.import_data(filename, report_type)
        print(report, end="") if report_type == report_options[0] else print(
            report
        )
        return

    if filename.endswith(".xml"):
        inventory = InventoryRefactor(XmlImporter)
        report = inventory.import_data(filename, report_type)
        print(report, end="") if report_type == report_options[0] else print(
            report
        )
        return
