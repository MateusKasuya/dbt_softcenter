yaml = f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_{schema}_tbhis # Nome do modelo
    description: "View Staging da TBHIS"  # Descrição do modelo
    columns:
          - name: codtransacao
            description: Código Transação - Primary Key

          - name: descricao
            description: Descrição Transação
"""
