WITH source AS (
    SELECT *
    FROM {{ source('rcr', 'TBCLI') }}
),

staging AS (
    SELECT
        cgccpfcli,
        codcid,
        INITCAP(nomefantasia) AS cliente
    FROM source
)

SELECT *
FROM staging
