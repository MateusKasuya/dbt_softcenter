create table postgres.silver.mgp_factrc__dbt_tmp

as

(
    with source as (
        select *
        from
            postgres.mgp."FACTRC"
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
