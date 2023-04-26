from collections.abc import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(data=self.data)

    def import_data(self, path, report_type):
        report_options = ["simpes", "completo"]
        data = self.importer.import_data(path)
        self.data.extend(data)

        report = (
            SimpleReport.generate(self.data)
            if report_type == report_options[0]
            else CompleteReport.generate(self.data)
        )

        return report
