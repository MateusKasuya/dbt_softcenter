
WITH source AS (
    SELECT
        *
    FROM
        {{source('rcr', 'FACTRC')}}
),

staging AS (
    SELECT
        nrofatura,
        anofatura,
        nrofatura || '-' || anofatura AS id,
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
        codtransacao
    FROM
        source
)

SELECT
    *
FROM
    staging
