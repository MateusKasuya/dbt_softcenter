def get_yml_content(source: str, schema: str) -> str:
    return f"""
yaml = f
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_{schema}_tbpro # Nome do modelo
    description: "View Staging da TBPRO"  # Descrição do modelo
    columns:
          - name: codpro
            description: Código Produto - Primary Key

          - name: nome
            description: Nome Produto
"""
