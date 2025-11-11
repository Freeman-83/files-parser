from abc import ABC, abstractmethod

from tabulate import tabulate


class Report(ABC):

    @abstractmethod
    def create_report_data(self):
        pass


class ReportAverage(Report):

    def __init__(self, input_data):
        self.input_data = input_data

    def create_report_data(
        self,
        position_value,
        culculated_value
    ):

        report_data = {}

        for row in self.input_data:
            report_data.setdefault(
                row[position_value], []
            ).append(float(row[culculated_value]))

        
        report_data = [
            [key, round(sum(values) / len(values), 2)] for key, values in report_data.items()
        ]
        report_data.sort(key=lambda i: i[1], reverse=True)
        
        return report_data
    

class ReportManager:

    def __init__(self, report: Report):
        self.report = report

    def get_report(self, position_value, culculated_value):
        return self.report.create_report_data(
            position_value, culculated_value
        )


class PrintableReport:

    def __init__(self, data):
        self.data = data

    def print_report_table(
        self,
        report_name: str,
        headers: list
    ) -> None:
        """Класс консольного вывода таблицы с отчетом."""

        report_table = tabulate(
            self.data,
            headers=headers,
            tablefmt='psql',
            showindex=range(1, len(self.data) + 1)
        )

        print(report_name, report_table, sep='\n')



        
