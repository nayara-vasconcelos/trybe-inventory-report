from inventory_report.importer.importer import Importer
import csv

# from importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(filename):
        if not filename.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(filename, encoding="utf-8") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            dict_list = [row for row in content]

        return dict_list


if __name__ == "__main__":
    data = CsvImporter.import_data("inventory.csv")
    print(data)
