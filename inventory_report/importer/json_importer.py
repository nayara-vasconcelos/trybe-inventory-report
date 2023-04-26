from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(filename):
        if not filename.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(filename) as file:
            content = file.read()
            list_dict = json.loads(content)

        return list_dict
