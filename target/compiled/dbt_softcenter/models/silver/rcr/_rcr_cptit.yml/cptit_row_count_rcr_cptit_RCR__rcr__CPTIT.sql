SELECT 1
FROM (
    SELECT COUNT(*) AS source_count
    FROM postgres.rcr."CPTIT"
) AS s,
    (
        SELECT COUNT(*) AS model_count
        FROM gold.cptit
        WHERE source = 'RCR'
    ) AS m
WHERE s.source_count != m.model_count
