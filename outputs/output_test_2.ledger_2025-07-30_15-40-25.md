---
# Reporte de prueba - 2025-07-30 15:40:25
Generado por: `test_doc.py`
Ruta del archivo: `/home/eddybel/Documentos/dev/personales/LedgerApp/ledger-cli-toolkit/test/ledgers/test_2.ledger`

Archivo fuente: `test/ledgers/test_2.ledger`

---


# Clase: `LedgerParser`


## parse()

Convierte las transacciones del archivo ledger a estructura JSON.

```json
[
    {
        "date": "2025-01-01",
        "time": null,
        "verified": true,
        "description": "Opening Balances",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 10000.0
            },
            {
                "account": "Assets:Bank:Savings",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Savings"
                ],
                "unit": "$",
                "amount": 25000.0
            },
            {
                "account": "Assets:Cash",
                "subAccounts": [
                    "Assets",
                    "Cash"
                ],
                "unit": "$",
                "amount": 1000.0
            },
            {
                "account": "Assets:Investments:Stocks",
                "subAccounts": [
                    "Assets",
                    "Investments",
                    "Stocks"
                ],
                "unit": "$",
                "amount": 15000.0
            },
            {
                "account": "Liabilities:CreditCard:Visa",
                "subAccounts": [
                    "Liabilities",
                    "CreditCard",
                    "Visa"
                ],
                "unit": "$",
                "amount": -2500.0
            },
            {
                "account": "Liabilities:Loan:CarLoan",
                "subAccounts": [
                    "Liabilities",
                    "Loan",
                    "CarLoan"
                ],
                "unit": "$",
                "amount": -10000.0
            },
            {
                "account": "Equity:OpeningBalances",
                "subAccounts": [
                    "Equity",
                    "OpeningBalances"
                ],
                "unit": "$",
                "amount": -38500.0
            }
        ]
    },
    {
        "date": "2025-01-15",
        "time": null,
        "verified": true,
        "description": "Paycheck",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 7500.0
            },
            {
                "account": "Income:Salary",
                "subAccounts": [
                    "Income",
                    "Salary"
                ],
                "unit": "$",
                "amount": -7500.0
            }
        ]
    },
    {
        "date": "2025-01-20",
        "time": null,
        "verified": true,
        "description": "Grocery Shopping",
        "accounts": [
            {
                "account": "Expenses:Food:Groceries",
                "subAccounts": [
                    "Expenses",
                    "Food",
                    "Groceries"
                ],
                "unit": "$",
                "amount": 250.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -250.0
            }
        ]
    },
    {
        "date": "2025-01-22",
        "time": null,
        "verified": true,
        "description": "Rent Payment",
        "accounts": [
            {
                "account": "Expenses:Rent",
                "subAccounts": [
                    "Expenses",
                    "Rent"
                ],
                "unit": "$",
                "amount": 1500.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -1500.0
            }
        ]
    },
    {
        "date": "2025-01-23",
        "time": null,
        "verified": true,
        "description": "Dinner Out",
        "accounts": [
            {
                "account": "Expenses:Food:DiningOut",
                "subAccounts": [
                    "Expenses",
                    "Food",
                    "DiningOut"
                ],
                "unit": "$",
                "amount": 75.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -75.0
            }
        ]
    },
    {
        "date": "2025-01-25",
        "time": null,
        "verified": true,
        "description": "Credit Card Payment",
        "accounts": [
            {
                "account": "Liabilities:CreditCard:Visa",
                "subAccounts": [
                    "Liabilities",
                    "CreditCard",
                    "Visa"
                ],
                "unit": "$",
                "amount": 1200.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -1200.0
            }
        ]
    },
    {
        "date": "2025-02-01",
        "time": null,
        "verified": true,
        "description": "Paycheck",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 7500.0
            },
            {
                "account": "Income:Salary",
                "subAccounts": [
                    "Income",
                    "Salary"
                ],
                "unit": "$",
                "amount": -7500.0
            }
        ]
    },
    {
        "date": "2025-02-03",
        "time": null,
        "verified": true,
        "description": "Utilities Bill",
        "accounts": [
            {
                "account": "Expenses:Utilities",
                "subAccounts": [
                    "Expenses",
                    "Utilities"
                ],
                "unit": "$",
                "amount": 300.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -300.0
            }
        ]
    },
    {
        "date": "2025-02-10",
        "time": null,
        "verified": true,
        "description": "Gasoline",
        "accounts": [
            {
                "account": "Expenses:Transportation:Gas",
                "subAccounts": [
                    "Expenses",
                    "Transportation",
                    "Gas"
                ],
                "unit": "$",
                "amount": 120.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -120.0
            }
        ]
    },
    {
        "date": "2025-02-15",
        "time": null,
        "verified": true,
        "description": "Freelance Project",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 3200.0
            },
            {
                "account": "Income:Freelance",
                "subAccounts": [
                    "Income",
                    "Freelance"
                ],
                "unit": "$",
                "amount": -3200.0
            }
        ]
    },
    {
        "date": "2025-02-20",
        "time": null,
        "verified": true,
        "description": "Car Loan Payment",
        "accounts": [
            {
                "account": "Liabilities:Loan:CarLoan",
                "subAccounts": [
                    "Liabilities",
                    "Loan",
                    "CarLoan"
                ],
                "unit": "$",
                "amount": 500.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -500.0
            }
        ]
    },
    {
        "date": "2025-02-22",
        "time": null,
        "verified": true,
        "description": "Stock Dividend",
        "accounts": [
            {
                "account": "Assets:Bank:Savings",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Savings"
                ],
                "unit": "$",
                "amount": 1000.0
            },
            {
                "account": "Income:Investments:Dividends",
                "subAccounts": [
                    "Income",
                    "Investments",
                    "Dividends"
                ],
                "unit": "$",
                "amount": -1000.0
            }
        ]
    },
    {
        "date": "2025-02-28",
        "time": null,
        "verified": true,
        "description": "Vacation Trip",
        "accounts": [
            {
                "account": "Expenses:Travel",
                "subAccounts": [
                    "Expenses",
                    "Travel"
                ],
                "unit": "$",
                "amount": 2800.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -2800.0
            }
        ]
    },
    {
        "date": "2025-03-01",
        "time": null,
        "verified": true,
        "description": "Paycheck",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 7500.0
            },
            {
                "account": "Income:Salary",
                "subAccounts": [
                    "Income",
                    "Salary"
                ],
                "unit": "$",
                "amount": -7500.0
            }
        ]
    },
    {
        "date": "2025-03-02",
        "time": null,
        "verified": true,
        "description": "Health Insurance",
        "accounts": [
            {
                "account": "Expenses:Insurance:Health",
                "subAccounts": [
                    "Expenses",
                    "Insurance",
                    "Health"
                ],
                "unit": "$",
                "amount": 450.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -450.0
            }
        ]
    },
    {
        "date": "2025-03-10",
        "time": null,
        "verified": true,
        "description": "Maintenance: Oil Change",
        "accounts": [
            {
                "account": "Expenses:Transportation:Maintenance",
                "subAccounts": [
                    "Expenses",
                    "Transportation",
                    "Maintenance"
                ],
                "unit": "$",
                "amount": 90.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -90.0
            }
        ]
    },
    {
        "date": "2025-03-15",
        "time": null,
        "verified": true,
        "description": "Monthly Rent",
        "accounts": [
            {
                "account": "Expenses:Rent",
                "subAccounts": [
                    "Expenses",
                    "Rent"
                ],
                "unit": "$",
                "amount": 1500.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -1500.0
            }
        ]
    },
    {
        "date": "2025-03-18",
        "time": null,
        "verified": true,
        "description": "Course Subscription",
        "accounts": [
            {
                "account": "Expenses:Education",
                "subAccounts": [
                    "Expenses",
                    "Education"
                ],
                "unit": "$",
                "amount": 300.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -300.0
            }
        ]
    },
    {
        "date": "2025-03-25",
        "time": null,
        "verified": true,
        "description": "Entertainment - Concert",
        "accounts": [
            {
                "account": "Expenses:Entertainment",
                "subAccounts": [
                    "Expenses",
                    "Entertainment"
                ],
                "unit": "$",
                "amount": 200.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -200.0
            }
        ]
    },
    {
        "date": "2025-04-01",
        "time": null,
        "verified": true,
        "description": "Paycheck",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 7500.0
            },
            {
                "account": "Income:Salary",
                "subAccounts": [
                    "Income",
                    "Salary"
                ],
                "unit": "$",
                "amount": -7500.0
            }
        ]
    },
    {
        "date": "2025-04-02",
        "time": null,
        "verified": true,
        "description": "Dentist Appointment",
        "accounts": [
            {
                "account": "Expenses:Medical",
                "subAccounts": [
                    "Expenses",
                    "Medical"
                ],
                "unit": "$",
                "amount": 1200.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -1200.0
            }
        ]
    },
    {
        "date": "2025-04-10",
        "time": null,
        "verified": true,
        "description": "Gasoline",
        "accounts": [
            {
                "account": "Expenses:Transportation:Gas",
                "subAccounts": [
                    "Expenses",
                    "Transportation",
                    "Gas"
                ],
                "unit": "$",
                "amount": 130.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -130.0
            }
        ]
    },
    {
        "date": "2025-04-15",
        "time": null,
        "verified": true,
        "description": "Monthly Rent",
        "accounts": [
            {
                "account": "Expenses:Rent",
                "subAccounts": [
                    "Expenses",
                    "Rent"
                ],
                "unit": "$",
                "amount": 1500.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -1500.0
            }
        ]
    },
    {
        "date": "2025-04-20",
        "time": null,
        "verified": true,
        "description": "Shopping - Electronics",
        "accounts": [
            {
                "account": "Expenses:Shopping",
                "subAccounts": [
                    "Expenses",
                    "Shopping"
                ],
                "unit": "$",
                "amount": 3000.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -3000.0
            }
        ]
    },
    {
        "date": "2025-04-25",
        "time": null,
        "verified": true,
        "description": "Dinner Out",
        "accounts": [
            {
                "account": "Expenses:Food:DiningOut",
                "subAccounts": [
                    "Expenses",
                    "Food",
                    "DiningOut"
                ],
                "unit": "$",
                "amount": 100.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -100.0
            }
        ]
    },
    {
        "date": "2025-05-01",
        "time": null,
        "verified": true,
        "description": "Paycheck",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 7500.0
            },
            {
                "account": "Income:Salary",
                "subAccounts": [
                    "Income",
                    "Salary"
                ],
                "unit": "$",
                "amount": -7500.0
            }
        ]
    },
    {
        "date": "2025-05-03",
        "time": null,
        "verified": true,
        "description": "Utilities",
        "accounts": [
            {
                "account": "Expenses:Utilities",
                "subAccounts": [
                    "Expenses",
                    "Utilities"
                ],
                "unit": "$",
                "amount": 310.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -310.0
            }
        ]
    },
    {
        "date": "2025-05-06",
        "time": null,
        "verified": true,
        "description": "Travel - Family Emergency",
        "accounts": [
            {
                "account": "Expenses:Travel",
                "subAccounts": [
                    "Expenses",
                    "Travel"
                ],
                "unit": "$",
                "amount": 5800.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -5800.0
            }
        ]
    },
    {
        "date": "2025-05-10",
        "time": null,
        "verified": true,
        "description": "Grocery Shopping",
        "accounts": [
            {
                "account": "Expenses:Food:Groceries",
                "subAccounts": [
                    "Expenses",
                    "Food",
                    "Groceries"
                ],
                "unit": "$",
                "amount": 270.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -270.0
            }
        ]
    },
    {
        "date": "2025-05-15",
        "time": null,
        "verified": true,
        "description": "Monthly Rent",
        "accounts": [
            {
                "account": "Expenses:Rent",
                "subAccounts": [
                    "Expenses",
                    "Rent"
                ],
                "unit": "$",
                "amount": 1500.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -1500.0
            }
        ]
    },
    {
        "date": "2025-05-25",
        "time": null,
        "verified": true,
        "description": "Car Repair (transmission)",
        "accounts": [
            {
                "account": "Expenses:Transportation:Maintenance",
                "subAccounts": [
                    "Expenses",
                    "Transportation",
                    "Maintenance"
                ],
                "unit": "$",
                "amount": 2200.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -2200.0
            }
        ]
    },
    {
        "date": "2025-06-01",
        "time": null,
        "verified": true,
        "description": "Paycheck",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 7500.0
            },
            {
                "account": "Income:Salary",
                "subAccounts": [
                    "Income",
                    "Salary"
                ],
                "unit": "$",
                "amount": -7500.0
            }
        ]
    },
    {
        "date": "2025-06-03",
        "time": null,
        "verified": true,
        "description": "Health Insurance",
        "accounts": [
            {
                "account": "Expenses:Insurance:Health",
                "subAccounts": [
                    "Expenses",
                    "Insurance",
                    "Health"
                ],
                "unit": "$",
                "amount": 450.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -450.0
            }
        ]
    },
    {
        "date": "2025-06-10",
        "time": null,
        "verified": true,
        "description": "Freelance Payment",
        "accounts": [
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": 4500.0
            },
            {
                "account": "Income:Freelance",
                "subAccounts": [
                    "Income",
                    "Freelance"
                ],
                "unit": "$",
                "amount": -4500.0
            }
        ]
    },
    {
        "date": "2025-06-15",
        "time": null,
        "verified": true,
        "description": "Monthly Rent",
        "accounts": [
            {
                "account": "Expenses:Rent",
                "subAccounts": [
                    "Expenses",
                    "Rent"
                ],
                "unit": "$",
                "amount": 1500.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -1500.0
            }
        ]
    },
    {
        "date": "2025-06-20",
        "time": null,
        "verified": true,
        "description": "Luxury Watch Purchase",
        "accounts": [
            {
                "account": "Expenses:Shopping",
                "subAccounts": [
                    "Expenses",
                    "Shopping"
                ],
                "unit": "$",
                "amount": 6500.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -6500.0
            }
        ]
    },
    {
        "date": "2025-06-30",
        "time": null,
        "verified": true,
        "description": "Entertainment - Festival",
        "accounts": [
            {
                "account": "Expenses:Entertainment",
                "subAccounts": [
                    "Expenses",
                    "Entertainment"
                ],
                "unit": "$",
                "amount": 350.0
            },
            {
                "account": "Assets:Bank:Checking",
                "subAccounts": [
                    "Assets",
                    "Bank",
                    "Checking"
                ],
                "unit": "$",
                "amount": -350.0
            }
        ]
    }
]
```

