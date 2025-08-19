
# 📒 Documentación: Ledger CLI Toolkit

Ledger CLI Toolkit es una librería en Python diseñada para **analizar, parsear y exportar archivos Ledger**. Su objetivo principal es simplificar el trabajo con la contabilidad personal de tipo Ledger CLI, permitiendo convertir estos datos en estructuras JSON y preparándolos para visualización, análisis y exportación en diversos formatos.

## 🚀 Instalación

Para empezar a usar la librería, instálala directamente desde PyPI:

```bash

pip install ledger-cli-toolkit

```

## 📦 Importación de Clases

La librería está modularizada en varias clases, cada una con una funcionalidad específica:

```python

from ledger_cli import LedgerParser     # Para parsear archivos Ledger a JSON
from ledger_cli import LedgerVisual     # Para visualizar datos
from ledger_cli import LedgerGrafics    # Para generar gráficos financieros
from ledger_cli import LedgerAnalyst    # Para usar herramientas de análisis
from ledger_cli import LedgerExport     # Para exportar datos en distintos formatos
from ledger_cli import LedgerMultiParser# Para manejar múltiples archivos

```

-----

## Capítulo 1: Sintaxis Extendida y Manejo de Transacciones

Ledger CLI Toolkit introduce una **sintaxis propia** que se basa en la sintaxis clásica de Ledger, pero que la extiende para incluir propiedades adicionales y manejar impuestos o valores agregados de manera más flexible. Esta nueva sintaxis permite que las transacciones sean más informativas sin sacrificar la compatibilidad con el formato original.

### Propiedades Adicionales

Puedes añadir propiedades personalizadas a una transacción utilizando el formato `-key: value`, donde `key` es el nombre de la propiedad y `value` es su valor. Esto es útil para asociar metadatos como etiquetas, identificadores únicos o cualquier otra información relevante.

**Ejemplo de sintaxis:**

```ledger

-tags: shopping, groceries, food
-uuid: f2c2a-3bd1

```

### Impuestos y Valores Agregados

La librería te permite manejar impuestos y valores agregados directamente en la transacción con la sintaxis `+{IMP}`, `-{IMP}` o `={IMP}`.

* `+{IMP}`: El impuesto o valor se **sumará** al monto original. Por ejemplo, `MXN 100.00 +{IVA}` significa que el IVA se calculará sobre los $100 y se agregará al total.

* `-{IMP}`: El impuesto o valor se **restará** del monto original.

* `={IMP}`: El monto de la transacción **ya incluye** el impuesto o valor agregado, y este se debe extraer para un cálculo separado.

**Ejemplo de sintaxis:**

```ledger

2025-01-20 * Grocery Shopping
  Expenses:Food:Groceries   $100.00 +{IVA}
  Assets:Bank:Checking

```

-----

## Capítulo 2: Métodos Principales de la Clase `LedgerParser`

La clase `LedgerParser` es el corazón de la librería para el procesamiento de archivos. Se inicializa pasando una ruta de archivo, el contenido como string o un archivo directamente desde una interfaz. También puede recibir un archivo de cuentas contables opcional.

```python

from ledger_cli import LedgerParser

ledger = LedgerParser(file=pathFile, file_accounts=pathFile)

```

### `parse_transactions()` 🧐

Este método es el primer paso en el procesamiento de datos. Su función es **extraer la información de las transacciones** del archivo Ledger y organizarla en una estructura JSON, sin realizar ningún cálculo.

**Ejemplo de uso:**

```python

transactions_data = ledger.parse_transactions()

print(transactions_data)

```

El resultado es una lista de diccionarios, donde cada diccionario representa una transacción con detalles como la fecha, descripción, cuentas involucradas, montos y las propiedades adicionales o impuestos detectados.

**Ejemplo de output:**

```json

[
  {
    "date": "2025-01-20",
    "time": null,
    "verified": true,
    "description": "Grocery Shopping",
    "accounts": [
      {
        "account": "Expenses:Food:Groceries",
        "subAccounts": ["Expenses", "Food", "Groceries"],
        "unit": "$",
        "amount": 100.0,
        "taxes": [{"name": "IVA", "mode": "+"}]
      },
      {
        "account": "Assets:Bank:Checking",
        "subAccounts": ["Assets", "Bank", "Checking"],
        "unit": "$",
        "amount": -100.0,
        "taxes": []
      }

    ],
    "properties": [
      {"key": "tags", "value": "shopping, groceries, food"},
      {"key": "uuid", "value": "f2c2a-3bd1"}
    ]
  },
  ...

]

```

