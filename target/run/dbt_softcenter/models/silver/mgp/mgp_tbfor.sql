create table postgres.silver.mgp_tbfor__dbt_tmp

as

(
    with source as (
        select *
        from postgres.mgp."TBFOR"
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
