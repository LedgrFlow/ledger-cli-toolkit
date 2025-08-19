import os
from datetime import datetime
from ledger_cli import (
    LedgerVisual,
    LedgerParser,
    LedgerGrafics,
    LedgerAnalyst,
<<<<<<< HEAD
=======
    LedgerExport,
    LedgerMultiParser,
>>>>>>> 5439302 (Primer commit)
)


def write_class_header(f, class_name):
    f.write(f"\n# Clase: `{class_name}`\n\n")


def write_section(f, title, description, content, code_block=True):
    f.write(f"\n## {title}\n\n")
    f.write(f"{description}\n\n")
    if code_block:
        f.write("```json\n")
        f.write(content)
        f.write("\n```\n")
    else:
        f.write(content + "\n")


if __name__ == "__main__":
    # Directorio de salida
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Nombre del archivo con fecha y hora
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
<<<<<<< HEAD
    filePath = "test/ledgers/test_2.ledger"
=======
    filePath = "test/ledgers/test_4.ledger"
    filePath2 = "test/ledgers/test_2.ledger"
    filePath3 = "test/ledgers/test_3.ledger"
>>>>>>> 5439302 (Primer commit)
    output_path = os.path.join(
        output_dir, f"output_{filePath.split("/")[2]}_{timestamp}.md"
    )

    # Inicialización
    other_parents = {
        "Assets": "Activos",
        "Liabilities": "Pasivos",
        "Equity": "Capital",
        "Income": "Ingresos",
        "Expenses": "Gastos",
    }

    parser = LedgerParser(
<<<<<<< HEAD
        file_path=filePath,
        file_accounts_path=filePath,
=======
        file=filePath,
        file_accounts=filePath,
>>>>>>> 5439302 (Primer commit)
        parents_accounts=other_parents,
    )
    visual = LedgerVisual()
    grafics = LedgerGrafics()

    # Parse the transactions and accounts
<<<<<<< HEAD
    transactions_json = parser.parse()
    accounts_list = parser.parse_accounts()
    accounts_advance = parser.parse_accounts_advance()
    metadata = parser.parse_metadata()

    analyst = LedgerAnalyst(
        transactions=transactions_json,
        accounts=accounts_list,
        income_parents=("Ingresos", "Income"),
        expense_parents=("Gastos", "Expenses"),
        asset_parents=("Activos", "Assets"),
        liability_parents=("Pasivos", "Liabilities"),
=======
    transactions_json = parser.parse_transactions()
    parents = parser.detected_parents_accounts()
    accounts_list = parser.parse_accounts()
    accounts_advance = parser.parse_accounts_advance()
    metadata = parser.parse_metadata()
    metadata_yaml = parser.parse_metadata_yaml()
    map_doc = parser.parse_doc()
    resolved_transactions = parser.resolve(
        transactions_json,
        {
            "IVA": {"percentage": 0.16},
            "RET_ISR": {"percentage": 0.10},
        },
>>>>>>> 5439302 (Primer commit)
    )

    balances = parser.calculate_balances(
        transactions_json=transactions_json, reference=accounts_list
    )
    balances_by_parents = parser.calculate_balances_by_parents_accounts(
        transactions_json=transactions_json
    )
    state_results = parser.calculate_status_results(balances)
    balances_by_details = parser.calculate_balances_by_details_accounts(
        transactions_json=transactions_json
    )
    period = parser.get_date_range(transactions_json=transactions_json)

<<<<<<< HEAD
    # Graficos y exportación
    grafics.create_balance_chart(balances, f"({period[0]} - {period[1]})")
    grafics.create_balance_pie_chart(balances, f"({period[0]} - {period[1]})")
    grafics.show_chart()

    # Cálculos analyst
=======
    # Multiparser
    multi_parser = LedgerMultiParser(
        files=[filePath, filePath2, filePath3],
        parents_accounts=other_parents,
    )

    parsers_all = multi_parser.parse_all()
    resolved_all = multi_parser.resolve_all()

    # Graficos y exportación
    # grafics.create_balance_chart(balances, f"({period[0]} - {period[1]})")
    # grafics.create_balance_pie_chart(balances, f"({period[0]} - {period[1]})")
    # grafics.show_chart()

    # Cálculos analyst

    analyst = LedgerAnalyst(
        transactions=transactions_json,
        accounts=accounts_list,
        income_parents=("Ingresos", "Income"),
        expense_parents=("Gastos", "Expenses"),
        asset_parents=("Activos", "Assets"),
        liability_parents=("Pasivos", "Liabilities"),
    )

>>>>>>> 5439302 (Primer commit)
    daily = analyst.get_daily_incomes_expenses()
    pie_expenses = analyst.get_expenses_pie()
    pie_incomes = analyst.get_incomes_pie()
    assets_summary = analyst.get_assets_summary()
    liabilities_summary = analyst.get_liabilities_summary()
    balance_by_day = analyst.get_balance_by_day()
    accounts_used = analyst.get_accounts_used()
    detected_alerts = analyst.detect_unusual_expenses(threshold=1.5)
    cashflow_by_month = analyst.get_cashflow_by_month()
    expenses_trends = analyst.get_expense_trends_by_category()
    monthly_growth_rates = analyst.get_monthly_growth_rates()
    monthly_expense_ratio = analyst.get_monthly_expense_ratio()
    moving_average = analyst.get_moving_average("in")
    trend_slope = analyst.get_trend_slope("in")
    predicted_months = analyst.predict_future_months("in")
    extreme_months = analyst.get_extreme_months()
    classify_months = analyst.classify_months_by_balance()
    compare_months = analyst.compare_months("2025-01", "2025-02")
    income_dependency = analyst.get_income_dependency_ratio()
    cumulative_net_income = analyst.get_cumulative_net_income()

<<<<<<< HEAD
=======
    # Exportación
    export = LedgerExport(resolved_transactions, accounts_list)
    content_xlsx, save_file_xlsx = export.export_excel("xlsx", "test_2.xlsx")
    content_csv, save_file_csv = export.export_excel("csv", "test_2.csv")
    content, save_file_classic = export.export_classic("test_2.ledger")
    content_sql, save_file_sql = export.export_sql("standard", "test_2.sql")

    save_file_classic()
    save_file_xlsx()
    save_file_csv()
    save_file_sql()

>>>>>>> 5439302 (Primer commit)
    # Escritura del archivo Markdown
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"# Reporte de prueba - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Generado por: `{os.path.basename(__file__)}`\n")
        f.write(f"Ruta del archivo: `{os.path.abspath(filePath)}`\n")
        f.write(f"\nArchivo fuente: `{filePath}`\n")
        f.write("\n---\n\n")
        # f.write(f"\nArchivo fuente: `test_2.ledger`\n")