### `resolve()` ➕➖

Este método toma las transacciones extraídas con `parse_transactions()` y **resuelve los cálculos de impuestos o valores agregados pendientes**. Recibe como argumento la lista de transacciones y un diccionario de configuración de impuestos, donde se especifican el porcentaje de cada impuesto y opcionalmente, la cuenta contable asociada.

**Ejemplo de uso:**

```python

taxes_config = {"IVA": {"percentage": 0.16, "account": "Assets:Taxes:IVA"}}

resolved_transactions = ledger.resolve(transactions_data, taxes_config)

print(resolved_transactions)

```

El método `resolve()` realiza los cálculos y actualiza los montos, añadiendo una nueva entrada en `accounts` para el impuesto. Esto te permite tener un registro contable completo y preciso. Si no se especifica una cuenta para el impuesto, la librería construirá una cuenta por defecto basada en la información de la transacción.

**Ejemplo de output:**

```json

[
  {
    "date": "2025-01-20",
    "time": null,
    "verified": true,
    "description": "Grocery Shopping",
    "accounts": [
      {
        "account": "Expenses:Food:Groceries",
        "subAccounts": ["Expenses", "Food", "Groceries"],
        "unit": "$",
        "amount": 100.0,
        "taxes": [{"name": "IVA", "mode": "+"}]
      },
      {
        "account": "Assets:Bank:Checking",
        "subAccounts": ["Assets", "Bank", "Checking"],
        "unit": "$",
        "amount": -116.0,
        "taxes": []
      },
      {
        "account": "Assets:Taxes:IVA",
        "subAccounts": ["Assets", "Taxes", "IVA"],
        "unit": "$",
        "amount": 16.0,
        "taxes": []
      }
    ],
    "properties": [
      {"key": "tags", "value": "shopping, groceries, food"},
      {"key": "uuid", "value": "f2c2a-3bd1"}
    ]
  },
  ...
]

```

## Capítulo 3: Gestión de Cuentas Contables 🏦

Además de parsear transacciones, la clase `LedgerParser` te permite extraer y gestionar la información de tus cuentas contables. Esto es crucial para organizar tu contabilidad y asegurar la consistencia de los datos.

### `parse_accounts()`

Este método escanea el archivo de cuentas que se le asignó al inicializar `LedgerParser` y extrae todas las cuentas que se definen con la palabra clave **`account`**. El resultado es una lista simple con los nombres completos de todas las cuentas encontradas.

**Ejemplo de uso:**

```python

ledger = LedgerParser(file='ruta/a/mi-archivo.ledger', file_accounts='ruta/a/cuentas.ledger')
accounts = ledger.parse_accounts()
print(accounts)

```

**Output:**

```

['Assets:Bank:Checking', 'Assets:Bank:Savings', 'Expenses:Food:Groceries', 'Expenses:Food:DiningOut']

```

### `parse_accounts_advance()`

A diferencia de `parse_accounts()`, este método va más allá y busca propiedades adicionales asociadas a cada cuenta. La sintaxis para estas propiedades es similar a la de las transacciones: `key: value`. Este método es ideal para cuando quieres añadir metadatos a tus cuentas, como descripciones, categorías o cualquier otra información relevante. El resultado es una lista de diccionarios, donde cada diccionario contiene la cuenta y sus propiedades asociadas.

**Ejemplo de uso:**

```python

advanced_accounts = ledger.parse_accounts_advance()
print(advanced_accounts)

```

**Output:**

```json

[
  {
    "account": "Assets:Bank:Checking",
    "description": "\"Cuenta bancaria principal para operaciones diarias\"",
    "category": "\"Activo Corriente\""
  },

  {
    "account": "Assets:Bank:Savings",
    "description": "\"Cuenta bancaria para ahorros\"",
    "category": "\"Activo Corriente\""
  },

  {
    "account": "Expenses:Food:Groceries",
    "description": "\"Egresos de comida\"",
    "category": "\"Egreso Corriente\""
  },

  {
    "account": "Expenses:Food:DiningOut",
    "description": "\"Egresos de comida rápida\"",
    "category": "\"Egreso Corriente\""
  }
]

```

