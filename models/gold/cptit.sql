WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM silver.fn9_cptit

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM silver.mgp_cptit

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM silver.rcr_cptit
)

SELECT *
FROM union_all
