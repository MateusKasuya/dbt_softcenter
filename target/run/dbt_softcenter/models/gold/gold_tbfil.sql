create table postgres.gold.gold_tbfil__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_silver_tbfil

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_silver_tbfil

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_silver_tbfil

    )

    select *

    from union_all
);
