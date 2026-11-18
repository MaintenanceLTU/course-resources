# Järnvägsdriftsäkerhet

Exempel på hur du utforskar anläggnings- och feldata från BIS och Ofelia med PostgreSQL och Python.

## Innehåll

- [SQL-exempel](sql/)
- [Python-exempel med SQL](python/index.sv.md)

## Anslutning

Installera paketen som anges i repots `requirements.txt`.

Exemplen förutsätter att ditt konto har åtkomst till databastabellerna `bisdata` och `ofeliadata`. Kolumnnamnen följer källdatan. Därför omges namn med mellanslag eller svenska tecken av citattecken i SQL.

### Ange inloggningsuppgifter som miljövariabler

Din lärare ger dig uppgifterna för databasanslutningen:

- VM (serverns) IP-adress, till exempel `156.xxx.xxx.xxx`
- Port: `5432`
- Databas: `rail8`
- Användarnamn
- Lösenord

Skapa en fil med namnet `.env` i samma mapp som Python-skriptet. Ersätt exempelvärdena med IP-adressen och inloggningsuppgifterna du fått:

```env
SQL_ENDPOINT=YOUR_VM_PUBLIC_IP
SQL_DBNAME=rail8
STUDENT_USER=myuser
STUDENT_PASSWORD=yourpass
```

## Kolumnbeskrivningar

SQL-exemplen innehåller en fråga som visar tabellernas kolumner och deras PostgreSQL-kommentarer. Kommentarerna måste ha lagts till i databasen när tabellerna skapades. Om frågan inte returnerar några rader bör du först kontrollera att du är ansluten till rätt databas och schema.
