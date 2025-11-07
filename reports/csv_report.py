from parsers.classes import Parser, ParserCSVtoDict
from reports.classes import Report, DictReport


def main():
    report_name = input()
    dir_path = input()
    parsing_files = list(map(input().split()))

    parser = ParserCSVtoDict()
    parsed_data = parser.create_parsed_data(dir_path, parsing_files)

    report = DictReport(report_name, parsed_data)
    report_data = report.create_report_data()



if __name__ == '__main__':
    main()