def get_yml_content(source: str, schema: str) -> str:
    return f"""
yaml = f
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_{schema}_tbcta # Nome do modelo
    description: "View Staging da TBCTA"  # Descrição do modelo
    columns:
          - name: contareduz
            description: Código Conta Reduzida - Primary Key

          - name: nomeconta
            description: Nome Conta
"""
