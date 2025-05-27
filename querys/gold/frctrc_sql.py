def get_query_content() -> str:
    return f"""
WITH union_all AS (
    SELECT
        'FN9' AS source,
        nroctrc,
        ufctrc,
        dataemissao,
        situacao,
        tipo_cte,
        codfilemite,
        codfilcobra,
        cgccpfdestina,
        cgccpfremete,
        cgccpffatura,
        codciddes,
        codpro,
        pesofrete_ton,
        vlrtotfrete,
        vlrpedagio,
        vlrimposto,
        id_fatura
    FROM silver.fn9_frctrc

    UNION ALL

    SELECT
        'MGP' AS source,
        nroctrc,
        ufctrc,
        dataemissao,
        situacao,
        tipo_cte,
        codfilemite,
        codfilcobra,
        cgccpfdestina,
        cgccpfremete,
        cgccpffatura,
        codciddes,
        codpro,
        pesofrete_ton,
        vlrtotfrete,
        vlrpedagio,
        vlrimposto,
        id_fatura
    FROM silver.mgp_frctrc

    UNION ALL

    SELECT
        'RCR' AS source,
        nroctrc,
        ufctrc,
        dataemissao,
        situacao,
        tipo_cte,
        codfilemite,
        codfilcobra,
        cgccpfdestina,
        cgccpfremete,
        cgccpffatura,
        codciddes,
        codpro,
        pesofrete_ton,
        vlrtotfrete,
        vlrpedagio,
        vlrimposto,
        id_fatura
    FROM silver.rcr_frctrc
)

SELECT *
FROM union_all
"""
