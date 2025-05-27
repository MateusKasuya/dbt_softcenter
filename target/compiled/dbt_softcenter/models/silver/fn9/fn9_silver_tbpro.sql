WITH source AS (
    SELECT *
    FROM postgres.fn9."TBPRO"
),

staging AS (
    SELECT
        codpro,
        INITCAP(nome) AS nome
    FROM source
)

SELECT *
FROM staging
