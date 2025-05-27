create table postgres.silver.mgp_silver_tbcli__dbt_tmp

as

(
    with source as (
        select *
        from postgres.mgp."TBCLI"
    ),

    staging as (
        select
            cgccpfcli,
            INITCAP(nomefantasia) as nomefantasia
        from source
    )

    select *
    from staging
);
