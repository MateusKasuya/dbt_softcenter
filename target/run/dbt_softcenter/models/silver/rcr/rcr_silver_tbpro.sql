create table postgres.silver.rcr_silver_tbpro__dbt_tmp

as

(
    with source as (
        select *
        from postgres.rcr."TBPRO"
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
