from utils.enums import Source

from src.utils.sources import sources
from src.utils.silver_models import silver_models
from src.utils.gold_models import gold_models
from src.utils.calendario import calendario_models


class Pipeline:
    def __init__(self, source: Source):
        """
        Initialize the Pipeline with a specific source.

        Args:
            source (Source): The source system to generate DBT files for.
        """
        self.source = source

    def write_source_yml(self):
        """
        Generates the source.yml file for the specified source system.
        This file contains the source configuration for DBT.
        """
        print(f"Writing source.yml for {self.source.value}")
        sources(self.source)
        print(f"source.yml for {self.source.value} written")

    def write_models(self):
        """
        Generates the silver layer models for the specified source system.
        This includes both SQL and YML files for all tables in the silver layer.
        """
        print(f"Writing models for {self.source.value}")
        silver_models(self.source)
        print(f"models for {self.source.value} written")

    def write_gold_models(self):
        """
        Generates the gold layer models for the specified source system.
        This includes both SQL and YML files for all tables in the gold layer.
        """
        print(f"Writing gold models for {self.source.value}")
        gold_models(self.source)
        print(f"gold models for {self.source.value} written")

    def write_calendario_models(self):
        """
        Generates the calendar models for the specified source system.
        This includes both SQL and YML files for the calendar table.
        """
        print(f"Writing calendario models")
        calendario_models(self.source)
        print(f"calendario models written")
