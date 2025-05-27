WITH source AS (
    SELECT *
    FROM
        postgres.fn9."TBFIL"
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
