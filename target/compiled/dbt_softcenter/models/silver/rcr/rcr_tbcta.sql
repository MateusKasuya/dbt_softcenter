WITH source AS (
    SELECT *
    FROM postgres.rcr."TBCTA"
),

staging AS (
    SELECT
        contareduz,
        nomeconta

    FROM source
)

SELECT *
FROM staging
