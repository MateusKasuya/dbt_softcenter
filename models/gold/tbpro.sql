WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM {{ ref('fn9_tbpro') }}

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM {{ ref('mgp_tbpro') }}

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM {{ ref('rcr_tbpro') }}
)

SELECT *
FROM union_all
