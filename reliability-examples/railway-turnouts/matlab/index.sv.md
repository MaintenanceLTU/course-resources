# Fråga PostgreSQL med MATLAB

Använd MATLAB för att ansluta till kursens PostgreSQL-databas och fråga efter data om järnvägsväxlar. Exemplet använder MATLABs PostgreSQL-gränssnitt i [Database Toolbox](https://www.mathworks.com/help/database/ug/postgresql.html). Funktionen `fetch` kör frågan och returnerar resultatet som en MATLAB-tabell.

Matlab kod finns också tillgängligt [Matlab exempel](sql_query_examples.m).

## 1. Ange anslutningsuppgifterna

Ersätt exempelvärdena med anslutningsuppgifterna för ditt databaskonto.

```matlab
%% Create PostgreSQL connection parameters
user = "YOUR_DATABASE_USER";
password = "YOUR_DATABASE_PASSWORD";
host = "YOUR_VM_PUBLIC_IP";
dbname = "rail8";
port = 5432;
```

## 2. Anslut till PostgreSQL

Funktionen `postgresql` öppnar en anslutning med kontot och serveruppgifterna ovan.

```matlab
%% Connect to PostgreSQL
conn = postgresql(user, password, ...
    Server=host, DatabaseName=dbname, PortNumber=port);
```

## 3. Lista växeltyperna i BIS

SQL-frågan är samma som du kan köra i ett PostgreSQL-program. `fetch` skickar frågan via anslutningen och MATLAB sparar de returnerade raderna i `vxltyp`.

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

## 4. Välj växlar av en viss typ

Ändra värdet i `WHERE`-villkoret om du vill söka efter en annan växeltyp. Frågan returnerar driftplatsreferensen och växelnumret.

```matlab
query = [ ...
    'SELECT "Pl_Forb", "Växelnr" ' ...
    'FROM bisdata ' ...
    'WHERE "Växeltyp" = ''EV-UIC60-760-1:15'';' ...
];

vxl = fetch(conn, query);
disp(vxl)
```

## 5. Stäng anslutningen

Stäng databasanslutningen när du har kört klart frågorna.

```matlab
close(conn)
```
