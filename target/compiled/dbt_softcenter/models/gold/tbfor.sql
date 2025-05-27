WITH union_all AS (

    SELECT

        'FN9' AS source,

        *

    FROM silver.fn9_tbfor

    UNION ALL

    SELECT

        'MGP' AS source,

        *

    FROM silver.mgp_tbfor

    UNION ALL

    SELECT

        'RCR' AS source,

        *

    FROM silver.rcr_tbfor

)

SELECT *

FROM union_all
