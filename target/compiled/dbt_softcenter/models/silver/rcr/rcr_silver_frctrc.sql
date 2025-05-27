WITH source AS (
    SELECT *
    FROM postgres.rcr."FRCTRC"
),

staging AS (
    SELECT
        -- Identificação e data do CT-e
        nroctrc,
        ufctrc,
        dataemissao::DATE,

        -- Situação e tipo do CT-e
        situacao,

        codfilemite,

        -- Filial
        codfilcobra,
        cgccpfdestina,

        -- Cliente
        cgccpfremete,
        cgccpffatura,
        codciddes,

        -- Destino
        codpro,

        -- Produto
        vlrtotfrete,

        -- Valores e peso do frete
        vlrpedagio,
        vlrimposto,
        CASE indctetpcte
            WHEN '0' THEN 'Normal'
            WHEN '1' THEN 'Complementar'
            WHEN '2' THEN 'Anulação'
            WHEN '3' THEN 'Substituição'
            ELSE indctetpcte
        END AS tipo_cte,
        pesofrete / 1000.0 AS pesofrete_ton,

        -- Fatura
        nrofatura || '-' || anofatura AS id_fatura

    FROM source
    WHERE situacao IN ('N', 'F')
)

SELECT *
FROM staging
