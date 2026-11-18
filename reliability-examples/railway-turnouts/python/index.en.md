# Querying BIS and Ofelia from Python

BIS and Ofelia data are stored in PostgreSQL databases. SQL is the language used to ask the database for data. You can run SQL in a database client, or send it from Python. In these examples, `pandas` sends each SQL query to PostgreSQL and stores the result in a DataFrame.

Run the code blocks in order. The code follows the style used in the [complete Python example](sql_query_examples.py).

## Connect to PostgreSQL

First, import the libraries. `load_dotenv()` reads the connection settings from your `.env` file. The values are used to build the connection string, and `create_engine()` creates the connection interface used by pandas.

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

## Explore BIS

### Read the column names and descriptions

This query asks PostgreSQL for the BIS table's column names and comments. A comment appears when one has been added to the column in the database. `pd.read_sql` runs the query and returns the result as a DataFrame named `bis_info`.

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

### List the available turnout types

`SELECT DISTINCT` returns each turnout type once. The query result is stored in `vxltyp`.

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

### Select turnouts of one type

This query selects two columns and uses `WHERE` to keep only rows matching the chosen turnout type. Change the value in the condition to search for another type. The matching rows are stored in `vxl`.

The double quotes around column names are needed because the source names contain uppercase or Swedish characters.

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

`head()` displays the first five rows, which is a quick way to inspect a result without printing the entire table.

## Explore Ofelia

### Read the column names and descriptions

This is the same kind of query as for BIS, but it reads the columns from `ofeliadata`.

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

### List the asset parts

This query lists each distinct value in the Ofelia column `Anläggningsdel (BVS)`.

```python
query = """
SELECT DISTINCT
    "Anläggningsdel (BVS)"
FROM ofeliadata;
"""
anldel = pd.read_sql(query, engine)
print(anldel)
```

### Find matching failure reports

The `WHERE` conditions narrow the result to one turnout type and train-delaying failures. `IN` keeps rows where the asset part matches either of the listed values. `SELECT *` returns all columns for the matching rows. The result is stored in `wo`.

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

## Save query results to a file

The results are pandas DataFrames, so pandas can write them to common file formats. Run the line for the format you want. These commands create the files in Python's current working directory. `index=False` leaves out pandas' row-number index.

```python
# Save the BIS result to Excel
vxl.to_excel('VxlObjekt.xlsx', index=False)

# Or save the same result to CSV
vxl.to_csv('VxlObjekt.csv', index=False)

# Save the Ofelia result to Excel
wo.to_excel('EV-UIC60.xlsx', index=False)
```

In short, the SQL query determines which data PostgreSQL returns, and `pd.read_sql` puts those rows and columns into a DataFrame that you can inspect or save.
