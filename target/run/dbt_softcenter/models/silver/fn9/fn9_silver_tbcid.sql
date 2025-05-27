create table postgres.silver.fn9_silver_tbcid__dbt_tmp

as

(
    with source as (
        select *
        from postgres.fn9."TBCID"
    ),

    staging as (
        select
            codcid,
            coduf,
            INITCAP(nome) as nome,
            INITCAP(nome) || '-' || coduf as cidade_uf,
            'Brasil,' || INITCAP(nome) || ',' || coduf as localizacao_pbi

        from source
    )

    select *
    from staging
);
