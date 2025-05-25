WITH source AS (
    SELECT *
    FROM {{ source('fn9', 'TBHIS') }}
),

staging AS (
    SELECT
        codtransacao,
        INITCAP(descricao) AS descricao
    FROM source
)

SELECT *
FROM staging
