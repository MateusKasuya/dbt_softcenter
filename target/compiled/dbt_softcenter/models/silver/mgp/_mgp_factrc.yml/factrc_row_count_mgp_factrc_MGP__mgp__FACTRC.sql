SELECT 1
FROM (
    SELECT COUNT(*) AS source_count
    FROM postgres.mgp."FACTRC"
) AS s,
    (
        SELECT COUNT(*) AS model_count
        FROM gold.factrc
        WHERE source = 'MGP'
    ) AS m
WHERE s.source_count != m.model_count
