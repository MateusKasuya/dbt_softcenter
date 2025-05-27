WITH source AS (
    SELECT *
    FROM postgres.fn9."TBHIS"
),

staging AS (
    SELECT
        codtransacao,
        INITCAP(descricao) AS descricao
    FROM source
)

SELECT *
FROM staging
