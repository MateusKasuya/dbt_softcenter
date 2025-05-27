SELECT 1
FROM (
    SELECT COALESCE(ROUND(SUM(vlrfatura)::NUMERIC, 1), 0) AS source_sum
    FROM postgres.fn9."FACTRC"
) AS s,
    (
        SELECT COALESCE(ROUND(SUM(vlrfatura)::NUMERIC, 1), 0) AS model_sum
        FROM gold.factrc
        WHERE source = 'FN9'
    ) AS m
WHERE NOT (s.source_sum IS NOT DISTINCT FROM m.model_sum)