## parse_accounts()

Lista de cuentas contables detectadas.

```json
[
    "Assets:Bank:Checking",
    "Assets:Bank:Savings",
    "Assets:Cash",
    "Assets:Investments:Stocks",
    "Assets:AccountsReceivable",
    "Liabilities:CreditCard:Visa",
    "Liabilities:Loan:CarLoan",
    "Equity:OpeningBalances",
    "Equity:Owner",
    "Income:Salary",
    "Income:Investments:Dividends",
    "Income:Freelance",
    "Expenses:Rent",
    "Expenses:Utilities",
    "Expenses:Food:Groceries",
    "Expenses:Food:DiningOut",
    "Expenses:Transportation:Gas",
    "Expenses:Transportation:Maintenance",
    "Expenses:Entertainment",
    "Expenses:Travel",
    "Expenses:Insurance:Car",
    "Expenses:Insurance:Health",
    "Expenses:Education",
    "Expenses:Medical",
    "Expenses:Shopping"
]
```

## parse_accounts_advance()

Lista de cuentas contables con metadatos detectadas.

```json
[
    {
        "account": "Assets:Bank:Checking",
        "description": "Cuenta bancaria principal para operaciones diarias",
        "category": "Activo Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Assets:Bank:Savings",
        "description": "Cuenta bancaria para ahorros",
        "category": "Activo Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Assets:Cash",
        "description": "Cuenta bancaria para depósitos y pagos automáticos",
        "category": "Activo Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Assets:Investments:Stocks",
        "description": "Cuenta bancaria para inversiones",
        "category": "Activo Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Assets:AccountsReceivable",
        "description": "Cuenta bancaria para ingresos y gastos de la empresa",
        "category": "Activo Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Liabilities:CreditCard:Visa",
        "description": "Cuenta bancaria para pagos de crédito",
        "category": "Pasivo Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Liabilities:Loan:CarLoan",
        "description": "Cuenta bancaria para préstamos de automóvil",
        "category": "Pasivo Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Equity:OpeningBalances",
        "description": "Saldo inicial de la empresa",
        "category": "Capital Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Equity:Owner",
        "description": "Capital de la empresa",
        "category": "Capital Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Income:Salary",
        "description": "Ingresos salariales",
        "category": "Ingreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Income:Investments:Dividends",
        "description": "Ingresos de dividendos",
        "category": "Ingreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Income:Freelance",
        "description": "Ingresos de trabajo por hora",
        "category": "Ingreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Rent",
        "description": "Egresos de alquiler",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Utilities",
        "description": "Egresos de utilidades",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Food:Groceries",
        "description": "Egresos de comida",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Food:DiningOut",
        "description": "Egresos de comida rápida",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Transportation:Gas",
        "description": "Egresos de gasolina",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Transportation:Maintenance",
        "description": "Egresos de mantenimiento de vehículos",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Entertainment",
        "description": "Egresos de entretenimiento",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Travel",
        "description": "Egresos de viaje",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Insurance:Car",
        "description": "Egresos de seguros de automóvil",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Insurance:Health",
        "description": "Egresos de seguros de salud",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Education",
        "description": "Egresos de educación",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Medical",
        "description": "Egresos médicos",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    },
    {
        "account": "Expenses:Shopping",
        "description": "Egresos de compras",
        "category": "Egreso Corriente",
        "created": "2023-01-15"
    }
]
```

