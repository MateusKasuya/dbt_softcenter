SELECT 1
FROM (
    SELECT COUNT(*) AS source_count
    FROM postgres.fn9."FRCTRC"
    WHERE situacao IN ('N', 'F')
) AS s,
    (
        SELECT COUNT(*) AS model_count
        FROM gold.frctrc
        WHERE source = 'FN9'
    ) AS m
WHERE s.source_count != m.model_count
