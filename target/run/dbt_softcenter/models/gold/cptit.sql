create table postgres.gold.cptit__dbt_tmp

as

(
    with union_all as (

        select

            'FN9' as source,

            *

        from silver.fn9_cptit

        union all

        select

            'MGP' as source,

            *

        from silver.mgp_cptit

        union all

        select

            'RCR' as source,

            *

        from silver.rcr_cptit

    )

    select *

    from union_all
);
