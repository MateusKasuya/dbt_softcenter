WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM {{ ref('fn9_tbcta') }}

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM {{ ref('mgp_tbcta') }}

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM {{ ref('rcr_tbcta') }}
)

SELECT *
FROM union_all
