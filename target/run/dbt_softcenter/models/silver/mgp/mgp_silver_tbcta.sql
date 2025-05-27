create table postgres.silver.mgp_silver_tbcta__dbt_tmp

as

(
    with source as (
        select *
        from postgres.mgp."TBCTA"
    ),

    staging as (
        select
            contareduz,
            nomeconta

        from source
    )

    select *
    from staging
);
