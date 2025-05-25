WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM silver.fn9_frctrc

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM silver.mgp_frctrc

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM silver.rcr_frctrc
)

SELECT *
FROM union_all
