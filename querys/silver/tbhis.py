query = f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{schema}', 'TBHIS')}}}}
),

staging AS (
    SELECT
        codtransacao,
        INITCAP(descricao) as descricao
    FROM source
)

SELECT *
FROM staging

"""
