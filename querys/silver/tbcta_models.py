def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_silver_tbcta # Nome do modelo
    description: "View Silver da TBCTA"  # Descrição do modelo
    columns:
          - name: contareduz
            description: Código Conta Reduzida - Primary Key

          - name: nomeconta
            description: Nome Conta
"""
