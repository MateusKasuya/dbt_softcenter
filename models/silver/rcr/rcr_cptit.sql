WITH source AS (
    SELECT *
    FROM
        {{ source('rcr', 'CPTIT') }}
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
        vlrsaldo,
        dataemissao::date,

        -- Datas
        datamovto::date,
        datavencto::date,
        contareduz::text,

        -- Condicao Fatura
        vlrtotal - vlrsaldo AS vlrpago,

        CASE
            WHEN vlrsaldo = 0 THEN 'Pago'
            WHEN vlrsaldo > 0 AND CURRENT_DATE <= datavencto::date THEN 'A Pagar'
            ELSE 'Em Atraso'
        END AS condicao_fatura
    FROM
        source
)

SELECT *
FROM
    staging
