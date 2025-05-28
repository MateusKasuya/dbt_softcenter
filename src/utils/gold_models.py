from src.utils.enums import Source, Table
from src.utils.writer import DBTFileWriter
from querys.gold.sql import get_query_content as gold_sql
from querys.gold.yml import get_yml_content as gold_yml
from querys.gold.cptit_yml import get_yml_content as cptit_yml
from querys.gold.factrc_yml import get_yml_content as factrc_yml
from querys.gold.frctrc_yml import get_yml_content as frctrc_yml
from querys.gold.frctrc_sql import get_query_content as frctrc_sql
from querys.gold.tbcli_yml import get_yml_content as tbcli_yml
from querys.gold.tbcli_sql import get_query_content as tbcli_sql


def gold_models(source: Source):
    """
    Generates all gold layer models for a specific source system.
    This function creates both SQL and YML files for all tables in the gold layer,
    including CPTIT, FACTRC, FRCTRC, TBCID, TBFOR, TBHIS, TBCLI, TBCTA, TBFIL, and TBPRO.
    Special handling is provided for CPTIT, FACTRC, and FRCTRC tables which have custom YML content.

    Args:
        source (Source): The source system to generate the gold layer models for.
    """
    writer = DBTFileWriter(source=source)

    list_of_tables = [
        Table.CPTIT,
        Table.FACTRC,
        Table.FRCTRC,
        Table.TBCID,
        Table.TBFOR,
        Table.TBHIS,
        Table.TBCLI,
        Table.TBCTA,
        Table.TBFIL,
        Table.TBPRO,
    ]

    for table in list_of_tables:
        if table == Table.CPTIT:
            yml_content = cptit_yml()
            sql_content = gold_sql(table.value)
        elif table == Table.FACTRC:
            yml_content = factrc_yml()
            sql_content = gold_sql(table.value)
        elif table == Table.FRCTRC:
            yml_content = frctrc_yml()
            sql_content = frctrc_sql()
        elif table == Table.TBCLI:
            yml_content = tbcli_yml()
            sql_content = tbcli_sql()
        else:
            yml_content = gold_yml(table.value)
            sql_content = gold_sql(table.value)
        writer.create_dbt_gold_model_yml(table=table, yml_content=yml_content)
        writer.create_dbt_gold_model_sql(table=table, sql_content=sql_content)
