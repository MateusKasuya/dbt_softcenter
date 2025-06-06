SELECT 1
FROM (
    SELECT COALESCE(ROUND(SUM(vlrtotfrete)::NUMERIC, 1), 0) AS source_sum
    FROM postgres.rcr."FRCTRC"
    WHERE situacao IN ('N', 'F')
) AS s,
    (
        SELECT COALESCE(ROUND(SUM(vlrtotfrete)::NUMERIC, 1), 0) AS model_sum
        FROM gold.frctrc
        WHERE source = 'RCR'
    ) AS m
WHERE NOT (s.source_sum IS NOT DISTINCT FROM m.model_sum)