## calculate_balances()

Cálculo de balances por cuenta detallada.

```json
{
    "Assets:Bank:Checking": {
        "$": 28605.0
    },
    "Assets:Bank:Savings": {
        "$": 26000.0
    },
    "Assets:Cash": {
        "$": 1000.0
    },
    "Assets:Investments:Stocks": {
        "$": 15000.0
    },
    "Liabilities:CreditCard:Visa": {
        "$": -1300.0
    },
    "Liabilities:Loan:CarLoan": {
        "$": -9500.0
    },
    "Equity:OpeningBalances": {
        "$": -38500.0
    },
    "Income:Salary": {
        "$": -45000.0
    },
    "Income:Investments:Dividends": {
        "$": -1000.0
    },
    "Income:Freelance": {
        "$": -7700.0
    },
    "Expenses:Rent": {
        "$": 7500.0
    },
    "Expenses:Utilities": {
        "$": 610.0
    },
    "Expenses:Food:Groceries": {
        "$": 520.0
    },
    "Expenses:Food:DiningOut": {
        "$": 175.0
    },
    "Expenses:Transportation:Gas": {
        "$": 250.0
    },
    "Expenses:Transportation:Maintenance": {
        "$": 2290.0
    },
    "Expenses:Entertainment": {
        "$": 550.0
    },
    "Expenses:Travel": {
        "$": 8600.0
    },
    "Expenses:Insurance:Health": {
        "$": 900.0
    },
    "Expenses:Education": {
        "$": 300.0
    },
    "Expenses:Medical": {
        "$": 1200.0
    },
    "Expenses:Shopping": {
        "$": 9500.0
    }
}
```

