from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET

# from importer import Importer


# Ref:
# https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
# https://stackoverflow.com/questions/60805355/convert-xml-to-list-of-dictionaries-in-python
# https://www.geeksforgeeks.org/python-xml-to-json/?ref=gcse


class XmlImporter(Importer):
    @staticmethod
    def import_data(filename):
        if not filename.endswith(".xml"):
            raise ValueError("Arquivo inválido")

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


if __name__ == "__main__":
    data = XmlImporter.import_data("inventory.xml")
    print(data)
