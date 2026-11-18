# -*- coding: utf-8 -*-

# Load libraries
from sqlalchemy import URL, create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

#%% Create sql db connection parameters
username = os.environ.get('STUDENT_USER')
password = os.environ.get('STUDENT_PASSWORD')
host = os.environ.get('SQL_ENDPOINT')  
dbname = os.environ.get('SQL_DBNAME')  
port = 5432

connection_url = URL.create(
    "postgresql+psycopg2",
    username=username,
    password=password,
    host=host,
    port=5432,
    database=dbname,
)

#%% Create an engine
engine = create_engine(connection_url) 

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


# Return all types of S&Cs (växeltyper) 
query = """
SELECT DISTINCT
    "Växeltyp"
FROM 
    bisdata;
"""
vxltyp = pd.read_sql(query, engine)


query = """
SELECT
    "Pl_Forb",
    "Växelnr"
FROM 
    bisdata
WHERE 
    "Växeltyp" = 'EV-UIC60-760-1:15';
"""
vxl = pd.read_sql(query, engine)

# Example how to write to excel or csv
# vxl.to_excel('VxlObjekt.xlsx')
# vxl.to_csv('VxlObjekt.csv')


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

# Return all S&C parts (anläggsningsdel) 
query = """
SELECT DISTINCT
    "Anläggningsdel (BVS)"
FROM 
    ofeliadata;
"""

anldel = pd.read_sql(query, engine)
print(anldel)


# Return all work orders for selected S&C type and part (växeltyp och anläggsningsdel) 
query = """
SELECT 
    *
FROM 
    ofeliadata
WHERE 
    "Växeltyp (ANL)" = 'EV-UIC60-760-1:15' AND
    "Tågstörande" = 'Ja' AND
    "Anläggningsdel (BVS)" IN ('Omläggningsanordning','Kontrollanordning');
"""

wo = pd.read_sql(query, engine)

# Example how to save data to excel
# wo.to_excel('EV-UIC60.xlsx')


