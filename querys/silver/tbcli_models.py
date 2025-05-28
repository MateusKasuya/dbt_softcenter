def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_tbcli # Nome do modelo
    description: "View Silver da TBCLI"  # Descrição do modelo
    columns:
          - name: cgccpfcli
            description: CPF/CNPJ Cliente - Primary Key

          - name: cliente
            description: Nome Fantasia Cliente
"""
