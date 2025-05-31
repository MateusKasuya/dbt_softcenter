WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM {{ ref('fn9_tbcid') }}

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM {{ ref('mgp_tbcid') }}

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM {{ ref('rcr_tbcid') }}
)

SELECT *
FROM union_all
