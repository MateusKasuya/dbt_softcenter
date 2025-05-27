create table postgres.gold.gold_factrc__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_silver_factrc

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_silver_factrc

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_silver_factrc

    )

    select *

    from union_all
);
