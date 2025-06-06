{% test factrc_sum_match(model, source_table, source_schema, column_name, nome_empresa) %}
    
    
    
    
    
    
SELECT 1
FROM (
    SELECT COALESCE(ROUND(SUM({{ column_name }})::NUMERIC, 1), 0) AS source_sum
    FROM {{ source(source_schema, source_table) }}
) s,
(
    SELECT COALESCE(ROUND(SUM({{ column_name }})::NUMERIC, 1), 0) AS model_sum
    FROM gold.factrc
    WHERE source = '{{ nome_empresa }}'
) m
WHERE NOT (s.source_sum IS NOT DISTINCT FROM m.model_sum)







{% endtest %}
