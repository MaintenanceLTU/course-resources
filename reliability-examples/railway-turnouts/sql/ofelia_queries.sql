-- List the asset parts available in Ofelia.
SELECT DISTINCT "Anläggningsdel (BVS)"
FROM ofeliadata
ORDER BY "Anläggningsdel (BVS)";

-- Find train-delaying failures for a turnout type and selected parts.
SELECT *
FROM ofeliadata
WHERE "Växeltyp (ANL)" = 'EV-UIC60-760-1:15'
  AND "Tågstörande" = 'Ja'
  AND "Anläggningsdel (BVS)" IN (
      'Omläggningsanordning',
      'Kontrollanordning'
  );
