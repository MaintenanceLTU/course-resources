# Railway Reliability

Examples for exploring railway asset and failure data from BIS and Ofelia with PostgreSQL and Python.

## Contents

SQL database connection and query examples for retrieving asset register and work-order data

- [SQL](sql/)
- [Python SQL](python/)
- [MATLAB SQL](matlab/)

Reliability analysis examples

- [Python non-repairable reliability analysis using a Weibull distribution](python/weibull-analysis.md)

## Connection setup

The examples expect the database tables `bisdata` and `ofeliadata` to be accessible to your account. Column names follow the source data, so names containing spaces or Swedish characters are quoted in SQL.

Your teacher will provide the database connection details:

- VM IP address, for example `156.xxx.xxx.xxx`
- Port: `5432`
- Database: `rail8`
- Username
- Password


## Column descriptions

The SQL examples include a query that lists the table columns and their PostgreSQL comments. Those comments must have been added to the database when the tables were created. If the query returns no rows, first check that you are connected to the correct database and schema.
