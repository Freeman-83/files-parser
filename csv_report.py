from parsers.classes import (
    Parser,
    CommandLineParser,
    ArgParser,
    ParserCSV,
    ParserManager
)
from reports.classes import (
    Report,
    ReportAverage,
    PrintableReport,
    ReportManager
)

from consts import REPORT_CHOISES


def main():
    # report_name = input()
    dir_path = input('Укажите путь к месту расположения файлов: ')
    # parsing_files = list(map(input().split()))

    arg_parser = ArgParser()
    args = arg_parser.get_args()

    report_name = args.report
    parsing_files = args.files
    headers = REPORT_CHOISES[report_name]


    csv_parser = ParserCSV()
    
    parser_manager = ParserManager(csv_parser)
    parsed_data = parser_manager.get_parsed_data(dir_path, parsing_files)


    report_average = ReportAverage(parsed_data)

    report_manager = ReportManager(report_average)
    report_data = report_manager.get_report(*headers)

    report = PrintableReport(report_data)
    report.print_report_table(report_name, headers)


if __name__ == '__main__':
    main()