from parsers.classes import Parser, CommandLineParser, ParserCSVtoDict
from reports.classes import Report, DictReport, PrintableReportView

from consts import REPORT_CHOISES


def main():
    # report_name = input()
    dir_path = input()
    # parsing_files = list(map(input().split()))

    command_line_parser = CommandLineParser()
    args = command_line_parser.get_args()

    report_name = args.report
    parsing_files = args.files
    
    parser = ParserCSVtoDict()
    parsed_data = parser.create_parsed_data(dir_path, parsing_files)

    report = DictReport(report_name)
    report_data = report.create_report_data(
        parsed_data,
        report_name,
        *REPORT_CHOISES[report_name]
    )

    printable_data = PrintableReportView()
    printable_data.print_report_table(*printable_data)



if __name__ == '__main__':
    main()