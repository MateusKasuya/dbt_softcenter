create table postgres.silver.fn9_tbpro__dbt_tmp

as

(
    with source as (
        select *
        from postgres.fn9."TBPRO"
    ),

    staging as (
        select
            codpro,
            INITCAP(nome) as nome
        from source
    )

    select *
    from staging
);
