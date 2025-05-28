WITH source AS (
    SELECT *
    FROM
        {{ source('fn9', 'TBFIL') }}
),

staging AS (
    SELECT
        codfil,
        INITCAP(nome) AS filial
    FROM
        source
)

SELECT *
FROM
    staging
