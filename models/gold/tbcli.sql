WITH union_all AS (
    SELECT
        'FN9' AS source,
        *
    FROM {{ ref('fn9_tbcli') }}

    UNION ALL

    SELECT
        'MGP' AS source,
        *
    FROM {{ ref('mgp_tbcli') }}

    UNION ALL

    SELECT
        'RCR' AS source,
        *
    FROM {{ ref('rcr_tbcli') }}
)

SELECT *
FROM union_all
