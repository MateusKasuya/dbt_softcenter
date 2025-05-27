create table postgres.silver.rcr_silver_factrc__dbt_tmp

as

(
    with source as (
        select *
        from
            postgres.rcr."FACTRC"
    ),

    staging as (
        select
            nrofatura,
            anofatura,
            cgccpfremete,
            cgccpfdestina,
            cgccpffatura,
            codfilfatur,
            codfilcobra,
            codfilemite,
            codciddes,
            codcidori,
            codpro,
            dataemissao::DATE,
            datavencto::DATE,
            datarecbto::DATE,
            vlrfatura,
            vlrrecbto,
            vlrsaldo,
            contareduz,
            codtransacao,
            nrofatura || '-' || anofatura as id
        from
            source
    )

    select *
    from
        staging
);
