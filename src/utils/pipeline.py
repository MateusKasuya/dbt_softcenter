from utils.enums import Source

from src.utils.sources import sources
from src.utils.silver_models import silver_models
from src.utils.gold_models import gold_models


class Pipeline:
    def __init__(self, source: Source):
        self.source = source

    def write_source_yml(self):
        print(f"Writing source.yml for {self.source.value}")
        sources(self.source)
        print(f"source.yml for {self.source.value} written")

    def write_models(self):
        print(f"Writing models for {self.source.value}")
        silver_models(self.source)
        print(f"models for {self.source.value} written")

    def write_gold_models(self):
        print(f"Writing gold models for {self.source.value}")
        gold_models(self.source)
        print(f"gold models for {self.source.value} written")
