create table postgres.gold.tbpro__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_tbpro

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_tbpro

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_tbpro

    )

    select *

    from union_all
);
