create table postgres.gold.frctrc__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_frctrc

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_frctrc

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_frctrc

    )

    select *

    from union_all
);
