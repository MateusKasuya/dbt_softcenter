create table postgres.silver.rcr_silver_tbfor__dbt_tmp

as

(
    with source as (
        select *
        from postgres.rcr."TBFOR"
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