## calculate_balances_by_parents_accounts()

Balance agrupado por cuentas padre.

```json
{
    "Assets": {
        "N/A": 0.0
    },
    "Liabilities": {
        "N/A": 0.0
    },
    "Equity": {
        "N/A": 0.0
    },
    "Income": {
        "N/A": 0.0
    },
    "Expenses": {
        "N/A": 0.0
    }
}
```

## calculate_status_results()

Estado de resultados (ingresos, gastos, utilidad).

```json
{
    "total_income_by_currency": {},
    "total_expenses_by_currency": {},
    "utility_by_currency": {},
    "income_details": [],
    "expenses_details": []
}
```

## calculate_balances_by_details_accounts()

Balance por subcuentas detalladas.

```json
{
    "Assets": {
        "balances": {
            "$": 70605.0
        },
        "sub_accounts": {
            "Bank": {
                "balances": {
                    "$": 54605.0
                },
                "sub_accounts": {
                    "Checking": {
                        "balances": {
                            "$": 28605.0
                        },
                        "sub_accounts": {}
                    },
                    "Savings": {
                        "balances": {
                            "$": 26000.0
                        },
                        "sub_accounts": {}
                    }
                }
            },
            "Cash": {
                "balances": {
                    "$": 1000.0
                },
                "sub_accounts": {}
            },
            "Investments": {
                "balances": {
                    "$": 15000.0
                },
                "sub_accounts": {
                    "Stocks": {
                        "balances": {
                            "$": 15000.0
                        },
                        "sub_accounts": {}
                    }
                }
            }
        }
    },
    "Liabilities": {
        "balances": {
            "$": -10800.0
        },
        "sub_accounts": {
            "CreditCard": {
                "balances": {
                    "$": -1300.0
                },
                "sub_accounts": {
                    "Visa": {
                        "balances": {
                            "$": -1300.0
                        },
                        "sub_accounts": {}
                    }
                }
            },
            "Loan": {
                "balances": {
                    "$": -9500.0
                },
                "sub_accounts": {
                    "CarLoan": {
                        "balances": {
                            "$": -9500.0
                        },
                        "sub_accounts": {}
                    }
                }
            }
        }
    },
    "Equity": {
        "balances": {
            "$": -38500.0
        },
        "sub_accounts": {
            "OpeningBalances": {
                "balances": {
                    "$": -38500.0
                },
                "sub_accounts": {}
            }
        }
    },
    "Income": {
        "balances": {
            "$": -53700.0
        },
        "sub_accounts": {
            "Salary": {
                "balances": {
                    "$": -45000.0
                },
                "sub_accounts": {}
            },
            "Freelance": {
                "balances": {
                    "$": -7700.0
                },
                "sub_accounts": {}
            },
            "Investments": {
                "balances": {
                    "$": -1000.0
                },
                "sub_accounts": {
                    "Dividends": {
                        "balances": {
                            "$": -1000.0
                        },
                        "sub_accounts": {}
                    }
                }
            }
        }
    },
    "Expenses": {
        "balances": {
            "$": 32395.0
        },
        "sub_accounts": {
            "Food": {
                "balances": {
                    "$": 695.0
                },
                "sub_accounts": {
                    "Groceries": {
                        "balances": {
                            "$": 520.0
                        },
                        "sub_accounts": {}
                    },
                    "DiningOut": {
                        "balances": {
                            "$": 175.0
                        },
                        "sub_accounts": {}
                    }
                }
            },
            "Rent": {
                "balances": {
                    "$": 7500.0
                },
                "sub_accounts": {}
            },
            "Utilities": {
                "balances": {
                    "$": 610.0
                },
                "sub_accounts": {}
            },
            "Transportation": {
                "balances": {
                    "$": 2540.0
                },
                "sub_accounts": {
                    "Gas": {
                        "balances": {
                            "$": 250.0
                        },
                        "sub_accounts": {}
                    },
                    "Maintenance": {
                        "balances": {
                            "$": 2290.0
                        },
                        "sub_accounts": {}
                    }
                }
            },
            "Travel": {
                "balances": {
                    "$": 8600.0
                },
                "sub_accounts": {}
            },
            "Insurance": {
                "balances": {
                    "$": 900.0
                },
                "sub_accounts": {
                    "Health": {
                        "balances": {
                            "$": 900.0
                        },
                        "sub_accounts": {}
                    }
                }
            },
            "Education": {
                "balances": {
                    "$": 300.0
                },
                "sub_accounts": {}
            },
            "Entertainment": {
                "balances": {
                    "$": 550.0
                },
                "sub_accounts": {}
            },
            "Medical": {
                "balances": {
                    "$": 1200.0
                },
                "sub_accounts": {}
            },
            "Shopping": {
                "balances": {
                    "$": 9500.0
                },
                "sub_accounts": {}
            }
        }
    }
}
```

