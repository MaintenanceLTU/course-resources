# Querying PostgreSQL with MATLAB

Use MATLAB to connect to the course PostgreSQL database and query railway turnout data. This example uses MATLAB's PostgreSQL interface from the [Database Toolbox](https://www.mathworks.com/help/database/ug/postgresql.html). The `fetch` function runs a query and returns its result as a MATLAB table.

Code is also available [Matlab example](sql_query_examples.m).

## 1. Enter the connection details

Replace the example values with the connection details provided for your database credentials.

```matlab
%% Create PostgreSQL connection parameters
user = "YOUR_DATABASE_USER";
password = "YOUR_DATABASE_PASSWORD";
host = "YOUR_VM_PUBLIC_IP";
dbname = "rail8";
port = 5432;
```

## 2. Connect to PostgreSQL

The `postgresql` function opens a connection using the account and server details above.

```matlab
%% Connect to PostgreSQL
conn = postgresql(user, password, ...
    Server=host, DatabaseName=dbname, PortNumber=port);
```

## 3. List the turnout types in BIS

The SQL query is the same query you could run in a PostgreSQL client. `fetch` sends it through the connection, and MATLAB stores the returned rows in `vxltyp`.

```matlab
%% BIS

% Return all turnout types
query = [ ...
    'SELECT DISTINCT "Växeltyp" ' ...
    'FROM bisdata;' ...
];

vxltyp = fetch(conn, query);
disp(vxltyp)
```

## 4. Select turnouts of one type

Change the value in the `WHERE` condition to search for another turnout type. This query returns the location reference and turnout number.

```matlab
query = [ ...
    'SELECT "Pl_Forb", "Växelnr" ' ...
    'FROM bisdata ' ...
    'WHERE "Växeltyp" = ''EV-UIC60-760-1:15'';' ...
];

vxl = fetch(conn, query);
disp(vxl)
```

## 5. Close the connection

Close the database connection when you have finished querying.

```matlab
close(conn)
```
