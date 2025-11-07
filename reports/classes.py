from abc import ABC, abstractmethod

from parsers.classes import Parser, ParserCSVtoDict


class Report(ABC):
    """Абстрактный класс Отчета."""

    def __init__(self, report_name: str, parsed_data):
        self.report_name = report_name
        self.parsed_data = parsed_data


    @abstractmethod
    def create_report_data(self):
        pass


class DictReport(Report):

    def create_report_data(self):

        return self.parsed_data