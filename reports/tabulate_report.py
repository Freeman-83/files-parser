from tabulate import tabulate


def print_report_table(
    report_name: str,
    report_data: list,
    headers: list
) -> None:
    """Функция консольного вывода таблицы с отчетом."""

    report_table = tabulate(
        report_data,
        headers=headers,
        tablefmt='psql',
        showindex=range(1, len(report_data) + 1)
    )

    print(report_name, report_table, sep='\n')