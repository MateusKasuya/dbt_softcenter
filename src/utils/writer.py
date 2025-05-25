import os
from src.utils.enums import Source, Table


class DBTFileWriter:
    def __init__(self, source: Source):
        """
        Initialize the DBTFileWriter with a specific source.

        Args:
            source (Source): The source system to generate DBT files for.
        """
        self.source = source

    def create_dbt_silver_model_sql(self, table: Table, sql_content: str) -> str:
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
        base_output_dir = f"models/silver/{self.source.value}"
        model_name = f"{self.source.value}_{table.value}.sql"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists and the table
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(sql_content)

        print(f"Generated SQL file: {file_path}")

    def create_dbt_silver_model_yml(self, table: Table, yml_content: str) -> str:
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
        base_output_dir = f"models/silver/{self.source.value}"
        model_name = f"_{self.source.value}_{table.value}.yml"
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
        base_output_dir = f"models/bronze"
        model_name = f"_{self.source.value}_sources.yml"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)

        print(f"Generated YML file: {file_path}")

    def create_dbt_gold_model_sql(self, table: Table, sql_content: str) -> str:
        """
        Generates a DBT model SQL file for gold layer tables.
        The output file will be placed in 'models/gold/{table}.sql'.

        Args:
            table (Table): The table enum representing the target table.
            sql_content (str): The SQL content to be written to the file.

        Returns:
            str: The file path of the generated .sql file.
        """
        base_output_dir = f"models/gold"
        model_name = f"{table.value}.sql"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(sql_content)

        print(f"Generated SQL file: {file_path}")

    def create_dbt_gold_model_yml(self, table: Table, yml_content: str) -> str:
        """
        Generates a DBT model YML file for gold layer tables.
        The output file will be placed in 'models/gold/{table}.yml'.

        Args:
            table (Table): The table enum representing the target table.
            yml_content (str): The YML content to be written to the file.

        Returns:
            str: The file path of the generated .yml file.
        """
        base_output_dir = f"models/gold"
        model_name = f"_{table.value}.yml"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)

        print(f"Generated YML file: {file_path}")

    def create_dbt_gold_calendar_yml(self, yml_content: str) -> str:
        """
        Generates a DBT model YML file for the calendar table in the gold layer.
        The output file will be placed in 'models/gold/calendario.yml'.

        Args:
            yml_content (str): The YML content to be written to the file.

        Returns:
            str: The file path of the generated .yml file.
        """
        base_output_dir = f"models/gold"
        model_name = f"calendario.yml"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)

        print(f"Generated YML file: {file_path}")

    def create_dbt_gold_calendar_sql(self, sql_content: str) -> str:
        """
        Generates a DBT model SQL file for the calendar table in the gold layer.
        The output file will be placed in 'models/gold/calendario.sql'.

        Args:
            sql_content (str): The SQL content to be written to the file.

        Returns:
            str: The file path of the generated .sql file.
        """
        base_output_dir = f"models/gold"
        model_name = f"calendario.sql"
        file_path = os.path.join(base_output_dir, model_name)

        # Ensure the subdirectory for the schema exists
        os.makedirs(base_output_dir, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(sql_content)

        print(f"Generated SQL file: {file_path}")