### `detected_parents_accounts()`

Este método se encarga de identificar automáticamente las cuentas padre (como `Assets`, `Liabilities`, `Income`, etc.) y asignarlas correctamente, independientemente del idioma en que estén escritas. Si no logra asociar una cuenta padre a una categoría conocida, la marcará con el prefijo **`Unknown-`** para que puedas identificarla y corregirla. Esto es útil para estandarizar la estructura de tus datos.

**Ejemplo de uso:**

```python

parent_accounts = ledger.detected_parents_accounts()
print(parent_accounts)

```

**Output:**

```json

{

  "Assets": "Assets",
  "Liabilities": "Unknown-Liabilities",
  "Equity": "Unknown-Equity",
  "Income": "Unknown-Income",
  "Expenses": "Expenses"

}

```

## Capítulo 4: Métodos de Archivo y Estructura 📁

La clase `LedgerParser` también ofrece utilidades para interactuar con la estructura del archivo en un nivel más bajo, permitiendo extraer metadatos y obtener un mapa detallado del documento para una gestión avanzada.

### `parse_metadata_yaml()`

Este método permite recuperar **metadatos globales** del archivo Ledger. La librería busca un bloque de texto delimitado por `---` al inicio del archivo. Dentro de este bloque, la información debe estar en formato **YAML** (YAML Ain't Markup Language). Este es un método práctico para definir configuraciones, información general del archivo, tasas de impuestos, o cualquier otro dato que no pertenezca a una transacción o cuenta específica.

**Ejemplo de uso:**

```python

ledger = LedgerParser(file=pathFile)
metadata = ledger.parse_metadata_yaml()
print(metadata)

```

**Output:**

```ledger
---
data:
  title: "Demo de archivo ledger"
  year: 2025

currency:
  MXN

taxes:
  IVA: .16
  ISR: .3
---

; Resto del archivo ...
```

```json

{
  "data": {
    "title": "Demo de archivo ledger",
    "year": 2025
  },
  "currency": "MXN",
  "taxes": {
    "IVA": 0.16,
    "ISR": 0.3
  }
}

```

### `parse_doc()`

Este método es una herramienta poderosa para desarrolladores que necesitan tener un control granular sobre el documento. `parse_doc()` analiza el archivo línea por línea y **crea un mapa estructurado** del mismo. Este mapa categoriza cada línea o bloque de líneas como un `metadata` (si es el bloque YAML), `transaction` (si es una transacción contable) o simplemente `line`. Además, registra los índices de las líneas, lo cual es fundamental para operaciones de edición o reconstrucción del archivo en el futuro.

**Ejemplo de uso:**

```python

doc_map = ledger.parse_doc()
print(doc_map)

```

**Output:**

```json

[
  {
    "type": "metadata",
    "index": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "lines": [
      "---",
      "data:",
      "  title: \"Demo de archivo ledger\"",
      "  year: 2025",
      "",
      "currency:",
      "  MXN",
      "",
      "taxes:",
      "  IVA: .16",
      "  ISR: .3",
      "---"
    ]
  },
  {
    "type": "line",
    "index": 12,
    "line": ""
  },
  {
    "type": "line",
    "index": 13,
    "line": ""
  },
  {
    "type": "line",
    "index": 14,
    "line": "account Assets:Bank:Checking"
  },
  ...
]

```

## Capítulo 5: Métodos de Cálculo y Análisis Financiero 📊

Una vez que has extraído y resuelto las transacciones, la clase `LedgerParser` te ofrece potentes métodos para realizar cálculos financieros. Estos te permiten obtener saldos por cuenta, estados de resultados, y balances generales.

### `calculate_balances()`

Este método calcula el **saldo acumulado para cada cuenta contable**, agrupado por moneda. Para su correcto funcionamiento, se recomienda utilizar el output del método `resolve()` como el argumento `transactions_json`. Además, puedes pasar una lista de cuentas (`reference`) para establecer el orden de los resultados.

**Ejemplo de uso:**

```python

balances = ledger.calculate_balances(transactions_json=transactions_resolved, reference=accounts)
print(balances)

```

**Output:**

```json

{
  "Assets:Bank:Checking": {"$": -116.0, "MXN": -116.0},
  "Expenses:Food:Groceries": {"$": 100.0, "MXN": 100.0},
  "Assets:Taxes:IVA": {"$": 16.0, "MXN": 16.0}
}

```

### `calculate_balances_by_parents_accounts()`

Este método es una versión resumida del cálculo de saldos. Recibe las transacciones y retorna los saldos **agrupados únicamente por las cuentas padre** (Assets, Liabilities, etc.). Es ideal para obtener una visión general rápida de la situación financiera.

**Ejemplo de uso:**

```python

parent_balances = ledger.calculate_balances_by_parents_accounts(transactions_json=transactions_resolved)
print(parent_balances)

```

**Output:**

```json

{
  "Assets": {"$": -100.0, "MXN": -100.0},
  "Liabilities": {"N/A": 0.0},
  "Equity": {"N/A": 0.0},
  "Income": {"N/A": 0.0},
  "Expenses": {"$": 100.0, "MXN": 100.0}
}

```

### `calculate_balances_by_details_accounts()`

Si necesitas una vista más granular, este método te proporciona un **balance detallado y jerárquico** por cuenta. El resultado es un diccionario anidado que muestra los saldos por cada nivel de la jerarquía de cuentas, lo que facilita la visualización de los saldos de subcuentas.

**Ejemplo de uso:**

```python

detailed_balances = ledger.calculate_balances_by_details_accounts(transactions_json=transactions_resolved)
print(detailed_balances)

```

**Output:**

```json

{
  "Expenses": {
    "balances": {"$": 100.0, "MXN": 100.0},
    "sub_accounts": {
      "Food": {
        "balances": {"$": 100.0, "MXN": 100.0},
        "sub_accounts": {
          "Groceries": {
            "balances": {"$": 100.0, "MXN": 100.0},
            "sub_accounts": {}
          }
        }
      }
    }
  },
  ...
}

```

### `calculate_status_results()`

Este método calcula el **estado de resultados** (ingresos - egresos) a partir de los balances obtenidos. Acepta el output de `calculate_balances_by_parents_accounts()` y proporciona un desglose de los totales por moneda, así como los detalles de cada ingreso y egreso.

**Ejemplo de uso:**

```python

state_results = ledger.calculate_status_results(balance=parent_balances)
print(state_results)

```

**Output:**

```json

{
  "total_income_by_currency": {},
  "total_expenses_by_currency": {
    "$": -100.0,
    "MXN": -100.0
  },
  "utility_by_currency": {
    "$": -100.0,
    "MXN": -100.0
  },
  "income_details": [],
  "expenses_details": [
    {
      "Expenses:Food:Groceries": {
        "currency": "$",
        "amount": -100.0
      }
    },
    ...
  ]
}

```

### `calculate_general_balance()`

Finalmente, este método calcula el **balance general** completo. Recibe como argumentos los balances detallados (obtenidos con `calculate_balances_by_details_accounts()`) y el resultado de las utilidades (obtenido de `calculate_status_results()`). El método ajusta los resultados, valida el balance contable y retorna un resumen completo, incluyendo totales, detalles de cuentas y la validación de que el balance esté equilibrado.

**Ejemplo de uso:**

```python

general_balance = ledger.calculate_general_balance(balance=balances, utility=state_results["utility_by_currency"])
print(general_balance)

```

**Output:**

```json
{
  "totals_by_currency": {
    "Assets": {"$": -100.0, "MXN": -100.0},
    "Liabilities": {},
    "Equity": {"$": -100.0, "MXN": -100.0}
  },
  "details": [
    {
      "account": "Assets:Bank:Checking",
      "currency": "$",
      "amount": -116.0
    },
    ...
  ],
  "validation": {
    "$": {
      "Assets": -100.0,
      "Liabilities": 0.0,
      "Equity": -100.0,
      "Liabilities+Equity": -100.0,
      "balanced": true
    },
    ...
  }
}

```
