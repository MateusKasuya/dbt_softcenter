WITH source AS (
    SELECT *
    FROM {{ source('fn9', 'TBFOR') }}
),

staging AS (
    SELECT
        cgccpfforne,
        INITCAP(nomefantasia) AS nomefantasia
    FROM source
)

SELECT *
FROM staging
