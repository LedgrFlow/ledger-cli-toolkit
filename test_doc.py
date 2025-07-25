import os
from datetime import datetime
from ledger_cli import (
    LedgerVisual,
    LedgerParser,
    LedgerExports,
    LedgerGrafics,
    LedgerAnalyst,
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
    filePath = "test/ledgers/test_3.ledger"
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
        file_path=filePath,
        file_accounts_path=filePath,
        parents_accounts=other_parents,
    )
    visual = LedgerVisual()
    grafics = LedgerGrafics()
    exports = LedgerExports("test")

    transactions_json = parser.parse()
    accounts_list = parser.parse_accounts()

    analyst = LedgerAnalyst(
        transactions=transactions_json,
        accounts=accounts_list,
        income_parents=("Ingresos", "Income"),
        expense_parents=("Gastos", "Expenses"),
        asset_parents=("Activos", "Assets"),
        liability_parents=("Pasivos", "Liabilities"),
    )

    # Cálculos analyst
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

    # Escritura del archivo Markdown
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"# Reporte de prueba - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Generado por: `{os.path.basename(__file__)}`\n")
        f.write(f"Ruta del archivo: `{os.path.abspath(filePath)}`\n")
        f.write(f"\nArchivo fuente: `{filePath}`\n")
        f.write("\n---\n\n")
        # f.write(f"\nArchivo fuente: `test_2.ledger`\n")

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
            "parse_accounts()",
            "Lista de cuentas contables detectadas.",
            parser.to_json(accounts_list),
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
            "get_accounts_used()",
            "Listado de todas las cuentas utilizadas.",
            "\n".join(f"- {acc}" for acc in accounts_used),
            code_block=False,
        )

        # (Puedes agregar aquí secciones para LedgerVisual, LedgerGrafics y LedgerExports si también deseas documentarlas.)

    print(f"\n✅ Reporte generado exitosamente: `{output_path}`\n")
