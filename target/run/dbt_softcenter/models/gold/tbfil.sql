create table postgres.gold.tbfil__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_tbfil

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_tbfil

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_tbfil

    )

    select *

    from union_all
);
