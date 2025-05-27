WITH source AS (
    SELECT *
    FROM postgres.mgp."TBHIS"
),

staging AS (
    SELECT
        codtransacao,
        INITCAP(descricao) AS descricao
    FROM source
)

SELECT *
FROM staging
