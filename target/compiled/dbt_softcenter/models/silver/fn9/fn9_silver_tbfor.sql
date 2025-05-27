WITH source AS (
    SELECT *
    FROM postgres.fn9."TBFOR"
),

staging AS (
    SELECT
        cgccpfforne,
        INITCAP(nomefantasia) AS nomefantasia
    FROM source
)

SELECT *
FROM staging
