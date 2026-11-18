-- List the turnout types available in BIS.
SELECT DISTINCT "Växeltyp"
FROM bisdata
ORDER BY "Växeltyp";

-- Find locations and turnout numbers for one turnout type.
SELECT "Pl_Forb", "Växelnr"
FROM bisdata
WHERE "Växeltyp" = 'EV-UIC60-760-1:15'
ORDER BY "Pl_Forb", "Växelnr";
