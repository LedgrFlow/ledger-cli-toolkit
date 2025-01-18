from ledger_cli import LedgerVisual
from ledger_cli import LedgerParser
from ledger_cli import LedgerExports
from ledger_cli import LedgerGrafics

if __name__ == "__main__":

    other_parents = {
        "Assets": "Activos",
        "Liabilities": "Pasivos",
        "Equity": "Capital",
        "Income": "Ingresos",
        "Expenses": "Gastos",
    }

    parser = LedgerParser(
        file_path="test/ledgers/test_3.ledger",
        file_accounts_path="test/ledgers/test_3.ledger",
        parents_accounts=other_parents,
    )
    visual = LedgerVisual()
    grafics = LedgerGrafics()
    exports = LedgerExports("test")

    transactions_json = parser.parse()
    accounts_list = parser.parse_accounts()
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
    print("Balance General")
    visual.display_general_balance(balances)
    print("Libro diario")
    visual.display_journal_table(transactions_json, style="pipe")
    print("Lista de cuentas contables")
    visual.display_accounts_list(accounts_list, style="github")
    print("Balance por detalles")
    visual.display_details_balances(balances_by_details, style="github")
    print("Balance por cuentas padre")
    visual.display_parents_balances(
        balances_by_parents=balances_by_parents, style="github"
    )

    # grafics.create_balance_chart(balances, f"({period[0]} - {period[1]})")
    # grafics.create_balance_pie_chart(balances, f"({period[0]} - {period[1]})")
    # grafics.show_chart()
    # exports.export_to_csv(transactions_json, balances, accounts_list)
    # exports.export_to_markdown(transactions_json, balances, accounts_list)
    # exports.export_to_pdf(transactions_json, balances, accounts_list)

    # print(transactions_json)
    # print(accounts_list)
    # print(json.dumps(transactions_json, indent=4, ensure_ascii=False))
    # visual.display_journal_table(transactions_json)
    # balances = parser.calculate_balances(transactions_json=transactions_json)
    # print()
    # visual.display_general_balance(balances)
    # print(
    #     parser._create_transaction(
    #         "2025/01/01",
    #         "Test",
    #         [
    #             {"account": "Activo:Banco", "unit": "USD", "amount": 120.12},
    #             {"account": "Activo:Banco", "unit": "USD", "amount": 120.12},
    #             {"account": "Activo:Banco", "unit": "USD", "amount": 120.12},
    #         ],
    #         True,
    #     )
    # )
    # print(parser.get_registers_between_dates("2025/01/02", "2025/01/04"))
    # print(parser.get_registers_by_month(2025, 1))
