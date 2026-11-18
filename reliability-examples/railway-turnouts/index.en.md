# Railway Reliability

Examples for exploring railway asset and failure data from BIS and Ofelia with PostgreSQL and Python.

## Contents

- [SQL examples](sql/)
- [Python example](python/query_data.py)

## Connection setup

Install the packages in the repository's `requirements.txt`. Copy `.env.example` to `.env` and enter the database connection values provided for your course. Keep `.env` private and never upload it.

The examples expect the database tables `bisdata` and `ofeliadata` to be accessible to your account. Column names follow the source data, so names containing spaces or Swedish characters are quoted in SQL.

## Column descriptions

The SQL examples include a query for table columns and their PostgreSQL comments. The comments must have been added to the database when the tables were created. If the query returns no rows, first check that you are connected to the right database and schema.
