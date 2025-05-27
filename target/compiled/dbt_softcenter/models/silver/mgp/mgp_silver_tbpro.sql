WITH source AS (
    SELECT *
    FROM postgres.mgp."TBPRO"
),

staging AS (
    SELECT
        codpro,
        INITCAP(nome) AS nome
    FROM source
)

SELECT *
FROM staging
