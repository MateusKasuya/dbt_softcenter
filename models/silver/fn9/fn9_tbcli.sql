WITH source AS (
    SELECT *
    FROM {{ source('fn9', 'TBCLI') }}
),

staging AS (
    SELECT
        cgccpfcli,
        INITCAP(nomefantasia) AS cliente
    FROM source
)

SELECT *
FROM staging
