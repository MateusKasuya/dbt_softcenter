create table postgres.silver.fn9_silver_cptit__dbt_tmp

as

(
    with source as (
        select *
        from
            postgres.fn9."CPTIT"
    ),

    staging as (
        select

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
            vlrtotal - vlrsaldo as vlrpago,

            -- Condicao Fatura
            case
                when vlrsaldo = 0 then 'Pago'
                when
                    vlrsaldo > 0 and CURRENT_DATE <= datavencto::DATE
                    then 'A Pagar'
                else 'Em Atraso'
            end as condicao_fatura
        from
            source
    )

    select *
    from
        staging
);
