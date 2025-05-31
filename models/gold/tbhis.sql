WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM {{ ref('fn9_tbhis') }}

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM {{ ref('mgp_tbhis') }}

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM {{ ref('rcr_tbhis') }}
)

SELECT *
FROM union_all
