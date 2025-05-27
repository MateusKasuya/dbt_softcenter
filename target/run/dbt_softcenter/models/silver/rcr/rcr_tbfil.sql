create table postgres.silver.rcr_tbfil__dbt_tmp

as

(
    with source as (
        select *
        from
            postgres.rcr."TBFIL"
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
