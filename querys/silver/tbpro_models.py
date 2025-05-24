def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_silver_tbpro # Nome do modelo
    description: "View Silver da TBPRO"  # Descrição do modelo
    columns:
          - name: codpro
            description: Código Produto - Primary Key

          - name: nome
            description: Nome Produto
"""
