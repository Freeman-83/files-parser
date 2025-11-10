from abc import ABC, abstractmethod
from tabulate import tabulate

from parsers.classes import Parser, ParserCSVtoDict



class Report(ABC):
    """Абстрактный класс Отчета."""

    def __init__(self, report_name: str):
        self.report_name = report_name

    @abstractmethod
    def create_report_data(self, parsed_data):
        pass


class PrintableReportView:

    def print_report_table(
        report_name: str,
        report_data: list,
        headers: list
    ) -> None:
        """Класс консольного вывода таблицы с отчетом."""

        report_table = tabulate(
            report_data,
            headers=headers,
            tablefmt='psql',
            showindex=range(1, len(report_data) + 1)
        )

        print(report_name, report_table, sep='\n')


class DictReport(Report):

    def create_report_data(
        self,
        parsed_data,
        position_value,
        culculated_value
    ):
        
        summary_report: dict = {}
        
        for row in parsed_data:
            summary_report.setdefault(
                row[position_value], []
            ).append(float(row[culculated_value]))


        report_data = [
            [key, round(sum(values) / len(values), 2)]
            for key, values in summary_report.items()
        ]
        report_data.sort(key=lambda i: i[1], reverse=True)

        headers = [position_value, culculated_value]

        return self.report_name, report_data, headers
