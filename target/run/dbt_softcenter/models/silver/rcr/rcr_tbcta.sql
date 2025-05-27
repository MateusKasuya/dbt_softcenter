create table postgres.silver.rcr_tbcta__dbt_tmp

as

(
    with source as (
        select *
        from postgres.rcr."TBCTA"
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