<<<<<<< HEAD
=======
        f.write(f"# Reporte generado el {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

>>>>>>> 5439302 (Primer commit)
        # ---------- LedgerParser ----------
        write_class_header(f, "LedgerParser")

        write_section(
            f,
            "parse()",
            "Convierte las transacciones del archivo ledger a estructura JSON.",
            parser.to_json(transactions_json),
        )
        write_section(
            f,
<<<<<<< HEAD
=======
            "resolve()",
            "Lista de transacciones.",
            parser.to_json(resolved_transactions),
        )
        write_section(
            f,
            "detected_parents_accounts()",
            "Lista de cuentas padres.",
            parser.to_json(parents),
        )
        write_section(
            f,
>>>>>>> 5439302 (Primer commit)
            "parse_accounts()",
            "Lista de cuentas contables detectadas.",
            parser.to_json(accounts_list),
        )
        write_section(
            f,
            "parse_accounts_advance()",
            "Lista de cuentas contables con metadatos detectadas.",
            parser.to_json(accounts_advance),
        )
        write_section(
            f,
            "calculate_balances()",
            "Cálculo de balances por cuenta detallada.",
            parser.to_json(balances),
        )
        write_section(
            f,
            "calculate_balances_by_parents_accounts()",
            "Balance agrupado por cuentas padre.",
            parser.to_json(balances_by_parents),
        )
        write_section(
            f,
            "calculate_status_results()",
            "Estado de resultados (ingresos, gastos, utilidad).",
            parser.to_json(state_results),
        )
        write_section(
            f,
            "calculate_balances_by_details_accounts()",
            "Balance por subcuentas detalladas.",
            parser.to_json(balances_by_details),
        )
        write_section(
            f,
            "get_date_range()",
            "Periodo detectado en las transacciones.",
            f"Desde: `{period[0]}` hasta `{period[1]}`",
            code_block=False,
        )

        write_section(
            f,
            "parse_metadata()",
            "Metadatos del archivo.",
            parser.to_json(metadata),
        )

<<<<<<< HEAD
=======
        write_section(
            f,
            "parse_metadata_yaml()",
            "Metadatos del archivo en formato YAML.",
            parser.to_json(metadata_yaml),
        )

        write_section(
            f,
            "parse_map()",
            "Mapa de cuentas.",
            parser.to_json(map_doc),
        )

        # ---------- LedgerMultiParser ----------
        write_class_header(f, "LedgerMultiParser")

        write_section(
            f,
            "parse_all()",
            "Parsea todos los archivos.",
            parser.to_json(parsers_all),
        )
        write_section(
            f,
            "resolve_all()",
            "Resolve todos los archivos.",
            parser.to_json(resolved_all),
        )

>>>>>>> 5439302 (Primer commit)
        # ---------- LedgerAnalyst ----------
        write_class_header(f, "LedgerAnalyst")

        write_section(
            f,
            "detect_unusual_expenses()",
            "Detecta gastos que exceden significativamente su promedio histórico.",
            parser.to_json(detected_alerts),
        )
        write_section(
            f,
            "get_daily_incomes_expenses()",
            "Muestra ingresos y gastos diarios.",
            parser.to_json(daily),
        )
        write_section(
            f,
            "get_expenses_pie()",
            "Distribución de gastos por cuenta.",
            parser.to_json(pie_expenses),
        )
        write_section(
            f,
            "get_incomes_pie()",
            "Distribución de ingresos por cuenta.",
            parser.to_json(pie_incomes),
        )
        write_section(
            f,
            "get_assets_summary()",
            "Resumen del total de activos.",
            parser.to_json(assets_summary),
        )
        write_section(
            f,
            "get_liabilities_summary()",
            "Resumen del total de pasivos.",
            parser.to_json(liabilities_summary),
        )
        write_section(
            f,
            "get_balance_by_day()",
            "Evolución del balance diario (ingresos - gastos).",
            parser.to_json(balance_by_day),
        )

        write_section(
            f,
            "get_cashflow_by_month()",
            "Flujo de caja mensual (ingresos - gastos).",
            parser.to_json(cashflow_by_month),
        )

        write_section(
            f,
            "get_expense_trends_by_category()",
            "Tendencias de gastos por categoría mensual.",
            parser.to_json(expenses_trends),
        )

        write_section(
            f,
            "get_monthly_incomes_expenses()",
            "Resumen mensual de ingresos y gastos.",
            parser.to_json(analyst.get_monthly_incomes_expenses()),
        )

        write_section(
            f,
            "get_monthly_growth_rates()",
            "Tasa de crecimiento mensual.",
            parser.to_json(monthly_growth_rates),
        )

        write_section(
            f,
            "get_monthly_expense_ratio()",
            "Tasa de gastos mensual.",
            parser.to_json(monthly_expense_ratio),
        )

        write_section(
            f,
            "get_moving_average()",
            "Promedio móvil.",
            parser.to_json(moving_average),
        )

        write_section(
            f,
            "get_trend_slope()",
            "Pendiente de la tendencia.",
            parser.to_json(trend_slope),
        )

        write_section(
            f,
            "predict_future_months()",
            "Predicción de meses futuros.",
            parser.to_json(predicted_months),
        )

        write_section(
            f,
            "get_extreme_months()",
            "Meses extremos.",
            parser.to_json(extreme_months),
        )

        write_section(
            f,
            "classify_months_by_balance()",
            "Clasificación de meses según balance.",
            parser.to_json(classify_months),
        )

        write_section(
            f,
            "compare_months()",
            "Comparación de meses.",
            parser.to_json(compare_months),
        )

        write_section(
            f,
            "get_income_dependency_ratio()",
            "Ratio de dependencia de ingresos.",
            parser.to_json(income_dependency),
        )

        write_section(
            f,
            "get_cumulative_net_income()",
            "Acumulación de ingresos netos.",
            parser.to_json(cumulative_net_income),
        )

        write_section(
            f,
            "get_accounts_used()",
            "Listado de todas las cuentas utilizadas.",
            "\n".join(f"- {acc}" for acc in accounts_used),
            code_block=False,
        )

        # (Puedes agregar aquí secciones para LedgerVisual, LedgerGrafics y LedgerExports si también deseas documentarlas.)

    print(f"\n✅ Reporte generado exitosamente: `{output_path}`\n")
