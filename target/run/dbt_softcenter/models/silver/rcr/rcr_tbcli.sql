create table postgres.silver.rcr_tbcli__dbt_tmp

as

(
    with source as (
        select *
        from postgres.rcr."TBCLI"
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