## get_date_range()

Periodo detectado en las transacciones.

Desde: `2025/01/01` hasta `2025/06/30`

## parse_metadata()

Metadatos del archivo.

```json
{
    "currency": "values = MXN, USD, EUR",
    "snippet": {
        "gasolina": "value = $DATE * Gasolina\n    Expenses:Transport  $monto\n    Assets:Cash",
        "sueldo": "value = $DATE * Sueldo\n  Assets:Bank:Checking  $monto\n  Income:Salary"
    }
}
```

# Clase: `LedgerAnalyst`


## detect_unusual_expenses()

Detecta gastos que exceden significativamente su promedio histórico.

```json
[
    {
        "account": "Expenses:Transportation:Maintenance",
        "month": "2025-05",
        "amount": 2200.0,
        "average": 1145.0,
        "alert": "Gasto inusualmente alto"
    }
]
```

## get_daily_incomes_expenses()

Muestra ingresos y gastos diarios.

```json
[
    {
        "date": "2025-01-15",
        "incoming": 7500.0,
        "expenses": 0.0
    },
    {
        "date": "2025-01-20",
        "incoming": 0.0,
        "expenses": 250.0
    },
    {
        "date": "2025-01-22",
        "incoming": 0.0,
        "expenses": 1500.0
    },
    {
        "date": "2025-01-23",
        "incoming": 0.0,
        "expenses": 75.0
    },
    {
        "date": "2025-02-01",
        "incoming": 7500.0,
        "expenses": 0.0
    },
    {
        "date": "2025-02-03",
        "incoming": 0.0,
        "expenses": 300.0
    },
    {
        "date": "2025-02-10",
        "incoming": 0.0,
        "expenses": 120.0
    },
    {
        "date": "2025-02-15",
        "incoming": 3200.0,
        "expenses": 0.0
    },
    {
        "date": "2025-02-22",
        "incoming": 1000.0,
        "expenses": 0.0
    },
    {
        "date": "2025-02-28",
        "incoming": 0.0,
        "expenses": 2800.0
    },
    {
        "date": "2025-03-01",
        "incoming": 7500.0,
        "expenses": 0.0
    },
    {
        "date": "2025-03-02",
        "incoming": 0.0,
        "expenses": 450.0
    },
    {
        "date": "2025-03-10",
        "incoming": 0.0,
        "expenses": 90.0
    },
    {
        "date": "2025-03-15",
        "incoming": 0.0,
        "expenses": 1500.0
    },
    {
        "date": "2025-03-18",
        "incoming": 0.0,
        "expenses": 300.0
    },
    {
        "date": "2025-03-25",
        "incoming": 0.0,
        "expenses": 200.0
    },
    {
        "date": "2025-04-01",
        "incoming": 7500.0,
        "expenses": 0.0
    },
    {
        "date": "2025-04-02",
        "incoming": 0.0,
        "expenses": 1200.0
    },
    {
        "date": "2025-04-10",
        "incoming": 0.0,
        "expenses": 130.0
    },
    {
        "date": "2025-04-15",
        "incoming": 0.0,
        "expenses": 1500.0
    },
    {
        "date": "2025-04-20",
        "incoming": 0.0,
        "expenses": 3000.0
    },
    {
        "date": "2025-04-25",
        "incoming": 0.0,
        "expenses": 100.0
    },
    {
        "date": "2025-05-01",
        "incoming": 7500.0,
        "expenses": 0.0
    },
    {
        "date": "2025-05-03",
        "incoming": 0.0,
        "expenses": 310.0
    },
    {
        "date": "2025-05-06",
        "incoming": 0.0,
        "expenses": 5800.0
    },
    {
        "date": "2025-05-10",
        "incoming": 0.0,
        "expenses": 270.0
    },
    {
        "date": "2025-05-15",
        "incoming": 0.0,
        "expenses": 1500.0
    },
    {
        "date": "2025-05-25",
        "incoming": 0.0,
        "expenses": 2200.0
    },
    {
        "date": "2025-06-01",
        "incoming": 7500.0,
        "expenses": 0.0
    },
    {
        "date": "2025-06-03",
        "incoming": 0.0,
        "expenses": 450.0
    },
    {
        "date": "2025-06-10",
        "incoming": 4500.0,
        "expenses": 0.0
    },
    {
        "date": "2025-06-15",
        "incoming": 0.0,
        "expenses": 1500.0
    },
    {
        "date": "2025-06-20",
        "incoming": 0.0,
        "expenses": 6500.0
    },
    {
        "date": "2025-06-30",
        "incoming": 0.0,
        "expenses": 350.0
    }
]
```

