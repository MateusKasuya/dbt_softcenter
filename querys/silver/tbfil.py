def get_query_content(schema: str) -> str:
    return f"""
query = f
WITH source AS (
    SELECT
        *
    FROM
        {{{{source('{schema}', 'TBFIL')}}}}
),

staging AS (
    SELECT
        codfil,
        INITCAP(nome) AS nome
    FROM
        source
)

SELECT
    *
FROM
    staging
"""
