def get_query_content(table: str) -> str:
    return f"""
WITH union_all AS (
SELECT 
    'FN9' AS source,
    *
FROM fn9_silver_{table}

UNION ALL

SELECT 
    'MGP' AS source,
    *
FROM mgp_silver_{table}

UNION ALL

SELECT 
    'RCR' AS source,
    *
FROM rcr_silver_{table}
)

SELECT *
FROM union_all
"""
