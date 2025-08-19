from ledger_cli.ledger import LedgerParser
from ledger_cli.ledger_analyst import LedgerAnalyst
from ledger_cli.ledger_export import LedgerExport
from ledger_cli.ledger_multifile import LedgerMultiParser

import json

if __name__ == "__main__":
    pathfile = "test/ledgers/simple-test.ledger"
    
    parser = LedgerParser(pathfile, pathfile)
    
    transactions = parser.parse_transactions()
    transactions_resolve = parser.resolve(transactions=transactions, tax_definitions={"IVA": {"percentage": 0.16, "account": "Assets:Taxes:IVA"}})
    accounts = parser.parse_accounts()
    accounts_advance = parser.parse_accounts_advance()
    metadata = parser.parse_metadata_yaml()
    doc = parser.parse_doc()
    balances = parser.calculate_balances(transactions_json=transactions_resolve, reference=accounts)
    debit_credit = parser.calculate_debit_credit(transactions=transactions_resolve)
    daterange = parser.get_date_range(transactions_json=transactions_resolve)
    status_results = parser.calculate_status_results(balances=balances)
    parser.calculate_general_balance(balances=balances, utility_by_currency=status_results["utility_by_currency"])
    unify = parser.unify_currencies(balances=balances, exchange_rates={
        "USD": 1.0,
        "MXN": 0.01
    }, target_currency="MXN", base_currency="USD")
    
    
    # print("Transactions:")
    # print(json.dumps(transactions, indent=4, ensure_ascii=False))
    # print("\nTransactions Resolved:")
    # print(json.dumps(transactions_resolve, indent=4, ensure_ascii=False))
    # print("\nAccounts:")
    # print(json.dumps(accounts, indent=4, ensure_ascii=False))
    # print("\nAccounts Advance:")
    # print(json.dumps(accounts_advance, indent=4, ensure_ascii=False))
    # print("\nMetadata:")
    # print(json.dumps(metadata, indent=4, ensure_ascii=False))
    # print("\nDoc:")
    # print(json.dumps(doc, indent=4, ensure_ascii=False))
    # print("\nBalances:")
    # print(json.dumps(balances, indent=4, ensure_ascii=False))
    # print("\nDebit/Credit:")
    # print(json.dumps(debit_credit, indent=4, ensure_ascii=False))
    # print("\nDate Range:")
    # print(json.dumps(daterange, indent=4, ensure_ascii=False))
    # print("\nStatus Results:")
    # print(json.dumps(status_results, indent=4, ensure_ascii=False))
    # print("\nGeneral Balance:")
    # print(json.dumps(parser.calculate_general_balance(balances=balances, utility_by_currency=status_results["utility_by_currency"]), indent=4, ensure_ascii=False))
    # print("\nUnify Currencies:")
    # print(json.dumps(unify, indent=4, ensure_ascii=False))
    
    
    # Multiarchivo
    ledger_multi = LedgerMultiParser(files=["test/ledgers/simple-test.ledger", "test/ledgers/test_2.ledger", "test/ledgers/test_3.ledger"])
    result_multifile = ledger_multi.parse_all()
    combined_transactions = result_multifile["ordered_transactions"]
    
    newTransactions = parser.resolve(transactions=combined_transactions, tax_definitions={"IVA": {"percentage": 0.16, "account": "Assets:Taxes:IVA"}})
    newAccounts = result_multifile["accounts_advance"]
    
    # Analisis
    print("\n\nAnalisis:")
    ledger_analyst = LedgerAnalyst(transactions=transactions_resolve, accounts=accounts, income_parents=("Income", "Incoming"), expense_parents=("Expenses", "Expenses"), asset_parents=("Assets", "Assets"), liability_parents=("Liabilities", "Liabilities"))
    
    resume = ledger_analyst.resume()
    print("\nResume:")
    print(json.dumps(resume, indent=4, ensure_ascii=False))
    
    # Export
    
    pathBase = "test/exports/"
    
    ledger_export = LedgerExport(transactions=newTransactions, accounts=newAccounts)
    content_classic, save_classic = ledger_export.export_classic(path=f"{pathBase}test1.ledger")
    content_sql, save_sql = ledger_export.export_sql(path=f"{pathBase}test1.sql")
    content_csv, save_csv = ledger_export.export_excel(type="csv", path=f"{pathBase}test1.csv")
    content_xlsx, save_xlsx = ledger_export.export_excel(type="xlsx", path=f"{pathBase}test1.xlsx")
    
    save_classic()
    save_sql()
    save_csv()
    save_xlsx()