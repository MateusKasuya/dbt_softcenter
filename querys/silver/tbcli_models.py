def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_silver_tbcli # Nome do modelo
    description: "View Silver da TBCLI"  # Descrição do modelo
    columns:
          - name: cgccpfcli
            description: CPF/CNPJ Cliente - Primary Key

          - name: nomefantasia
            description: Nome Fantasia Cliente
"""
