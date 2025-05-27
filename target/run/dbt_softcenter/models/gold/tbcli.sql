create table postgres.gold.tbcli__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_tbcli

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_tbcli

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_tbcli

    )

    select *

    from union_all
);
