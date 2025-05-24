def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_silver_tbhis # Nome do modelo
    description: "View Silver da TBHIS"  # Descrição do modelo
    columns:
          - name: codtransacao
            description: Código Transação - Primary Key

          - name: descricao
            description: Descrição Transação
"""
