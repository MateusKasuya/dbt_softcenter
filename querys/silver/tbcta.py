def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{source}', 'TBCTA')}}}}
),

staging AS (
    SELECT
        contareduz,
        INITCAP(nomeconta) AS nomeconta

    FROM source
)

SELECT *
FROM staging
"""
