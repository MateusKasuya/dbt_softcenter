create table postgres.silver.mgp_tbhis__dbt_tmp

as

(
    with source as (
        select *
        from postgres.mgp."TBHIS"
    ),

    staging as (
        select
            codtransacao,
            INITCAP(descricao) as descricao
        from source
    )

    select *
    from staging
);
