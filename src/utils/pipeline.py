from utils.enums import Source

from bronze.sources import sources


def write_source_yml():
    list_of_sources = [Source.FN9, Source.MGP, Source.RCR]

    for source in list_of_sources:
        print(f"Writing source.yml for {source.value}")
        sources(source)
        print(f"source.yml for {source.value} written")
