create table postgres.silver.rcr_silver_frctrc__dbt_tmp

as

(
    with source as (
        select *
        from postgres.rcr."FRCTRC"
    ),

    staging as (
        select
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
            case indctetpcte
                when '0' then 'Normal'
                when '1' then 'Complementar'
                when '2' then 'Anulação'
                when '3' then 'Substituição'
                else indctetpcte
            end as tipo_cte,
            pesofrete / 1000.0 as pesofrete_ton,

            -- Fatura
            nrofatura || '-' || anofatura as id_fatura

        from source
        where situacao in ('N', 'F')
    )

    select *
    from staging
);
