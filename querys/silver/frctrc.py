def get_query_content(source: str) -> str:
    return f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{source}', 'FRCTRC')}}}}
),

staging AS (
    SELECT
        -- Identificação e data do CT-e
        nroctrc::text,
        ufctrc,
        dataemissao::DATE,

        -- Situação e tipo do CT-e
        situacao,

        CASE indctetpcte
            WHEN '0' THEN 'Normal'
            WHEN '1' THEN 'Complementar'
            WHEN '2' THEN 'Anulação'
            WHEN '3' THEN 'Substituição'
            ELSE indctetpcte
        END AS tipo_cte,

        -- Filial
        codfilemite::text,
        codfilcobra::text,

        -- Cliente
        cgccpfdestina,
        cgccpfremete,
        cgccpffatura,

        -- Destino
        codciddes::text,

        -- Produto
        codpro::text,

        -- Valores e peso do frete
        totalpeso / 1000.0 AS pesofrete_ton,
        vlrtotfrete,
        vlrpedagio,
        vlrcarreto + vlrseguromerca + vlrpis + vlriapas + vlricmsst + vlricms AS vlrcusto,

        -- Fatura
        nrofatura || '-' || anofatura AS id_fatura

    FROM source
    WHERE situacao IN ('N', 'F')
)

SELECT *
FROM staging
"""
