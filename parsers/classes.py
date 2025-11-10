import csv
import os

from argparse import ArgumentParser

from abc import ABC, abstractmethod

from consts import REPORT_CHOISES


class Parser(ABC):
    """Абстрактный класс Парсера."""

    @abstractmethod
    def create_parsed_data(self, dir_path, parsing_files):
        pass


class CommandLineParser:
    """Парсер коммандной строки."""

    def get_args(self, args=None):

        parser = ArgumentParser(description='Command Line Parser')

        report = parser.add_argument(
            '--report',
            type=str,
            choices=list(REPORT_CHOISES),
            help='Наименование отчета'
        )
        files = parser.add_argument(
            '--files',
            type=str,
            nargs='+',
            help='Перечень файлов для составления отчета',
        )

        parser_args = parser.parse_args(args)

        # check_exist_parser_args(report, files, parser_args)

        return parser_args


class ParserCSVtoDict(Parser):
    """Класс CSV-парсера."""

    def create_parsed_data(self, dir_path, parsing_files) -> dict:

        parsed_data: dict = {}

        for current_file in parsing_files:
            current_files_path = os.path.join(dir_path, current_file)
            with open(current_files_path, mode='r') as file:
                current_data = csv.DictReader(current_file)
                for row in current_data:
                    parsed_data.update(row)

        return parsed_data

