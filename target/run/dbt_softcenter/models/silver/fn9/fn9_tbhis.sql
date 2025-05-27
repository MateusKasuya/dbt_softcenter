create table postgres.silver.fn9_tbhis__dbt_tmp

as

(
    with source as (
        select *
        from postgres.fn9."TBHIS"
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
