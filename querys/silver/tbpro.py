def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{source}', 'TBPRO')}}}}
),

staging AS (
    SELECT
        codpro,
        INITCAP(nome) as produto
    FROM source
)

SELECT *
FROM staging
"""
