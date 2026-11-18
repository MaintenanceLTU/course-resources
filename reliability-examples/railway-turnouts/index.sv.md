# Tillförlitlighet järnväg

Exempel på hur du utforskar anläggnings- och feldata från BIS och Ofelia med PostgreSQL och Python.

## Innehåll
Exempel på anslutning och SQL *queries* för att hämta anläggningsregister- och arbetsorderdata

- [SQL](sql/)
- [SQL med Python](python/index.sv.md)
- [SQL med MATLAB](matlab/index.sv.md)

Exempel på tillförlitlighetsanalyser

- [Python: Icke-reparerbar tillförlitlighetsanalys med Weibullfördelning](python/weibull-analysis.sv.md)


## Anslutning

Exemplen förutsätter att ditt konto har åtkomst till databastabellerna `bisdata` och `ofeliadata`. Kolumnnamnen följer källdatan. Därför omges namn med mellanslag eller svenska tecken av citattecken i SQL.

Din lärare ger dig uppgifterna för databasanslutningen:

- VM (serverns) IP-adress, till exempel `156.xxx.xxx.xxx`
- Port: `5432`
- Databas: `rail8`
- Användarnamn
- Lösenord

## Kolumnbeskrivningar

SQL-exemplen innehåller en fråga som visar tabellernas kolumner och deras PostgreSQL-kommentarer. Kommentarerna måste ha lagts till i databasen när tabellerna skapades. Om frågan inte returnerar några rader bör du först kontrollera att du är ansluten till rätt databas och schema.
