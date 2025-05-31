def get_query_content(table: str) -> str:
    return f"""
WITH union_all AS (
SELECT 
    'FN9' AS source,
    *
FROM {{{{ref('fn9_{table}')}}}}

UNION ALL

SELECT 
    'MGP' AS source,
    *
FROM {{{{ref('mgp_{table}')}}}}

UNION ALL

SELECT 
    'RCR' AS source,
    *
FROM {{{{ref('rcr_{table}')}}}}
)

SELECT *
FROM union_all
"""
