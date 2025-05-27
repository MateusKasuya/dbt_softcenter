SELECT 1
FROM (
    SELECT COUNT(*) AS source_count
    FROM postgres.mgp."FRCTRC"
    WHERE situacao IN ('N', 'F')
) AS s,
    (
        SELECT COUNT(*) AS model_count
        FROM gold.frctrc
        WHERE source = 'MGP'
    ) AS m
WHERE s.source_count != m.model_count
