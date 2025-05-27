WITH source AS (
    SELECT *
    FROM postgres.rcr."TBHIS"
),

staging AS (
    SELECT
        codtransacao,
        INITCAP(descricao) AS descricao
    FROM source
)

SELECT *
FROM staging
