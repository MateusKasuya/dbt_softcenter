create table postgres.silver.fn9_silver_tbfil__dbt_tmp

as

(
    with source as (
        select *
        from
            postgres.fn9."TBFIL"
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
