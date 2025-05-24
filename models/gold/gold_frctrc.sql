
WITH union_all AS (
SELECT 
    'FN9' AS source,
    *
FROM fn9_silver_frctrc

UNION ALL

SELECT 
    'MGP' AS source,
    *
FROM mgp_silver_frctrc

UNION ALL

SELECT 
    'RCR' AS source,
    *
FROM rcr_silver_frctrc
)

SELECT *
FROM union_all
