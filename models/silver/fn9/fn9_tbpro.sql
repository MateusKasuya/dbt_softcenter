WITH source AS (
    SELECT *
    FROM {{ source('fn9', 'TBPRO') }}
),

staging AS (
    SELECT
        codpro,
        INITCAP(nome) AS nome
    FROM source
)

SELECT *
FROM staging
