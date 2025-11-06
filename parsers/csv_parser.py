


class ReportCSV(Report):

    def __init__(self, report_name, parsed_data):
        super().__init__(report_name, parsed_data)


def create_report_data(
    report_name: str,
    files_data: list,
    dir_path: str
) -> tuple[str, list, list]:
    """Функция парсинга csv файлов и формирования сводного отчета."""

    position_value, culculated_value = REPORT_CHOISES[report_name]

    summary_report: dict[str, list] = {}

    for current_file in files_data:
        try:
            current_files_path = os.path.join(dir_path, current_file)
            with open(current_files_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    summary_report.setdefault(
                        row[position_value], []
                    ).append(float(row[culculated_value]))

        except KeyError:
            raise KeyError(
                f'В файле {current_file} отсутствует позиция {position_value}'
            )

        except Exception:
            raise FileNotFoundError(
                f'Несуществующая директория или файл {current_files_path}'
            )

    report_data = [
        [key, round(sum(values) / len(values), 2)]
        for key, values in summary_report.items()
    ]
    report_data.sort(key=lambda i: i[1], reverse=True)

    headers = [position_value, culculated_value]

    return report_name, report_data, headers