## get_expenses_pie()

Distribución de gastos por cuenta.

```json
[
    {
        "account": "Expenses:Food:Groceries",
        "amount": 520.0
    },
    {
        "account": "Expenses:Rent",
        "amount": 7500.0
    },
    {
        "account": "Expenses:Food:DiningOut",
        "amount": 175.0
    },
    {
        "account": "Expenses:Utilities",
        "amount": 610.0
    },
    {
        "account": "Expenses:Transportation:Gas",
        "amount": 250.0
    },
    {
        "account": "Expenses:Travel",
        "amount": 8600.0
    },
    {
        "account": "Expenses:Insurance:Health",
        "amount": 900.0
    },
    {
        "account": "Expenses:Transportation:Maintenance",
        "amount": 2290.0
    },
    {
        "account": "Expenses:Education",
        "amount": 300.0
    },
    {
        "account": "Expenses:Entertainment",
        "amount": 550.0
    },
    {
        "account": "Expenses:Medical",
        "amount": 1200.0
    },
    {
        "account": "Expenses:Shopping",
        "amount": 9500.0
    }
]
```

## get_incomes_pie()

Distribución de ingresos por cuenta.

```json
[
    {
        "account": "Income:Salary",
        "amount": 45000.0
    },
    {
        "account": "Income:Freelance",
        "amount": 7700.0
    },
    {
        "account": "Income:Investments:Dividends",
        "amount": 1000.0
    }
]
```

## get_assets_summary()

Resumen del total de activos.

```json
[
    {
        "account": "Assets:Bank:Checking",
        "amount": 96795.0
    },
    {
        "account": "Assets:Bank:Savings",
        "amount": 26000.0
    },
    {
        "account": "Assets:Cash",
        "amount": 1000.0
    },
    {
        "account": "Assets:Investments:Stocks",
        "amount": 15000.0
    }
]
```

## get_liabilities_summary()

Resumen del total de pasivos.

```json
[
    {
        "account": "Liabilities:CreditCard:Visa",
        "amount": 3700.0
    },
    {
        "account": "Liabilities:Loan:CarLoan",
        "amount": 10500.0
    }
]
```

## get_balance_by_day()

Evolución del balance diario (ingresos - gastos).

