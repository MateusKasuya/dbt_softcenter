create table postgres.silver.fn9_silver_tbfor__dbt_tmp

as

(
    with source as (
        select *
        from postgres.fn9."TBFOR"
    ),

    staging as (
        select
            cgccpfforne,
            INITCAP(nomefantasia) as nomefantasia
        from source
    )

    select *
    from staging
);
