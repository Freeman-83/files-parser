import csv
import os

from argparse import ArgumentParser

from abc import ABC, abstractmethod

from consts import REPORT_CHOISES



class FilesParser(ABC):
    """Абстрактный класс Парсера."""

    @abstractmethod
    def create_parsed_data(self):
        pass


class CommandLineParser(ABC):
    """Абстрактный класс парсера коммандной строки."""

    @abstractmethod
    def get_args(self, args=None):
        pass


class ParserManager(ABC):
    pass


class ParserCSV(FilesParser):
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


class FilesParserManager(ParserManager):

    def __init__(self, files_parser: FilesParser):
        self.files_parser = files_parser

    def get_files_parsed_data(self, dir_path, parsing_files):
        return self.files_parser.create_parsed_data(dir_path, parsing_files)


class CommandLineParserManager(ParserManager):

    def __init__(self, command_line_parser: CommandLineParser):
        self.command_line_parser = command_line_parser

    def get_command_line_args(self, args=None):
        return self.command_line_parser.get_args(args)
