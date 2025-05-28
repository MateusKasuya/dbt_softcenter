WITH union_all AS (
    SELECT
        'FN9' AS source,
        cli.*,
        cid.cidade_uf
    FROM silver.fn9_tbcli AS cli
    LEFT JOIN silver.tbcid AS cid ON cli.codcid = cid.codcid

    UNION ALL

    SELECT
        'MGP' AS source,
        cli.*,
        cid.cidade_uf
    FROM silver.mgp_tbcli AS cli
    LEFT JOIN silver.tbcid AS cid ON cli.codcid = cid.codcid

    UNION ALL

    SELECT
        'RCR' AS source,
        cli.*,
        cid.cidade_uf
    FROM silver.rcr_tbcli AS cli
    LEFT JOIN silver.tbcid AS cid ON cli.codcid = cid.codcid
)

SELECT *
FROM union_all
