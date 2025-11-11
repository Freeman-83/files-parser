from parsers.classes import (
    FilesParser,
    CommandLineParser,
    ArgParser,
    ParserCSV,
    FilesParserManager,
    CommandLineParserManager
)
from reports.classes import (
    Report,
    ReportAverage,
    PrintableReport,
    ReportManager
)

from consts import REPORT_CHOISES


def main():

    dir_path = input('Укажите путь к месту расположения файлов: ')

    arg_parser = ArgParser()
    csv_parser = ParserCSV()

    files_parser_manager = FilesParserManager(csv_parser)
    command_line_parser_manager = CommandLineParserManager(arg_parser)

    command_line_args = command_line_parser_manager.get_command_line_args()
    report_name = command_line_args.report
    parsing_files = command_line_args.files
    headers = REPORT_CHOISES[report_name]

    parsed_data = files_parser_manager.get_files_parsed_data(dir_path, parsing_files)

    report_average = ReportAverage(parsed_data)

    report_manager = ReportManager(report_average)
    report_data = report_manager.get_report(*headers)

    report = PrintableReport(report_data)
    report.print_report_table(report_name, headers)


if __name__ == '__main__':
    main()