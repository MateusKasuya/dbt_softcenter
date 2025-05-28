WITH source AS (
    SELECT *
    FROM {{ source('mgp', 'TBFOR') }}
),

staging AS (
    SELECT
        cgccpfforne,
        INITCAP(nomefantasia) AS fornecedor
    FROM source
)

SELECT *
FROM staging
