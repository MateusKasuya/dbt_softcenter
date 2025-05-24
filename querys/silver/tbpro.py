def get_query_content(schema: str) -> str:
    return f"""
query = f
WITH source AS (
    SELECT *
    FROM {{{{source('{schema}', 'TBPRO')}}}}
),

staging AS (
    SELECT
        codpro,
        INITCAP(nome) as nome
    FROM source
)

SELECT *
FROM staging
"""
