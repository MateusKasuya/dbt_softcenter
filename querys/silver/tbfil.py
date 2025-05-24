def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT
        *
    FROM
        {{{{source('{source}', 'TBFIL')}}}}
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
