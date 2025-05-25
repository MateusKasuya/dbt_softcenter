from src.utils.enums import Source
from src.utils.writer import DBTFileWriter
from querys.bronze.sources import get_yml_content


def sources(source: Source):
    """
    Generates the source.yml file for a specific source system.
    This function creates the source configuration file that defines the source tables
    and their schemas in DBT.

    Args:
        source (Source): The source system to generate the source.yml file for.
    """
    writer = DBTFileWriter(source=source)

    writer.create_dbt_source_yml(yml_content=get_yml_content(source.value))
