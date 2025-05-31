WITH source AS (
    SELECT *
    FROM {{ source('rcr', 'FRCTRC') }}
),

staging AS (
    SELECT
        -- Identificação e data do CT-e
        nroctrc::text,
        ufctrc,
        dataemissao::date,

        -- Situação e tipo do CT-e
        situacao,

        codfilemite::text,

        -- Filial
        codfilcobra::text,
        cgccpfdestina,

        -- Cliente
        cgccpfremete,
        cgccpffatura,
        codciddes::text,

        -- Destino
        codpro::text,

        -- Produto
        vlrtotfrete,

        -- Valores e peso do frete
        vlrpedagio,
        CASE indctetpcte
            WHEN '0' THEN 'Normal'
            WHEN '1' THEN 'Complementar'
            WHEN '2' THEN 'Anulação'
            WHEN '3' THEN 'Substituição'
            ELSE indctetpcte
        END AS tipo_cte,
        totalpeso / 1000.0 AS pesofrete_ton,
        vlrcarreto + vlrseguromerca + vlrpis + vlriapas + vlricmsst + vlricms AS vlrcusto,

        -- Fatura
        nrofatura || '-' || anofatura AS id_fatura

    FROM source
    WHERE situacao IN ('N', 'F')
)

SELECT *
FROM staging
