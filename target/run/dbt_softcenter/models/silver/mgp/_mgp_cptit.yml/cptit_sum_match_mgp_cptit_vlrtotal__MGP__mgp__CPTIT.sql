select
    count(*) as failures,
    count(*) != 0 as should_warn,
    count(*) != 0 as should_error
from (

    select 1
    from (
        select coalesce(round(sum(vlrtotal)::NUMERIC, 1), 0) as source_sum
        from postgres.mgp."CPTIT"
    ) as s,
        (
            select coalesce(round(sum(vlrtotal)::NUMERIC, 1), 0) as model_sum
            from gold.cptit
            where source = 'MGP'
        ) as m
    where s.source_sum != m.model_sum

) as dbt_internal_test
