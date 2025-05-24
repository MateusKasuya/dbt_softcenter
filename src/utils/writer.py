import os
from src.utils.enums import Schema, Source, Table


class DBTFileWriter:
    def __init__(self, source: Source):
        self.source = source

    def create_dbt_model_sql(
        self, schema: Schema, table: Table, sql_content: str
    ) -> str:
        """
        Generates a DBT model SQL file for the FRCTRC table with a dynamic source schema.
        The output file will be placed in 'models/{source}/{schema}/{table}.sql'.

        Args:
                source: The name of the source schema (e.g., 'fn9', 'f98').
                schema: The name of the schema to be replicated.
                table: The name of the table to be replicated.
                sql_content: The content of the SQL file to be written.

        Returns:
            The file path of the generated .sql file.
        """
        base_output_dir = f"models/{self.source.value}/{schema}"
        model_name = f"{self.source.value}_{schema}_{table}.sql"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists and the table
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(sql_content)

        print(f"Generated SQL file: {file_path}")

    def create_dbt_model_yml(
        self, schema: Schema, table: Table, yml_content: str
    ) -> str:
        """
        Generates a DBT model SQL file for the FRCTRC table with a dynamic source schema.
        The output file will be placed in 'dbt_softcenter/models/staging/{schema_name}/'.

        Args:
            schema: The name of the source schema (e.g., 'fn9', 'f98').
            table: The name of the table to be replicated.
            yml_content: The content of the yml file to be written.

        Returns:
            The file path of the generated .yml file.
        """
        base_output_dir = f"models/{self.source.value}/{schema}"
        model_name = f"_{self.source.value}_{schema}_{table}.yml"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)

        print(f"Generated YML file: {file_path}")

    def create_dbt_source_yml(self, yml_content: str) -> str:
        """
        Generates a DBT model SQL file for the FRCTRC table with a dynamic source schema.
        The output file will be placed in 'models/{source}/{schema}/'.

        Args:
            source: The name of the source schema (e.g., 'fn9', 'f98').
            yml_content: The content of the yml file to be written.

        Returns:
            The file path of the generated .yml file.
        """
        base_output_dir = f"models/{self.source.value}"
        model_name = f"_{self.source.value}_sources.yml"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)

        print(f"Generated YML file: {file_path}")
