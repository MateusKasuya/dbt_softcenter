create table postgres.silver.rcr_silver_tbhis__dbt_tmp

as

(
    with source as (
        select *
        from postgres.rcr."TBHIS"
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
