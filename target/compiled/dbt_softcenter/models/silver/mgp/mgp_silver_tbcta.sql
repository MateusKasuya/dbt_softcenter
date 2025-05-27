WITH source AS (
    SELECT *
    FROM postgres.mgp."TBCTA"
),

staging AS (
    SELECT
        contareduz,
        nomeconta

    FROM source
)

SELECT *
FROM staging
