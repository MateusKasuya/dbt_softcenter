def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{source}', 'TBCLI')}}}}
),

staging AS (
    SELECT
        cgccpfcli,
        INITCAP(nomefantasia) AS cliente,
        codcid
    FROM source
)

SELECT *
FROM staging
"""
