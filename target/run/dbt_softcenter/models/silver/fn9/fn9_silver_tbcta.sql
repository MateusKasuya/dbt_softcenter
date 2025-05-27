create table postgres.silver.fn9_silver_tbcta__dbt_tmp

as

(
    with source as (
        select *
        from postgres.fn9."TBCTA"
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
