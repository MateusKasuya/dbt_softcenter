def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{source}', 'TBFOR')}}}}
),

staging AS (
    SELECT
        cgccpfforne,
        INITCAP(nomefantasia) as fornecedor
    FROM source
)

SELECT *
FROM staging
"""
