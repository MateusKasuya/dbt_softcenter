WITH source AS (
    SELECT *
    FROM {{ source('mgp', 'TBHIS') }}
),

staging AS (
    SELECT
        codtransacao,
        INITCAP(descricao) AS descricao
    FROM source
)

SELECT *
FROM staging
