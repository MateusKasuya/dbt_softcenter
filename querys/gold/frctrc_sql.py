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
        vlrcusto,
        id_fatura
    FROM {{{{ref('fn9_frctrc')}}}}

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
        vlrcusto,
        id_fatura
    FROM {{{{ref('mgp_frctrc')}}}}

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
        vlrcusto,
        id_fatura
    FROM {{{{ref('rcr_frctrc')}}}}
)

SELECT *
FROM union_all
"""
