def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{source}', 'TBHIS')}}}}
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
