create table postgres.gold.tbhis__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_tbhis

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_tbhis

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_tbhis

    )

    select *

    from union_all
);
