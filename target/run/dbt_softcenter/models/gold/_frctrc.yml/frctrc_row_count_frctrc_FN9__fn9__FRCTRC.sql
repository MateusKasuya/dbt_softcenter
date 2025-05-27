select
    count(*) as failures,
    count(*) != 0 as should_warn,
    count(*) != 0 as should_error
from (

    select 1
    from (
        select count(*) as source_count
        from postgres.fn9."FRCTRC"
        where situacao in ('N', 'F')
    ) as s,
        (
            select count(*) as model_count
            from gold.frctrc
            where source = 'FN9'
        ) as m
    where s.source_count != m.model_count

) as dbt_internal_test
