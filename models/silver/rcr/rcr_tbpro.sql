WITH source AS (
    SELECT *
    FROM {{ source('rcr', 'TBPRO') }}
),

staging AS (
    SELECT
        codpro,
        INITCAP(nome) AS nome
    FROM source
)

SELECT *
FROM staging
