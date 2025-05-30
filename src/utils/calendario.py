from src.utils.enums import Source
from src.utils.writer import DBTFileWriter
from querys.gold.calendar_sql import get_query_content as calendar_sql
from querys.gold.calendar_yml import get_yml_content as calendar_yml


def calendario_models(source: Source):
    """
    Generates the calendar models for a specific source system.
    This function creates both SQL and YML files for the calendar table in the gold layer.
    The calendar table is used for date-related operations and time-based analysis.

    Args:
        source (Source): The source system to generate the calendar models for.
    """
    writer = DBTFileWriter(source=source)

    yml_content = calendar_yml()
    sql_content = calendar_sql()
    writer.create_dbt_gold_calendar_yml(yml_content=yml_content)
    writer.create_dbt_gold_calendar_sql(sql_content=sql_content)
