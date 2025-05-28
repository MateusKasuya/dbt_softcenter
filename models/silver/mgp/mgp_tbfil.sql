WITH source AS (
    SELECT *
    FROM
        {{ source('mgp', 'TBFIL') }}
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
