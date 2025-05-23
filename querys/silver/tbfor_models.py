yaml = f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_{schema}_tbfor # Nome do modelo
    description: "View Staging da TBFOR"  # Descrição do modelo
    columns:
          - name: cgccpfforne
            description: Código Fornecedor - Primary Key

          - name: nomefantasia
            description: Nome Fantasia Fornecedor
"""