```json
[
    {
        "date": "2025-01-15",
        "incoming": 7500.0,
        "expenses": 0.0,
        "balance": 7500.0
    },
    {
        "date": "2025-01-20",
        "incoming": 0.0,
        "expenses": 250.0,
        "balance": 7250.0
    },
    {
        "date": "2025-01-22",
        "incoming": 0.0,
        "expenses": 1500.0,
        "balance": 5750.0
    },
    {
        "date": "2025-01-23",
        "incoming": 0.0,
        "expenses": 75.0,
        "balance": 5675.0
    },
    {
        "date": "2025-02-01",
        "incoming": 7500.0,
        "expenses": 0.0,
        "balance": 13175.0
    },
    {
        "date": "2025-02-03",
        "incoming": 0.0,
        "expenses": 300.0,
        "balance": 12875.0
    },
    {
        "date": "2025-02-10",
        "incoming": 0.0,
        "expenses": 120.0,
        "balance": 12755.0
    },
    {
        "date": "2025-02-15",
        "incoming": 3200.0,
        "expenses": 0.0,
        "balance": 15955.0
    },
    {
        "date": "2025-02-22",
        "incoming": 1000.0,
        "expenses": 0.0,
        "balance": 16955.0
    },
    {
        "date": "2025-02-28",
        "incoming": 0.0,
        "expenses": 2800.0,
        "balance": 14155.0
    },
    {
        "date": "2025-03-01",
        "incoming": 7500.0,
        "expenses": 0.0,
        "balance": 21655.0
    },
    {
        "date": "2025-03-02",
        "incoming": 0.0,
        "expenses": 450.0,
        "balance": 21205.0
    },
    {
        "date": "2025-03-10",
        "incoming": 0.0,
        "expenses": 90.0,
        "balance": 21115.0
    },
    {
        "date": "2025-03-15",
        "incoming": 0.0,
        "expenses": 1500.0,
        "balance": 19615.0
    },
    {
        "date": "2025-03-18",
        "incoming": 0.0,
        "expenses": 300.0,
        "balance": 19315.0
    },
    {
        "date": "2025-03-25",
        "incoming": 0.0,
        "expenses": 200.0,
        "balance": 19115.0
    },
    {
        "date": "2025-04-01",
        "incoming": 7500.0,
        "expenses": 0.0,
        "balance": 26615.0
    },
    {
        "date": "2025-04-02",
        "incoming": 0.0,
        "expenses": 1200.0,
        "balance": 25415.0
    },
    {
        "date": "2025-04-10",
        "incoming": 0.0,
        "expenses": 130.0,
        "balance": 25285.0
    },
    {
        "date": "2025-04-15",
        "incoming": 0.0,
        "expenses": 1500.0,
        "balance": 23785.0
    },
    {
        "date": "2025-04-20",
        "incoming": 0.0,
        "expenses": 3000.0,
        "balance": 20785.0
    },
    {
        "date": "2025-04-25",
        "incoming": 0.0,
        "expenses": 100.0,
        "balance": 20685.0
    },
    {
        "date": "2025-05-01",
        "incoming": 7500.0,
        "expenses": 0.0,
        "balance": 28185.0
    },
    {
        "date": "2025-05-03",
        "incoming": 0.0,
        "expenses": 310.0,
        "balance": 27875.0
    },
    {
        "date": "2025-05-06",
        "incoming": 0.0,
        "expenses": 5800.0,
        "balance": 22075.0
    },
    {
        "date": "2025-05-10",
        "incoming": 0.0,
        "expenses": 270.0,
        "balance": 21805.0
    },
    {
        "date": "2025-05-15",
        "incoming": 0.0,
        "expenses": 1500.0,
        "balance": 20305.0
    },
    {
        "date": "2025-05-25",
        "incoming": 0.0,
        "expenses": 2200.0,
        "balance": 18105.0
    },
    {
        "date": "2025-06-01",
        "incoming": 7500.0,
        "expenses": 0.0,
        "balance": 25605.0
    },
    {
        "date": "2025-06-03",
        "incoming": 0.0,
        "expenses": 450.0,
        "balance": 25155.0
    },
    {
        "date": "2025-06-10",
        "incoming": 4500.0,
        "expenses": 0.0,
        "balance": 29655.0
    },
    {
        "date": "2025-06-15",
        "incoming": 0.0,
        "expenses": 1500.0,
        "balance": 28155.0
    },
    {
        "date": "2025-06-20",
        "incoming": 0.0,
        "expenses": 6500.0,
        "balance": 21655.0
    },
    {
        "date": "2025-06-30",
        "incoming": 0.0,
        "expenses": 350.0,
        "balance": 21305.0
    }
]
```

## get_cashflow_by_month()

Flujo de caja mensual (ingresos - gastos).

```json
[
    {
        "month": "2025-01",
        "in": 7500.0,
        "out": 1825.0,
        "net": 5675.0
    },
    {
        "month": "2025-02",
        "in": 11700.0,
        "out": 3220.0,
        "net": 8480.0
    },
    {
        "month": "2025-03",
        "in": 7500.0,
        "out": 2540.0,
        "net": 4960.0
    },
    {
        "month": "2025-04",
        "in": 7500.0,
        "out": 5930.0,
        "net": 1570.0
    },
    {
        "month": "2025-05",
        "in": 7500.0,
        "out": 10080.0,
        "net": -2580.0
    },
    {
        "month": "2025-06",
        "in": 12000.0,
        "out": 8800.0,
        "net": 3200.0
    }
]
```

## get_expense_trends_by_category()

Tendencias de gastos por categoría mensual.

```json
{
    "Expenses:Food:Groceries": {
        "2025-01": 250.0,
        "2025-05": 270.0
    },
    "Expenses:Rent": {
        "2025-01": 1500.0,
        "2025-03": 1500.0,
        "2025-04": 1500.0,
        "2025-05": 1500.0,
        "2025-06": 1500.0
    },
    "Expenses:Food:DiningOut": {
        "2025-01": 75.0,
        "2025-04": 100.0
    },
    "Expenses:Utilities": {
        "2025-02": 300.0,
        "2025-05": 310.0
    },
    "Expenses:Transportation:Gas": {
        "2025-02": 120.0,
        "2025-04": 130.0
    },
    "Expenses:Travel": {
        "2025-02": 2800.0,
        "2025-05": 5800.0
    },
    "Expenses:Insurance:Health": {
        "2025-03": 450.0,
        "2025-06": 450.0
    },
    "Expenses:Transportation:Maintenance": {
        "2025-03": 90.0,
        "2025-05": 2200.0
    },
    "Expenses:Education": {
        "2025-03": 300.0
    },
    "Expenses:Entertainment": {
        "2025-03": 200.0,
        "2025-06": 350.0
    },
    "Expenses:Medical": {
        "2025-04": 1200.0
    },
    "Expenses:Shopping": {
        "2025-04": 3000.0,
        "2025-06": 6500.0
    }
}
```

## get_monthly_incomes_expenses()

Resumen mensual de ingresos y gastos.

```json
[
    {
        "month": "2025-01",
        "incoming": 7500.0,
        "expenses": 1825.0
    },
    {
        "month": "2025-02",
        "incoming": 11700.0,
        "expenses": 3220.0
    },
    {
        "month": "2025-03",
        "incoming": 7500.0,
        "expenses": 2540.0
    },
    {
        "month": "2025-04",
        "incoming": 7500.0,
        "expenses": 5930.0
    },
    {
        "month": "2025-05",
        "incoming": 7500.0,
        "expenses": 10080.0
    },
    {
        "month": "2025-06",
        "incoming": 12000.0,
        "expenses": 8800.0
    }
]
```

