def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT
        *
    FROM
        {{{{source('{source}', 'FACTRC')}}}}
),

staging AS (
    SELECT
        nrofatura,
        anofatura,
        nrofatura || '-' || anofatura AS id,
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
        CASE
            WHEN datavencto < CURRENT_DATE AND vlrsaldo > 0 THEN 'Em Atraso'
            WHEN vlrsaldo = 0 THEN 'Recebida'
            ELSE 'A Receber'
        END AS condicao_fatura,
        contareduz,
        codtransacao
    FROM
        source
)

SELECT
    *
FROM
    staging
"""
