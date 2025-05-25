from src.utils.enums import Source, Table
from src.utils.writer import DBTFileWriter
from querys.silver.cptit_models import get_yml_content as cptit_yml
from querys.silver.cptit import get_query_content as cptit_sql
from querys.silver.factrc_models import get_yml_content as factrc_yml
from querys.silver.factrc import get_query_content as factrc_sql
from querys.silver.frctrc_models import get_yml_content as frctrc_yml
from querys.silver.frctrc import get_query_content as frctrc_sql
from querys.silver.tbcid_models import get_yml_content as tbcid_yml
from querys.silver.tbcid import get_query_content as tbcid_sql
from querys.silver.tbfor_models import get_yml_content as tbfor_yml
from querys.silver.tbfor import get_query_content as tbfor_sql
from querys.silver.tbhis_models import get_yml_content as tbhis_yml
from querys.silver.tbhis import get_query_content as tbhis_sql
from querys.silver.tbcli_models import get_yml_content as tbcli_yml
from querys.silver.tbcli import get_query_content as tbcli_sql
from querys.silver.tbcta_models import get_yml_content as tbcta_yml
from querys.silver.tbcta import get_query_content as tbcta_sql
from querys.silver.tbfil_models import get_yml_content as tbfil_yml
from querys.silver.tbfil import get_query_content as tbfil_sql
from querys.silver.tbpro_models import get_yml_content as tbpro_yml
from querys.silver.tbpro import get_query_content as tbpro_sql


def silver_models(source: Source):
    """
    Generates all silver layer models for a specific source system.
    This function creates both SQL and YML files for all tables in the silver layer,
    including CPTIT, FACTRC, FRCTRC, TBCID, TBFOR, TBHIS, TBCLI, TBCTA, TBFIL, and TBPRO.

    Args:
        source (Source): The source system to generate the silver layer models for.
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
            yml_content = cptit_yml(source.value)
            sql_content = cptit_sql(source.value)
        elif table == Table.FACTRC:
            yml_content = factrc_yml(source.value)
            sql_content = factrc_sql(source.value)
        elif table == Table.FRCTRC:
            yml_content = frctrc_yml(source.value)
            sql_content = frctrc_sql(source.value)
        elif table == Table.TBCID:
            yml_content = tbcid_yml(source.value)
            sql_content = tbcid_sql(source.value)
        elif table == Table.TBFOR:
            yml_content = tbfor_yml(source.value)
            sql_content = tbfor_sql(source.value)
        elif table == Table.TBHIS:
            yml_content = tbhis_yml(source.value)
            sql_content = tbhis_sql(source.value)
        elif table == Table.TBCLI:
            yml_content = tbcli_yml(source.value)
            sql_content = tbcli_sql(source.value)
        elif table == Table.TBCTA:
            yml_content = tbcta_yml(source.value)
            sql_content = tbcta_sql(source.value)
        elif table == Table.TBFIL:
            yml_content = tbfil_yml(source.value)
            sql_content = tbfil_sql(source.value)
        elif table == Table.TBPRO:
            yml_content = tbpro_yml(source.value)
            sql_content = tbpro_sql(source.value)

        writer.create_dbt_silver_model_yml(table=table, yml_content=yml_content)
        writer.create_dbt_silver_model_sql(table=table, sql_content=sql_content)
