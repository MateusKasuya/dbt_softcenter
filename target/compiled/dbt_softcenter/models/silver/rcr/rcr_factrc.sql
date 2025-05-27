WITH source AS (
    SELECT *
    FROM
        postgres.rcr."FACTRC"
),

staging AS (
    SELECT
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
        nrofatura || '-' || anofatura AS id
    FROM
        source
)

SELECT *
FROM
    staging
