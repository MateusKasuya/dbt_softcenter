WITH source AS (
    SELECT *
    FROM postgres.fn9."TBCLI"
),

staging AS (
    SELECT
        cgccpfcli,
        INITCAP(nomefantasia) AS nomefantasia
    FROM source
)

SELECT *
FROM staging
