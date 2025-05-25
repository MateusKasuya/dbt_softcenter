WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM silver.fn9_tbcid

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM silver.mgp_tbcid

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM silver.rcr_tbcid
)

SELECT *
FROM union_all
