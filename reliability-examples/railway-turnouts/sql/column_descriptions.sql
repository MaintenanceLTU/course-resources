-- Show columns and their PostgreSQL comments for the BIS and Ofelia tables.
-- Change current_schema() below if the tables are in a different schema.
SELECT
    c.table_schema,
    c.table_name,
    c.column_name,
    pg_catalog.col_description(
        format('%I.%I', c.table_schema, c.table_name)::regclass,
        c.ordinal_position
    ) AS description
FROM information_schema.columns AS c
WHERE c.table_name IN ('bisdata', 'ofeliadata')
  AND c.table_schema = current_schema()
ORDER BY c.table_name, c.ordinal_position;
