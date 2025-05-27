create table postgres.gold.gold_tbcli__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_silver_tbcli

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_silver_tbcli

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_silver_tbcli

    )

    select *

    from union_all
);
