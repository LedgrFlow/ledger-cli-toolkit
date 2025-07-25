from ledger_cli import LedgerVisual
from ledger_cli import LedgerParser
from ledger_cli import LedgerExports
from ledger_cli import LedgerGrafics
from ledger_cli import LedgerAnalyst

if __name__ == "__main__":

    other_parents = {
        "Assets": "Activos",
        "Liabilities": "Pasivos",
        "Equity": "Capital",
        "Income": "Ingresos",
        "Expenses": "Gastos",
    }

    parser = LedgerParser(
        file_path="test/ledgers/test_2.ledger",
        file_accounts_path="test/ledgers/test_2.ledger",
        parents_accounts=other_parents,
    )
    visual = LedgerVisual()
    grafics = LedgerGrafics()
    exports = LedgerExports("test")

    transactions_json = parser.parse()
    accounts_list = parser.parse_accounts()
    
    
    # print("Transacciones JSON:")
    # print(transactions_json)
    # print(parser.to_json(transactions_json))
    # print("Lista de cuentas contables:")
    # print(accounts_list)
    # print(parser.to_json(accounts_list))
    
    analyst = LedgerAnalyst(
        transactions=transactions_json,
        accounts=accounts_list,
        income_parents=("Ingresos", "Income"),
        expense_parents=("Gastos", "Expenses"),
        asset_parents=("Activos", "Assets"),
        liability_parents=("Pasivos", "Liabilities"),
    )
    
    daily = analyst.get_daily_incomes_expenses()
    pie_expenses = analyst.get_expenses_pie()
    pie_incomes = analyst.get_incomes_pie()
    assets_summary = analyst.get_assets_summary()
    liabilities_summary = analyst.get_liabilities_summary()
    balance_by_day = analyst.get_balance_by_day()
    accounts_used = analyst.get_accounts_used()
    detected_alerts = analyst.detect_unusual_expenses(threshold=1.5)
    
    
    print("Alertas de gastos inusuales:")
    print(parser.to_json(detected_alerts))

    print("Datos diarios de ingresos y gastos: ", parser.to_json(daily))
    print("Gráfica de pastel de gastos: ", parser.to_json(pie_expenses))
    print("Gráfica de pastel de ingresos: ", parser.to_json(pie_incomes))
    print("Resumen de activos: ", parser.to_json(assets_summary))
    print("Resumen de pasivos: ", parser.to_json(liabilities_summary))
    print("Balance por día: ", parser.to_json(balance_by_day))
    print("Cuentas utilizadas: ", accounts_used)
    
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
    # print(balances)
    # print(balances_by_parents)
    # print(parser.to_json(transactions_json))
    # print(parser.to_json(state_results))
    # print("Balance General")
    # visual.display_general_balance(balances)
    # print("Libro diario")
    # visual.display_journal_table(transactions_json, style="pipe")
    # print("Lista de cuentas contables")
    # visual.display_accounts_list(accounts_list, style="github")
    # print("Balance por detalles")
    # visual.display_details_balances(balances_by_details, style="github")
    # print("Balance por cuentas padre")
    # visual.display_parents_balances(
    #     balances_by_parents=balances_by_parents, style="github"
    # )

    # grafics.create_balance_chart(balances, f"({period[0]} - {period[1]})")
    # grafics.create_balance_pie_chart(balances, f"({period[0]} - {period[1]})")
    # grafics.show_chart()
    # exports.export_to_csv(transactions_json, balances, accounts_list)
    # exports.export_to_markdown(transactions_json, balances, accounts_list)
    # exports.export_to_pdf(transactions_json, balances, accounts_list)
