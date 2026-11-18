# Fråga databaserna med Python

Datan lagras i PostgreSQL-databaser. Python kan skicka SQL-frågor till databasen och läsa in resultaten i pandas-DataFrames. Följ stegen nedan eller se det [kompletta Python-skriptet](query_data.py).

## 1. Importera paketen

```python
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text
```

## 2. Läs anslutningsinställningarna och anslut

`load_dotenv()` läser värdena från din `.env`-fil. `URL.create()` bygger anslutningen till PostgreSQL och `create_engine()` förbereder den för frågor.

```python
load_dotenv()

username = os.getenv("STUDENT_USER")
password = os.getenv("STUDENT_PASSWORD")
host = os.getenv("SQL_ENDPOINT")
database = os.getenv("SQL_DBNAME")

connection_url = URL.create(
    "postgresql+psycopg2",
    username=username,
    password=password,
    host=host,
    port=5432,
    database=database,
)
engine = create_engine(connection_url)
```

## 3. Hämta kolumnnamn och beskrivningar

SQL-frågan listar kolumnerna i `bisdata` och `ofeliadata`. PostgreSQL visar en beskrivning om en `COMMENT` har lagts till på kolumnen.

```python
column_query = text("""
    SELECT
        c.table_name,
        c.column_name,
        pg_catalog.col_description(
            format('%I.%I', c.table_schema, c.table_name)::regclass,
            c.ordinal_position
        ) AS description
    FROM information_schema.columns AS c
    WHERE c.table_name IN ('bisdata', 'ofeliadata')
      AND c.table_schema = current_schema()
    ORDER BY c.table_name, c.ordinal_position
""")

column_info = pd.read_sql_query(column_query, engine)
print(column_info)
```

## 4. Skicka en SQL-fråga och läs resultatet

Frågan hämtar driftplatser och växelnummer från BIS för en viss växeltyp. `:turnout_type` är en parameter som skickas separat från SQL-texten.

```python
turnout_query = text('''
    SELECT "Pl_Forb", "Växelnr"
    FROM bisdata
    WHERE "Växeltyp" = :turnout_type
    ORDER BY "Pl_Forb", "Växelnr"
''')

turnouts = pd.read_sql_query(
    turnout_query,
    engine,
    params={"turnout_type": "EV-UIC60-760-1:15"},
)
print(turnouts)
```

Resultatet är en pandas-DataFrame. Du kan använda samma metod för Ofelia:

```python
failure_query = text('''
    SELECT *
    FROM ofeliadata
    WHERE "Växeltyp (ANL)" = :turnout_type
      AND "Tågstörande" = :train_delaying
      AND "Anläggningsdel (BVS)" IN (
          'Omläggningsanordning', 'Kontrollanordning'
      )
''')

failures = pd.read_sql_query(
    failure_query,
    engine,
    params={
        "turnout_type": "EV-UIC60-760-1:15",
        "train_delaying": "Ja",
    },
)
print(failures.head())
```

## 5. Spara resultatet

Till exempel kan du spara Ofelia-resultatet i en Excel-fil:

```python
failures.to_excel("railway_turnout_failures.xlsx", index=False)
```
