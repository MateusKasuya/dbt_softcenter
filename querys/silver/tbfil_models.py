def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_tbfil # Nome do modelo
    description: "View Silver da TBFIL"  # Descrição do modelo
    columns:
          - name: codfil
            description: Código Filial - Primary Key

          - name: filial
            description: Nome Filial
"""
