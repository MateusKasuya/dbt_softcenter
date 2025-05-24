from src.utils.enums import Source
from src.utils.writer import DBTFileWriter
from querys.bronze.sources import get_yml_content


def sources(source: Source):
    writer = DBTFileWriter(source=source)

    writer.create_dbt_source_yml(yml_content=get_yml_content(source.value))
