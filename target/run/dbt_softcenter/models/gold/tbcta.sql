create table postgres.gold.tbcta__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_tbcta

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_tbcta

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_tbcta

    )

    select *

    from union_all
);
