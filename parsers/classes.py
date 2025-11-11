import csv
import os

from argparse import ArgumentParser

from abc import ABC, abstractmethod

from consts import REPORT_CHOISES


class Parser(ABC):
    """Абстрактный класс Парсера."""

    @abstractmethod
    def create_parsed_data(self):
        pass


class ParserCSV(Parser):
    """Класс CSV-парсера."""

    def create_parsed_data(
        self,
        dir_path,
        parsing_files
    ) -> list:

        parsed_data: list = []

        for current_file in parsing_files:
            current_files_path = os.path.join(dir_path, current_file)
            with open(current_files_path, mode='r') as file:
                dict_parser = csv.DictReader(file)
                for row in dict_parser:
                    parsed_data.append(row)

        return parsed_data


class CommandLineParser(ABC):

    def get_args(self):
        pass


class ArgParser(CommandLineParser):
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

        args = parser.parse_args(args)

        # check_exist_parser_args(report, files, parser_args)

        return args


class ParserManager:

    def __init__(self, parser: Parser):
        self.parser = parser

    def get_parsed_data(self, dir_path, parsing_files):
        return self.parser.create_parsed_data(dir_path, parsing_files)



