from ledger_cli import LedgerVisual
from ledger_cli import LedgerParser
import json

if __name__ == "__main__":
    parser = LedgerParser("test/test.ledger")
    visual = LedgerVisual()
    transactions_json = parser.parse()
    print(json.dumps(transactions_json, indent=4, ensure_ascii=False))
    visual.display_journal_table(transactions_json)
    balances = parser.calculate_balances(transactions_json=transactions_json)
    print()
    visual.display_general_balance(balances)
    print(
        parser._create_transaction(
            "2025/01/01",
            "Test",
            [
                {"account": "Activo:Banco", "unit": "USD", "amount": 120.12},
                {"account": "Activo:Banco", "unit": "USD", "amount": 120.12},
                {"account": "Activo:Banco", "unit": "USD", "amount": 120.12},
            ],
            True,
        )
    )
    # print(parser.get_registers_between_dates("2025/01/02", "2025/01/04"))
    # print(parser.get_registers_by_month(2025, 1))
