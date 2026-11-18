# Järnvägsdriftsäkerhet

Exempel på hur du kan utforska anläggnings- och feldata från BIS och Ofelia med PostgreSQL och Python.

## Innehåll

- [SQL-exempel](sql/)
- [Python-exempel](python/query_data.py)

## Anslutning

Installera paketen i repots `requirements.txt`. Kopiera `.env.example` till `.env` och fyll i de anslutningsuppgifter du fått för kursen. Håll `.env` privat och ladda aldrig upp den.

Exemplen förutsätter att ditt konto har åtkomst till tabellerna `bisdata` och `ofeliadata`. Kolumnnamnen följer källdatan, så namn med mellanslag eller svenska tecken omges av citattecken i SQL.

## Kolumnbeskrivningar

SQL-exemplen innehåller en fråga som visar tabellernas kolumner och PostgreSQL-kommentarer. Kommentarerna måste ha lagts in i databasen när tabellerna skapades. Om frågan inte returnerar några rader, kontrollera först att du är ansluten till rätt databas och schema.
