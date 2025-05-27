WITH union_all AS (

    SELECT

        'FN9' AS source,

        *

    FROM silver.fn9_tbpro

    UNION ALL

    SELECT

        'MGP' AS source,

        *

    FROM silver.mgp_tbpro

    UNION ALL

    SELECT

        'RCR' AS source,

        *

    FROM silver.rcr_tbpro

)

SELECT *

FROM union_all
