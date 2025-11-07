import csv
import os

from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс Парсера."""

    @abstractmethod
    def create_parsed_data(self, dir_path, parsing_files: list):
        pass


class ParserCSVtoDict(Parser):
    """Класс CSV-парсера."""

    def create_parsed_data(self, dir_path, parsing_files: list):

        parsed_data: dict = {}

        for current_file in parsing_files:
            current_files_path = os.path.join(dir_path, current_file)
            with open(current_files_path, mode='r') as file:
                current_data = csv.DictReader(current_file)
                parsed_data.update(current_data)

        return parsed_data

