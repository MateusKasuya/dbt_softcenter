WITH source AS (
    SELECT *
    FROM {{ source('rcr', 'TBPRO') }}
),

staging AS (
    SELECT
        codpro,
        INITCAP(nome) AS produto
    FROM source
)

SELECT *
FROM staging