## get_monthly_growth_rates()

Tasa de crecimiento mensual.

```json
[
    {
        "month": "2025-01",
        "in_growth": 0.0,
        "out_growth": 0.0,
        "net_growth": 0.0
    },
    {
        "month": "2025-02",
        "in_growth": 56.0,
        "out_growth": 76.44,
        "net_growth": 49.43
    },
    {
        "month": "2025-03",
        "in_growth": -35.9,
        "out_growth": -21.12,
        "net_growth": -41.51
    },
    {
        "month": "2025-04",
        "in_growth": 0.0,
        "out_growth": 133.46,
        "net_growth": -68.35
    },
    {
        "month": "2025-05",
        "in_growth": 0.0,
        "out_growth": 69.98,
        "net_growth": -264.33
    },
    {
        "month": "2025-06",
        "in_growth": 60.0,
        "out_growth": -12.7,
        "net_growth": -224.03
    }
]
```

## get_monthly_expense_ratio()

Tasa de gastos mensual.

```json
[
    {
        "month": "2025-01",
        "expense_ratio": 24.33
    },
    {
        "month": "2025-02",
        "expense_ratio": 27.52
    },
    {
        "month": "2025-03",
        "expense_ratio": 33.87
    },
    {
        "month": "2025-04",
        "expense_ratio": 79.07
    },
    {
        "month": "2025-05",
        "expense_ratio": 134.4
    },
    {
        "month": "2025-06",
        "expense_ratio": 73.33
    }
]
```

## get_moving_average()

Promedio móvil.

```json
[
    {
        "month": "2025-01",
        "in_moving_avg": 0.0
    },
    {
        "month": "2025-02",
        "in_moving_avg": 0.0
    },
    {
        "month": "2025-03",
        "in_moving_avg": 8900.0
    },
    {
        "month": "2025-04",
        "in_moving_avg": 8900.0
    },
    {
        "month": "2025-05",
        "in_moving_avg": 7500.0
    },
    {
        "month": "2025-06",
        "in_moving_avg": 9000.0
    }
]
```

## get_trend_slope()

Pendiente de la tendencia.

```json
282.86
```

## predict_future_months()

Predicción de meses futuros.

```json
[
    {
        "month": "2025-07",
        "predicted_in": 9940.02
    },
    {
        "month": "2025-08",
        "predicted_in": 10222.88
    },
    {
        "month": "2025-09",
        "predicted_in": 10505.74
    }
]
```

## get_extreme_months()

Meses extremos.

```json
{
    "highest_income": {
        "month": "2025-06",
        "in": 12000.0,
        "out": 8800.0,
        "net": 3200.0
    },
    "highest_expense": {
        "month": "2025-05",
        "in": 7500.0,
        "out": 10080.0,
        "net": -2580.0
    },
    "best_balance": {
        "month": "2025-02",
        "in": 11700.0,
        "out": 3220.0,
        "net": 8480.0
    }
}
```

## classify_months_by_balance()

Clasificación de meses según balance.

```json
{
    "positive": [
        "2025-01",
        "2025-02",
        "2025-03",
        "2025-04",
        "2025-06"
    ],
    "negative": [
        "2025-05"
    ],
    "neutral": []
}
```

## compare_months()

Comparación de meses.

```json
{
    "in_diff": 4200.0,
    "out_diff": 1395.0,
    "net_diff": 2805.0
}
```

## get_income_dependency_ratio()

Ratio de dependencia de ingresos.

```json
[
    {
        "month": "2025-01",
        "dependency_ratio": 24.33
    },
    {
        "month": "2025-02",
        "dependency_ratio": 27.52
    },
    {
        "month": "2025-03",
        "dependency_ratio": 33.87
    },
    {
        "month": "2025-04",
        "dependency_ratio": 79.07
    },
    {
        "month": "2025-05",
        "dependency_ratio": 134.4
    },
    {
        "month": "2025-06",
        "dependency_ratio": 73.33
    }
]
```

## get_cumulative_net_income()

Acumulación de ingresos netos.

```json
[
    {
        "month": "2025-01",
        "cumulative_net": 5675.0
    },
    {
        "month": "2025-02",
        "cumulative_net": 14155.0
    },
    {
        "month": "2025-03",
        "cumulative_net": 19115.0
    },
    {
        "month": "2025-04",
        "cumulative_net": 20685.0
    },
    {
        "month": "2025-05",
        "cumulative_net": 18105.0
    },
    {
        "month": "2025-06",
        "cumulative_net": 21305.0
    }
]
```

## get_accounts_used()

Listado de todas las cuentas utilizadas.

- Assets:Bank:Checking
- Assets:Bank:Savings
- Assets:Cash
- Assets:Investments:Stocks
- Equity:OpeningBalances
- Expenses:Education
- Expenses:Entertainment
- Expenses:Food:DiningOut
- Expenses:Food:Groceries
- Expenses:Insurance:Health
- Expenses:Medical
- Expenses:Rent
- Expenses:Shopping
- Expenses:Transportation:Gas
- Expenses:Transportation:Maintenance
- Expenses:Travel
- Expenses:Utilities
- Income:Freelance
- Income:Investments:Dividends
- Income:Salary
- Liabilities:CreditCard:Visa
- Liabilities:Loan:CarLoan
