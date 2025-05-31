def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT
        *
    FROM
        {{{{source('{source}', 'CPTIT')}}}}
),

staging AS (
    SELECT

        -- Primary Keys
        nrocontrole::text,
        anocontrole::text,

        -- Foreign Keys
        codfil::text,
        cgccpfforne::text,
        codtransacao::text,

        -- Valores
        vlrtotal,
        vlrtotal - vlrsaldo AS vlrpago,
        vlrsaldo,

        -- Datas
        dataemissao::DATE,
        datamovto::DATE,
        datavencto::DATE,

        -- Condicao Fatura
        CASE
            WHEN vlrsaldo = 0 THEN 'Pago'
            WHEN vlrsaldo > 0 AND CURRENT_DATE <= datavencto::DATE THEN 'A Pagar'
            ELSE 'Em Atraso'
        END AS condicao_fatura,
        
        contareduz::text
    FROM
        source
)

SELECT
    *
FROM
    staging
"""
