WITH source AS (
    SELECT *
    FROM
        postgres.rcr."TBFIL"
),

staging AS (
    SELECT
        codfil,
        INITCAP(nome) AS nome
    FROM
        source
)

SELECT *
FROM
    staging
