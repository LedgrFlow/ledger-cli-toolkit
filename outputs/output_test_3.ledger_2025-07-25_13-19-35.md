---
# Reporte de prueba - 2025-07-25 13:19:35
Generado por: `test_doc.py`
Ruta del archivo: `/home/eddybel/Documentos/dev/personales/LedgerApp/ledger-cli-toolkit/test/ledgers/test_3.ledger`

Archivo fuente: `test/ledgers/test_3.ledger`

---


# Clase: `LedgerParser`


## parse()

Convierte las transacciones del archivo ledger a estructura JSON.

```json
[
    {
        "date": "2025/01/01",
        "time": null,
        "verified": false,
        "description": "Salario Mensual",
        "accounts": [
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": 25000.0
            },
            {
                "account": "Ingresos:Salarios",
                "subAccounts": [
                    "Ingresos",
                    "Salarios"
                ],
                "unit": "MXN",
                "amount": -25000.0
            }
        ]
    },
    {
        "date": "2025-01-02",
        "time": null,
        "verified": false,
        "description": "Compra de alimentos",
        "accounts": [
            {
                "account": "Gastos:Comida",
                "subAccounts": [
                    "Gastos",
                    "Comida"
                ],
                "unit": "MXN",
                "amount": 1200.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -1200.0
            }
        ]
    },
    {
        "date": "2025-01-03",
        "time": null,
        "verified": false,
        "description": "Transporte público",
        "accounts": [
            {
                "account": "Gastos:Transporte",
                "subAccounts": [
                    "Gastos",
                    "Transporte"
                ],
                "unit": "MXN",
                "amount": 500.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -500.0
            }
        ]
    },
    {
        "date": "2025-01-05",
        "time": null,
        "verified": false,
        "description": "Cena en restaurante",
        "accounts": [
            {
                "account": "Gastos:Comida",
                "subAccounts": [
                    "Gastos",
                    "Comida"
                ],
                "unit": "MXN",
                "amount": 750.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -750.0
            }
        ]
    },
    {
        "date": "2025-01-07",
        "time": null,
        "verified": false,
        "description": "Pago de tarjeta de crédito",
        "accounts": [
            {
                "account": "Pasivos:Tarjeta",
                "subAccounts": [
                    "Pasivos",
                    "Tarjeta"
                ],
                "unit": "MXN",
                "amount": 5000.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -5000.0
            }
        ]
    },
    {
        "date": "2025-01-08",
        "time": null,
        "verified": false,
        "description": "Suscripción de streaming",
        "accounts": [
            {
                "account": "Gastos:Entretenimiento",
                "subAccounts": [
                    "Gastos",
                    "Entretenimiento"
                ],
                "unit": "MXN",
                "amount": 250.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -250.0
            }
        ]
    },
    {
        "date": "2025-01-10",
        "time": null,
        "verified": false,
        "description": "Transporte (taxi)",
        "accounts": [
            {
                "account": "Gastos:Transporte",
                "subAccounts": [
                    "Gastos",
                    "Transporte"
                ],
                "unit": "MXN",
                "amount": 300.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -300.0
            }
        ]
    },
    {
        "date": "2025-01-12",
        "time": null,
        "verified": false,
        "description": "Supermercado",
        "accounts": [
            {
                "account": "Gastos:Comida",
                "subAccounts": [
                    "Gastos",
                    "Comida"
                ],
                "unit": "MXN",
                "amount": 2100.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -2100.0
            }
        ]
    },
    {
        "date": "2025-01-15",
        "time": null,
        "verified": false,
        "description": "Salario extra",
        "accounts": [
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": 10000.0
            },
            {
                "account": "Ingresos:Salarios",
                "subAccounts": [
                    "Ingresos",
                    "Salarios"
                ],
                "unit": "MXN",
                "amount": -10000.0
            }
        ]
    },
    {
        "date": "2025-01-16",
        "time": null,
        "verified": false,
        "description": "Pago parcial tarjeta de crédito",
        "accounts": [
            {
                "account": "Pasivos:Tarjeta",
                "subAccounts": [
                    "Pasivos",
                    "Tarjeta"
                ],
                "unit": "MXN",
                "amount": 3000.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -3000.0
            }
        ]
    },
    {
        "date": "2025-01-17",
        "time": null,
        "verified": false,
        "description": "Cine",
        "accounts": [
            {
                "account": "Gastos:Entretenimiento",
                "subAccounts": [
                    "Gastos",
                    "Entretenimiento"
                ],
                "unit": "MXN",
                "amount": 400.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -400.0
            }
        ]
    },
    {
        "date": "2025-01-17",
        "time": null,
        "verified": false,
        "description": "Gasolina",
        "accounts": [
            {
                "account": "Gastos:Transporte",
                "subAccounts": [
                    "Gastos",
                    "Transporte"
                ],
                "unit": "MXN",
                "amount": 1000.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -1000.0
            }
        ]
    },
    {
        "date": "2025-01-18",
        "time": null,
        "verified": false,
        "description": "Pago de luz",
        "accounts": [
            {
                "account": "Gastos:Comida",
                "subAccounts": [
                    "Gastos",
                    "Comida"
                ],
                "unit": "MXN",
                "amount": 600.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -600.0
            }
        ]
    },
    {
        "date": "2025-01-18",
        "time": null,
        "verified": false,
        "description": "Comida rápida",
        "accounts": [
            {
                "account": "Gastos:Comida",
                "subAccounts": [
                    "Gastos",
                    "Comida"
                ],
                "unit": "MXN",
                "amount": 800.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -800.0
            }
        ]
    },
    {
        "date": "2025-01-18",
        "time": null,
        "verified": false,
        "description": "Transporte privado",
        "accounts": [
            {
                "account": "Gastos:Transporte",
                "subAccounts": [
                    "Gastos",
                    "Transporte"
                ],
                "unit": "MXN",
                "amount": 450.0
            },
            {
                "account": "Activos:Banco",
                "subAccounts": [
                    "Activos",
                    "Banco"
                ],
                "unit": "MXN",
                "amount": -450.0
            }
        ]
    }
]
```

