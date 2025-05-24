
WITH union_all AS (
SELECT 
    'FN9' AS source,
    *
FROM fn9_silver_tbpro

UNION ALL

SELECT 
    'MGP' AS source,
    *
FROM mgp_silver_tbpro

UNION ALL

SELECT 
    'RCR' AS source,
    *
FROM rcr_silver_tbpro
)

SELECT *
FROM union_all
