SELECT 1
FROM (
    SELECT COALESCE(ROUND(SUM(vlrtotfrete)::NUMERIC, 1), 0) AS source_sum
    FROM postgres.mgp."FACTRC"
) AS s,
    (
        SELECT COALESCE(ROUND(SUM(vlrtotfrete)::NUMERIC, 1), 0) AS model_sum
        FROM gold.factrc
        WHERE source = 'MGP'
    ) AS m
WHERE NOT (s.source_sum IS NOT DISTINCT FROM m.model_sum)
