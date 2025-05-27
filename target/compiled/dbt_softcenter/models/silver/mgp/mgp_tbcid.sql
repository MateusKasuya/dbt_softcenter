WITH source AS (
    SELECT *
    FROM postgres.mgp."TBCID"
),

staging AS (
    SELECT
        codcid,
        coduf,
        INITCAP(nome) AS nome,
        INITCAP(nome) || '-' || coduf AS cidade_uf,
        'Brasil,' || INITCAP(nome) || ',' || coduf AS localizacao_pbi

    FROM source
)

SELECT *
FROM staging
