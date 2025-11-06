import csv
import os

from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс Парсера."""

    @abstractmethod
    def create_parsed_data(self):
        pass


class ParserCSVtoDict(Parser):
    """Класс CSV-парсера."""

    def __init__(self, parsing_files: list):
        self.parsing_files = parsing_files

    def create_parsed_data(self, dir_path):

        parsed_data: dict = {}

        for current_file in self.parsing_files:
            current_files_path = os.path.join(dir_path, current_file)
            with open(current_files_path, mode='r') as file:
                current_data = csv.DictReader(current_file)
                parsed_data.update(current_data)

        return parsed_data









