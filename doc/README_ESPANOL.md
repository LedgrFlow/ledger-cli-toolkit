# ledgerpy

`ledgerpy` es una librería en Python diseñada para leer, manipular y generar archivos de contabilidad en formato `.ledger`. Ofrece una forma sencilla de trabajar con estos archivos dentro del ecosistema de Python, transformándolos en estructuras como JSON que son fáciles de procesar y analizar.

## ¿Por qué `ledgerpy`?

El proyecto nació de la necesidad de contar con una herramienta para manipular y leer archivos `.ledger` directamente desde Python. Si bien existen herramientas poderosas como `ledger-cli` para interactuar con este tipo de archivos desde la línea de comandos, `ledgerpy` busca ofrecer la misma capacidad, pero dentro del lenguaje, permitiendo a los desarrolladores integrar estos datos en sus aplicaciones de manera sencilla.

## Funcionalidades

### Funcionalidades actuales

- Conversión a JSON: Convierte archivos .ledger en estructuras JSON para análisis y manipulación sencilla.
- Filtrado de transacciones: Filtra registros entre fechas específicas.
- Cálculo de balances: Calcula los saldos por cuenta a partir de las transacciones procesadas.
- Agregar transacciones: Añade nuevas transacciones a los archivos .ledger.

### En desarrollo
- Complemento: LedgerVisual: Un módulo adicional que permite la visualización de datos contables en tablas de manera sencilla.

  - Visualización de transacciones en formato de diario: Presenta transacciones en una tabla estilo diario contable, con columnas para:
    - Número de transacción.
    - Fecha y hora.
    - Concepto.
    - Débito.
    - Crédito.
    - Incluye una fila final con "SUMAS IGUALES" para totalizar débitos y créditos.
  
- Visualización de balances generales: Muestra los saldos por cuenta en una tabla organizada con:

    - Número de cuenta.
    - Nombre de la cuenta.
    - Unidad (ejemplo: USD, MXN).
    - Saldo.

## Metas a largo plazo
  - Exportación a formatos populares:
  - Exportar transacciones y balances a archivos CSV.
  - Generar reportes en formato PDF con tablas y gráficos.
  - Conexión con bases de datos SQL:
    - Integración con bases de datos como MySQL, PostgreSQL y SQLite para almacenamiento y consulta avanzada de datos contables.

## Instalación

Puedes instalar `ledgerpy` fácilmente desde PyPI con el siguiente comando:

```bash
pip install ledgerpy
```

## Ejemplos de uso

### Leer y convertir un archivo `.ledger` a JSON

```python
from ledgerpy import LedgerParser

# Crear una instancia del parser
parser = LedgerParser("mi_archivo.ledger")

# Convertir el archivo a JSON
transactions_json = parser.to_json()
print(transactions_json)
```

### Filtrar transacciones por fechas

```python
# Obtener transacciones entre dos fechas
filtered_transactions = parser.get_registers_between_dates("2023/01/01", "2023/12/31")
print(filtered_transactions)
```

### Calcular saldos por cuenta

```python
# Parsear transacciones
transactions = parser.parse()

# Calcular saldos
balances = parser.calculate_balances(transactions)
print(balances)
```

### Agregar una nueva transacción

```python
# Agregar una transacción al archivo .ledger
parser.add_transaction(
    date="2024/01/01",
    description="Pago de servicios",
    accounts=[
        {"account": "Gastos:Servicios", "unit": "USD", "amount": 50.00},
        {"account": "Activos:Banco", "unit": "USD", "amount": -50.00},
    ]
)
```

## Contribuir

¡Las contribuciones son bienvenidas! Si tienes ideas, encuentras errores o deseas mejorar la funcionalidad de `ledgerpy`, no dudes en abrir un [issue](https://github.com/tu-usuario/ledgerpy/issues) o enviar un pull request. 

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Esto significa que puedes usar, modificar y distribuir el código libremente, siempre y cuando incluyas el aviso de la licencia original.