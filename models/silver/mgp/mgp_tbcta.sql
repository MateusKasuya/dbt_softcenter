WITH source AS (
    SELECT *
    FROM {{ source('mgp', 'TBCTA') }}
),

staging AS (
    SELECT
        contareduz,
        INITCAP(nomeconta) AS nomeconta

    FROM source
)

SELECT *
FROM staging
