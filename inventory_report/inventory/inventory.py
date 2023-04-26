import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


report_options = ["simples", "completo"]


def read_csv(filename):
    with open(filename, encoding="utf-8") as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        list_dict = [row for row in content]
    return list_dict


def read_json(filename):
    with open(filename) as file:
        content = file.read()
        list_dict = json.loads(content)
    return list_dict


def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    list_dict = []
    # <dataset> -> <record>
    for element in root.findall("./record"):
        item = {}
        for child in element:
            item[child.tag] = child.text
        list_dict.append(item)
    return list_dict


class Inventory:
    @staticmethod
    def import_data(filename, report_type):
        if report_type not in report_options:
            raise ValueError("Tipo de relatório inválido")

        inventory = []
        if filename.endswith(".csv"):
            inventory = read_csv(filename)
        elif filename.endswith(".json"):
            inventory = read_json(filename)
        elif filename.endswith(".xml"):
            inventory = read_xml(filename)
        else:
            raise ValueError("Arquivo inválido")

        report = (
            SimpleReport.generate(inventory)
            if report_type == report_options[0]
            else CompleteReport.generate(inventory)
        )

        return report
