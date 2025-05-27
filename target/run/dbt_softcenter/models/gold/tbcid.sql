create table postgres.gold.tbcid__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_tbcid

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_tbcid

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_tbcid

    )

    select *

    from union_all
);
