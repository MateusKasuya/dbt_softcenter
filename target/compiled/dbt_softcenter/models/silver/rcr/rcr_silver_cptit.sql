WITH source AS (
    SELECT *
    FROM
        postgres.rcr."CPTIT"
),

staging AS (
    SELECT

        -- Primary Keys
        nrocontrole,
        anocontrole,

        -- Foreign Keys
        codfil,
        cgccpfforne,
        codtransacao,

        -- Valores
        vlrtotal,
        vlrsaldo,
        dataemissao::DATE,

        -- Datas
        datamovto::DATE,
        datavencto::DATE,
        vlrtotal - vlrsaldo AS vlrpago,

        -- Condicao Fatura
        CASE
            WHEN vlrsaldo = 0 THEN 'Pago'
            WHEN
                vlrsaldo > 0 AND CURRENT_DATE <= datavencto::DATE
                THEN 'A Pagar'
            ELSE 'Em Atraso'
        END AS condicao_fatura
    FROM
        source
)

SELECT *
FROM
    staging
