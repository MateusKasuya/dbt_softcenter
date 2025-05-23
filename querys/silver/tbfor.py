query = f"""
WITH source AS (
    SELECT *
    FROM {{{{source('{schema}', 'TBFOR')}}}}
),

staging AS (
    SELECT
        cgccpfforne,
        INITCAP(nomefantasia) as nomefantasia
    FROM source
)

SELECT *
FROM staging


"""
