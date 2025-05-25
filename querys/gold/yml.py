def get_yml_content(table: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {table} # Nome do modelo
    description: "Tabela Gold da {table}"  # Descrição do modelo
    columns:
        - name: source
          description: Fonte de origem/ Empresa
"""
