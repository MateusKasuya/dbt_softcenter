WITH source AS (
    SELECT *
    FROM
        {{ source('fn9', 'FACTRC') }}
),

staging AS (
    SELECT
        nrofatura,
        anofatura,
        cgccpfremete,
        cgccpfdestina,
        cgccpffatura,
        codfilfatur,
        codfilcobra,
        codfilemite,
        codciddes,
        codcidori,
        codpro,
        dataemissao::DATE,
        datavencto::DATE,
        datarecbto::DATE,
        vlrfatura,
        vlrrecbto,
        vlrsaldo,
        contareduz,
        codtransacao,
        nrofatura || '-' || anofatura AS id,
        datarecbto::DATE - dataemissao::DATE AS dias_recebimento,
        CASE
            WHEN datavencto < CURRENT_DATE AND vlrsaldo > 0 THEN 'Em Atraso'
            WHEN vlrsaldo = 0 THEN 'Recebida'
            ELSE 'A Receber'
        END AS condicao_fatura
    FROM
        source
)

SELECT *
FROM
    staging
