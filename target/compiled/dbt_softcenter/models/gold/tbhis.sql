WITH union_all AS (

    SELECT

        'FN9' AS source,

        *

    FROM silver.fn9_tbhis

    UNION ALL

    SELECT

        'MGP' AS source,

        *

    FROM silver.mgp_tbhis

    UNION ALL

    SELECT

        'RCR' AS source,

        *

    FROM silver.rcr_tbhis

)

SELECT *

FROM union_all
