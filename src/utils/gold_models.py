from src.utils.enums import Source, Table
from src.utils.writer import DBTFileWriter
from querys.gold.sql import get_query_content as gold_sql
from querys.gold.yml import get_yml_content as gold_yml


def gold_models(source: Source):
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
        yml_content = gold_yml(table.value)
        sql_content = gold_sql(table.value)
        writer.create_dbt_gold_model_yml(table=table, yml_content=yml_content)
        writer.create_dbt_gold_model_sql(table=table, sql_content=sql_content)
