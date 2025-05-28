def get_yml_content() -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: tbcli # Nome do modelo
    description: "Tabela Gold da tbcli"  # Descrição do modelo
    columns:
        - name: source
          description: Fonte de origem/ Empresa
"""
