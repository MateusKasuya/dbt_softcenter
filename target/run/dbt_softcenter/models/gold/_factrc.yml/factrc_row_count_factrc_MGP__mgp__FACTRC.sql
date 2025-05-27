select
    count(*) as failures,
    count(*) != 0 as should_warn,
    count(*) != 0 as should_error
from (

    select 1
    from (
        select count(*) as source_count
        from postgres.mgp."FACTRC"
    ) as s,
        (
            select count(*) as model_count
            from gold.factrc
            where source = 'MGP'
        ) as m
    where s.source_count != m.model_count

) as dbt_internal_test
