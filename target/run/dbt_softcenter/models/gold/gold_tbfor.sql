create table postgres.gold.gold_tbfor__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_silver_tbfor

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_silver_tbfor

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_silver_tbfor

    )

    select *

    from union_all
);
