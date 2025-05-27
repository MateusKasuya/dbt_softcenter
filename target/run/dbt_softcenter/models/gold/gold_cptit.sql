create table postgres.gold.gold_cptit__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_silver_cptit

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_silver_cptit

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_silver_cptit

    )

    select *

    from union_all
);
