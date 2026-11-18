"""Run example BIS and Ofelia queries and save the Ofelia result to Excel."""

import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text


def make_engine():
    load_dotenv()
    required = {
        "username": os.getenv("STUDENT_USER"),
        "password": os.getenv("STUDENT_PASSWORD"),
        "host": os.getenv("SQL_ENDPOINT"),
        "database": os.getenv("SQL_DBNAME"),
    }
    missing = [key for key, value in required.items() if not value]
    if missing:
        raise RuntimeError(
            "Missing database settings in .env: " + ", ".join(missing)
        )

    url = URL.create(
        drivername="postgresql+psycopg2",
        username=required["username"],
        password=required["password"],
        host=required["host"],
        port=5432,
        database=required["database"],
    )
    return create_engine(url)


def main():
    engine = make_engine()

    with engine.connect() as connection:
        bis_info = pd.read_sql(
            text("""
                SELECT column_name, description
                FROM (
                    SELECT
                        c.ordinal_position,
                        c.column_name,
                        pg_catalog.col_description(
                            format('%I.%I', c.table_schema, c.table_name)::regclass,
                            c.ordinal_position
                        ) AS description
                    FROM information_schema.columns AS c
                    WHERE c.table_name = 'bisdata'
                      AND c.table_schema = current_schema()
                ) AS columns_with_descriptions
                ORDER BY ordinal_position
            """),
            connection,
        )
        ofelia_info = pd.read_sql(
            text("""
                SELECT column_name, description
                FROM (
                    SELECT
                        c.ordinal_position,
                        c.column_name,
                        pg_catalog.col_description(
                            format('%I.%I', c.table_schema, c.table_name)::regclass,
                            c.ordinal_position
                        ) AS description
                    FROM information_schema.columns AS c
                    WHERE c.table_name = 'ofeliadata'
                      AND c.table_schema = current_schema()
                ) AS columns_with_descriptions
                ORDER BY ordinal_position
            """),
            connection,
        )
        turnouts = pd.read_sql(
            text('''
                SELECT "Pl_Forb", "Växelnr"
                FROM bisdata
                WHERE "Växeltyp" = :turnout_type
                ORDER BY "Pl_Forb", "Växelnr"
            '''),
            connection,
            params={"turnout_type": "EV-UIC60-760-1:15"},
        )
        failures = pd.read_sql(
            text('''
                SELECT *
                FROM ofeliadata
                WHERE "Växeltyp (ANL)" = :turnout_type
                  AND "Tågstörande" = :train_delaying
                  AND "Anläggningsdel (BVS)" IN (
                      'Omläggningsanordning', 'Kontrollanordning'
                  )
            '''),
            connection,
            params={
                "turnout_type": "EV-UIC60-760-1:15",
                "train_delaying": "Ja",
            },
        )

    print("BIS columns and descriptions:")
    print(bis_info.to_string(index=False))
    print("\nOfelia columns and descriptions:")
    print(ofelia_info.to_string(index=False))
    print("\nMatching BIS turnouts:")
    print(turnouts.to_string(index=False))

    failures.to_excel("railway_reliability_failures.xlsx", index=False)
    print(f"\nSaved {len(failures)} failure rows to railway_reliability_failures.xlsx")
    engine.dispose()


if __name__ == "__main__":
    main()
