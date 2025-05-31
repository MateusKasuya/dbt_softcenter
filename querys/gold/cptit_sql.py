def get_query_content() -> str:
    return f"""
WITH union_all AS (
    SELECT
        'FN9' AS source,
        nrocontrole,
        anocontrole,
        codfil,
        cgccpfforne,
        codtransacao,
        vlrtotal,
        vlrpago,
        vlrsaldo,
        dataemissao,
        datamovto,
        datavencto,
        condicao_fatura,
        contareduz
    FROM {{{{ref('fn9_cptit')}}}}

    UNION ALL

    SELECT
        'MGP' AS source,
        nrocontrole,
        anocontrole,
        codfil,
        cgccpfforne,
        codtransacao,
        vlrtotal,
        vlrpago,
        vlrsaldo,
        dataemissao,
        datamovto,
        datavencto,
        condicao_fatura,
        contareduz
    FROM {{{{ref('mgp_cptit')}}}}


    UNION ALL

    SELECT
        'RCR' AS source,
        nrocontrole,
        anocontrole,
        codfil,
        cgccpfforne,
        codtransacao,
        vlrtotal,
        vlrpago,
        vlrsaldo,
        dataemissao,
        datamovto,
        datavencto,
        condicao_fatura,
        contareduz
    FROM {{{{ref('rcr_cptit')}}}}
)

SELECT *
FROM union_all
"""
