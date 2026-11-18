# Querying the databases with Python

BIS and Ofelia data are stored in PostgreSQL databases. These examples show how to write SQL queries in Python and load the results into pandas. Run the code blocks in order. The style follows the complete [Python example](sql_query_examples.py).

## Load libraries and connect to the database

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

## BIS

Get the column names and PostgreSQL comments for the BIS table:

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
```

List the turnout types and find locations and turnout numbers for one type:

```python
# Return all turnout types
query = """
SELECT DISTINCT
    "Växeltyp"
FROM bisdata;
"""
vxltyp = pd.read_sql(query, engine)

# Return locations and turnout numbers for one turnout type
query = """
SELECT
    "Pl_Forb",
    "Växelnr"
FROM bisdata
WHERE "Växeltyp" = 'EV-UIC60-760-1:15';
"""
vxl = pd.read_sql(query, engine)

# Example: write the result to Excel or CSV
# vxl.to_excel('VxlObjekt.xlsx')
# vxl.to_csv('VxlObjekt.csv')
```

## Ofelia

Get the column descriptions, then list the asset parts and matching failure reports:

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

# Return all asset parts
query = """
SELECT DISTINCT
    "Anläggningsdel (BVS)"
FROM ofeliadata;
"""
anldel = pd.read_sql(query, engine)
print(anldel)

# Return work orders for one turnout type and selected parts
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

# Example: save the result to Excel
# wo.to_excel('EV-UIC60.xlsx')
```

The SQL query is sent to PostgreSQL by `pd.read_sql`. Its results are returned as pandas DataFrames, such as `bis_info`, `vxltyp`, `vxl`, `ofelia_info`, `anldel`, and `wo`.
