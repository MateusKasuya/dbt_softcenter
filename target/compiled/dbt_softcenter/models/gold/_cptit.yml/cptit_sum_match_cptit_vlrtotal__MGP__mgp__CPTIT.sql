SELECT 1
FROM (
    SELECT COALESCE(ROUND(SUM(vlrtotal)::NUMERIC, 1), 0) AS source_sum
    FROM postgres.mgp."CPTIT"
) AS s,
    (
        SELECT COALESCE(ROUND(SUM(vlrtotal)::NUMERIC, 1), 0) AS model_sum
        FROM gold.cptit
        WHERE source = 'MGP'
    ) AS m
WHERE s.source_sum != m.model_sum
