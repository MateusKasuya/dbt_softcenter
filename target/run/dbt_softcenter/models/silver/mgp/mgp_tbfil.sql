create table postgres.silver.mgp_tbfil__dbt_tmp

as

(
    with source as (
        select *
        from
            postgres.mgp."TBFIL"
    ),

    staging as (
        select
            codfil,
            INITCAP(nome) as nome
        from
            source
    )

    select *
    from
        staging
);
