WITH source AS (
    SELECT *
    FROM postgres.rcr."TBFOR"
),

staging AS (
    SELECT
        cgccpfforne,
        INITCAP(nomefantasia) AS nomefantasia
    FROM source
)

SELECT *
FROM staging
