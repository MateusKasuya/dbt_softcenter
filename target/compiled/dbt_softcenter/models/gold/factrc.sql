WITH union_all AS (

    SELECT

        'FN9' AS source,

        *

    FROM silver.fn9_factrc

    UNION ALL

    SELECT

        'MGP' AS source,

        *

    FROM silver.mgp_factrc

    UNION ALL

    SELECT

        'RCR' AS source,

        *

    FROM silver.rcr_factrc

)

SELECT *

FROM union_all
