select
    count(*) as failures,
    count(*) != 0 as should_warn,
    count(*) != 0 as should_error
from (

    select 1
    from (
        select coalesce(round(sum(vlrtotfrete)::NUMERIC, 1), 0) as source_sum
        from postgres.fn9."FRCTRC"
        where situacao in ('N', 'F')
    ) as s,
        (
            select coalesce(round(sum(vlrtotfrete)::NUMERIC, 1), 0) as model_sum
            from gold.frctrc
            where source = 'FN9'
        ) as m
    where not (s.source_sum is not distinct from m.model_sum)

) as dbt_internal_test
