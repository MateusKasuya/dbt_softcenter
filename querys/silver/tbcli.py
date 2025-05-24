def get_query_content(schema: str) -> str:
    return f"""
query = f
WITH source AS (
    SELECT *
    FROM {{{{source('{schema}', 'TBCLI')}}}}
),

staging AS (
    SELECT
        cgccpfcli,
        INITCAP(nomefantasia) AS nomefantasia
    FROM source
)

SELECT *
FROM staging
"""
