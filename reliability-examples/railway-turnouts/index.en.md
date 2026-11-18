# Railway Reliability

Examples for exploring railway asset and failure data from BIS and Ofelia with PostgreSQL and Python.

## Contents

- [SQL examples](sql/index.md)
- [Python SQL example](python/index.en.md)

## Connection setup

Install the packages listed in the repository's `requirements.txt`.

The examples expect the database tables `bisdata` and `ofeliadata` to be accessible to your account. Column names follow the source data, so names containing spaces or Swedish characters are quoted in SQL.

### Set credentials in environment variables

Your instructor will provide the database connection details:

- VM IP address, for example `156.xxx.xxx.xxx`
- Port: `5432`
- Database: `rail8`
- Username
- Password

Create a file named `.env` in the same folder as the Python script. Replace the example values with the host IP address and credentials provided for your account:

```env
SQL_ENDPOINT=YOUR_VM_PUBLIC_IP
SQL_DBNAME=rail8
STUDENT_USER=myuser
STUDENT_PASSWORD=yourpass
```

## Column descriptions

The SQL examples include a query that lists the table columns and their PostgreSQL comments. Those comments must have been added to the database when the tables were created. If the query returns no rows, first check that you are connected to the correct database and schema.
