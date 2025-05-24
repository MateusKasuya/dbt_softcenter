
WITH union_all AS (
SELECT 
    'FN9' AS source,
    *
FROM fn9_silver_tbcli

UNION ALL

SELECT 
    'MGP' AS source,
    *
FROM mgp_silver_tbcli

UNION ALL

SELECT 
    'RCR' AS source,
    *
FROM rcr_silver_tbcli
)

SELECT *
FROM union_all
