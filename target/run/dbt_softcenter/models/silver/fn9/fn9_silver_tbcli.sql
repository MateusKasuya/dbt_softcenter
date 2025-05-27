create table postgres.silver.fn9_silver_tbcli__dbt_tmp

as

(
    with source as (
        select *
        from postgres.fn9."TBCLI"
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
