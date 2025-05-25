def get_query_content(table: str) -> str:
    return f"""
WITH union_all AS (
SELECT 
    'FN9' AS source,
    *
FROM silver.fn9_{table}

UNION ALL

SELECT 
    'MGP' AS source,
    *
FROM silver.mgp_{table}

UNION ALL

SELECT 
    'RCR' AS source,
    *
FROM silver.rcr_{table}
)

SELECT *
FROM union_all
"""