## parse_accounts()

Lista de cuentas contables detectadas.

```json
[
    "Activos:Banco",
    "Ingresos:Salarios",
    "Gastos:Comida",
    "Gastos:Transporte",
    "Gastos:Entretenimiento",
    "Pasivos:Tarjeta"
]
```

## calculate_balances()

Cálculo de balances por cuenta detallada.

```json
{
    "Activos:Banco": {
        "MXN": 18650.0
    },
    "Ingresos:Salarios": {
        "MXN": -35000.0
    },
    "Gastos:Comida": {
        "MXN": 5450.0
    },
    "Gastos:Transporte": {
        "MXN": 2250.0
    },
    "Gastos:Entretenimiento": {
        "MXN": 650.0
    },
    "Pasivos:Tarjeta": {
        "MXN": 8000.0
    }
}
```

## calculate_balances_by_parents_accounts()

Balance agrupado por cuentas padre.

```json
{
    "Assets": {
        "MXN": 18650.0
    },
    "Liabilities": {
        "MXN": 8000.0
    },
    "Equity": {
        "N/A": 0.0
    },
    "Income": {
        "MXN": -35000.0
    },
    "Expenses": {
        "MXN": 8350.0
    }
}
```

## calculate_status_results()

Estado de resultados (ingresos, gastos, utilidad).

```json
{
    "total_income_by_currency": {
        "MXN": 35000.0
    },
    "total_expenses_by_currency": {
        "MXN": -8350.0
    },
    "utility_by_currency": {
        "MXN": 26650.0
    },
    "income_details": [
        {
            "Ingresos:Salarios": {
                "currency": "MXN",
                "amount": 35000.0
            }
        }
    ],
    "expenses_details": [
        {
            "Gastos:Comida": {
                "currency": "MXN",
                "amount": -5450.0
            }
        },
        {
            "Gastos:Transporte": {
                "currency": "MXN",
                "amount": -2250.0
            }
        },
        {
            "Gastos:Entretenimiento": {
                "currency": "MXN",
                "amount": -650.0
            }
        }
    ]
}
```

## calculate_balances_by_details_accounts()

Balance por subcuentas detalladas.

```json
{
    "Activos": {
        "balances": {
            "MXN": 18650.0
        },
        "sub_accounts": {
            "Banco": {
                "balances": {
                    "MXN": 18650.0
                },
                "sub_accounts": {}
            }
        }
    },
    "Ingresos": {
        "balances": {
            "MXN": -35000.0
        },
        "sub_accounts": {
            "Salarios": {
                "balances": {
                    "MXN": -35000.0
                },
                "sub_accounts": {}
            }
        }
    },
    "Gastos": {
        "balances": {
            "MXN": 8350.0
        },
        "sub_accounts": {
            "Comida": {
                "balances": {
                    "MXN": 5450.0
                },
                "sub_accounts": {}
            },
            "Transporte": {
                "balances": {
                    "MXN": 2250.0
                },
                "sub_accounts": {}
            },
            "Entretenimiento": {
                "balances": {
                    "MXN": 650.0
                },
                "sub_accounts": {}
            }
        }
    },
    "Pasivos": {
        "balances": {
            "MXN": 8000.0
        },
        "sub_accounts": {
            "Tarjeta": {
                "balances": {
                    "MXN": 8000.0
                },
                "sub_accounts": {}
            }
        }
    }
}
```

