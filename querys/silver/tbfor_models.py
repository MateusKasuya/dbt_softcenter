def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_tbfor # Nome do modelo
    description: "View Silver da TBFOR"  # Descrição do modelo
    columns:
          - name: cgccpfforne
            description: Código Fornecedor - Primary Key

          - name: fornecedor
            description: Nome Fantasia Fornecedor
"""
