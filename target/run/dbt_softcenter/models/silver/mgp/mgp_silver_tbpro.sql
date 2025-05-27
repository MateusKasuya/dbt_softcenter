create table postgres.silver.mgp_silver_tbpro__dbt_tmp

as

(
    with source as (
        select *
        from postgres.mgp."TBPRO"
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