## get_date_range()

Periodo detectado en las transacciones.

Desde: `2025/01/01` hasta `2025/01/18`

# Clase: `LedgerAnalyst`


## detect_unusual_expenses()

Detecta gastos que exceden significativamente su promedio histórico.

```json
[]
```

## get_daily_incomes_expenses()

Muestra ingresos y gastos diarios.

```json
[
    {
        "date": "2025-01-01",
        "incoming": 25000.0,
        "expenses": 0.0
    },
    {
        "date": "2025-01-02",
        "incoming": 0.0,
        "expenses": 1200.0
    },
    {
        "date": "2025-01-03",
        "incoming": 0.0,
        "expenses": 500.0
    },
    {
        "date": "2025-01-05",
        "incoming": 0.0,
        "expenses": 750.0
    },
    {
        "date": "2025-01-08",
        "incoming": 0.0,
        "expenses": 250.0
    },
    {
        "date": "2025-01-10",
        "incoming": 0.0,
        "expenses": 300.0
    },
    {
        "date": "2025-01-12",
        "incoming": 0.0,
        "expenses": 2100.0
    },
    {
        "date": "2025-01-15",
        "incoming": 10000.0,
        "expenses": 0.0
    },
    {
        "date": "2025-01-17",
        "incoming": 0.0,
        "expenses": 1400.0
    },
    {
        "date": "2025-01-18",
        "incoming": 0.0,
        "expenses": 1850.0
    }
]
```

## get_expenses_pie()

Distribución de gastos por cuenta.

```json
[
    {
        "account": "Gastos:Comida",
        "amount": 5450.0
    },
    {
        "account": "Gastos:Transporte",
        "amount": 2250.0
    },
    {
        "account": "Gastos:Entretenimiento",
        "amount": 650.0
    }
]
```

## get_incomes_pie()

Distribución de ingresos por cuenta.

```json
[
    {
        "account": "Ingresos:Salarios",
        "amount": 35000.0
    }
]
```

## get_assets_summary()

Resumen del total de activos.

```json
[
    {
        "account": "Activos:Banco",
        "amount": 51350.0
    }
]
```

## get_liabilities_summary()

Resumen del total de pasivos.

```json
[
    {
        "account": "Pasivos:Tarjeta",
        "amount": 8000.0
    }
]
```

## get_balance_by_day()

Evolución del balance diario (ingresos - gastos).

```json
[
    {
        "date": "2025-01-01",
        "incoming": 25000.0,
        "expenses": 0.0,
        "balance": 25000.0
    },
    {
        "date": "2025-01-02",
        "incoming": 0.0,
        "expenses": 1200.0,
        "balance": 23800.0
    },
    {
        "date": "2025-01-03",
        "incoming": 0.0,
        "expenses": 500.0,
        "balance": 23300.0
    },
    {
        "date": "2025-01-05",
        "incoming": 0.0,
        "expenses": 750.0,
        "balance": 22550.0
    },
    {
        "date": "2025-01-08",
        "incoming": 0.0,
        "expenses": 250.0,
        "balance": 22300.0
    },
    {
        "date": "2025-01-10",
        "incoming": 0.0,
        "expenses": 300.0,
        "balance": 22000.0
    },
    {
        "date": "2025-01-12",
        "incoming": 0.0,
        "expenses": 2100.0,
        "balance": 19900.0
    },
    {
        "date": "2025-01-15",
        "incoming": 10000.0,
        "expenses": 0.0,
        "balance": 29900.0
    },
    {
        "date": "2025-01-17",
        "incoming": 0.0,
        "expenses": 1400.0,
        "balance": 28500.0
    },
    {
        "date": "2025-01-18",
        "incoming": 0.0,
        "expenses": 1850.0,
        "balance": 26650.0
    }
]
```

## get_accounts_used()

Listado de todas las cuentas utilizadas.

- Activos:Banco
- Gastos:Comida
- Gastos:Entretenimiento
- Gastos:Transporte
- Ingresos:Salarios
- Pasivos:Tarjeta
