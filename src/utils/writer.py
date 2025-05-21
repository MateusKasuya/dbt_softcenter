import os
from src.utils.enums import Schema, Source, Table


class DBTFileWriter:
    def __init__(
        self,
        schema: Schema,
        table: Table,
        source: Source,
        sql_content: str,
        yml_content: str,
        yml_content_source: str = None,
    ):
        self.schema = schema
        self.table = table
        self.source = source
        self.sql_content = sql_content
        self.yml_content = yml_content
        self.yml_content_source = yml_content_source

    def create_dbt_model_sql(self) -> str:
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
        base_output_dir = f"models/{self.source.value}/{self.schema.value}"
        model_name = f"{self.source.value}_{self.schema.value}_{self.table.value}.sql"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists and the table
        os.makedirs(base_output_dir, exist_ok=True)

        sql_content = self.sql_content

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(sql_content)

        print(f"Generated SQL file: {file_path}")
        return file_path

    def create_dbt_model_yml(self) -> str:
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
        base_output_dir = f"models/{self.source.value}/{self.schema.value}"
        model_name = f"_{self.source.value}_{self.schema.value}_{self.table.value}.yml"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        yml_content = self.yml_content

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)

        print(f"Generated YML file: {file_path}")
        return file_path

    def create_dbt_source_yml(self) -> str:
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
        schema_output_dir = os.path.join(base_output_dir, self.schema.value)
        file_path = os.path.join(schema_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(schema_output_dir, exist_ok=True)

        yml_content = self.yml_content_source

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)

        print(f"Generated YML file: {file_path}")
        return file_path
