# Fråga BIS och Ofelia från Python

BIS- och Ofelia-data lagras i PostgreSQL-databaser. SQL är språket som används för att hämta data ur databasen. Du kan köra SQL i ett databasprogram eller skicka frågorna från Python. I exemplen skickar `pandas` varje SQL-fråga till PostgreSQL och sparar resultatet i en DataFrame.

Installera paketen som anges i repots `requirements.txt`, exempelvis `python -m pip install -r requirements.txt`.

Kör kodblocken i ordning. Koden följer stilen i det [kompletta Python-exemplet](sql_query_examples.py).

## Anslut till PostgreSQL

Börja med att importera paketen. `load_dotenv()` läser anslutningsinställningarna från din `.env`-fil. Värdena används för att skapa anslutningssträngen, och `create_engine()` skapar anslutningen som pandas använder.

```python
# -*- coding: utf-8 -*-

# Load libraries
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

#%% Create SQL database connection parameters
user = os.environ.get('STUDENT_USER')
password = os.environ.get('STUDENT_PASSWORD')
host = os.environ.get('SQL_ENDPOINT')
dbname = os.environ.get('SQL_DBNAME')
port = 5432

connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

#%% Create an engine
engine = create_engine(connection_string)
```

## Utforska BIS

### Hämta kolumnnamn och beskrivningar

Frågan ber PostgreSQL om kolumnnamnen och kommentarerna för BIS-tabellen. En kommentar visas om den har lagts till på kolumnen i databasen. `pd.read_sql` kör frågan och returnerar resultatet som en DataFrame med namnet `bis_info`.

```python
#%% BIS

# Get columns for bisdata table
query = """
SELECT
    column_name,
    col_description(
        (table_schema || '.' || table_name)::regclass,
        ordinal_position
    ) AS description
FROM information_schema.columns
WHERE table_name = 'bisdata'
ORDER BY ordinal_position;
"""

bis_info = pd.read_sql(query, engine)
print(bis_info)
```

### Lista tillgängliga växeltyper

`SELECT DISTINCT` returnerar varje växeltyp en gång. Resultatet sparas i `vxltyp`.

```python
# Return all turnout types
query = """
SELECT DISTINCT
    "Växeltyp"
FROM bisdata;
"""
vxltyp = pd.read_sql(query, engine)
print(vxltyp)
```

### Välj växlar av en viss typ

Frågan väljer två kolumner och använder `WHERE` för att bara ta med rader som har den valda växeltypen. Ändra värdet i villkoret för att söka efter en annan typ. Raderna som matchar sparas i `vxl`.

Dubbla citattecken runt kolumnnamnen behövs eftersom källans namn innehåller versaler eller svenska tecken.

```python
query = """
SELECT
    "Pl_Forb",
    "Växelnr"
FROM bisdata
WHERE "Växeltyp" = 'EV-UIC60-760-1:15';
"""
vxl = pd.read_sql(query, engine)
print(vxl.head())
```

`head()` visar de fem första raderna. Det är ett snabbt sätt att kontrollera resultatet utan att skriva ut hela tabellen.

## Utforska Ofelia

### Hämta kolumnnamn och beskrivningar

Det här är samma typ av fråga som för BIS, men den hämtar kolumnerna från `ofeliadata`.

```python
#%% OFELIA

# Get columns for ofeliadata table
query = """
SELECT
    column_name,
    col_description(
        (table_schema || '.' || table_name)::regclass,
        ordinal_position
    ) AS description
FROM information_schema.columns
WHERE table_name = 'ofeliadata'
ORDER BY ordinal_position;
"""

ofelia_info = pd.read_sql(query, engine)
print(ofelia_info)
```

### Lista anläggningsdelar

Frågan listar varje unikt värde i Ofelia-kolumnen `Anläggningsdel (BVS)`.

```python
query = """
SELECT DISTINCT
    "Anläggningsdel (BVS)"
FROM ofeliadata;
"""
anldel = pd.read_sql(query, engine)
print(anldel)
```

### Hitta matchande felrapporter

Villkoren efter `WHERE` begränsar resultatet till en växeltyp och tågstörande fel. `IN` tar med rader där anläggningsdelen matchar något av de angivna värdena. `SELECT *` hämtar alla kolumner för raderna som matchar. Resultatet sparas i `wo`.

```python
query = """
SELECT *
FROM ofeliadata
WHERE "Växeltyp (ANL)" = 'EV-UIC60-760-1:15'
  AND "Tågstörande" = 'Ja'
  AND "Anläggningsdel (BVS)" IN (
      'Omläggningsanordning',
      'Kontrollanordning'
  );
"""
wo = pd.read_sql(query, engine)
print(wo.head())
```

## Spara frågeresultat till en fil

Resultaten är pandas-DataFrames, så pandas kan spara dem i vanliga filformat. Kör raden för det format du vill använda. Filerna skapas i Pythons aktuella arbetsmapp. `index=False` gör att pandas inte lägger till ett separat radnummer i filen.

```python
# Spara BIS-resultatet som en Excel-fil
vxl.to_excel('VxlObjekt.xlsx', index=False)

# Eller spara samma resultat som en CSV-fil
vxl.to_csv('VxlObjekt.csv', index=False)

# Spara Ofelia-resultatet som en Excel-fil
wo.to_excel('EV-UIC60.xlsx', index=False)
```

Kort sagt avgör SQL-frågan vilken data PostgreSQL returnerar. `pd.read_sql` lägger raderna och kolumnerna i en DataFrame som du kan granska eller spara.
